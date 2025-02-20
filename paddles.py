from turtle import Turtle


class Paddle(Turtle):
    '''Game Paddle Control'''

    def __init__(self, one_or_two):
        super().__init__()

        if not one_or_two:
            self.one_or_two = one_or_two * 390
        else:
            self.one_or_two = one_or_two * 380
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(self.one_or_two, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
