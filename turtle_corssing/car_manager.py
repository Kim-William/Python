from turtle import Turtle
from threading import Thread
import random, time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []  
        self.move_speed = STARTING_MOVE_DISTANCE
        self.maximun_car_number=30
        self.wait_for_claer = False

    def make_new_car(self):
        if random.randint(1,2) == 2 and len(self.cars) < self.maximun_car_number:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(280, random.randint(-240,240))
            self.cars.append((new_car, random.randint(int(self.move_speed), self.move_speed)))

    def move_cars(self):
        while self.wait_for_claer:
            time.sleep(0.01)

        for car in self.cars:
            car[0].goto(car[0].xcor() - car[1],  car[0].ycor())
            if car[0].xcor() < -320:
                self.cars.remove(car)

    def level_up(self):
        self.wait_for_claer= True
        for car in self.cars:
            car[0].goto(-350,0)
            car[0].clear()
        self.cars.clear()
        self.maximun_car_number += 10
        self.move_speed += MOVE_INCREMENT
        self.wait_for_claer= False
