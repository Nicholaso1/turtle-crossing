from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Scoreboard text"""
        self.clear()
        self.goto(-260, 240)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update_score(self):
        """Update score"""
        self.score += 1
        self.update_scoreboard()

