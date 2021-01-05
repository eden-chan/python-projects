from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 20
SAFE_ZONE = {'START': -200, 'FINISH': 200}
SIDE_EDGES = {'LEFT': -300, 'RIGHT': 300}
CAR_GAP = 30

STARTING_DIRECTION = {'LEFT': 180}

class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

        for i in range(NUMBER_OF_CARS):
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(STARTING_DIRECTION['LEFT'])
            self.cars.append(new_car)

        self.refresh()

    def refresh(self):
        for i in range(NUMBER_OF_CARS):
            current_car = self.cars[i]
            current_car.hideturtle()

            must_generate_again = True

            while must_generate_again:
                must_generate_again = False
                random_xcor = random.randint(SIDE_EDGES['LEFT'], SIDE_EDGES['RIGHT'])
                random_ycor = random.randint(SAFE_ZONE['START'], SAFE_ZONE['FINISH'])
                current_car.goto(random_xcor,random_ycor)
                for car in self.cars[0:i]:
                    if current_car.distance(car) < CAR_GAP:
                        must_generate_again = True

            current_car.showturtle()


    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() <= SIDE_EDGES['LEFT']:
                car.setx(SIDE_EDGES['RIGHT'])

    def level_up(self):
        self.move_distance += MOVE_INCREMENT



