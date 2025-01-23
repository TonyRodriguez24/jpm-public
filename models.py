from database import db
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from emails import send_email
import os
from info import SERVICES

# Load the .env file
load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")



bcrypt = Bcrypt()

def get_column_names(cls):
        return [column.name for column in cls.__table__.columns] # type: ignore

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False, default = False) #True if admin

    @classmethod
    def create_admin(cls, username, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(username = username, password = hashed_password, is_admin = True) # type: ignore
        
    def set_password(self, new_password):
        if self.is_admin:
            self.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            return True
        return False
    
    @classmethod
    def authenticate_admin(cls, username, password):
        admin = Admin.query.filter_by(username = username).first()
        if admin and bcrypt.check_password_hash(admin.password,  password):
            return admin
        else:
            return None

#in seed py
class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False, unique = True)

class Projects(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    type_of_work = db.Column(db.String(50), nullable = False)

    #foreign keys
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))

class Reviews(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    rating = db.Column(db.Integer, nullable = False)
    message = db.Column(db.Text(), nullable = True)

    #foreign key
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    #foreign key
    service_type = db.Column(db.Integer, db.ForeignKey('services.id'))
    referral = db.Column(db.String(50))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

    #relationship
    service = db.relationship('Services', backref='contacts')

    @classmethod
    def create_complete_contact(cls, form):
        try:
            # Step 1: Validate form data
            if not form.name.data or not form.email.data:
                raise ValueError("Name and Email are required.")

            # Debug form data
            print("Form Data:")
            print(f"Name: {form.name.data}, Email: {form.email.data}, Phone: {form.phone.data}")
            print(f"Service Type: {form.service_type.data}, Address: {form.address.data}")
            print(f"Message: {form.message.data}, Referral: {form.referral.data}")

            # Step 2: Save to the database
            new_contact = cls(
                name=form.name.data,
                phone=form.phone.data,
                email=form.email.data,
                service_type=form.service_type.data,
                address=form.address.data,
                message=form.message.data,
                referral=form.referral.data
            )
            db.session.add(new_contact)
            db.session.commit()


            service_type_dict = dict(SERVICES)

            # Get the service name from the dictionary
            service_name = service_type_dict.get(form.service_type.data, "Unknown Service Type")

            # Step 3: Debug email parameters
            subject = f"Form submission from {form.name.data}"
            # Construct the email content
            content = f"""
                <h2>New Complete Contact Form</h2>
                <p><strong>Name:</strong> {form.name.data}</p>
                <p><strong>Email:</strong> {form.email.data}</p>
                <p><strong>Phone:</strong> {form.phone.data}</p>
                <p><strong>Service Type:</strong> {service_name}</p>
                <p><strong>Address:</strong> {form.address.data}</p>
                """

            # Add message if it's provided
            if form.message.data:
                content += f"<p><strong>Message:</strong> {form.message.data}</p>"

            # Step 4: Send the email
            try:
                response = send_email(
                    api_key=SENDGRID_API_KEY,
                    from_email=MAIL_DEFAULT_SENDER,
                    to_email="tonyrodriguez2497@gmail.com",
                    subject=subject,
                    content=content
                )
                if response != 202:
                    raise Exception(f"Email failed to send with status code: {response}")
                print("Email sent successfully.")
                return True
            except Exception as email_err:
                print(f"Email sending failed: {email_err}")
                return False

        except ValueError as val_err:
            print(f"Validation error: {val_err}")
            return False

        except Exception as error:
            print(f"Error creating contact: {error}")
            db.session.rollback()  # Rollback the database session
            return False


    @classmethod
    def create_contact(cls, form):
        try:
            new_contact = cls(  name = form.name.data, phone = form.phone.data, email = form.email.data,service_type = form.service_type.data) # type: ignore
            db.session.add(new_contact)
            db.session.commit()
            return True
        
        except Exception as error:
            print(f'Error creating contact: {error}')
            return False