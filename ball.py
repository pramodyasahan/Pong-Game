from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.goto(x=0, y=0)
        self.new_x = 10
        self.new_y = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.new_x
        y_cor = self.ycor() + self.new_y
        self.goto(x_cor, y_cor)

    def bounce_ydir(self):
        self.new_y *= -1

    def bounce_xdir(self):
        self.new_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.new_x *= -1
