from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/c5ce5730c0dfdc33fa14")
blog_text = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', text=blog_text)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def get_blog(num):
    return render_template("post.html", num=num, text=blog_text)


if __name__ == '__main__':
    app.run(debug=True)
