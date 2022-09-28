from datetime import date, datetime
import imp
import cx_Oracle
from flask import render_template,session,request,redirect,url_for,flash
from shop import app,db,bcrypt
from sqlalchemy import func
from sqlalchemy import desc

from shop.order.models import MDM_CUS_SETUP, MDM_DEALER_SETUP, MDM_SALES_TYPE_SETUP,MDM_IT_SETUP,CRM_SD_SO_OPERATION

from shop.order.forms import sales_order_form

import os


@app.route('/Sales_Order', methods=['GET', 'POST'])

def Sales_order():
    #retail_layout_view = CRM_MDM_RETAIL_OUTLET_SETUP.query.order_by(CRM_MDM_RETAIL_OUTLET_SETUP.RETAIL_ID.desc()).all()
    Dealer = MDM_DEALER_SETUP.query.all()
    Customer = MDM_CUS_SETUP.query.order_by(MDM_CUS_SETUP.CUS_NAME.asc()).all()
    Sale_Class = MDM_SALES_TYPE_SETUP.query.all()
    it = MDM_IT_SETUP.query.all()
    form = sales_order_form()
    if form.validate_on_submit():
        sales_order_data = CRM_SD_SO_OPERATION (form.v_no.data,
        V_DATE = form.v_date.data,
        M_NO = "12",
        CUS_CODE = "12",
        EMP_CODE = "1",
        SL_CODE = "1")
        # AGENT_CODE = "1",
        # SR_NO = "1",
        # IT_CODE = "12",
        # UNIT = "pcs",
        # QUANTITY = "2",
        # QUANTITY_2ND = "2",
        # QUANTITY_3RD = "2",
        # RATE = "2",
        # AMOUNT = "4",
        # NET_QUANTITY = "2",
        # NET_RATE = "8",
        # NET_AMOUNT = "8",
        # DELIVERY_DATE = form.deleivery_date.data,
        # CUR_CODE = "1",
        # EXC_RATE = "1",
        # BATCH_NO = "1",
        # TRACK_NO = "1",
        # STOCK_BLOCK_FLAG  = "1",
        # DEALER_CODE  = "1",
        # DED_QTY = "1",
        # ADD_QTY = "1",
        # REJECT_FLAG = "1",
        # REF_FLAG = "1",
        # ADJUST_UID = "1",
        # ADJUST_DATE = '',
        # ADJUST_REMARKS = "1",
        # PRIORITY_ID = "1",
        # OPENING_FLAG = "1",
        # SHIPPING_ADDRESS = "1",
        # SHIPPING_CONTACT_NO = "1",
        # SD_TYPE_CODE = "1",
        # AREA_ID = "1",
        # PERSON_NAME = "1",
        # SECTOR_CODE = "1",
        # REMARKS = "1",
        # DOC_CODE = "1",
        # COM_CODE = "1",
        # BRA_CODE = "1",
        # DIV_CODE = "1",
        # MAKE_UID = "1",
        # MAKE_DATE = '9/27/2022 1:37:06 PM',
        # SYNC_ID = "1",
        # SESSION_ID = "1",
        # MDY_DATE = '',
        # MDY_UID = "1",
        # RECYCLED_UID = "1",
        # RECYCLED_DATE = '',
        # RECYCLED_FLAG = "1",
        # REF_NO = "1",
        # REF_DOC_CODE = "1",
        # AUTHORIZED_QTY = "1",
        # PAY_MODE_CODE = "1",
        # DOC_IEL_ID = "1",
        # DOC_MODE = "1",
        # SCHEME_ADJUST_QTY = "1",
        # LINE_IT_DISCOUNT = "1",
        # LINE_IT_PREMIUM = "1",
        # PREMIUM_PERCENT = "1",
        # DIS_PERCENT = "1",
        # IT_SPEC = "1",
        # LC_ID = "1",
        # IT_SIZE_ID = "1",
        # COLOR_ID = "1",
        # FREE_QTY = "1",
        # BUNDLE_QTY = "1",
        # MRP = "1",
        # EXPIRY_DATE = '')
        db.session.add(sales_order_data)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('order/Salesordertest.html',title='Sales Order Setup',form=form, Dealer=Dealer,Customer=Customer, Sale_Class=Sale_Class,it=it)

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('order/test.html',title='test')
