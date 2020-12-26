from turtle import *
import time

pencolor('purple')
bgcolor('black')
penup()
goto(-50, 50)
pendown()
speed(0)
hideturtle()
#time.sleep(5)
while True:
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('yellow')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    pencolor('white')
    forward(20)
    right(10)
    right(120)

    if abs(pos()) < 1:
        break



done()
