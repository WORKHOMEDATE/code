import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Sky")

# Create a turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)  # Set the drawing speed to the maximum

# Function to draw a star
def draw_star(size):
    star_turtle.color("white")
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Draw stars randomly on the screen
for _ in range(100):
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)

    size = random.uniform(1, 4)
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    
    draw_star(size)

# Hide the turtle and display the window
star_turtle.hideturtle()
turtle.done()