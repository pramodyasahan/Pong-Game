from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
