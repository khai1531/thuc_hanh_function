import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
screen.bgcolor("skyblue")
def ve_nha():
    t.fillcolor("red")
    t.begin_fill()
    t.speed(0)
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    for _ in range(2):
        t.forward(125)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.penup()
    t.goto(75, 50)
    t.pendown()
    for _ in range(2):
        t.forward(125)
        t.right(90)
        t.forward(200)
        t.right(90)
    for _ in range(2):
        t.forward(125)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()
    turtle.done()
ve_nha()