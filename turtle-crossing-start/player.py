from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_DIRECTION = {'UP':90}

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(STARTING_DIRECTION['UP'])
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)


    def check_finished(self):
        """Determines if turtle has reached the finish line."""
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)