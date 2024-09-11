#Create a program which allows the user to enter a two whole numbers. 
#Depending on what the user selects. 
#You should display the two numbers either added together,
#multiplied together, divided together or subtracted.

#Variables - number1, number2, symbol-...
number1 = int(input("Please enter the first number: ")) #integer - whole number
number2 = int(input("Please enter the second number: ")) #integer - whole number
symbol = str(input("Enter a symbol [+ , * , - , / ]: ")) #string "any characters grouped together"

if symbol == "+":
    add = number1+number2
    print(number1 , symbol , number2, "=" , add)

elif symbol
