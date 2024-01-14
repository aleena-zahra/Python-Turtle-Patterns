import turtle
import random


angle=10
colors = ["blue", "red", "orange", "pink", "purple", "yellow", "cyan", "light blue", "brown", "light green"  ]
thing = turtle.Turtle()
for i in range (0,90):
    thing.color(random.choice(colors))
    thing.circle(radius=40)
    thing.left(angle)
    
turtle.done()