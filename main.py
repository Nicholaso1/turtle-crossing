import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # Instantiate cars
    if randint(1,15) == 1:
        car.make_car()
    car.move_car()

    # Finish line
    if player.ycor() >= 230:
        car.speed_up()
        player.reset_position()
        score_board.update_score()

    # Detect collision with cars
    if car.check_collision(player):
        player.game_over()
        game_is_on = False

screen.exitonclick()