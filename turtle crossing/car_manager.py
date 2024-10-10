from turtle import Turtle
import  random



COLOR_LIST=["black","blue","red","brown","pink","gray","green","yellow"]
class Car:
    def __init__(self):
        self.car_list=[]
        self.car_speed=5

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.goto(300,random.randint(-250,250))
            self.car_list.append(new_car)

    def speed_up(self):
        self.car_speed+=2

    def move(self):
        for car in self.car_list:
            car.backward(5)

