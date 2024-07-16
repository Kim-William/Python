from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_heading_counter_clockwise():
    tim.setheading(tim.heading()-5)

def rotate_heading_clockwise():
    tim.setheading(tim.heading()+5)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=rotate_heading_counter_clockwise)
screen.onkeypress(key="d", fun=rotate_heading_clockwise)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()