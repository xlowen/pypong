import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5.0, 1.0)
        self.color("white")
        self.penup()
        self.setpos(x, y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
