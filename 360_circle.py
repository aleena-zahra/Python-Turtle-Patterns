import turtle
import random
#making a colored circle in a loop
#the angle the circle is drawn from changes everytime making a 3d looking cylindrical shape
angle=10
colors = ["blue", "red", "orange", "pink", "purple", "yellow", "cyan", "light blue", "brown", "light green"  ]
circle = turtle.Turtle()
for i in range (0,90):
    circle.color(random.choice(colors))
    circle.circle(radius=40)
    circle.left(angle)
    
turtle.done()
