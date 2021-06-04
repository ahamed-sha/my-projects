from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    df = pandas.read_csv("words_to_learn.csv")

except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

else:
    df_as_list = df.to_dict(orient="records")

random_pair = {}
def new_flashcard():
    global random_pair, flip_timer
    window.after_cancel(flip_timer)
    random_pair = random.choice(df_as_list)
    french_word = random_pair["French"]
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    canvas.itemconfig(image, image=card_front)
    flip_timer = window.after(3000, func=flip_over)


def flip_over():
    english_word = random_pair["English"]
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")


def learned_words():
    df_as_list.remove(random_pair)
    new_df = pandas.DataFrame(df_as_list)
    new_df.to_csv('words_to_learn.csv', index=False)
    new_flashcard()


# -------------------------- USER INTERFACE -------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_over)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="title", fill="#000000", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="word", fill="#000000", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button 1
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=learned_words)
right_button.grid(row=1, column=0)

# Button 2
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_flashcard)
wrong_button.grid(row=1, column=1)

new_flashcard()

canvas.mainloop()
