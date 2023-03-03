from turtle import Screen, Turtle
from food import Food
from worm import Worm
from scoreboard import ScoreBoard
import time


def main():
    screen = Screen()

    screen.setup(width=620, height=620)
    screen.bgcolor('sienna')
    screen.title('Grow Ur Worm')
    screen.tracer(0)

    scoreboard = ScoreBoard()
    worm = Worm()
    food = Food()
    feeding_worm = True

    screen.listen()
    screen.onkey(worm.up, "Up")
    screen.onkey(worm.down, "Down")
    screen.onkey(worm.left, "Left")
    screen.onkey(worm.right, "Right")

    def full_reset():
        screen.clear()
        scoreboard.clear()
        main()

    screen.onkey(full_reset, "r")

    while feeding_worm:
        screen.update()
        time.sleep(0.1)
        worm.move()

        if worm.head.distance(food) < 15:
            food.refresh()
            scoreboard.plus_point()
            worm.more_worm()

        if worm.head.xcor() > 290 or worm.head.xcor() < -300 or worm.head.ycor() > 300 or worm.head.ycor() < -290:
            feeding_worm = False
            scoreboard.game_over()

        for segment in worm.segments[1:]:
            if worm.head.distance(segment) < 10:
                feeding_worm = False
                scoreboard.game_over()

    screen.exitonclick()


main()

