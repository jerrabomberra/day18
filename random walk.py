from turtle import Turtle , Screen
import random


"""draw different shapes with random colors
triangle = 120 =3 
square = 90=4"""

colors = ["yellow","blue","red","green","pink", "purple",
           "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", 
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim = Turtle()
tim.hideturtle()
tim.speed(2)

def random_color():
     return random.choice(colors)

def random_paths():
    dirs = [90, -90,  180]
    return random.choice(dirs)


print(random_paths())
print(random_color())
tim.color(random_color())
tim.fd(200)
tim.lt(90)
tim.fd(200)



screen = Screen()
screen.exitonclick()
