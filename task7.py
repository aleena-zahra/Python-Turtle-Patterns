import turtle
import random
from turtle import Screen
screen = Screen() 
screen.setup(width=800,height=600)

turtle_array = []
colors = [ "red", "pink", "violet", "yellow",  "light blue", "light green"]
y=-200
x=-200
for dot in range (0,10):
    for dot in range (0,10):
        dot = turtle.Turtle()
        dot.penup()
        dot.shape("circle")
        dot.color(random.choice(colors))
        dot.goto(x, y)
        y+=50
        turtle_array.append(dot)
    #dot.circle(radius=10)
    y=-200    
    x+=50    
    
    
turtle.done()