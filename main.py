from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_going = True
while game_is_going:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ydir()
        ball.move()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_xdir()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
