import imp
from flask import render_template,session,request,redirect,url_for,flash
from shop import app,db,bcrypt
from sqlalchemy import func

from .forms import RegistrationForm
from .forms import LoginForm
from .forms import OutletSetupForm
from .forms import OutletCategorySetupForm
from .forms import RouteSetupForm
from .forms import ComplainSetupForm
from .models import Userf
from .models import CRM_ROUTE_SETUP
from .models import CRM_COMPLAIN_TYPE_SETUP
import os

@app.route('/')
def home():
   # return 'home Page pf shop'
    routesetupdata = CRM_ROUTE_SETUP.query.all()
    print (routesetupdata)
    return render_template('admin/view.html',routesetupdata=routesetupdata)
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
       
        maxid = db.session.query(func.max(Userf.id)).scalar()
        maxid=maxid+1
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = Userf(id=maxid,name=form.name.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash(f'welcome {form.name.data} Thanks for registering','success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Register user')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Userf.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'welcome {form.email.data} you are logedin now','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('login'))
    return render_template('admin/login.html',title='Login page',form=form)



@app.route('/Outlet_setup', methods=['GET', 'POST'])
def Outlet_setup():
    form = OutletSetupForm()
    return render_template('admin/Outlet_setup.html',title='Outlet Setup',form=form)

@app.route('/Outlet_Category_setup', methods=['GET', 'POST'])
def Outlet_Categoory_setup():
    form = OutletCategorySetupForm()
    return render_template('admin/Outlet_Category_setup.html',title='Outlet Category Setup',form=form)

@app.route('/Routesetup', methods=['GET', 'POST'])
def Route_setup():
    form = RouteSetupForm()
    if form.validate_on_submit():
        route_data = CRM_ROUTE_SETUP(ROUTE_ID='6',ROUTE_NAME=form.Name.data,DESCRIPTION=form.Description.data)
        db.session.add(route_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/Route_Setup.html',title='Route Setup',form=form)

@app.route('/Complainsetup', methods=['GET', 'POST'])
def Complain_setup():
    form = ComplainSetupForm()
    if form.validate_on_submit():
        setup_data = CRM_COMPLAIN_TYPE_SETUP(COMPLAIN_ID='1',COMPLAIN_TYPE=form.Complain_Type.data,ACTION=form.com_Action.data)
        db.session.add(setup_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/Complain_setup.html', title='Complain Setup',form=form)


