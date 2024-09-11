import random

diceroll = 0

y = 0

#whileLoop
#while y is equal to 0 it runs this code
while y == 0:
    #gets the user's input
    choice = str(input("Choose a 4, 6 or 12 sided dice to roll, Press x to quit.   "))
    #checks if the user inputted 4
    if choice == "4":
        diceroll = random.randint(1, 4)
        print ("Your score is", diceroll)
    #checks if the user inputted 6
    elif choice == "6":
        diceroll = random.randint(1, 6)
        print ("Your score is", diceroll)
    #checks if the user inputted 8
    elif choice == "8":
        diceroll = random.randint(1, 8)
        print ("Your score is", diceroll)
    #checks if the user inputted 12
    elif choice == "12":
        diceroll = random.randint(1, 12)
        print ("Your score is", diceroll)
    #checks if the user inputted x
    elif choice == "x":
        print ("The program has ended!")
        #changes the value of y so the loop is cancelled
        y == 1
        #stops the program
        break

    # tells the user to input valid data
    else:
        print("enter either four, six or twelve")
    
