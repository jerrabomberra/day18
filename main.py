import colorgram
import turtle as t
from turtle import Screen
from turtle import Turtle
import random



t.colormode(255)

screen = Screen()
screen.setup(width=600, height=600)

rgb_colors = [(35, 19, 15), (197, 144, 123), (30, 106, 155), 
              (142, 85, 55), (9, 21, 45), (236, 213, 85), 
              (196, 135, 155), (156, 62, 90), (221, 85, 66), 
              (153, 17, 37), (202, 79, 104)]


def random_color():
     """ returns a random rgb color"""
     return random.choice(rgb_colors)

paint = 0
dot_distance = 50
width = 10
height = 10

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(tim.pos() + (-200, 200))

tim.speed('fastest')

try:
    for y in range(height):
        for i in range(width):
            tim.pendown()
            tim.dot(20, random_color())
            tim.penup()
            tim.forward(dot_distance)
        tim.backward(dot_distance * width)
        tim.right(90)
        tim.forward(dot_distance)
        tim.left(90)
except:
    tim.done()

screen.exitonclick()

