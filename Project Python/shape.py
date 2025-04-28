import turtle
import math

t = turtle.Turtle()
t.color("green","yellow")
t.speed(10)

t.begin_fill()
for i in range(2000):
    t.forward(math.sqrt(i))
    t.left(i % 180)
t.end_fill()

turtle.done()