from turtle import Turtle, Screen
from newturtle import NewTurtle
from level import Level
from car import Car
import random
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = NewTurtle()
level = Level()
car = Car()
game_is_on = True
screen.listen()


screen.onkey(key="Up", fun=turtle.move_up)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()
    if turtle.ycor() > 280:
        turtle.reset_position()
        level.increase_level()
        car.increase_speed()

    for each_car in car.all_cars:
        if each_car.distance(turtle) < 20:
            game_is_on = False
            level.game_over()






















screen.exitonclick()