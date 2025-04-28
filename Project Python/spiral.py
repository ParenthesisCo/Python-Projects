import turtle

te = turtle.Turtle()

te.getscreen().bgcolor("#7fffd4")
te.color("#55aa00")

te.speed(3)
for i in range(12):
    te.forward(200)
    te.left(90)
    te.forward(100)
    te.right(300)
    te.forward(45)
turtle.done()