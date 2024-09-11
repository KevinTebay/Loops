count = 0

while count <= 150: 
    print("Count is", count)
    count = count + 5 
   #nested if
    if count == 10:
        print("===========")
        print("Number is ten")
        print("===========")
    elif count == 20:
        print("===========")
        print("Number is twenty")
        print("===========")
    elif count == 100:
        print("===========")
        print("Number is a hundred")
        print("===========")
        break #stops your program mid loop

print("Loop has broken")
    
