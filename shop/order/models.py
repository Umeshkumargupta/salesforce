from shop import db
from datetime import datetime

#MDM_DEALER_SETUP 
class MDM_DEALER_SETUP(db.Model):
    #DEALER_CODE = db.Column(db.String(100),unique=False, nullable=False)
    DEALER_CODE = db.Column(db.Integer, primary_key=True)
    DEALER_NAME = db.Column(db.String(100),unique=False, nullable=False)

    def __repr__(self):
        return '<MDM_DEALER_SETUP %r>' % self.DEALER_NAME

#MDM_CUS_SETUP 
class MDM_CUS_SETUP(db.Model):
    CUS_CODE = db.Column(db.Integer, primary_key=True)
    CUS_NAME = db.Column(db.String(100),unique=False, nullable=False)

    def __repr__(self):
        return '<MDM_CUS_SETUP %r>' % self.CUS_NAME

#MDM_SALES_TYPE_SETUP 
class MDM_SALES_TYPE_SETUP(db.Model):
    SD_TYPE_CODE = db.Column(db.Integer, primary_key=True)
    SD_TYPE_NAME = db.Column(db.String(100),unique=False, nullable=False)

    def __repr__(self):
        return '<MDM_SALES_TYPE_SETUP %r>' % self.SD_TYPE_NAME

#MDM_IT_SETUP
class MDM_IT_SETUP(db.Model):
    IT_CODE = db.Column(db.Integer, primary_key=True)
    IT_NAME = db.Column(db.String(100),unique=False, nullable=False)
    KEY_UNIT =  db.Column(db.String(50),unique=False, nullable=False)
    def __repr__(self):
        return '<MDM_IT_SETUP %r>' % self.IT_NAME


#SD_SO_OPERATION 
class CRM_SD_SO_OPERATION(db.Model):
    #RETAIL_ID = db.Column(db.Integer, primary_key=True)
    V_NO = db.Column(db.String(50), primary_key=True,nullable=False)
    V_DATE = db.Column(db.DateTime,unique=False, nullable=False)
    M_NO = db.Column(db.String(50),unique=False, nullable=False)
    CUS_CODE = db.Column(db.String(50),unique=False, nullable=False)
    EMP_CODE = db.Column(db.String(50),unique=False, nullable=False)
    SL_CODE = db.Column(db.String(50),unique=False, nullable=False)
    AGENT_CODE = db.Column(db.String(50),unique=False, nullable=False)
    SR_NO = db.Column(db.String(50),unique=False, nullable=False)
    IT_CODE = db.Column(db.String(50),unique=False, nullable=False)
    UNIT = db.Column(db.String(50),unique=False, nullable=False)
    QUANTITY = db.Column(db.String(50),unique=False, nullable=False)
    QUANTITY_2ND = db.Column(db.String(50),unique=False, nullable=False)
    QUANTITY_3RD = db.Column(db.String(50),unique=False, nullable=False)
    RATE = db.Column(db.String(50),unique=False, nullable=False)
    AMOUNT = db.Column(db.String(50),unique=False, nullable=False)
    NET_QUANTITY = db.Column(db.String(50),unique=False, nullable=False)
    NET_RATE = db.Column(db.String(50),unique=False, nullable=False)
    NET_AMOUNT = db.Column(db.String(50),unique=False, nullable=False)
    DELIVERY_DATE = db.Column(db.DateTime(50),unique=False, nullable=False)
    CUR_CODE = db.Column(db.String(50),unique=False, nullable=False)
    EXC_RATE = db.Column(db.String(50),unique=False, nullable=False)
    BATCH_NO = db.Column(db.String(50),unique=False, nullable=False)
    TRACK_NO = db.Column(db.String(50),unique=False, nullable=False)
    STOCK_BLOCK_FLAG = db.Column(db.String(50),unique=False, nullable=False)
    DEALER_CODE = db.Column(db.String(50),unique=False, nullable=False)
    DED_QTY = db.Column(db.String(50),unique=False, nullable=False)
    ADD_QTY = db.Column(db.String(50),unique=False, nullable=False)
    REJECT_FLAG = db.Column(db.String(50),unique=False, nullable=False)
    REF_FLAG = db.Column(db.String(50),unique=False, nullable=False)
    ADJUST_UID = db.Column(db.String(50),unique=False, nullable=False)
    ADJUST_DATE = db.Column(db.String(50),unique=False, nullable=False)
    ADJUST_REMARKS = db.Column(db.String(50),unique=False, nullable=False)
    PRIORITY_ID = db.Column(db.String(50),unique=False, nullable=False)
    OPENING_FLAG = db.Column(db.String(50),unique=False, nullable=False)
    SHIPPING_ADDRESS = db.Column(db.String(50),unique=False, nullable=False)
    SHIPPING_CONTACT_NO = db.Column(db.String(50),unique=False, nullable=False)
    SD_TYPE_CODE = db.Column(db.String(50),unique=False, nullable=False)
    AREA_ID = db.Column(db.String(50),unique=False, nullable=False)
    PERSON_NAME = db.Column(db.String(50),unique=False, nullable=False)
    SECTOR_CODE = db.Column(db.String(50),unique=False, nullable=False)
    REMARKS = db.Column(db.String(50),unique=False, nullable=False)
    DOC_CODE = db.Column(db.String(50),unique=False, nullable=False)
    COM_CODE = db.Column(db.String(50),unique=False, nullable=False)
    BRA_CODE = db.Column(db.String(50),unique=False, nullable=False)
    DIV_CODE = db.Column(db.String(50),unique=False, nullable=False)
    MAKE_UID = db.Column(db.String(50),unique=False, nullable=False)
    MAKE_DATE = db.Column(db.String(50),unique=False, nullable=False)
    SYNC_ID = db.Column(db.String(50),unique=False, nullable=False)
    SESSION_ID = db.Column(db.String(50),unique=False, nullable=False)
    MDY_DATE = db.Column(db.String(50),unique=False, nullable=False)
    MDY_UID = db.Column(db.String(50),unique=False, nullable=False)
    RECYCLED_UID = db.Column(db.String(50),unique=False, nullable=False)
    RECYCLED_DATE = db.Column(db.String(50),unique=False, nullable=False)
    RECYCLED_FLAG = db.Column(db.String(50),unique=False, nullable=False)
    REF_NO = db.Column(db.String(50),unique=False, nullable=False)
    REF_DOC_CODE = db.Column(db.String(50),unique=False, nullable=False)
    AUTHORIZED_QTY = db.Column(db.String(50),unique=False, nullable=False)
    PAY_MODE_CODE = db.Column(db.String(50),unique=False, nullable=False)
    DOC_IEL_ID = db.Column(db.String(50),unique=False, nullable=False)
    DOC_MODE = db.Column(db.String(50),unique=False, nullable=False)
    SCHEME_ADJUST_QTY = db.Column(db.String(50),unique=False, nullable=False)
    LINE_IT_DISCOUNT = db.Column(db.String(50),unique=False, nullable=False)
    LINE_IT_PREMIUM = db.Column(db.String(50),unique=False, nullable=False)
    DIS_PERCENT = db.Column(db.String(10),unique=False, nullable=False)
    PREMIUM_PERCENT = db.Column(db.String(50),unique=False, nullable=False)
    IT_SPEC = db.Column(db.String(50),unique=False, nullable=False)
    LC_ID = db.Column(db.String(50),unique=False, nullable=False)
    IT_SIZE_ID = db.Column(db.String(50),unique=False, nullable=False)
    COLOR_ID = db.Column(db.String(50),unique=False, nullable=False)
    FREE_QTY = db.Column(db.String(50),unique=False, nullable=False)
    BUNDLE_QTY = db.Column(db.String(50),unique=False, nullable=False)
    MRP = db.Column(db.String(50),unique=False, nullable=False)
    EXPIRY_DATE = db.Column(db.String(50),unique=False, nullable=False)

    def __repr__(self):
        return '<CRM_SD_SO_OPERATION %r>' % self.V_NO

db.create_all()

