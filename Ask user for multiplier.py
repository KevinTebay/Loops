print("===Task 4===")
value = int(input("What value do you wish to multiply: ")) 
multiplier = int(input("How many times do you wish to multiply: ")) 
for i in range(1, multiplier+1, 1): 
    product = i * value 
    print(i, "x" ,value, "=", product)

print("=End of program=")
