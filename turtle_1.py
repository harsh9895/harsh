#python turtle code 10 
#beautiful design in python
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(2)
t.speed(25)
col=('orange','white','green','red','blue')
for i in range(6000):
    t.pencolor(col[i%5])
    t.forward(i*4)
    t.right(121)