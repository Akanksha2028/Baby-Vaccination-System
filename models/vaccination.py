from extensions import db
from datetime import datetime

class VaccinationRecord(db.Model):
    __tablename__ = 'vaccination_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    baby_name = db.Column(db.String(100))
    vaccine_name = db.Column(db.String(100))
    next_due_date = db.Column(db.Date)
    parent_name = db.Column(db.String(100))
    dose_number = db.Column(db.Integer)
    vaccination_date = db.Column(db.Date) 
    created_at = db.Column(db.DateTime,  default=datetime.utcnow)