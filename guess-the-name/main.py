from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

comp_guessed = random.randint(0, 99)

ask_user = input("Choose a difficulty. Type 'easy' or 'hard':  ")

def game_logic(counter):
    global game_continue
    global counter_num
    if comp_guessed > user_guessed:
        
        print("Too low")
        print("Guess again")
        counter_num -= 1
        print(f"You have {counter_num} attempts remaining to guess the number")
        if counter_num == 0:
            print(f"You ran out of guesses, the correct answer is {comp_guessed}")
            game_continue = False

    elif user_guessed > comp_guessed:
        print("Too high")
        print("Guess again")
        counter_num -= 1
        print(f"You have {counter_num} attempts remaining to guess the number")
        if counter_num == 0:
            print(f"You ran out of guesses, the correct answer is {comp_guessed}")
            game_continue = False

    elif user_guessed == comp_guessed:
        print(f"You got it! The answer was {comp_guessed}")
        game_continue = False

if ask_user == "hard":
    counter_num = 5
    game_continue = True
    while game_continue:
        user_guessed = int(input("guess a number:  "))
        game_logic(counter_num)

if ask_user == "easy":
    counter_num = 10
    game_continue = True
    while game_continue:
        user_guessed = int(input("guess a number:  "))
        game_logic(counter_num)
