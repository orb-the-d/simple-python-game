from turtle import Screen
import time
from player import Player
from car_manager import Car
from scoreboard import Score

screen=Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player=Player()
car_manager = Car()
score=Score()



screen.listen()
screen.onkey(player.up,"Up")

game_on = True
while game_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.car_list:
        if car.distance(player)<20:
            score.game_over()
            game_on=False

    if player.finish_line():
        player.go_to_start()
        car_manager.speed_up()
        score.level_up()























screen.exitonclick()