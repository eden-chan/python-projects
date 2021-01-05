from turtle import Turtle

BALL_WIDTH_FACTOR = 0.5
BALL_LENGTH_FACTOR = 0.5
STARTING_HEADING = 45
class Ball(Turtle):

    def __init__(self, size):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=BALL_WIDTH_FACTOR * size, stretch_len= BALL_LENGTH_FACTOR * size)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1.1


    def reset_position(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
