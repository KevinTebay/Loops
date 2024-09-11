accepted = False

while accepted == False:
    anynumber = int(input("Please enter a number above 50: "))

    if anynumber <= 50:
        print(anynumber, "is below 50. Try again!")
    else:
        print(anynumber, "is above 50!!!")
        accepted = True

while anynumber > 0:
    print("Value is : ", anynumber)
    anynumber = anynumber - 1

print("Value is zero!")
print("End of loop")
                      
