import turtle
#code to draw a square using a loop
speed=100
angle=90
thing = turtle.Turtle()
for i in range (4):
    thing.forward(speed)
    thing.left(angle)
turtle.done()
