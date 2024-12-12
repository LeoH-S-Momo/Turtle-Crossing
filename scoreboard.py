from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=("Arial", 24, "normal"))

    def increase_level(self):
        self.score += 1
        self.update_score_board()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "normal"))
