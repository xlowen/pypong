from turtle import Turtle
import random
class Ball(Turtle):


    heading_1 = 0;

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize()
        self.color("white")
        self.penup()
        self.speed(1)

    def ball_heading(self):
        self.heading_1 = random.randint(-65, 65)
        print("random heading value = " + str(self.heading_1))
        self.setheading(self.heading_1)

    def ball_move_fw(self):
        self.forward(15)

    def ball_move_bw(self):
        self.backward(15)
    def bounce(self, heading):
        print("this is the y angle: " + str(self.heading_1) + "this is the angle it should go: " + str(-self.heading_1))
        self.setheading(-heading)

    def bounce_back(self):
        self.setheading(-self.heading_1)