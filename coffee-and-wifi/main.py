from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def my_length_check(form, field):
    if len(field.data) > 20:
        raise ValidationError('Field must be less than 10 characters')


def url_check(form, field):
    if "https" not in field.data.split(":"):
        raise ValidationError('Please type a valid url')

coffee = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
wifi = ["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
power = ["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(), my_length_check])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), url_check])
    opening_time = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label="--coffee rating--", choices=coffee)
    wifi_strength_rating = SelectField(label="--wifi strength rating--", choices=wifi)
    power_availability = SelectField(label="Power Socket Availability", choices=power)
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    cafe_name = form.cafe.data
    location = form.location.data
    opening = form.opening_time.data
    closing = form.closing_time.data
    coffee_rating = form.coffee_rating.data
    wifi_rating = form.wifi_strength_rating.data
    power_rating = form.power_availability.data

    if form.validate_on_submit():
        print(form)
        with open('cafe-data.csv', newline='', encoding='utf8', mode="a") as csv_file:
            csv_file.write(f"\n{cafe_name},{location},{opening},{closing},{coffee_rating},{wifi_rating},{power_rating}")
            return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', n_form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
