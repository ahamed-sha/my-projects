from flask import Flask
from random import randint

random_num = randint(1, 9)
starting_gif = "https://media.giphy.com/media/5t3POlVgm29ZiERRXT/giphy.gif"
correct_gif = "https://media.giphy.com/media/ZgYBhq1x7L1bW/giphy.gif"
low_gif = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
high_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Choose a number between 0 to 9</h1>' \
           '<br>' \
           f'<img src={starting_gif} width=400px height=400px>'


@app.route('/<int:number>')
def game(number):
    if number > random_num:
        return '<h1 style="color:#D83A56"> Too High </h1>' \
               f'<img src={high_gif} width=400px height=400px>'
    elif number < random_num:
        return '<h1 style="color:#39A2DB"> Too low </h1>' \
               f'<img src={low_gif} width=400px height=400px>'
    elif number == random_num:
        return '<h1 style="color:#01937C"> Correct! </h1>' \
               f'<img src={correct_gif} width=600px height=400px>'


if __name__ == "__main__":
    app.run(debug=True)
