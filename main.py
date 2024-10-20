import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()

screen.title("Lowen's pong")
screen.bgcolor("black")
screen.screensize(800, 600)
screen.tracer(0)

scoreboard_1 = Scoreboard(-120)
scoreboard_2 = Scoreboard(140)
paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)

ball = Ball()


screen.listen()
screen.onkeypress(paddle_1.move_up, "Up")
screen.onkeypress(paddle_1.move_down, "Down")
screen.onkeypress(paddle_2.move_up, "w")
screen.onkeypress(paddle_2.move_down, "s")

game_is_on = True
ball.ball_heading()
forward = True
ball_speed = 0


while game_is_on:
    screen.update()
    time.sleep(0.1 + ball_speed)

    if forward:
        ball.ball_move_fw()

        if ball.distance(paddle_1) < 50 and ball.xcor() > 330:
            ball.ball_heading()
            ball_speed -= 0.01
            forward = False

    else:
        ball.ball_move_bw()

        if ball.distance(paddle_2) < 50 and ball.xcor() < -330:
            ball.ball_heading()
            ball_speed -= 0.01
            forward = True

    if ball.xcor() > 465:
        scoreboard_1.p1_scr_update()
        ball.reset()
        screen.update()
        time.sleep(1)
        ball_speed = 0
        forward = True

    if ball.xcor() < -465:
        scoreboard_2.p2_scr_update()
        ball.reset()
        screen.update()
        time.sleep(1)
        ball_speed = 0
        forward = False

    if ball.ycor() > 405:
        ball.bounce(ball.heading())

    if ball.ycor() < -405:
        ball.bounce(ball.heading())

    if scoreboard_1.get_score() == 5 or scoreboard_2.get_score() == 5:
        scoreboard_1.clear()
        scoreboard_2.clear()
        scoreboard_1.write("Game over. :)", False, "center", ("Arial", 40, "normal"))
        game_is_on = False

screen.exitonclick()
