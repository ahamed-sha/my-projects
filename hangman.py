

import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

guessed = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in guessed:
        print(f'The letter "{guess}" is already guessed, {strike(guessed)}')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        if guess not in guessed:
            lives -= 1
            if lives > 1:
                print(f'the letter "{guess}" is not in the word...try again')
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word is ")
    guessed.append(guess)
    if lives > 0:
        print(f"{' '.join(display)}")
    elif lives == 0:
        print(chosen_word)
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
