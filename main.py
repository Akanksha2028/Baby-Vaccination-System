from flask import Flask
from extensions import db, jwt,mail
from scheduler import start_scheduler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2820@localhost/vaccination_tracker'
app.config['JWT_SECRET_KEY'] = 'supersecretkey1234567890'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_USE_TLS'] = True

db.init_app(app)
jwt.init_app(app)
mail.init_app(app)

from routes.user_routes import user_bp
from routes.vaccine_routes import vaccine_bp

app.register_blueprint(user_bp)
app.register_blueprint(vaccine_bp)

#start_scheduler(app)

if __name__ == '__main__':
    app.run(debug=True)