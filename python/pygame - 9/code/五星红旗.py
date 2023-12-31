import turtle as t

# 颜色
t.bgcolor("red")
t.pencolor("yellow")
t.fillcolor("yellow")
t.setup(1280, 800, 0, 0)
t.speed(5)

# 画五角函数
def five_star(x, y, heading, fw):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(fw)
        t.right(144)
    t.end_fill()

five_star(-520, 240, 0, 240)       # 大五角星
five_star(-230, 345, 305, 70)      # 第二颗五角星
five_star(-150, 230, -8, 70)       # 第三颗五角星
five_star(-150, 150, -35, 70)      # 第四颗五角星
five_star(-230, 68, 300, 70)       # 第五颗五角星

t.hideturtle()
t.done()
