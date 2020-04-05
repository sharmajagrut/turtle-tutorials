import turtle

t = turtle.Turtle()

def make_L():

    t.pendown()     # To make L
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.penup()
    t.goto(0, 0)

def turn():

    t.right(180)    # To make turn

def m_dot():

    global a    # to make dots
    global b
    t.goto(a, b)
    t.dot(10)


make_L()
turn()
make_L()
turn()
make_L()
turn()
make_L()
a = 50      # defining positions
b = 50
m_dot()
b -= 100    # defining positions
m_dot()
a -= 100    # defining positions
m_dot()
b += 100    # defining positions
m_dot()
t.penup()
t.goto(0, 0)

turtle.exitonclick()

