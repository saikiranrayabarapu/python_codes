import turtle
from turtle import *
t=Pen()
t.speed(1)
t.color("red")
t.begin_fill()
t.left(45)
t.forward(100)
t.circle(50,extent=180)
t.setheading(135)
t.circle(50,extent=180)
t.forward(100)
t.end_fill()
t.hideturtle()
t.up()
t.setheading(270)
t.forward(50)
t.write("I love You",False,"center",font=("Monotype Corsiva",30,"bold"))
turtle.done()