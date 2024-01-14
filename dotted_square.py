import turtle

speed=20
angle=90
thing = turtle.Turtle()
#making a dotted square by using a nested loop and penup and pendown functions
for i in range (4):
    for j in range (5):
        thing.penup()
        thing.forward(speed)
        thing.pendown()
        thing.forward(speed)
    thing.left(angle)    

turtle.done()
