from flask import Flask, render_template, request
import requests
import smtplib

USERNAME = "username"
PASSWORD = "pass"

response = requests.get(url="https://api.npoint.io/c5ce5730c0dfdc33fa14")
blog_text = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', text=blog_text)


@app.route('/about')
def about():
    return render_template('about.html')


def send_mail():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=USERNAME, password=PASSWORD)
        conn.sendmail(
            from_addr=USERNAME,
            to_addrs=USERNAME,
            msg=f"Subject:A mail from a fan!\n\nName:{username}\nMAIL_ID:{email}\nPhone:{phone}\nMessage:{message}"
        )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    method = request.method
    if method == 'POST':
        send_mail()
        return render_template('contact.html', method=method)
    else:
        return render_template('contact.html', method=method)


@app.route('/post/<int:num>')
def get_blog(num):
    return render_template("post.html", num=num, text=blog_text)


if __name__ == '__main__':
    app.run(debug=True)
