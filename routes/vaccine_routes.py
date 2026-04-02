from flask import Blueprint, request, jsonify
from extensions import db
from models.vaccination import VaccinationRecord
from flask_jwt_extended import jwt_required
from datetime import datetime
vaccine_bp = Blueprint('vaccine', __name__)

# CREATE
@vaccine_bp.route('/add', methods=['POST'])
@jwt_required()
def add_record():
    data = request.json

    record = VaccinationRecord(
    user_id=data.get('user_id'),
    baby_name=data.get('baby_name'),
    parent_name=data.get('parent_name'),
    vaccine_name=data.get('vaccine_name'),
    dose_number=data.get('dose_number'),
    vaccination_date=datetime.strptime(data.get('vaccination_date'), "%Y-%m-%d"),
    next_due_date=datetime.strptime(data.get('next_due_date'), "%Y-%m-%d")
)

    db.session.add(record)
    db.session.commit()

    return jsonify({"msg": "Record added successfully"})

# READ
@vaccine_bp.route('/records', methods=['GET'])
@jwt_required()
def get_records():
    records = VaccinationRecord.query.all()

    data = []
    for r in records:
        data.append({
            "id": r.id,
            "baby_name": r.baby_name,
            "vaccine_name": r.vaccine_name
        })

    return jsonify(data)

# UPDATE
@vaccine_bp.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_record(id):
    record = VaccinationRecord.query.get(id)
    data = request.json

    record.baby_name = data['baby_name']
    db.session.commit()

    return jsonify({"msg": "Updated"})

# DELETE
@vaccine_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_record(id):
    record = VaccinationRecord.query.get(id)

    db.session.delete(record)
    db.session.commit()

    return jsonify({"msg": "Deleted"})

@vaccine_bp.route('/test-reminder', methods=['GET'])
def test_reminder():
    from scheduler import send_reminders
    send_reminders()
    return {"msg": "Reminder triggered successfully"}