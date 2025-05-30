from turtle import Turtle
from random import choice, uniform

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITION = (-230, 230)

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        """Create a single car randomly positioned on right side of the screen"""
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.goto(300, uniform(Y_POSITION[0], Y_POSITION[1]))
        self.all_cars.append(new_car)

    def move_car(self):
        """Move all cars to the left and delete off-screen cars"""
        for i in range(len(self.all_cars) - 1,-1,-1):
            car = self.all_cars[i]
            car.backward(self.car_speed)

            # Remove off-screen cars
            if car.xcor() < -320:
                car.hideturtle()
                del self.all_cars[i]

    def speed_up(self):
        """Increase speed of all cars"""
        self.car_speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.all_cars:
            if player.distance(car) < 25:
                return True
        return False




