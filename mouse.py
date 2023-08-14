import turtle
import math

t = turtle.Turtle()

t.pencolor("black")

t.pensize(5)

t.penup()

t.goto(-0, 0)

t.pendown()

t.begin_fill()

for i in range(4):

    t.right(90)

    t.forward(100)

t.penup

t.fillcolor("gray")

for o in range(4):

    t.right(-90)  

    t.forward(-200)

t.right(90)

t.forward(200)

for p in range(2):

    t.left(-90)

    t.forward(100)

t.end_fill()

t.hideturtle()

t.left(90)

t.forward(200)

turtle.exitonclick()