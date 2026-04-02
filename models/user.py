from extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(150))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(15))