from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DATABASE_URL, SECRET_KEY, DEBUG, ENV

app = Flask(__name__)

app.config['DEBUG'] = DEBUG
app.config['ENV'] = ENV
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

migrate = Migrate(app, db)
import models


@app.route('/')
def hello_world():
    return 'Welcome in Invoice microservice!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)