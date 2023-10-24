from turtle import Turtle

TURTLE_SPEED =10

class NewTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0 , -280)

    def move_up(self):
        self.forward(TURTLE_SPEED)
    
    
    def move_down(self):
        self.backward(TURTLE_SPEED)


    def reset_position(self):
        self.clear()
        self.goto(0 , -280)