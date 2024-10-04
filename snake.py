from turtle import Turtle
POSITIONS=[-10,-30,-50]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self) :
        self.snakes=[]
        self.createSnakes()
        self.head=self.snakes[0]
    def createSnakes(self):
        """Creates the initial snake segments."""
        for x_position in POSITIONS:  # Iterate over x-coordinates
            self.addseg(x_position)

    def addseg(self, x_position):
        """Adds a new segment at the given x_position on the y = 0 line."""
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(x_position, 0)  # Set the y-coordinate to 0
        self.snakes.append(snake)

    def extend(self):
        """Extend the snake by adding a new segment at the last segment's position."""
        last_segment_position = self.snakes[-1].position()  # Get the position of the last segment
        self.addseg(last_segment_position[0]) 
    def move(self):
        for seg in range(len(self.snakes)-1,0,-1):
             new_xcor=self.snakes[seg-1].xcor()
             new_ycor=self.snakes[seg-1].ycor()
             self.snakes[seg].goto(new_xcor,new_ycor)
        
        self.head.forward(20)    
    def up(self):
        if self.head.heading()!=DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
          self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
          self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
           self.head.setheading(RIGHT)
        