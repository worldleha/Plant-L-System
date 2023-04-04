from collections import deque
import random as rd
from turtle import *
import math

points = ((0,380),(0,-50),(-30,0),(30,0))

#淘汰规则是返回值小，生存能力越强
# 此处为 越像Sin函数生存能力越强
def cal_length(pos):
    x,y = pos
    return abs(y-x*math.sin(x)+(1000-x))

def draw_expression(expression,distance,angle,stangle=0,pen_size = 2,stx=0,sty=0):
    reset()
    stack = deque()
    tracer(0)
    penup()
    goto(stx,sty)
    pendown()
    seth(stangle)
    colormode(255)
    pensize(pen_size)
    length = 0
    count = 0
    
    for char in expression:
        match char:
            case '+':
                right(angle)
            case '-':
                left(angle)
            case 'F':
                color(rd.randint(100,230),rd.randint(100,230),rd.randint(100,230))
                forward(distance)
                length += cal_length(position())
                count +=1
            case '[':
                #使用栈保存上一步
                stack.append((position(),heading()))
            case ']':
                pa = stack.pop()
                penup()
                goto(*pa[0])
                pendown()
                seth(pa[1])
        
    #color(41,253,41)
    #forward(50)
    update()
    if count:
        return length/count
    else:
        return 0

if __name__ == "__main__":
    pass
    draw_expression('',10,5)
