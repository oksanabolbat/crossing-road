from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.go_to_the_start()
        self.shape("turtle")


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_reached_finish(self):
        return self.ycor() > 280

    def go_to_the_start(self):
        self.goto(STARTING_POSITION)

