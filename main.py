import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()

screen.tracer(0)
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"w")
screen.onkey(player.back,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #Detecting collision with the cars
    for car in cars.all_cars:
        if (player.distance(car) < 25 and player.ycor()-15 <= car.ycor()) or (player.distance(car) < 25 and car.ycor() <= player.ycor()+10):
            print("You have been hit")
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update_score_board()
        cars.level_up()

screen.exitonclick()