from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Optional, EqualTo, Length
from app.info import SERVICES, REFERRAL_OPTIONS

class ContactForm(FlaskForm):
    """Creates contact form: address, referral, message are left optional to create a quick version of form"""

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
                          validators=[Optional()],
                          render_kw={"placeholder": "239 Cherry Lane, Levittown"})
    
    service_type = SelectField("Which Service Are You Interested In?", 
                            choices = SERVICES, coerce=int, validators=[DataRequired()] )
    
    referral = SelectField("How did you hear about us", 
                            choices = REFERRAL_OPTIONS, validators=[Optional()] )
    
    
    message = TextAreaField("Message",
                            validators=[Optional()],
                            render_kw={"placeholder": "Tell us what you need! We are more than happy to help."})
    
class LoginForm(FlaskForm):
    """Form for logging admin in"""

    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})


class SetPasswordForm(FlaskForm):
    """Form for admin changing a password"""

    new_password = PasswordField(
        'New Password', 
        validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long.")]
    )
    confirm_password = PasswordField(
        'Confirm New Password', 
        validators=[DataRequired(), EqualTo('new_password', message="Passwords must match.")]
    )

# class ReviewForm(FlaskForm):
#     rating = IntegerField("Rating", validators=[DataRequired()])

#     message = TextAreaField("Message", render_kw={"placeholder": "Tell us about your experience, your feedback is important to us."})

#     service_type = SelectField("Select the service you received",
#                                validators=[DataRequired()],
#                                choices = SERVICES, coerce=int )

#     def validate_service_type(self, field):
#         if field.data == 0:  # Check if placeholder is selected
#             raise ValueError("Please select a valid service.")
        
class ProjectForm(FlaskForm):
    """Form for adding a project *needs to be fleshed out"""

    type_of_work = StringField(
        'Type of Work',
        validators=[DataRequired()],
        render_kw={"placeholder": "e.g., Residential Masonry"}
    )
    service_id = SelectField(
        'Service',
        choices = SERVICES,coerce=int,  # Expect an integer (foreign key)
        validators=[DataRequired()]
    )
