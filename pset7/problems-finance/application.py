from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from passlib.context import CryptContext

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

pwd_context = CryptContext(
    # Replace this list with the hash(es) you wish to support.
    # this example sets pbkdf2_sha256 as the default,
    # with additional support for reading legacy des_crypt hashes.
    schemes=["pbkdf2_sha256", "des_crypt"],

    # Automatically mark all but first hasher in list as deprecated.
    # (this will be the default in Passlib 2.0)
    deprecated="auto",

    # Optionally, set the number of rounds that should be used.
    # Appropriate values may vary for different schemes,
    # and the amount of time you wish it to take.
    # Leaving this alone is usually safe, and will use passlib's defaults.
    ## pbkdf2_sha256__rounds = 29000,
    )



@app.route("/")
@login_required
def index():

    def remove_duplicates(values):
        output = []
        seen = set()
        for value in values:
            # If value has not been encountered yet,
            # ... add it to both list and set.
            if value not in seen:
                output.append(value)
                seen.add(value)
        return output
        
    portfolio = db.execute("SELECT * FROM portfolio WHERE id = :id", id=session["user_id"])
    user = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
    
    
    
    test = []
    for item in portfolio:
        test.append(item['symbol'])
    test2 = remove_duplicates(test)
    
    
    
    return render_template("index.html", portfolio=portfolio, user=user, test=test2)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    if request.method == "POST":
        if request.form["symbol"] == "" or request.form["shares"] == "":
            num = str(session["user_id"])
            return apology(num)
            
        query = lookup(request.form["symbol"])
        if isinstance(query, dict) == False:
            return apology("not a valid symbol")
            
        symbol = query["symbol"]
        name = query["name"]
        stock_price = query["price"]
        shares = int(request.form["shares"])
        user_id = session["user_id"]
        transaction = float("{0:.2f}".format(shares * stock_price))
        
        if shares > 0:
            
            user = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
            user_cash = user[0]["cash"]
            portfolio = db.execute("SELECT * FROM portfolio WHERE id = :id", id=session["user_id"])

            if user_cash > transaction:
                    
                db.execute("INSERT INTO 'portfolio' ('id','transaction','symbol','name','shares','price') VALUES (:user_id,:transaction,:symbol,:name,:shares,:price)",
                user_id=int(user_id),
                transaction=float(transaction),
                symbol=symbol,
                name=str(name),
                shares=int(shares),
                price=float(stock_price))
                
                db.execute("UPDATE users SET cash = cash - :transaction WHERE id = :user_id",
                            transaction=transaction, 
                            user_id=user_id)
        
                return redirect(url_for("index"))
            else:
                return apology("not enough cash for the transaction")
        else:
            apology("you don't have any money..")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    return apology("TODO")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    if request.method == "POST":
        
        if request.form["company"] == "":
            return apology("enter a stock's symbol")
            
        query_lookup = lookup(request.form["company"])
        
        if isinstance(query_lookup, dict):
            return render_template("quoted.html", query_lookup=query_lookup)
        else:
            return apology("thats not an actual stock symbol")
    
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method == "POST":
        
        if request.form["username"] == "" or request.form["password"] == "" or request.form["confirm_password"] != request.form["password"]:
            return render_template("apology.html")
            
        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) >= 1:
            return apology("username already exists")
            
        # hash the users password
        pw_hash = pwd_context.hash(request.form["password"])
    
        # insert username and hased pw into db
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :password)", username=request.form["username"], password=pw_hash)
        
        return redirect(url_for("index"))
        
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    return apology("TODO")




# TODO: recreate the portfolio table but this time make
# the 'symbol' field unique. Then, i dunno, somehow make that work.