import turtle as t

import random

# def dash(dash_len, length):
#     repeat = int(length / dash_len)
    
#     for _ in range(int(repeat/2)):
#         tim.forward(dash_len)
#         tim.penup()
#         tim.forward(dash_len)
#         tim.pendown()
#     drawn_len = repeat * dash_len
#     if drawn_len < length:
#         tim.forward(length - drawn_len)
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for n in range(num_sides):
#         tim.forward(3)
#         if num_sides % 2 == 0:
#             tim.right(angle)
#         else :
#             tim.left(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

tim = t.Turtle()
t.colormode(255)

tim.speed(0)
tim.color("red","green")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# tim.pen()

# dash(10, 100)

# draw_shape(360)

# for shape_side_n in range(3,360):
#     draw_shape(shape_side_n)

# direction = [0,90,180,270]

# for _ in range(1000):
#     tim.color(random_color())
#     tim.forward(random.randint(0, 30))
#     tim.setheading(random.choice(direction))

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.setheading(tim.heading() + size_of_gap)
#         tim.circle(100)

# tim.home()


# tim.circle(120,180)

# draw_spirograph(5)
tim.penup()
for y in range(0,10):
    for x in range(0,10):
        tim.setpos(x*50 - 250, y*50 - 250)
        tim.dot(20, random_color())

screen = t.Screen()

screen.exitonclick()