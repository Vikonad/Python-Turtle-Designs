from turtle import *
import math

black =     '#000000'
red =       '#FF0000'
yellow =    '#FFFF00'
magenta =   '#FF00FF'
olive =     '#808000' 

screen = Screen()
screen.setup(width=490,height=486)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor(black)
dimension = 120
rq = math.sqrt(dimension**2+dimension**2)
v = Turtle()
screen.title("Tasselation")
kh = 0
v.pensize(3)
v.speed(0)
#v.shape('turtle')
v.hideturtle()
v.penup()
v.goto(-243,125)
v.pendown()
for i in range(16):
    for i in range(4):
        v.forward(dimension)
        v.left(90)
    v.forward(dimension/3)
    v.right(90)
    for i in range(4):
        v.begin_fill()
        v.fillcolor(magenta)
        v.left(180)
        v.forward(dimension/6)
        v.left(45)
        v.forward(rq/6)
        v.left(45)
        v.forward(dimension/6)
        v.left(90)
        v.forward(dimension/3)
        v.end_fill()
        v.forward(-dimension/3)
        v.right(90)
        v.begin_fill()
        v.fillcolor(olive)
        v.right(180)
        v.forward(dimension/6)
        v.left(45)
        v.forward(rq/6)
        v.left(90)
        v.forward(rq/6)
        v.left(45)
        v.forward(dimension/6)
        v.end_fill()
    v.right(90)
    v.forward(dimension/3)
    v.right(90)
    for i in range(4):
        v.forward(dimension)
        v.right(90)
    v.forward(dimension/3)
    v.right(90)
    v.forward(dimension/6)
    v.left(45)
    v.forward(rq/6*2)
    v.begin_fill()
    v.fillcolor(red)
    for i in range(4):
        v.right(90)
        v.forward(rq/6)
    v.end_fill()
    for i in range(4):
        v.begin_fill()
        v.fillcolor(yellow)
        for i in range(3):
            v.forward(rq/6)
            v.right(90)
        v.end_fill()
        v.left(180)
    for i in range(4):
        v.left(-90)
        v.forward(rq/6)
    v.right(90)
    v.forward(rq/6*2)
    v.left(45)
    v.forward(dimension/6)
    if kh == 3 or kh == 11:
        v.right(90)
        v.forward(dimension/3)
        v.right(90)
    elif kh == 7 or kh == 8:
        v.left(90)
        v.forward(dimension/3*2)
    else:
        v.right(90)
        v.forward(dimension/3)
        v.left(90)
    kh += 1
    print(kh)

screen.mainloop()