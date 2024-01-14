from turtle import Turtle,Screen
import random
screen = Screen() 
screen.setup(width=600,height=600)
screen.title('aleena')
turtles = []
speed = 10
y = -100
in_screen = True
def make_turtle():
    global y
    for i in range(0,5):
        t = Turtle()
        t.penup()
        t.shape("turtle")
        t.color("light green")
        random_number1 = random.randint(-300,300)
        random_number2 = random.randint(-300,300)
        t.goto(-280, y)
        y+=50
        turtles.append(t)

def move_turtles():
    for turtle in turtles: 
        random_number1 = random.randint(0,50)
        turtle.forward(random_number1)

make_turtle()   
while in_screen==True:     
    move_turtles()
    for turtle in turtles:
        xposition = turtle.xcor()
        if xposition >=270:
            in_screen = False



screen.exitonclick()