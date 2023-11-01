from turtle import Turtle , Screen
import random


"""draw different shapes with random colors
triangle = 120 =3 
square = 90=4"""

colors = ["yellow","blue","red","green","pink", "purple",
           "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray"]

tim = Turtle()
tim.hideturtle()
tim.pensize(15)
tim.speed(0)

screen = Screen()
screen.setup(width=600, height=600)


def random_color():
     return random.choice(colors)

def random_paths():
    dirs = [90, -90, 0,  180]
    return random.choice(dirs)

paint =0

screen.setup(width=1.0, height=1.0)

while True:
    tim.color(random_color())
    tim.fd(40)
    tim.setheading(random_paths())
    if abs(tim.xcor()) == 200 or abs(tim.ycor()==200):
        tim.left(180)
    paint += 1
    if paint == 10000:
        break

screen.exitonclick()
