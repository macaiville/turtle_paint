from turtle import Turtle, Screen
import random


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def make_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

def make_dashed_line():
    for _ in range(15):
        timmy.pendown()
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)

def make_hexagon():
    for _ in range(5):
        timmy.forward(100)
        timmy.right(72)

def make_pentagon():
    for _ in range(6):
        timmy.forward(100)
        timmy.right(60)

def make_octagon():
    for _ in range(8):
        timmy.forward(100)
        timmy.right(45)

def make_7gon():
    for _ in range(7):
        timmy.forward(100)
        timmy.right(51)

def make_shapes():
    make_square()
    make_hexagon()
    make_pentagon()
    make_7gon()
    make_octagon()


random_color = ['red', 'black', 'yellow', 'brown', 'blue', 'green'] 
direction = [0, 90, 180, 270]

def random_movement():
    for _ in range(100):
        timmy.setheading(random.choice(direction))
        timmy.pendown()
        timmy.width(5)
        timmy.color(random.choice(random_color))
        timmy.forward(15)
        timmy.speed('fastest')

random_movement()

screen = Screen()
screen.exitonclick()