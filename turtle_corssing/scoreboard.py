from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
SCORE_POSITION = (-280,250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.color("black")
        self.level = 0
        self.write(f"Level: {self.level}",False, ALIGNMENT, FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",False, ALIGNMENT, FONT)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", False, align="center", font =FONT)
    