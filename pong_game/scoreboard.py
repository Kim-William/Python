from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score= 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-100, 250)
        self.write(self.l_score, False, align=ALIGNMENT, font =FONT)
        self.goto(100, 250)
        self.write(self.r_score, False, align=ALIGNMENT, font =FONT)
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, False, align=ALIGNMENT, font =FONT)
        self.goto(100, 250)
        self.write(self.r_score, False, align=ALIGNMENT, font =FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", False, align=ALIGNMENT, font =FONT)
    
    def increase_left_score(self):
        self.l_score+=1
        self.update_scoreboard()

    def increase_right_score(self):
        self.r_score+=1
        self.update_scoreboard()