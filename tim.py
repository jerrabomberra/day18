from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

def dash(num):
    """draws dash lines"""
    for _ in range(num):
        tim.fd(100/num)
        tim.penup()
        tim.fd(100/num)
        tim.pendown()

for _ in range(4):
    dash(10)
    tim.rt(90)

tim.home()




screen = Screen()
screen.exitonclick()