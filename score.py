import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.write(f"Player 1: {self.score_1}  Player 2: {self.score_2}", align="center", font=("Arial", 24, "normal"))

    def increase_score_1(self, player):
        self.score_1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_2(self, player):
        self.score_2 += 1
        self.clear()
        self.update_scoreboard()
