import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key = 'Up', fun = player.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    is_next_round_on = player.check_finished()
    if is_next_round_on:
        scoreboard.score+=1
        scoreboard.refresh()

    for car in cars.cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()