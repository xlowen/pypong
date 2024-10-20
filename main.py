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
forward = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if forward:
        ball.ball_move_fw()

        if ball.distance(paddle_1) < 50 and ball.xcor() > 330:
            print("ball.xcor() é:  " + str(ball.xcor()))
            ball.ball_heading()
            forward = False

    else:
        ball.ball_move_bw()

        if ball.distance(paddle_2) < 50 and ball.xcor() < -330:
            print("ball.xcor() é:  " + str(ball.xcor()))
            ball.ball_heading()
            forward = True

    if ball.xcor() > 465 or ball.xcor() < -465:
        print("outside at x", ball.xcor())
        game_is_on = False

    if ball.ycor() > 405 or ball.ycor() < -405:
        print("outside at y", ball.ycor())
        ball.bounce(ball.heading())


# todo Create Screen
# todo Create and move paddle
# todo Create another paddle
# todo Create ball and move it
# todo detect collision with wall and bounce
# todo detect collision with paddle and bounce
# todo detect detect paddle miss
# todo detect keep score







screen.exitonclick()