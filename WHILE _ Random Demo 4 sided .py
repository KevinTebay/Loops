import random
diceroll = 0
y = 0

#whileLoop
#while y is equal to 0 it runs this code
while y == 0:
    #gets the user's input
    choice = str(input("Press 4 to roll the dice. Press x to quit.   "))
    #checks if the user inputted 4
    if choice == "4":
        diceroll = random.randint(1, 4)
        print ("Your score is", diceroll)
    elif choice == "x":
        print ("The program has ended!")
        #changes the value of y so the loop is cancelled
        y == 1
        #stops the program
        break
    # tells the user to input valid data
    else:
        print("Please enter a four...")
    
