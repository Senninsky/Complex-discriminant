# Importation
import turtle
import time

# Input
n = int(input('Hoeveel hoeken en zijdes moet je figuur hebben? '))
length_side = int(input('Hoelang moeten de zidjes van je figuur zijn? '))

# Calculations
hoek = 360 / n

# Initializations
counter = 0

# Turtle drawing
while counter < n:
    turtle.forward(length_side)
    turtle.right(hoek)
    counter += 1
    time.sleep(2)
