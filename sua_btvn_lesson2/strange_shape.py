
from turtle import *
import math

a = 100

#first square
forward(a)
right(90)
forward(a)
right(90)
forward(a)
right(90)
forward(a)

#second square
penup()
# xem cach 3 cua video de hieu dong 19: 
forward(a * (math.sqrt(2) - 1) / 2)
right(90)
forward(a/2)
pendown()

right(45)
forward(a)

right(90)
forward(a)

right(90)
forward(a)

right(90)
forward(a)

mainloop()