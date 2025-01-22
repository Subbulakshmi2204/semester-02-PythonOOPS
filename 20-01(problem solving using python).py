"""
import turtle
star=turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()
star.hideturtle()

import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)
    s.left(90)
s.hideturtle()


import turtle
s=turtle.Turtle()
s.forward(100)
s.penup()
s.right(90)
s.forward(100)
s.right(90)
s.pendown()
s.forward(100)


import turtle
s=turtle.Turtle()
s.fillcolor("blue")
s.begin_fill()
for i in range(4):
    s.forward(100)
    s.left(90)
s.end_fill()


import turtle
s=turtle.Turtle()
s.fillcolor('light pink')
s.begin_fill()
s.right(45)
s.forward(100)
s.left(90)
s.forward(100)
s.circle(50,180)
s.right(90)
s.circle(50,180)
s.end_fill()
s.write("Subbu",font=("Roman",40),align="left")

import turtle
s=turtle.Turtle()
for i in range(3):
    s.forward(100)
    s.left(120)
s.hideturtle()
"""
import turtle
s=turtle.Turtle()
s.circle(50)
s.hideturtle()
