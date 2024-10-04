from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(500,500)
screen.tracer(0)
screen.listen()


# pos=random.choice(position)
score=Score()
snake=Snake()
is_run=True
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
while is_run==True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if its near to food
    if(snake.head.distance(food)<15):
        food.relocate()
        snake.extend()
        score.increase()
    # if it touches the wall
    if(snake.head.xcor()>240 or snake.head.xcor()<-240 or snake.head.ycor()>240 or snake.head.ycor()<-240):
        
        score.game_over()
        is_run=False
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment)<10:
            is_run=False
            score.game_over()
    
 

screen.exitonclick()