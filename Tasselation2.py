from turtle import *
screen = Screen()
screen.setup(width=800,height=600)
screen.cv._rootwindow.resizable(False, False)
screen.title('Tasselation')
screen.bgcolor('black') 
v = Turtle()
v.hideturtle()
v.speed(0)
v.pensize(4)
v.penup()
v.forward(-500) #-825
v.right(90)
v.forward(291) #400
v.left(90)
v.pendown()

t = 9

for i in range(7):
    for i in range(t): #16
        v.begin_fill()
        v.fillcolor('red')
        for i in range(3):
            v.forward(100)
            v.left(120)
        v.end_fill()
        v.forward(100)
    v.forward(50)
    v.left(90)
    v.forward(88)
    v.left(90)
    for i in range(10): #16
        v.begin_fill()
        v.fillcolor('cyan')
        for i in range(3):
            v.forward(100)
            v.left(120)
        v.end_fill()
        v.forward(100)
    v.right(180)
    if t == 9:
        t += 1
    else:
        t -= 1
v.penup()
screen.mainloop()
