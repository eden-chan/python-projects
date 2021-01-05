from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.refresh()

    def refresh(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode = 'w') as file:
                file.write(str(self.highscore))

        self.write(f"Score: {self.score} Highscore: {self.highscore}", align= ALIGNMENT, font= FONT)

    def final_score(self):
        self.clear()
        self.write(f"Game Over! Your final score is: {self.score} ", align= ALIGNMENT, font= FONT)