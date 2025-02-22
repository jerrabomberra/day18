from turtle import Turtle , Screen
import random


"""draw different shapes with random colors
triangle = 120 =3 
square = 90=4"""

colors = ["yellow","blue","red","green","pink", "purple",
           "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



tim = Turtle()
tim.shape("turtle")

def shapes(num_sides):
    """draws shapes"""
    angle = 360/num_sides

    for _ in range(num_sides):
        tim.fd(100)
        tim.rt(angle)


tim.lt(90)
tim.penup()
tim.fd(250)
tim.lt(90)
tim.fd(50)
tim.rt(180)
tim.pendown()


for _ in range(3,21):
   tim.color(random.choice(colors))
   shapes(_)

screen = Screen()
screen.exitonclick()