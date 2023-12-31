import time
from turtle import * 
pensize(3)
fillcolor('black')
begin_fill()
circle(100,180)
circle(50,180)
circle(-50,180)
end_fill()
circle(-100,180)

penup()
goto(0,150)
dot(20,'white')

goto(0,50)
dot(20,'black')
hideturtle()
time.sleep(3)