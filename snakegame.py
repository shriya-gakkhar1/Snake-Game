from turtle import Turtle,Screen
from snake import Snake
from food import Food
import time



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()

#CONTROL THE SNAKE
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")







#MOVING THE SNAKE
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#DETECT COLLISION WITH FOOD
#DISTANCE METHOD
if snake.head.distance(food) < 70:
    food.refresh() 
    

    



screen.exitonclick() 

    
        
    

