import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game = True
while game:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            scoreboard.game_over()

    if player.finish_line():
        player.go_start()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()