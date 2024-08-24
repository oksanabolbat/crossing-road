from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 255)
        self.show_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_level()

    def show_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def show_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
