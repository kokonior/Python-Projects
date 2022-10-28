from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score=Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_on=True

while game_on :
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 380 or ball.ycor() < -380 :
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
   
    if ball.xcor() > 380  :
        ball.reset_pos()
        score.l_point()
        
    if  ball.xcor() < -380 :
        ball.reset_pos()
        score.r_point()
        
screen.exitonclick()
