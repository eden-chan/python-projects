from turtle import Turtle, Screen
import time
from Snake import Snake
import food
import scoreboard

# TODO create background
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)

food = food.Food()
scoreboard = scoreboard.Scoreboard()

# TODO CREATE Snake Bod

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    xcor = snake.head.xcor()
    ycor = snake.head.ycor()

    # Collision with Border
    if xcor > 280 or xcor < -280 or ycor > 280 or ycor < -280:
        game_is_on = False
        scoreboard.final_score()
        play_again = screen.textinput(title="Game Over! You hit the wall!",
                                      prompt="Do you want to play again? [y or n]").lower()
    else:
        snake.move()
        # Collision with Food
        if snake.head.distance(food) < 15:
            snake.grow_segment()
            food.refresh()
            scoreboard.score += 1
            if scoreboard.score > scoreboard.highscore:
                scoreboard.highscore = scoreboard.score
            scoreboard.refresh()

        # Collision with Body
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.final_score()
                play_again = screen.textinput(title="Game Over! You hit your Own tail!"
                                              , prompt="Do you want to play again? [y or n]").lower()

    if not game_is_on:
        if play_again == 'y':
            game_is_on = True
            scoreboard.score = 0
            scoreboard.refresh()
            food.refresh()
            snake.reset()
            screen.listen()
            screen.onkey(key="Up", fun=snake.turn_up)
            screen.onkey(key="Down", fun=snake.turn_down)
            screen.onkey(key="Left", fun=snake.turn_left)
            screen.onkey(key="Right", fun=snake.turn_right)

screen.exitonclick()