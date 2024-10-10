from logging import setLogRecordFactory
from turtle import Turtle
STARTING_POSITION=(0,-200)
STEP=10
FINISH_LINE_Y=200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        y_pos = self.ycor() + STEP
        self.goto(0,y_pos)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor()>280:
            return True
        else:
            return False