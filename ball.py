from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 10  # Horizontal velocity
        self.dy = 10  # Vertical velocity

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1  # Reverse the vertical velocity to bounce off surfaces

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0,0)
