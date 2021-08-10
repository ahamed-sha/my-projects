from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
from sqlalchemy import desc

API_KEY = "1d2bedeba9cc9696827039d1b2d6c528"
URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class MyForm(FlaskForm):
    rating = StringField(label='Your rating', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[Length(min=1, max=25, message="Field should have minimum 8 characters")])
    submit = SubmitField(label='Submit', validators=[DataRequired()])


class MovieNameForm(FlaskForm):
    name = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField(label='Add Movie', validators=[DataRequired()])


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(70), nullable=False)


db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    method = request.method
    if method == "POST":
        movie_id = request.args.get("id")
        rating = request.form["rating"]
        review = request.form["review"]
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()
        return redirect(location=url_for('home'))
    form = MyForm()
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        movie_title = request.form["name"]
        params = {
            "api_key": API_KEY,
            "query": movie_title
        }
        response = requests.get(url=URL, params=params)
        movie_details = response.json()
        list_of_movies = movie_details["results"]
        return render_template("select.html", movies=list_of_movies)

    form = MovieNameForm()
    return render_template("add.html", form=form)


@app.route("/select", methods=['POST', 'GET'])
def select():
    movie_id = int(request.args.get("id"))
    params = {
        "api_key": API_KEY
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=params)
    movie_details = response.json()
    poster_path = movie_details["poster_path"]
    description = movie_details["overview"]
    year = movie_details["release_date"]
    title = movie_details["title"]
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=0,
        ranking=0,
        review="None",
        image_url=f"https://www.themoviedb.org/t/p/w500{poster_path}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
