from turtle import Turtle,Screen
import random
screen = Screen() 
screen.setup(width=800,height=600)
screen.title('geometric shapes')
speed = 100
angle=360
turtle = Turtle() 
turtle2 = Turtle()
#random geometric shapes generated
#any shape between a triangel and nonagon
turtle2.goto(200,0)
for i in range (0,5):
    random_number = random.randint(3,9)
    for i in range (0,random_number):
        turtle.forward(speed)
        turtle.left(angle/random_number)
#geometric shapes generated where sides increase by 1 in each iteration
#going from a triangle upto a nonagon
turtle2.goto(-200,0)
for i in range (3,9):
    for j in range (0,i):
        turtle2.left(angle/i)
        turtle2.forward(speed)

screen.exitonclick()
