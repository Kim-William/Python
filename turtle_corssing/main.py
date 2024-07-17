import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard =Scoreboard()

screen.onkeypress(player.move_player, "Up")
car_manager.make_new_car()

game_is_on = True
# while True:
#     is_play = screen.textinput(title = "Do you want to play game?", prompt="Press 'y' to play this game : ").lower()

#     print(is_play)
#     if is_play == 'y':
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_new_car()
    car_manager.move_cars()

    if player.goal():
        car_manager.level_up()
        scoreboard.increase_level()
        player.reset_player()

    for car in car_manager.cars:
        if car[0].distance(player) < 20:
            print("collision!")
            game_is_on = False
            scoreboard.game_over()
    # else:
    #     break



screen.exitonclick()