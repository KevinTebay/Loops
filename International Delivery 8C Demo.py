status = False #variable for the status

while status == False:

    weight = float(input("Enter the weight to the nearest kg: ")) #float is a decimal num
    destination =str(input("Enter 'I' for International delivery or 'S' for Standard delivery: ")) #string is "any characters"
    #Mr Tebay Example
    if destination == "I":
        if weight > 5:
            print("Overweight for international shipping. Reduce the weight!")
        else:
            cost = 40
            print("Total cost is €:", cost)
            status = True
    #Mr Tebay
    elif destination == "S":
        if weight > 5:
            cost = 20 + 1 * (weight - 5)
            print("Total cost is €:", cost)
            status = True
        else:
            cost = 20
            print("Total cost is €:", cost)
            status = True
    #Mr Tebay Example
    else:
        print("Invalid option of destination")

print("Program finishes")
