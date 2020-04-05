import turtle

t = turtle.Turtle()

def square():
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)  # Completed a Square

square()
t.forward(100)
square()
turtle.exitonclick()
