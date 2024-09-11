attempts = 0

correct = False

while correct == False:

    if attempts < 4:

        
        password = str(input("Enter a password: "))

        if password == "123456":
            print("Correct")
            correct = True
        else:
            print("Incorrect")
            attempts = attempts + 1
