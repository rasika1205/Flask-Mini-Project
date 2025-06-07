from flask import Flask,redirect,request, url_for, flash
app=Flask(__name__)
app.secret_key = 'your_secret_key'
hotels = {
    "Grand Palace Hotel": [
        "Luxury hotel in New York", 200, "New York", 4.5, [], "/static/images/hotel1.jpg"
    ],
    "Ocean View Resort": [
        "Beachfront resort in Miami", 250, "Miami", 4.7, [], "/static/images/oswald-elsaboath-ym_EI-DTS1g-unsplash.jpg"
    ],
    "Mountain Retreat": [
        "Cozy cabins in Colorado mountains", 180, "Colorado", 4.6, [], "/static/images/hotel3.jpg"
    ],
    "Desert Mirage Hotel": [
        "Elegant stay in the heart of the desert", 220, "Nevada", 4.4, [], "/static/images/hotel4.jpg"
    ],
    "Lakeside Paradise": [
        "Scenic hotel by the lake", 190, "Michigan", 4.3, [], "/static/images/hotel5.jpg"
    ],
    "City Lights Inn": [
        "Modern hotel in downtown Los Angeles", 230, "Los Angeles", 4.2, [], "/static/images/hotel6.jpg"
    ],
    "Forest Haven": [
        "Peaceful retreat in the forest", 160, "Oregon", 4.6, [], "/static/images/hotel7.jpg"
    ],
    "Snowflake Lodge": [
        "Winter lodge with ski access", 240, "Vermont", 4.8, [], "/static/images/hotel8.jpg"
    ],
    "Island Breeze Resort": [
        "Relaxing resort on a private island", 300, "Hawaii", 4.9, [], "/static/images/hotel9.jpg"
    ],
    "Sunset Boulevard Hotel": [
        "Trendy hotel near Hollywood", 210, "California", 4.1, [], "/static/images/hotels10.jpg"
    ]
}
users={"rasika":"abcd"}
from flask import render_template

@app.route("/list_hotels", methods=["GET"])
def list_hotels():
    return render_template("index.html", hotels=hotels)
@app.route("/show/<hotel_name>", methods=["GET"])
def show_hotel(hotel_name):
    if hotel_name in hotels:
        hotel_data = hotels[hotel_name]
        return render_template("show.html",
                               hotel_name=hotel_name,
                               description=hotel_data[0],
                               price=hotel_data[1],
                               location=hotel_data[2],
                               rating=hotel_data[3],
                               image_url=hotel_data[5],
                               hotels=hotels)
    return "Hotel not found", 404


@app.route("/new_hotel", methods=["GET"])
def new_hotel():
    return render_template("add.html")


@app.route("/add_hotel", methods=["POST"])
def add_hotel():
    name = request.form["name"]
    description = request.form["description"]
    price = float(request.form["price"])
    location = request.form["location"]
    rating = float(request.form["rating"])
    image_url = request.form["image_url"]
    if rating > 5:
        flash("Rating cannot be more than 5.")
        return redirect(url_for("new_hotel"))
    if not image_url:
        image_url ="/static/images/oswald-elsaboath-ym_EI-DTS1g-unsplash.jpg"
    hotels[name] = [description, price, location, rating, [], image_url]

    return redirect(url_for("list_hotels"))

@app.route("/delete_hotel/<hotel_name>", methods=["POST"])
def delete_hotel(hotel_name):
    if hotel_name in hotels:
        del hotels[hotel_name]
        return redirect(url_for("list_hotels"))
    return "Hotel not found", 404
@app.route("/edit_hotel/<hotel_name>", methods=["GET"])
def edit_hotel_form(hotel_name):
    if hotel_name in hotels:
        hotel_data = hotels[hotel_name]
        return render_template("edit.html", hotel_name=hotel_name, hotel=hotel_data)
    return "Hotel not found", 404
@app.route("/edit_hotel/<hotel_name>", methods=["POST"])
def edit_hotel(hotel_name):
    if hotel_name in hotels:
        hotel = hotels[hotel_name]
        hotel[0] = request.form.get("description", hotel[0])
        hotel[1] = float(request.form.get("price", hotel[1]))
        hotel[2] = request.form.get("location", hotel[2])
        hotel[3] = float(request.form.get("rating", hotel[3]))
        hotel[5] = request.form.get("image_url", hotel[5])
        if hotel[3] > 5:
            flash("Rating cannot be more than 5.")
            return redirect(url_for("list_hotels"))
        if not hotel[5]:
            hotel[5] = "/static/images/oswald-elsaboath-ym_EI-DTS1g-unsplash.jpg"
        return redirect(url_for("list_hotels"))
    return "Hotel not found", 404
@app.route("/add_comment/<hotel_name>", methods=["POST"])
def add_comment(hotel_name):
    if hotel_name in hotels:
        comment = request.form.get("comment")
        rating = request.form.get("rating")
        if comment:
            hotels[hotel_name][4].append({"text": comment, "rating": rating})
        return redirect(url_for("show_hotel", hotel_name=hotel_name))
    return "Hotel not found", 404
@app.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")
@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users:
        flash("Username already exists. Please login.")
        return redirect(url_for("home"))

    users[username] = password
    return redirect(url_for("list_hotels"))
@app.route("/login", methods=["GET"])
def login_form():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_user():
    username = request.form.get("username")
    password = request.form.get("password")

    if username not in users:
        flash("Username not found. Please sign up.")
        return redirect(url_for("home"))

    if users[username] != password:
        flash("Wrong password.")
        return redirect(url_for("home"))

    return redirect(url_for("list_hotels"))

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
if __name__=='__main__':
    app.run(debug=True)