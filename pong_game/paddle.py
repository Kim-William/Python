from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        print(f"Up : {self.ycor()}")
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor()-20)



