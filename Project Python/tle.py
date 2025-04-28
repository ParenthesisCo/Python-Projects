import turtle

te = turtle.Turtle()

te.getscreen().bgcolor("#7fffd4")
te.color("#aa00ff","#00aa55")

te.speed(3)
for i in range(19):
    te.begin_fill()
    te.forward(50)
    te.right(30)
    te.forward(50)
    te.left(45)
    te.forward(50)
    te.right(85)
    te.forward(100)
    te.right(150)
    te.pencolor("#aaffff")
    te.end_fill()

turtle.done()