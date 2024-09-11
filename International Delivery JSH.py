status = False

#What should status be here?
while status == :


    weight = int(input("Enter the weight to the nearest kg: "))
    destination =str(input("Enter 'I' for International delivery or 'S' for Standard delivery: "))

    if destination == "I":

        if weight > 5:
            print("Overweight for international shipping. Reduce the weight!")
        else:
            cost = 40
            print("Total cost is €:", cost)
            #What should status be here?
            status = 

    elif destination == "S":
        if weight > 5:
            cost = 20 + 1*(weight-5)
            print("Total cost is €:", cost)
            #What should status be here?    
            status = 
            
        else:
            cost = 20
            print("Total cost is €:", cost)
            #What should status be here?
            status =
            

    else:
        print("Invalid Selection. Re-enter the selection")

    
