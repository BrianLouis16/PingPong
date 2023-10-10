from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")

# Create a Scoreboard instance
scoreboard = Scoreboard()

screen.tracer(0)

paddle_1 = Paddle()
paddle_2 = Paddle()
paddle_2.create_paddle_two()

ball = Ball()


def up_paddle_1():
    new_y = paddle_1.ycor() + 40  # Adjust the new y-coordinate
    paddle_1.goto(paddle_1.xcor(), new_y)


def down_paddle_1():
    new_y = paddle_1.ycor() - 40  # Adjust the new y-coordinate
    paddle_1.goto(paddle_1.xcor(), new_y)


def up_paddle_2():
    new_y = paddle_2.ycor() + 40  # Adjust the new y-coordinate
    paddle_2.goto(paddle_2.xcor(), new_y)


def down_paddle_2():
    new_y = paddle_2.ycor() - 40  # Adjust the new y-coordinate
    paddle_2.goto(paddle_2.xcor(), new_y)


def exit_game():
    screen.bye()  # Close the Turtle graphics window


screen.listen()
screen.onkeypress(up_paddle_1, "Up")
screen.onkeypress(down_paddle_1, "Down")
screen.onkeypress(up_paddle_2, "w")
screen.onkeypress(down_paddle_2, "s")
screen.onkeypress(exit_game, "q")



game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(paddle_1) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(paddle_2) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 350:
        # Player 2 scores a point
        ball.reset_position()
        scoreboard.increase_score_2(paddle_2)

    if ball.xcor() < -350:
        # Player 1 scores a point
        ball.reset_position()
        scoreboard.increase_score_1(paddle_1)

