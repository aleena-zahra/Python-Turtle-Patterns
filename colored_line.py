import turtle
from turtle import Screen
import random

#going forward at a 90 degree angle, either clockwise or anticlockwise, or going straight 
#each time with a random color selected from a list
#to draw a colorful geometric looking pattern
screen= Screen()
speed=30
angle = [90,180,270]
colors = ["blue", "red", "pink", "purple", "yellow", "cyan", "light blue", "brown", "light green"  ]
line = turtle.Turtle()
line.hideturtle()
line.width(width=5)
for i in range (0,50):
    line.forward(speed)
    line.setheading(random.choice(angle))
    line.color(random.choice(colors))

turtle.done()
