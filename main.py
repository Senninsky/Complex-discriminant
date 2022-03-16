# Importation
import turtle
import random

# Drawing
#Drawing finish
drawer = turtle.Turtle()
drawer.color('black')
drawer.shape('turtle')

drawer.penup()
drawer.goto(150, 200)

drawer.pensize(6)
drawer.pendown()
drawer.right(90)
drawer.forward(200)

# Turtle initialization
tur1 = turtle.Turtle()
tur1.color('green')
tur1.shape('turtle')

tur1.penup()
tur1.goto(-360, 150)
tur1.pendown()

tur2 = turtle.Turtle()
tur2.color('red')
tur2.shape('turtle')

tur2.penup()
tur2.goto(-360, 100)
tur2.pendown()

tur3 = turtle.Turtle()
tur3.shape('turtle')
tur3.color('blue')

tur3.penup()
tur3.goto(-360, 50)
tur3.pendown()

# Initialization variables
racing = True
turtles = [tur1, tur2, tur3]

# Racing loop
while racing:
    tur1.forward(random.randint(1,10))
    tur2.forward(random.randint(1,10))
    tur3.forward(random.randint(1,10))

    if tur1.xcor() >= 150:
        print('Turtle 1 wint!')
        racing = False 
    elif tur2.xcor() >= 150:
        print('Turtle 2 wint!')
        racing = False
    elif tur3.xcor() >= 150:
        print('Turtle 3 wint!')
        racing = False