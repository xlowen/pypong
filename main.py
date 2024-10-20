import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
screen = Screen()

screen.title("Lowen's pong")
screen.bgcolor("black")
screen.screensize(800, 600)
screen.tracer(0)


paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)

ball = Ball()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_is_on = True
ball.ball_heading()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.ball_move()

# todo Create Screen
# todo Create and move paddle
# todo Create another paddle
# todo Create ball and move it
# todo detect collision with wall and bounce
# todo detect collision with paddle and bounce
# todo detect detect paddle miss
# todo detect keep score







screen.exitonclick()