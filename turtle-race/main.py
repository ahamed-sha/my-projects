from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = 0
for turtle_color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("normal")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    y += 30
    new_turtle.goto(x=-230, y=-90 + y)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win = turtle.pencolor()
            if win == user_bet:
                print(f"you've won! the {win} turtle is the winnner")
            else:
                print(f"you've lost the game! the {win} turtle won the game")
        pace = random.randint(0, 10)
        turtle.forward(pace)

screen.exitonclick()
