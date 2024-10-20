from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize()
        self.color("white")
        self.penup()
        self.speed(1)

    def ball_heading(self):
        x = random.randint(-45, 45)
        self.setheading(x)

    def ball_move(self):
        self.forward(15)