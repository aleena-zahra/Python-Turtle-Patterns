import turtle
from turtle import Screen
import random

screen= Screen()
speed=10
angle = [90,180,270]
colors = ["blue", "red", "pink", "purple", "yellow", "cyan", "light blue", "brown", "light green"  ]
thing = turtle.Turtle()
thing.hideturtle()
thing.width(width=5)
for i in range (0,100):
    thing.forward(speed)
    thing.setheading(random.choice(angle))
    thing.color(random.choice(colors))

turtle.done()