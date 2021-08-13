from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as r

API_KEY = "373"

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random")
def random():
    cafes = db.session.query(Cafe).all()
    random_cafe = r.choice(cafes)
    # Convert to dictionary
    cafe = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    }
    return jsonify(cafe)


@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    list_of_cafes = []
    for cafe in cafes:
        each_cafe = {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        list_of_cafes.append(each_cafe)
    return jsonify(cafes=list_of_cafes)


@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    if cafes:
        list_of_cafes = []
        for cafe in cafes:
            each_cafe = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
            list_of_cafes.append(each_cafe)
        return jsonify(cafes=list_of_cafes)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(int(request.form.get("sockets"))),
        has_toilet=bool(int(request.form.get("toilet"))),
        has_wifi=bool(int(request.form.get("wifi"))),
        can_take_calls=bool(int(request.form.get("calls"))),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe"})


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def price_update(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_new_price = request.form.get("new_price")
        cafe_to_update.coffee_price = cafe_new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully Updated the coffee Price for the selected cafe id"})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe for the selected cafe id"})


## HTTP DELETE - Delete Record

@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    if cafe_to_delete:
        api_key = request.form.get("api_key")
        if api_key == API_KEY:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully Deleted the cafe"})
        else:
            return jsonify(error={"error": "Sorry, that's not allowed, make sure you have the correct api key"})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe for the selected cafe id"})

if __name__ == '__main__':
    app.run(debug=True)
