from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.up()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-260,260))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT