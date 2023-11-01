from turtle import Turtle , Screen
import random


"""draw different shapes with random colors
triangle = 120 =3 
square = 90=4"""

colors = ["yellow","blue","red","green","pink", "purple",
           "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray"]

tim = Turtle()


screen = Screen()
screen.setup(width=600, height=600)
screen.setup(width=1.0, height=1.0)

for _ in range(20,300, 10):
    tim.circle(_)

screen.exitonclick()
