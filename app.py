import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    homepage = mongo.db.events.find()
    return render_template("home.html", homepage=homepage)


@app.route("/get_events")
def get_events():
    events = list(mongo.db.events.find())
    return render_template("events.html", events=events)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please try a different one.")
            return redirect(url_for("sign_up"))

        signUp = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signUp)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign up Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("Username and/or password not recognised. Please try again.")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username and/or password not recognised. Please try again.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    
    # get users events from database
    events = list(mongo.db.events.find())
    # get the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:        
        return render_template("profile.html", username=username, events=events)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    # log user out and remove session cookie
    flash("Logged out!")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        event = {
            "event_name": request.form.get("event_name"),
            "event_description": request.form.get("event_description"),
            "event_date": request.form.get("event_date"),
            "event_time": request.form.get("event_time"),
            "event_location": request.form.get("event_location"),
            "created_by": session["user"],
        }
        mongo.db.events.insert_one(event)
        flash("Event added sucessfully!")
        return redirect(url_for("get_events"))
        
    return render_template("add_event.html")
    

@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    return render_template("edit_event.html", event=event)
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)