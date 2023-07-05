from turtle import Turtle
import random

class Food(Turtle):# inheriting turtle method
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
        self.color("purple")
        self.speed("fastest")
        random_x = round(random.randint(-14, 14)) * 20
        random_y = round(random.randint(-14, 14)) * 20
        self.setposition(x=random_x, y=random_y)

    def refresh(self):
        random_x = round(random.randint(-14, 14)) * 20
        random_y = round(random.randint(-14, 14)) * 20
        self.setposition(x=random_x, y=random_y)


