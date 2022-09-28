import imp
from sqlite3 import DatabaseError
from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, SelectField,DateField
from flask_wtf import FlaskForm, Form
from .models import MDM_DEALER_SETUP,CRM_SD_SO_OPERATION


class sales_order_form(FlaskForm):
    Product_discount = StringField('Product_discount', [validators.Length(min=0, max=2)])
    v_no =StringField('v_no', [validators.Length(min=0, max=2)])
    v_date = DateField('v_date'),
    Dealer =  StringField('Dealer'),[validators.Length(min=4, max=25)]
    Customer = StringField('Customer'),[validators.Length(min=4, max=25)]
    deleivery_date = DateField('deleivery_date')
   