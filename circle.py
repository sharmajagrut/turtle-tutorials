
import turtle# Importing the module
t = turtle.Turtle()# initializing turtle

radius = int(input("Enter radius of circle :") )#declaring the unit of radius

t.color("red")# fills red color in circle

t.begin_fill()# starts to fill red color 

t.circle(radius) #calling the circle(built-in) method

t.end_fill()#fills red color inside circle when circle is drawn 

time.sleep(5)#pauses the screen to view result for few more moments
