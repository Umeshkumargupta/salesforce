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

#crm_outlet_cat setup
class CRM_OUTLET_CAT_SETUP(db.Model):
    OUTLET_CAT_ID = db.Column(db.Integer, primary_key=True)
    OUTLET_CAT_NAME = db.Column(db.String(50),unique=False, nullable=False)
    ACTION = db.Column(db.String(80), unique=True, nullable=False,default='')

    def __repr__(self):
        return '<CRM_OUTLET_CAT_SETUP %r>' % self.OUTLET_CAT_NAME

#CRM_MDM_RETAIL_OUTLET_SETUP 
class CRM_MDM_RETAIL_OUTLET_SETUP(db.Model):
    RETAIL_ID = db.Column(db.Integer, primary_key=True)
    RETAIL_NAME = db.Column(db.String(50),unique=False, nullable=False)
    PAN_NO = db.Column(db.String(50),unique=False, nullable=False)
    ADDRESS = db.Column(db.String(50),unique=False, nullable=False)
    MONLI_NO = db.Column(db.String(50),unique=False, nullable=False)
    TEL_NO = db.Column(db.String(50),unique=False, nullable=False)
    CONATACT_PERSON = db.Column(db.String(50),unique=False, nullable=False)
    ROUTE_ID = db.Column(db.String(50),unique=False, nullable=False)
    PAN_IMAGEE = db.Column(db.String(50),unique=False, nullable=False)
    PROFILE_IMAGE = db.Column(db.String(50),unique=False, nullable=False)
    OUTLET_CAT_ID = db.Column(db.String(50),unique=False, nullable=False)
    OUTLET_TYPE_ID = db.Column(db.String(50),unique=False, nullable=False)
    ANNUAL_TURNOVER = db.Column(db.String(50),unique=False, nullable=False)
    CITY = db.Column(db.String(50),unique=False, nullable=False)
    DISTRICT = db.Column(db.String(50),unique=False, nullable=False)
    BG_AMOUNT = db.Column(db.String(50),unique=False, nullable=False)
    PDC_AMOUNT = db.Column(db.String(50),unique=False, nullable=False)
    CR_DAYS = db.Column(db.String(50),unique=False, nullable=False)
    GPS_ID = db.Column(db.String(50),unique=False, nullable=False)
    def __repr__(self):
        return '<CRM_MDM_RETAIL_OUTLET_SETUP %r>' % self.RETAIL_NAME


db.create_all()

