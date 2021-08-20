from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime
import bleach

now = datetime.datetime.now()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(BlogPost).all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["POST", "GET"])
def create_post():
    post_form = CreatePostForm()
    if request.method == "POST":
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        img_url = request.form.get("img_url")
        author = request.form.get("author")
        body = request.form.get("body")
        body_bleached = bleach.clean(body)
        date = now.strftime("%B %d ,%Y")
        new_post = BlogPost(
            title=title,
            author=author,
            subtitle=subtitle,
            date=date,
            body=body_bleached,
            img_url=img_url
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    else:
        return render_template('make-post.html', form=post_form)


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    if request.method == "GET":
        edit_form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        return render_template('make-post.html', edit=True, form=edit_form)
    else:
        post.title = request.form["title"]
        post.author = request.form["author"]
        post.img_url = request.form["img_url"]
        post.subtitle = request.form["subtitle"]
        post.body = request.form["body"]
        db.session.commit()
        return redirect(url_for('show_post', index=post_id))


@app.route("/delete/<int:post_id>")
def delete(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
