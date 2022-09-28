from shop import db
from datetime import datetime

#VISIT ENTRY
class CRM_OP_VISIT(db.Model):
    VISIT_ID = db.Column(db.Integer, primary_key=True)
    EMPLOYEE_ID = db.Column(db.Integer,unique=False, nullable=False)
    ROUTE_ID = db.Column(db.Integer,unique=False, nullable=False)

    VISIT_DATE = db.Column(db.String(80), unique=True, nullable=False)
    CUSTOMER_ID = db.Column(db.Integer,unique=False, nullable=False)
    WORKS = db.Column(db.String(250), unique=True, nullable=False)

    REMARKS = db.Column(db.String(100), unique=True, nullable=False)
    PRODUCT_CODE = db.Column(db.Integer, unique=True, nullable=False)
    AVAILABLE_QTY = db.Column(db.Integer, unique=True, nullable=False)
    def __repr__(self):
        return '<CRM_OP_VISIT %r>' % self.EMPLOYEE_ID