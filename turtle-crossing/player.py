from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create a turtle that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north./
# Detect when the turtle player collides with a car and stop the game if this happens./
# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
# When this happens, return the turtle to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.left(90)

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.forward(MOVE_DISTANCE)

    def move(self):
        self.forward(MOVE_DISTANCE)