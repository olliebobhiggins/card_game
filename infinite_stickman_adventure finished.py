import turtle
import time

# Set up the screen correctly
window = turtle.Screen()
window.bgcolor("white")
window.title("Infinite Stickman Adventure!")

# Create our stickman
stick = turtle.Turtle()
stick.speed(0)
stick.pensize(3)

def draw_stickman(x, y):
    stick.clear()
    stick.penup()
    stick.goto(x, y)
    stick.pendown()
    
    # Head
    stick.circle(15)
    
    # Body
    stick.right(90)
    stick.forward(50)
    
    # Legs
    stick.right(30)
    stick.forward(40)
    stick.backward(40)
    stick.left(60)
    stick.forward(40)
    stick.backward(40)
    
    # Back to center
    stick.right(30)
    stick.backward(25)
    
    # Arms
    stick.right(90)
    stick.forward(25)
    stick.backward(50)

# Starting position
x = 0
y = 0

# Move stickman with arrow keys
def move_right():
    global x
    x += 10
    draw_stickman(x, y)

def move_left():
    global x
    x -= 10
    draw_stickman(x, y)

def move_up():
    global y
    y += 10
    draw_stickman(x, y)

def move_down():
    global y
    y -= 10
    draw_stickman(x, y)

# Set up key controls
window.onkey(move_right, "Right")
window.onkey(move_left, "Left")
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.listen()

# Draw initial stickman
draw_stickman(x, y)

# Keep the window open (using the correct command)
window.mainloop() 