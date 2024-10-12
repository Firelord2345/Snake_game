from turtle import Turtle
FONT=("Arial",24,"normal")
ALIGN="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,230)
        self.update_score()
        self.hideturtle()
            
    def reset(self):
        if self.score>self.high_score:
                self.high_score=self.score
        with open("data.txt",mode="w") as update:
            update.write(f'{self.high_score}')
        self.score=0  
        self.update_score()
        
    def update_score(self):
        
        self.clear()
        self.write(f"SCORE:{self.score} HighScore:{self.high_score}",align=ALIGN,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAMEOVER ",align=ALIGN,font=FONT)
    def increase(self):
        self.score+=1
        
        self.clear()
        self.update_score()