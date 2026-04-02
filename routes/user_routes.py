from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user', __name__)

# Register
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        phone = data.get('phone')
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User registered"})

# Login
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(email=data['email']).first()

    if user and user.password == data['password']:
        token = create_access_token(identity=str(user.id))
        return jsonify({"token": token})

    return jsonify({"msg": "Invalid credentials"}), 401