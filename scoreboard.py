from turtle import Turtle


class Scoreboard(Turtle):

    score = 0

    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x, 280)
        self.write(f'0', False, "center", ("Arial", 80, "normal"))
        self.ht()

    def inc_p1(self):
        self.score += 1

    def inc_p2(self):
        self.score += 1

    def update_1(self):
        self.write(f'{self.score}', False, "center", ("Arial", 80, "normal"))

    def p1_scr_update(self):
        self.inc_p1()
        self.clear()
        self.update_1()

    def update_2(self):
        self.write(f'{self.score}', False, "center", ("Arial", 80, "normal"))

    def p2_scr_update(self):
        self.inc_p2()
        self.clear()
        self.update_1()

    def get_score(self):
        return self.score
