correct = False #set correct to False #boolean data 
day = "Thursday" #set day to Thursday

while correct == False: #will loop if correct is False
    dayoftheweek = str(input("Enter day of the week: "))
    #Nested Condition
    if dayoftheweek == day:
        correct = True #break the loop

print("correct = True")
print("Loop has ended.")

