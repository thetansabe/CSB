
from turtle import *
import math

black = 200
red = 180

forward(black)

# chu M
pensize(10)
pencolor("red")
left(90)
forward(red)

left(180 - 45)
forward(black*math.sqrt(2)/2)

right(90)
forward(black*math.sqrt(2)/2)

left(red - 45)
forward(red)

#net gach den

shape("turtle")
backward(red)
left(90)

pensize(1)
pencolor("black")
forward(black)

# move con rua
penup()
backward(black / 2)
left(90)
forward(40)

mainloop()