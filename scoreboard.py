from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font= ('courier', 80, 'normal'))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font= ('courier', 80, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()
