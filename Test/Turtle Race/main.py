from turtle import Turtle, Screen
import random

def init_turtle(turtle, color, position):
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(position)

colors = ["Green", "Blue", "Red", "Purple", "Yellow", "Orange"]
y_positions = [-100, -50, 0, 50, 100, 150]

screen =Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color (Green, Blue, Red, Purple, Yellow, Orange): ").lower()
print(user_bet)

all_turtle = []

is_race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle()
    init_turtle(new_turtle, colors[turtle_index], (-230,y_positions[turtle_index]))
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winnercolor = turtle.pencolor().lower()
            break

if user_bet == winnercolor:
    print (f"You've won! The {winnercolor} turtle is the winner!")
else:
    print (f"You've lost! The {winnercolor} turtle is the winner!")

print(winnercolor)
    


screen.exitonclick()