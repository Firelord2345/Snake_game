from turtle import Turtle
FONT=("Arial",24,"normal")
ALIGN="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,230)
        self.update_score()
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"SCORE:{self.score} ",align=ALIGN,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER ",align=ALIGN,font=FONT)
    def increase(self):
        self.score+=1
        self.clear()
        self.update_score()