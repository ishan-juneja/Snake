from turtle import Screen, Turtle  # importing the classes
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

x = 0
y = 0
turtle_list = []

# screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # we turn off the animations so we can control when the


# creating the snake blocks
snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

#animating the turtle
game_is_on = True
while game_is_on:

    time.sleep(0.08)

    #giving user control over snake
    screen.onkey(fun=snake.up, key="w")
    screen.onkey(fun=snake.down, key="s")
    screen.onkey(fun=snake.left, key="a")
    screen.onkey(fun=snake.right, key="d")



    screen.update()
    screen.listen()
    if snake.turtle_list[0].distance(food) < 15:
        food.refresh()
        scoreboard.increment()
        snake.extend()


    #detect wall collision

    if snake.turtle_list[0].xcor() > 280 or snake.turtle_list[0].xcor() < -280 or snake.turtle_list[0].ycor() > 280 or snake.turtle_list[0].ycor() < -280:
        snake.reset()
        scoreboard.game_over()


    print(snake.check_coil())
    if snake.check_coil() == True:
        print("Snake has collided with itself")
        snake.reset()
        scoreboard.game_over()

    snake.move()



screen.exitonclick()
