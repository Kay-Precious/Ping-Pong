from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Screen Set-up
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

# Paddles and Ball
r_paddle = Paddle(+1)
l_paddle = Paddle(-1)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True                   # Switch on/off
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # DETECT COLLISION WITH WALL
    if ball.ycor() > 281 or ball.ycor() < -281:
        ball.bounce_y()
    # DETECT COLLISION WITH WALL
    if ball.distance(r_paddle) < 51 and ball.xcor() > 356 or ball.distance(l_paddle) < 51 and ball.xcor() < -366:
        ball.bounce_x()

    # DETECT IF R MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # DETECT IF L MISSES
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
