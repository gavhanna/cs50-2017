amount = 0
goodinput = False
counter = 0
while not goodinput:
    try:
        number = float(input('How much is owed: '))
        if number > 0:
            goodinput = True
            amount = number
        else:
            print("Positive nunmber please!")
    except ValueError:
        print("That's not positive. Try again.")
        
print(amount * 100)

change = amount * 100


while change > 0:
    if change >= 25:
        change -= 25
        counter += 1
    elif change >= 10:
        change -= 10
        counter += 1
    elif change >= 5:
        change -= 5
        counter += 1
    elif change >= 1:
        change -= 1
        counter += 1
        
print(counter)