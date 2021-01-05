from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
SCOREBOARD_POS = (-200, 225)
GAME_OVER_POS = (0, 225)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.refresh()


    def refresh(self):
        self.clear()
        self.goto(SCOREBOARD_POS)
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.clear()
        self.goto(GAME_OVER_POS)
        self.color('red')
        self.write(f"GAME OVER! Score: {self.score}", align=ALIGNMENT, font=FONT)