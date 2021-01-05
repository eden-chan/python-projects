from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {'UP': 90, 'RIGHT': 0, 'LEFT': 180, 'DOWN': 270}

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.number_of_segments = len(self.segments)
        self.tail = self.segments[self.number_of_segments - 1]


    def create_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.speed("slowest")
        segment.penup()
        return segment

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            new_segment = self.create_segment()
            new_segment.goto(pos)
            self.segments.append(new_segment)
        self.head = self.segments[0]
        self.number_of_segments = len(self.segments)
        self.tail = self.segments[self.number_of_segments - 1]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def move(self):
        number_of_seg = len(self.segments)
        for i in range(number_of_seg - 1, 0, -1):
            current_segment = self.segments[i]
            following_segment = self.segments[i - 1]
            current_segment.goto(following_segment.position())
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DIRECTIONS['DOWN']:
            self.head.setheading(DIRECTIONS['UP'])

    def turn_down(self):
        if self.head.heading() != DIRECTIONS['UP']:
            self.head.setheading(DIRECTIONS['DOWN'])

    def turn_right(self):
        if self.head.heading() != DIRECTIONS['LEFT']:
            self.head.setheading(DIRECTIONS['RIGHT'])

    def turn_left(self):
        if self.head.heading() != DIRECTIONS['RIGHT']:
            self.head.setheading(DIRECTIONS['LEFT'])

    def grow_segment(self):
        new_tail = self.create_segment()
        tail_heading = self.tail.heading()

        if tail_heading == DIRECTIONS['DOWN']:
            new_tail.goto(self.tail.xcor(), self.tail.ycor() + 20)
        elif tail_heading == DIRECTIONS['UP']:
            new_tail.goto(self.tail.xcor(), self.tail.ycor() - 20)
        elif tail_heading == DIRECTIONS['RIGHT']:
            new_tail.goto(self.tail.xcor() - 20, self.tail.ycor())
        else:
            new_tail.goto(self.tail.xcor()+20, self.tail.ycor())

        self.segments.append(new_tail)
        self.tail = new_tail
