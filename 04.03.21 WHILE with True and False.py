count = 0 #set the variable count to 0
status = False #variable status False - Boolean data

print("Loop until count equals 75 is True")

while status == False: #status equals False - program will loop
        print("Count is:", count)
        count = count + 5 #increment the count by 5
        if count == 75: #count variable equals 75
            print("Count has reached 75")
            status = True #status changes from False to True.

print("Print end of loop")

