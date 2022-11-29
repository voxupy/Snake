from turtle import Turtle

FONT = ("Arial",24,"normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        with open("highest_score.txt") as data:
            self.highest_score = int(data.read())

        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highest_score}", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode='w') as file:
                file.write(f'{self.highest_score}')
        self.score = 0
        self.update_scoreboard()
