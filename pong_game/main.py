from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong game")
screen.tracer(0)

r_paddle= Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkeypress(key = "Up", fun = r_paddle.go_up)
screen.onkeypress(key = "Down", fun = r_paddle.go_down)

screen.onkeypress(key = "w", fun = l_paddle.go_up)
screen.onkeypress(key = "s", fun = l_paddle.go_down)

ball = Ball()
scoreboard = Scoreboard()

game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if (ball.distance(r_paddle) <50  or ball.distance(l_paddle) < 50) and abs(ball.xcor())>320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.increase_left_score()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick()

