
height = 0
goodinput = False
while not goodinput:
    try:
        number = int(input('Enter a number: '))
        if number > 0 and number <= 23:
            goodinput = True
            height = number
        else:
            print("We need a number between 0 and 24 please!")
    except ValueError:
        print("that's not an integer. Try again.")
        

for i in range(height):
    space = height - i
    for j in range(space, 1, -1):
        print(" ", end="")
    
    for hash in range(0, i + 2):
        print("#", end="")
        
    print("")
        
