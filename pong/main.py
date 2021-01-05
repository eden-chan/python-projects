from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
import ball
import time

# TODO Background
BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600
background = Screen()
background.title("My Pong Game")
background.setup(width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
background.bgcolor("black")
background.tracer(0)

# TODO dashed-line in the middle
dashed_midline = Turtle()
dashed_midline.penup()
dashed_midline.color("white")
dashed_midline.speed("fastest")
dashed_midline.hideturtle()
dashed_midline.goto(0, -300)
dashed_midline.setheading(90)

number_of_dashes = 30
dash_length = 10
gap_length = 10
for _ in range(number_of_dashes):
    background.update()
    dashed_midline.pendown()
    dashed_midline.forward(dash_length)
    dashed_midline.penup()
    dashed_midline.forward(gap_length)

# TODO paddle
# - generate paddles
PADDLE_STARTING_POSITIONS = {'LEFT_PADDLE_STARTING_POSITION': (-360, 0),
                             'RIGHT_PADDLE_STARTING_POSITION': (360, 0)}

l_paddle = Paddle('blue')
r_paddle = Paddle('red')

l_paddle.goto(PADDLE_STARTING_POSITIONS['LEFT_PADDLE_STARTING_POSITION'])
r_paddle.goto(PADDLE_STARTING_POSITIONS['RIGHT_PADDLE_STARTING_POSITION'])

background.update()


# TODO Scoreboard


# TODO Ball
# move ball
size = float(background.textinput(title='Ball Sizer', prompt =
'how big do you want your ball?' ))


ball = ball.Ball(size)
scoreboard = Scoreboard()
game_is_on = True

# move paddles
background.listen()
background.onkey(key='Up', fun=r_paddle.up)
background.onkey(key='Down', fun=r_paddle.down)
background.onkey(key='o', fun=l_paddle.up)
background.onkey(key='q', fun=l_paddle.down)

while game_is_on:
    time.sleep(0.05)
    ball.move()
    background.update()
    x = ball.xcor()
    y = ball.ycor()
    if y > 280 or y < -280:
        ball.bounce_wall()
    elif x > 350 and ball.distance(r_paddle) < 50 or x < -350 and ball.distance(l_paddle) < 50:
        ball.bounce_paddle()
    elif x > 350:
        ball.reset_position()
        scoreboard.l_point()
    elif x < -350:
        scoreboard.r_point()
        ball.reset_position()


# detect collision with wall
# detect collision with paddle
# collision angle change
# speed of ball change

background.exitonclick()
