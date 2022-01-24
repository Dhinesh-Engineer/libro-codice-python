# Draw an object using turtle module

# import required modules
import turtle
import math

# Function for draw Rectangle

def drawRectangle(t,width,height,color):
    t.fillcolor(color)#filling color
    t.begin_fill()     #begin to color
    t.forward(width)     # moving forward
    t.left(90)                  #moving left
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


# Function for draw Triangle

def drawTriangle(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length/math.sqrt(2))
    t.left(90)
    t.forward(length/math.sqrt(2))
    t.left(135)
    t.end_fill()


# Set  the Background Color
screen = turtle.Screen()
screen.bgcolor("skyblue") #bg=background color


# Creating  turtle object

tip =turtle.Turtle()
tip.color("white") #pencil tip color
tip.shape("turtle")#pencil shape
tip.speed(1)


# Tree base

tip.penup() # pencil up
tip.goto(100,-130) #goto funtion
tip.pendown()#pencil down
drawRectangle(tip,20,40,"brown")

# Tree top
tip.penup()
tip.goto(65,-90)
tip.pendown()
drawTriangle(tip,90,"lightgreen")
tip.penup()
tip.goto(70,-45)
tip.pendown()
drawTriangle(tip,80,"lightgreen")
tip.penup()
tip.goto(75,-5)
tip.pendown()
drawTriangle(tip,70,"lightgreen")
