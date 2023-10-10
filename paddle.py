from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)  # You should use 'self' here to set the position of the paddle object

    def create_paddle_two(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(-350, 0)
