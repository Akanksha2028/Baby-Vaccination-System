from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, timedelta
from extensions import db
from models.vaccination import VaccinationRecord
from models.user import User
from flask_mail import Message
from extensions import mail
from twilio.rest import Client

def start_scheduler(app):
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        func=lambda: run_with_context(app),
        trigger='interval',
        hours=24
    )

    scheduler.start()


def run_with_context(app):
    with app.app_context():
        send_reminders()

def send_reminders():
    records = VaccinationRecord.query.all()

    print("\n====== REMINDER LOG START ======\n")

    for record in records:

        if not record.next_due_date:
            continue

        user = User.query.get(record.user_id)

        if not user:
            continue

        date_str = record.next_due_date.strftime("%d-%m-%Y")

        message = f"Vaccination Reminder: {record.baby_name}'s vaccine ({record.vaccine_name}) is due on {date_str}"

        print("------------")
        print(f"User: {user.username}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone}")

        #  EMAIL
        print("[EMAIL SENT]")
        print(f"Message: {message}")

        # SMS
        if user.phone:
            print("[SMS SENT]")
            print(f"Message: {message}")
        else:
            print("[SMS SKIPPED] No phone number")

        print("------------\n")

    print("====== REMINDER LOG END ======\n")