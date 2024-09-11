
correct = False

while correct == False:
    anynum = int(input("Please enter a number above 50: "))
    if anynum > 50:
        correct = True

        while anynum > 0:
            print("Number is: ", anynum)
            anynum = anynum - 1

        print("Value is now: ", anynum)
