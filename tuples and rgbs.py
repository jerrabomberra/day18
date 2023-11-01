import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
tim.hideturtle()
tim.pensize(15)

directions = [0,90,180,270]
tim.speed('fastest')

screen = t.Screen()
screen.setup(width=600, height=600)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

for _ in range(200):
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()