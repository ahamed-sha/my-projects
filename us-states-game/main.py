import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

new_turtle = turtle.Turtle()
new_turtle.hideturtle()

df = pandas.read_csv("50_states.csv")
states_series = df["state"]
states = states_series.to_list()

a_list = []
is_game_on = True
while is_game_on:
    correct_guesses = len(a_list)
    answer_state = screen.textinput(title=f"states correct: {correct_guesses}/ 50",
                                    prompt="Name a states name:  ").title()

    # TODO convert the guess to Title Case '/

    # TODO check if the guess is among 50 states '/

    for ind_state in states:
        if answer_state == ind_state:
            row = df[df.state == ind_state]
            print(row)
            x = int(row.x)
            y = int(row.y)
            new_turtle.penup()
            new_turtle.goto(x, y)
            new_turtle.write(answer_state, align="center", font=("Arial", 10, "normal"))
            a_list.append(answer_state)
        if correct_guesses == 50:
            is_game_on = False
            new_turtle.write("you got all the states correct", align="center", font=("Arial", 25, "normal"))


# TODO write correct guesses onto the map '/

# TODO use a loop to allow the user to keep guessing '/

# TODO record the correct guesses in a list '/

# TODO keep track of the score '/
