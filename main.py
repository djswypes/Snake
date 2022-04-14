from turtle import Screen
import time
from scoreboard import Scoarboard
from food import Food
from snake import Snake
DIFFICULTY_LEVELS = {
    1:  0.4,
    2:  0.2,
    3:  0.08,
    4:  0.06,
    5:  0.04
}

score = Scoarboard()


def set_difficulty(chosen_level):
    for level in DIFFICULTY_LEVELS:
        if level == chosen_level:
            return time.sleep(DIFFICULTY_LEVELS[level])



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
        set_difficulty(level)
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
