from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.y_move = MOVE_DISTANCE

    def move_up(self):
        """Go up"""
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        """New level, reset player's position"""
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)
