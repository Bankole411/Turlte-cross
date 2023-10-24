from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.move_level()
        

    def move_level(self):
        self.clear()
        self.goto(-220, 270)
        self.write(f"Level: {self.score}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 20, "normal"))
