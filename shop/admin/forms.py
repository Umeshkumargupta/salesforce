import imp
from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError
from flask_wtf import FlaskForm, Form
from .models import Userf,CRM_ROUTE_SETUP,CRM_COMPLAIN_TYPE_SETUP







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
    Category_Name = StringField('Outlet_Category_Name', [validators.Length(min=6, max=35)])

class RouteSetupForm(FlaskForm):
    Name = StringField('Name', [validators.Length(min=6, max=35)])
    Description = StringField('Description', [validators.Length(min=6, max=35)])

class ComplainSetupForm(FlaskForm):
    Complain_Type = StringField('Complain_Type', [validators.Length(min=6, max=35)])
    com_Action = StringField('com_Action', [validators.Length(min=6, max=35)])
