from datetime import datetime
from app import db


class Invoice(db.Model):
    __tablename__ = 'invoice'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False, index=True)
    invoice_number = db.Column('Invoice Number', db.String(255), nullable=False, unique=True, index=True)
    currency = db.Column('Invoice Currency', db.String(255), nullable=False, index=True)
    invoice_amount = db.Column('Invoice Amount', db.Numeric(10,2), nullable=False, index=True)
    country = db.Column('Invoice Country', db.String(255), nullable=True, index=True)
    enabled = db.Column('Enabled', db.Boolean(), default=True, index=True)
    date_added = db.Column('Date Added', db.DateTime(), default=datetime.now())
    date_modified = db.Column('Date Modified', db.DateTime(), default=datetime.now())

    def __repr__(self):
        return self.invoice_number
