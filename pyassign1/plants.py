import turtle

def drawplant(t,r,color,speed):
    t.resizemode("user")
    t.pu()
    t.speed(0)
    t.goto(0,-r)
    t.speed(speed)
    t.pencolor(color)
    t.shapesize(1,1)
    t.shape("circle")
    t.pd()
    t.circle(r)

mer=turtle.Turtle()
ve=turtle.Turtle()
ear=turtle.Turtle()
ma=turtle.Turtle()
ju=turtle.Turtle()
sa=turtle.Turtle()
sun=turtle.Turtle()
sun.ht()
sun.dot(20,"yellow")
drawplant(mer,38,"blue",4)
drawplant(ve,72,"green",3)
drawplant(ear,100,"red",3)
drawplant(ma,152,"black",2)
drawplant(ju,250,"orange",5)
drawplant(sa,350,"blue",5)