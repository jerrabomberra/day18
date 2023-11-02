import colorgram
import turtle as t
from turtle import Screen
from turtle import Turtle
import random



t.colormode(255)

screen = Screen()
screen.setup(width=600, height=600)

rgb_colors = []

colors = colorgram.extract('download.jpeg', 100)
for color in colors:
    rgb_colors.append(color.rgb)

def random_color():
     return random.choice(rgb_colors)

paint = 0
dot_distance = 10
width = 40
height = 40

tim = Turtle()
tim.penup()
tim.goto(tim.pos() + (-200, 200))
tim.hideturtle()
tim.speed('fastest')

try:
    for y in range(height):
        for i in range(width):
            tim.pendown()
            tim.dot(5, random_color())
            tim.penup()
            tim.forward(dot_distance)
        tim.backward(dot_distance * width)
        tim.right(90)
        tim.forward(dot_distance)
        tim.left(90)
except:
    tim.done()

screen.exitonclick()

