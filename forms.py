import email
from email import contentmanager
from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SelectField, EmailField, TextAreaField, ValidationError
from wtforms.validators import DataRequired

SERVICES = [
    (0, "Please Select A Service"),
    (1, 'Asphalt'),
    (2, 'Concrete'),
    (3, 'Home Improvement'),
    (4, 'Masonry Work'),
    (5, 'Paver Sealing'),
    (6, 'Pressure Washing'),
]


class ContactForm(FlaskForm):
    name = StringField('Name', 
                             validators=[DataRequired()],
                             render_kw={"placeholder": "John Smith"})
    phone = StringField('Phone Number', 
                        validators=[DataRequired()],
                        render_kw={"placeholder": "516-581-5636"})
    email = EmailField('Email Address',
                         validators=[DataRequired()],
                         render_kw={"placeholder": "example123@outlook.com"})
    address = StringField('Address', 
                          validators=[DataRequired()],
                          render_kw={"placeholder": "239 Cherry Lane, Levittown"})
    
    service_type = SelectField("Which Service Are You Interested In?", 
                               choices = SERVICES, coerce=int )

    message = TextAreaField("Message",
                            render_kw={"placeholder": "Tell us what you need! We are more than happy to help."})
    
    def validate_service_type(self, field):
        if field.data == 0:
            raise ValidationError("Please select a valid service")


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})

    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})

    email = EmailField("Email", validators=[DataRequired()], render_kw= {"placeholder": "Enter your email address"})

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})

    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})


class ReviewForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired()])

    message = TextAreaField("Message", render_kw={"placeholder": "Tell us about your experience, your feedback is important to us."})

    service_type = SelectField("Select the service you received",
                               validators=[DataRequired()],
                               choices = SERVICES, coerce=int )

    def validate_service_type(self, field):
        if field.data == 0:  # Check if placeholder is selected
            raise ValueError("Please select a valid service.")

