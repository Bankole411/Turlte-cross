from turtle import Turtle
import random

STARTING_CAR_SPEED = 10

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = "#{:02X}{:02X}{:02X}".format(r, g, b) 
    return random_color

class Car():
    def __init__(self):
        self.all_cars =[]
        self.speed = STARTING_CAR_SPEED
        
    def create_car(self):
        random_number = random.randint(0, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random_color())
            random_ycor = random.randint(-250, 250)
            new_car.goto(300, random_ycor)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += 5
        self.move_car()
