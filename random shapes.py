from turtle import Turtle, Screen
from random import choice


"""draw different shapes with random colours
triangle = 120 =3 
square = 90=4"""





tim = Turtle()
tim.shape("turtle")

def shapes(num_sides):
    """draws dash lines"""
    for _ in range(num_sides):
        tim.color(colour)
        tim.fd(100)
        tim.rt(360/num_sides)



for _ in range(3,9):
    colours = ["yellow","blue","red","green","pink", "purple"]
    colour = choice(colours)
    shapes(_)



screen = Screen()
screen.exitonclick()