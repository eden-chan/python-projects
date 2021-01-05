from turtle import Turtle, Screen
import random
canvas = Screen()

racers_colors = ['blue', 'green', 'orange', 'red', 'purple', 'black']
racers = {}
canvas.colormode(255)


def generate_racers(number_of_racers):
    start_y = number_of_racers * 20
    for i in range(number_of_racers):
        racer = Turtle("turtle")
        racer.speed("slow")
        racer.color(racers_colors[i])
        racer.penup()
        racer.goto(x=-240, y=start_y)
        racers[racers_colors[i]] = racer
        start_y-=50
    return racers

def race(racers):
    number_of_racers = len(racers_colors)
    race_is_on = True
    finish_line = int(canvas.window_width() / 2) - 20
    current_racer_index = 0
    while race_is_on:
        current_racer_index = (current_racer_index + 1) % number_of_racers
        pace = random.randint(10,50)
        current_racer_color = racers_colors[current_racer_index]
        current_racer = racers[current_racer_color]



        current_racer.forward(pace)
        if current_racer.xcor() >= finish_line:
            winner_color = current_racer_color
            race_is_on = False

    return winner_color

canvas.setup(height= 400, width=500)
racers = generate_racers(6)
user_bet = canvas.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color").lower()
winner_color = race(racers)
if user_bet == winner_color:
    print("YOU WON")
else:
    print(f"You lost. {winner_color} turtle won!")
canvas.exitonclick()