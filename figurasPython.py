import turtle
import math
#carlos 

def rectangulo():
    for i in range (4):
        if(i%2):
            turtle.forward(50)
            turtle.left(90)
        else:
            turtle.forward(100)
            turtle.left(90)

def cuadradoEnEspiral():
    for i in range(3):
         turtle.left(20)
         for j in range(4):
            turtle.forward(90)
            turtle.left(90)


def cuadradoTriang():
    c = math.sqrt(120 ** 2 + 120 ** 2)
    for i in range(4):
        turtle.forward(120)
        turtle.left(90)
    turtle.left(45)
    turtle.forward(c)
    turtle.left(90)
    turtle.forward(c / 2)
    turtle.left(90)
    turtle.forward(c / 2)
    turtle.left(90)
    turtle.forward(c)


def poligonos(n):
    for i in range(n):
        turtle.forward(120)
        turtle.left(360 / n)


def cuadrado():
    for i in range(4):
        turtle.forward(120)
        turtle.left(90)

def lineapuntead():
    for i in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()


#cuadradoEnEspiral()

#cuadradoTriang()

#poligonos(6)

#cuadrado()

lineapuntead()
a = int(input("1 = Hombre \n2 = Mujer \n\n"))

