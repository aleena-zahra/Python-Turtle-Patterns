import turtle
import random
from turtle import Screen
screen = Screen() 
screen.setup(width=800,height=600)
#making dots with various different colors on the screen
turtle_array = []
colors = [ "red", "pink", "violet", "yellow",  "light blue", "light green"]
#setting x and y coordinates to the bottom of the screen
y=-200 
x=-200
#using a nested loop
for dot in range (0,10):
    for dot in range (0,10):
        dot = turtle.Turtle()
        dot.penup()
        dot.shape("circle")
        dot.color(random.choice(colors))
        dot.goto(x, y)
        #increasing the y value to shift the dot vertically
        y+=50
        turtle_array.append(dot)
    #increasing the x value to shift the dot horizontally
    #changing the y value back to the bottom of the screen
    y=-200    
    x+=50    
    
    
turtle.done()
