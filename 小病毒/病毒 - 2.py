from turtle import * 

speed(0)
Screen().setup(1.0,1.0)
bgcolor('black')
color('green')
for i in range(200):
    left(i)
    forward(i * 3)
    i -= 1
done()