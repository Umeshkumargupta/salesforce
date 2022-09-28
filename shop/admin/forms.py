import imp
from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, SelectField
from flask_wtf import FlaskForm, Form
from .models import Userf,CRM_ROUTE_SETUP,CRM_COMPLAIN_TYPE_SETUP,CRM_OUTLET_CAT_SETUP,CRM_MDM_RETAIL_OUTLET_SETUP








class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def validate_username(self, field):
        if Userf.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

        
    def validate_email(self, field):
        if Userf.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')



class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])

class OutletSetupForm(FlaskForm):
    Outlet_Name = StringField('Outlet_Name', [validators.Length(min=6, max=35)])


class OutletCategorySetupForm(FlaskForm):
    Category_Name = StringField('Outlet Category Name', [validators.Length(min=6, max=35)])

class RouteSetupForm(FlaskForm):
    Name = StringField('Name', [validators.Length(min=6, max=35)])
    Description = StringField('Descriptions', [validators.Length(min=6, max=35)])
    select_b = SelectField('Select_b')
class ComplainSetupForm(FlaskForm):
    Complain_Type = StringField('Complain_Type', [validators.Length(min=6, max=35)])
    com_Action = StringField('com_Action', [validators.Length(min=6, max=35)])

class Retail_outlet_creation_form(FlaskForm):
    Retailer = StringField('Retailer Name', [validators.Length(min=4, max=25)])
    Address = StringField('Address', [validators.Length(min=4, max=25)])
    Pan_no = StringField('PAN', [validators.Length(min=9, max=9)])
    mobile_no = StringField('Mobile', [validators.Length(min=4, max=25)])
    telephone_no = StringField('Telephone', [validators.Length(min=4, max=25)])
    Contact_person = StringField('Conatact Person', [validators.Length(min=4, max=25)])
    route = StringField('route', [validators.Length(min=1, max=25)])
    pan_image = StringField('Pan Image', [validators.Length(min=4, max=250)])
    Profile_Image = StringField('Profile_Image', [validators.Length(min=4, max=250)])
    Outlet_cat = StringField('Outlet Category', [validators.Length(min=1, max=25)])
    Outlet_type = StringField('Outlet Type',[validators.length(min=1,max=9)])
    Annual_Turnover = StringField('Annual Turnover', [validators.Length(min=4, max=25)])
    city = StringField('City', [validators.Length(min=1, max=25)])
    District = StringField('District', [validators.Length(min=1, max=25)])
    Bg_amount = StringField('BG Amount', [validators.Length(min=1, max=25)])
    pdc_amount = StringField('PDC Amount', [validators.Length(min=1, max=25)])
    cr_days = StringField('cr days', [validators.Length(min=1, max=25)])
    gps_id = StringField('gps', [validators.Length(min=0, max=25)])
   
   