from turtle import Screen
import time
from scoreboard import Scoarboard
from food import Food
from snake import Snake

score = Scoarboard()


def difficulty(level):
    if level == 1:
        return time.sleep(0.4)
    if level == 2:
        return time.sleep(0.2)
    if level == 3:
        return time.sleep(0.08)
    if level == 4:
        return time.sleep(0.06)
    if level == 5:
        return time.sleep(0.04)


def game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    level = int(screen.textinput('Level', 'Choose from level 1 to 5'))
    screen.tracer(0)
    score.update_create_scoreboard()
    snake = Snake()
    food = Food()

    game_is_on = True
    while game_is_on:
        screen.update()
        difficulty(level)
        snake.move()

        if snake.head.distance(food) < 15:
            score.increase_score()
            food.create_food()
            snake.grow()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            screen.clear()
            score.game_over()
            game()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                screen.clear()
                score.game_over()
                game()
        screen.listen()
        screen.onkey(key='Up', fun=snake.up)
        screen.onkey(key='Down', fun=snake.down)
        screen.onkey(key='Right', fun=snake.right)
        screen.onkey(key='Left', fun=snake.left)

    screen.exitonclick()


game()
