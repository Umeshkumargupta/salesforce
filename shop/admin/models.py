from shop import db
from datetime import datetime

class Userf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180),unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False,default='profile.jpg')

    def __repr__(self):
        return '<Userf %r>' % self.username




db.create_all()

#route setup
class CRM_ROUTE_SETUP(db.Model):
    ROUTE_ID = db.Column(db.Integer, primary_key=True)
    ROUTE_NAME = db.Column(db.String(50),unique=False, nullable=False)
    DESCRIPTION = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<CRM_ROUTE_SETUP %r>' % self.ROUTE_NAME

#complain setup
class CRM_COMPLAIN_TYPE_SETUP(db.Model):
    COMPLAIN_ID = db.Column(db.Integer, primary_key=True)
    COMPLAIN_TYPE = db.Column(db.String(50),unique=False, nullable=False)
    ACTION = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<CRM_ROUTE_SETUP %r>' % self.COMPLAIN_TYPE




db.create_all()

