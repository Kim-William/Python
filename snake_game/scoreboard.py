from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score:{self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font =FONT)
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font =FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score=0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", False, align=ALIGNMENT, font =FONT)
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def load_high_score(self):
        with open('data.txt') as file:
            hiscore = file.read()
        self.high_score = int(hiscore)
        
    def save_high_score(self):
        with open('data.txt', mode='w') as file:
            file.write(str(self.high_score))