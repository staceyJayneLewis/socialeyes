import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    events = mongo.db.events.find()
    return render_template("events.html", events=events)


@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    return render_template("sign_up.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)