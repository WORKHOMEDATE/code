from turtle import * 
pencolor("blue")
pensize(6)
penup()
goto(-100,-230)
pendown()
for i in range(12):
    forward(200)
    left(90)
    pencolor("red")
    forward(20)
    left(90)
    pencolor("green")
    forward(200)
    right(90)
    pencolor("purple")
    forward(20)
    right(90)
for i in range(120):
    undo()

done()