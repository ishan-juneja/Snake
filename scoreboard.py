from turtle import Turtle

class Scoreboard(Turtle):
    score_counter = 0

    def __init__(self):
        super().__init__()
        self.setposition(-288, 275)
        self.color("white")
        with open("highscore.text", mode='r') as file:
            score = file.read()
        self.high_score_counter = int(score)
        self.clear()
        self.write(f"{self.score_counter}", font=("Arial", 20, "normal"), align="center")
        self.hideturtle()

    def increment(self):
        self.score_counter += 1
        if(self.score_counter > self.high_score_counter):
            self.high_score_counter = self.score_counter
            with open("highscore.text", mode='w') as file:
                score = file.write(str(self.high_score_counter))
        self.clear()
        self.write(f"{self.score_counter}   HS: {self.high_score_counter}", font=("Arial", 20, "normal"), align="left")

    def game_over(self):
        self.score_counter = 0
        self.clear()
        self.write(f"{self.score_counter}   HS: {self.high_score_counter}", font=("Arial", 20, "normal"), align="left")

