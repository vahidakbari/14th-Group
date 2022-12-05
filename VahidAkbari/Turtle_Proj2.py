import turtle
import time

t = 270

a = turtle.Turtle()
a.hideturtle()
a.speed("fastest")
a.penup()
a.goto(-300,300)
a.pendown()

a.pensize(5)
for i in range(4):
    a.forward(t)
    a.right(90)

a.penup()
a.goto(-300,300)
a.pendown()
a.pensize(3)


for i in range(2):
    x = a.pos()
    a.goto(x[0],x[1]-90)
    a.forward(t)
    a.goto(x[0],x[1]-90)
a.penup()
a.goto(-300,300)
a.pendown()
a.right(90)

for i in range(2):
    x = a.pos()
    a.goto(x[0]+90,x[1])
    a.forward(t)
    a.goto(x[0]+90,x[1])

a.pensize(1)
a.penup()
a.goto(-300,300)
a.pendown()

a.left(90)

for i in range(8):
    x = a.pos()
    a.goto(x[0],x[1]-30)
    a.forward(t)
    a.goto(x[0],x[1]-30)
a.penup()
a.goto(-300,300)
a.pendown()
a.right(90)

for i in range(8):
    x = a.pos()
    a.goto(x[0]+30,x[1])
    a.forward(t)
    a.goto(x[0]+30,x[1])

################################################################

base = 3
side = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

from random import sample
def shuffle(s): return sample(s,len(s))
rBase = range(base)
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

################################################################

a.penup()
a.goto(-300,300)

a.goto(-285,278)
x = a.pos()

for line in board:
    for i in range(9):
        a.write(line[i],False,"center")
        x = a.pos()
        a.goto(x[0]+30,x[1])
    a.goto(-285,x[1]-30)


################################################################

time.sleep(3)




