import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_is_on = True
player = Player()
screen.onkey(player.move_up, "Up")
cars = CarManager()
game_score = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move_cars()
    for car in cars.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            game_score.show_game_over()
    if player.is_reached_finish():
        player.go_to_the_start()
        game_score.increase_level()
        cars.increase_level()

screen.exitonclick()
