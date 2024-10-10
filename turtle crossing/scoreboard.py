from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.lever=1
        self.goto(-280, 250)
        self.update()


    def update(self):
        self.clear()
        self.write(f"level :{self.lever}", align="left")

    def level_up(self):

        self.lever+=1
        self.update()

    def game_over(self):
        self.write("game over ",align="center")