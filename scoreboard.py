from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=0
        self.up()
        self.level_up()
        self.hideturtle()
        self.goto(x=-290, y=260)
        self.update_scoreboard()

    def level_up(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):

        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

