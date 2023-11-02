import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)



tim.home()
tim.speed('fastest')

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size_of_gap)


runs =int(input("Enter the gap between the circles you want to draw : "))
draw_spirograph(runs)



screen.exitonclick()