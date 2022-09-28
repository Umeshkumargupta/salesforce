import imp
from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, SelectField
from flask_wtf import FlaskForm, Form

class Visit_Form(FlaskForm):
    Visit_date = StringField('Visit Date', [validators.Length(min=6, max=35)])
    Works =  StringField('Works',[validators.Length(min=6, max = 100)])
    Remarks = StringField('Remarks',[validators.Length(min=2,max=100)])
    Available_qty = StringField('Available Qty',[validators.Length(min=1,max=10)])
