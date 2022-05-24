from turtle import *
from functools import reduce
# brew install python-tk
# pip3 install turtle

fibSeq = lambda n : [reduce(lambda x,_ : [x[1], x[0]+x[1]], range(num), [0,1] )[0] for num in range(n+1)]

def draw1():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def draw2():
    speed(0)
    color('blue', 'green')
    begin_fill()
    while True:
        forward(200)
        left(179)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def draw3():
    speed(0)
    color('blue', 'green')
    while True:
        forward(200)
        left(91)
        if abs(pos()) < 1:
            break
    done()

def draw4(ran, angle):
    speed(0)
    color('blue', 'green')
    for i in range(ran):
        forward(i)
        left(angle)
    done()

def draw5(ran, angle):
    speed(0)
    color('blue', 'green')
    for i in range(ran):
        forward(i)
        left(angle)
    for i in range(ran,0,-1):
        forward(i)
        left(angle)
    done()

def draw_fibonacci(n):
    color('red', 'yellow')
    begin_fill()
    for i in fibSeq(n):
        circle(i)
        left(90)
    setpos(0,0)
    for i in fibSeq(n):
        forward(i)
        left(90)
    end_fill()

    getscreen().getcanvas().postscript(file="img.eps")
    done()

draw5(1000,89)

"""
Examples:

draw1()
draw2()
draw3()
draw4(1000, 150)
draw5(1000, 90.1)
draw5(1000,89)
"""