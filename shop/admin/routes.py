import imp
from flask import render_template,session,request,redirect,url_for,flash
from shop import app,db,bcrypt
from sqlalchemy import func
from sqlalchemy import desc

from .forms import RegistrationForm
from .forms import LoginForm
from .forms import OutletSetupForm
from .forms import RouteSetupForm
from .forms import ComplainSetupForm
from .forms import OutletCategorySetupForm
from .forms import Retail_outlet_creation_form
from .models import Userf
from .models import CRM_ROUTE_SETUP
from .models import CRM_COMPLAIN_TYPE_SETUP
from .models import CRM_OUTLET_CAT_SETUP
from .models import CRM_MDM_RETAIL_OUTLET_SETUP
import os

@app.route('/')
def home():
   # return 'home Page of shop'
   
    routesetupdata = CRM_ROUTE_SETUP.query.all()
    print (routesetupdata)
    return render_template('admin/Route_view.html',routesetupdata=routesetupdata)
@app.route('/Retail_layout_view')
def retail_view():
   # return 'home Page pf shop'EX Brand.query.order_by(Brand.id.desc()).all()
   
    retail_layout_view = CRM_MDM_RETAIL_OUTLET_SETUP.query.order_by(CRM_MDM_RETAIL_OUTLET_SETUP.RETAIL_ID.desc()).all()
    return render_template('admin/retail_outlet_view.html',retail_layout_view=retail_layout_view)
   
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
def Outlet_Category_setup():
    form = OutletCategorySetupForm()
    if form.validate_on_submit():
        maxid = db.session.query(func.max(CRM_OUTLET_CAT_SETUP.OUTLET_CAT_ID)).scalar()
        maxid = maxid+1
        outlet_data = CRM_OUTLET_CAT_SETUP(OUTLET_CAT_ID=maxid,OUTLET_CAT_NAME=form.Category_Name.data,ACTION='')
        db.session.add(outlet_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/Outlet_Category_setup.html',title='Outlet Category Setup',form=form)



@app.route('/Routesetup', methods=['GET', 'POST'])

def Route_setup():
    form = RouteSetupForm()
    if form.validate_on_submit():
        maxid = db.session.query(func.max(CRM_ROUTE_SETUP.ROUTE_ID)).scalar()
        maxid=maxid+1
        route_data = CRM_ROUTE_SETUP(ROUTE_ID=maxid,ROUTE_NAME=form.Name.data,DESCRIPTION=form.Description.data)
        db.session.add(route_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/Route_Setup.html',title='Route Setup',form=form)

@app.route('/Retail_outlet_creation', methods=['GET', 'POST'])
def Retail_outlet_creation():
    Route = CRM_ROUTE_SETUP.query.all()
    Out_cat = CRM_OUTLET_CAT_SETUP.query.all()
    form = Retail_outlet_creation_form()
    if form.validate_on_submit():
        maxid = db.session.query(func.max(CRM_MDM_RETAIL_OUTLET_SETUP.RETAIL_ID)).scalar()
        maxid = maxid+1
        retail_data = CRM_MDM_RETAIL_OUTLET_SETUP(RETAIL_ID = maxid,
        RETAIL_NAME = form.Retailer.data,
        PAN_NO = form.Pan_no.data,
        ADDRESS = form.Address.data,
        MONLI_NO = form.mobile_no.data,
        TEL_NO = form.telephone_no.data,
        CONATACT_PERSON = form.Contact_person.data,
        ROUTE_ID = form.route.data,
        PAN_IMAGEE = form.pan_image.data,
        PROFILE_IMAGE = form.Profile_Image.data,
        OUTLET_CAT_ID = form.Outlet_cat.data,
        OUTLET_TYPE_ID = form.Outlet_type.data,
        ANNUAL_TURNOVER = form.Annual_Turnover.data,
        CITY = form.Annual_Turnover.data,
        DISTRICT =form.District.data,
        BG_AMOUNT = form.Bg_amount.data,
        PDC_AMOUNT = form.pdc_amount.data,
        CR_DAYS = form.cr_days.data,GPS_ID = form.gps_id.data)
        db.session.add(retail_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin/retail_outlet_setup.html',title='Retail outlet',form=form,Route = Route,Out_cat=Out_cat)

@app.route('/Complainsetup', methods=['GET', 'POST'])
def Complain_setup():
    form = ComplainSetupForm()
    if form.validate_on_submit():
        maxid = db.session.query(func.max(CRM_COMPLAIN_TYPE_SETUP.COMPLAIN_ID)).scalar()
        setup_data = CRM_COMPLAIN_TYPE_SETUP(COMPLAIN_ID=maxid+1,COMPLAIN_TYPE=form.Complain_Type.data,ACTION=form.com_Action.data)
        db.session.add(setup_data)
        db.session.commit()
        flash(f'DATA INSERTED','success')
        #return redirect(url_for('login'))
    return render_template('admin/Complain_setup.html', title='Complain Setup',form=form)


