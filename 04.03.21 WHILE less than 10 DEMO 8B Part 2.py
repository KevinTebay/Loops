count = 0
status = False

while status == False:
    print("Count is: ", count)
    count = count + 5
    if count == 75:
        print("Count has reached 75")
        status = True

print("End of loop")

