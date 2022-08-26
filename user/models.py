from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column('Email', db.String(255), nullable=False, unique=True, index=True)
    password = db.Column('Password', db.String(128))
    name = db.Column('Name', db.String(256))
    enabled = db.Column('Enabled', db.Boolean(), default=True, index=True)
    date_added = db.Column('Date Added', db.DateTime(), default=datetime.now())
    date_modified = db.Column('Date Modified', db.DateTime(), default=datetime.now())

    def __repr__(self):
        return self.email