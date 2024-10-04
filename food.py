from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.relocate()
        
    def relocate(self):
        x_cor=random.randint(-230,230)
        y_cor=random.randint(-230,230)
        self.goto(x_cor,y_cor)
      