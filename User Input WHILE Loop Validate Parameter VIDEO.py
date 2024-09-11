correct = False #set correct to FALSE

while correct == False: # I want the anynum to be above 50
    anynum = int(input("Please enter a number above 50: "))
    if anynum >50: #condition to check if anynum is above 50
        correct = True
        #if number is above 50 - correct becomes True. Loop should end.

        #NESTED LOOP
        # This will will only run now if the number is above 50.
        while anynum > 0:
            print("Number is: ", anynum)
            anynum = anynum - 1

        print("Value is now: ", anynum)
        #Lets see! 
