from turtle import *

pensize(10)

#leaves
pencolor('green')
penup()
goto(-50, 100)
pendown()
fillcolor('greenyellow')
begin_fill()

goto(50, 100)
goto(0, 50)
goto(-50, 100)
end_fill()

#stem
penup()
goto(0, 200)
pendown()
goto(0, 0)

#ve hinh tron 1
goto(0,200)
pencolor("deeppink")
fillcolor("pink")
begin_fill()
circle(100)
end_fill()

#ve hinh tron 2
penup()
goto(0,250)
pendown()

pencolor("yellow")
fillcolor("yellow")
begin_fill()
circle(50)
end_fill()

mainloop()