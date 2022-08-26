from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DATABASE_URL, SECRET_KEY, DEBUG, ENV


app = Flask(__name__)

app.debug = DEBUG
app.config['ENV'] = ENV
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

migrate = Migrate(app, db)
import models


@app.route('/')
def hello_world():
    return 'Welcome in User microservice!'


if __name__ == "__main__":
    app.run("0.0.0.0", 5001)