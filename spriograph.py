from turtle import Turtle, Screen

tim = Turtle()

for _ in range(1,4):
    tim.forward(100)
    tim.right(90)

tim.home()

screen = Screen()
screen.exitonclick()