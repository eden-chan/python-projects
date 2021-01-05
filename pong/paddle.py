from turtle import Turtle

PADDLE_LENGTH_STRETCH_FACTOR = 1
PADDLE_WIDTH_STRECH_FACTOR = 5
PADDLE_MOVEMENT = 10

# TODO Paddles


class Paddle(Turtle):
    def __init__(self, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=PADDLE_LENGTH_STRETCH_FACTOR, stretch_wid=PADDLE_WIDTH_STRECH_FACTOR)

    def up(self):
        if self.ycor() < 280:
            self.sety(self.ycor() + 10)
    def down(self):
        if self.ycor() > -280:
             self.sety(self.ycor() - 10)


