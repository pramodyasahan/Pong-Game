from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player_01 = Turtle()
player_01.shape("square")
player_01.color("white")
player_01.penup()
player_01.turtlesize(stretch_len=1, stretch_wid=5)
player_01.goto(x=350, y=0)


def go_up():
    y_cor = player_01.ycor() + 20
    player_01.goto(player_01.xcor(), y_cor)


def go_down():
    y_cor = player_01.ycor() - 20
    player_01.goto(player_01.xcor(), y_cor)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")

game_is_going = True
while game_is_going:
    screen.update()



screen.exitonclick()
