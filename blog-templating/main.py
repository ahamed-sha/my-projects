from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/c5ce5730c0dfdc33fa14")
text = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", text=text)


@app.route('/post/<int:num>')
def get_blog(num):
    num -= 1
    return render_template("post.html", num=num, text=text)

if __name__ == "__main__":
    app.run(debug=True)
