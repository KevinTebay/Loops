import time

count = 0
print("While Loop Example 1")
while count != 5:
    count =count +1
    time.sleep(2)
    print("The count is: ", count)

print("End Loop")



number_wanted = int(input("What number do you want?: "))
print("For Loop Example 1")
for counter in range(0, number_wanted):
    time.sleep(2)
    print("The count is: ", counter)

print("End Loop")
