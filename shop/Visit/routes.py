import imp
from flask import render_template,session,request,redirect,url_for,flash
from shop import app,db,bcrypt
from sqlalchemy import func
from sqlalchemy import desc

from .forms import Visit_Form
from .models import CRM_OP_VISIT

@app.route('/Visitform', methods=['GET', 'POST'])

def Visit_form():
    form = Visit_Form()
    if form.validate_on_submit():
        maxid = db.session.query(func.max(CRM_OP_VISIT.VISIT_ID)).scalar()
        maxid=maxid+1

        visit_data = CRM_OP_VISIT(VISIT_ID=maxid,
        EMPLOYEE_ID = '',
        ROUTE_ID = '',

        VISIT_DATE = '',
        CUSTOMER_ID = '',
        WORKS = '',

        REMARKS = '',
        PRODUCT_CODE = '',
        AVAILABLE_QTY = '')

        db.session.add(visit_data)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('visit/Visit.html',title='Visit',form=form)