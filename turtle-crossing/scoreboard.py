from turtle import Turtle
FONT = ("Courier", 21, "normal")

# Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("firebrick")
        self.penup()
        self.hideturtle()
        self.score = 1

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align="center", font=FONT)

    def level(self):
        level = f"level : {self.score}"
        self.goto(-220, 250)
        self.write(level, align="center", font=FONT)

    def level_increase(self):
        self.clear()
        self.score += 1
        self.level()