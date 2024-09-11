status = False #variable status False - Boolean data

while status == False: #status equals False - program will loop

    weight = int(input("Enter the weight to the nearest kg: "))
    destination =str(input("Enter 'I' for International delivery or 'S' for Standard delivery: "))
    #Mr Tebay Example
    if destination == "I":
        #Nested IF Statement for the weight of the parcel
        if weight > 5:
            print("Overweight for international shipping. Reduce the weight!")
        else:
            cost = 40
            print("Total cost is : €" ,cost)
            status = True
    #Mr Tebay Example
    elif destination == "S":
        #Nested IF Statement for the weight of the parcel
        if weight > 5:
            cost = 20 + (weight-5)
            print("Total cost is : €" ,cost)
            status = True
        else:
            cost = 20
            print("Total cost is : €" ,cost)
            status = True

    else:
        print("Invalid selection - retype option...")
