from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_level(self):
        self.move_speed += MOVE_INCREMENT

