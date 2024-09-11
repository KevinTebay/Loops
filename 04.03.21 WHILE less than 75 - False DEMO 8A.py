count = 0 # variable
status = False #Boolean date
print("Made by Mr Tebay - 05.03.21")
print("Loop until count equals 75 is True")
while status == False:
    print("Count is:",count)
    count = count + 5
    #nested
    if count == 75:
        print("Count has reached 75")
        status = True

print("End of loop")
