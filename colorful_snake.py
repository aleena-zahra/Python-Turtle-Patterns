import turtle
from turtle import Screen
import random

screen = Screen()
speed=10

colors = ["blue", "red", "orange", "pink", "purple", "yellow", "cyan", "light blue", "brown", "light green"  ]
snake = turtle.Turtle()
snake.width(width=5)
snake.hideturtle()
snake.color(random.choice(colors))
#functions that define movement in 4 directions
#color changes each time snake moves
def go_up():
    global snake
    snake.color(random.choice(colors))
    y=snake.ycor()
    snake.sety(y+speed)
def go_down():
    global snake
    snake.color(random.choice(colors))
    snake.color(random.choice(colors))
    y=snake.ycor()
    snake.sety(y-speed)
def go_right():
    global snake
    snake.color(random.choice(colors))
    x=snake.xcor()
    snake.setx(x+speed) 
def go_left():
    global snake
    snake.color(random.choice(colors))
    x=snake.xcor()
    snake.setx(x-speed) 

#functions to respond to user pressing arrow keys
screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_right,"Right")
screen.onkeypress(go_left,"Left")
    
turtle.done()
