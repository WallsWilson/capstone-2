from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):

    db.app = app
    db.init_app(app)

class CustomerReview(db.Model):

    __tablename__ = 'CustomerReview'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text(50), nullable = False)

    rating = db.Column(db.Float, nullable = False)

    review_text = db.Column(db.Text(500), nullable = False)

    created_at = db.Column(db.DateTime, default = datetime.now)

    