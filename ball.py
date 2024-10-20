from turtle import Turtle
import random


class Ball(Turtle):

    heading_1 = 0

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize()
        self.color("white")
        self.penup()
        self.speed(1)

    def ball_heading(self):
        self.heading_1 = random.randint(-65, 65)
        self.setheading(self.heading_1)

    def ball_move_fw(self):
        self.forward(15)

    def ball_move_bw(self):
        self.backward(15)

    def bounce(self, heading):
        self.setheading(-heading)

    def bounce_back(self):
        self.setheading(-self.heading_1)

    def reset(self):
        self.goto(0, 0)
        self.ball_heading()
