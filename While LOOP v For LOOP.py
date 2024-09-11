import turtle

turns = 0
turtle.pendown()
#What is the difference here?
while turns < 4:
        turtle.forward (100)
        turtle.right(90)
        turns = turns + 1

##########
turtle.penup()
turtle.forward(150)
##########

turtle.pendown()
#What is the difference here?
for i in range(4): 
        turtle.forward (100)
        turtle.right(90)


