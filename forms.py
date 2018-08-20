from flask_wtf import FlaskForm, RecaptchaField
from wtforms import  StringField , PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    firstname = StringField("First name", validators=[DataRequired("Enter your name")])
    lastname = StringField("Last name", validators=[DataRequired("Enter your last name")])
    email =  StringField("Email", validators=[DataRequired("Provide your email"), Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[DataRequired("Enter a valid password"), Length(min=8, message="Password must be a minimum of 8 charaters")])
    submit = SubmitField("Submit", validators=[DataRequired()])
    #recaptcha = RecaptchaField({'hl': 'zh', 'render': 'explicit'})
    