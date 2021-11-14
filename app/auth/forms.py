from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  username = StringField('Enter Preferred Username', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords MUST Match')])
  password_confirm = PasswordField('Confirm Password', validators=[Required()])
  submit = SubmitField('Sign Up')
  
  def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('An account with that email already exists')
    
  def validate_username(self, data_field):
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError('The Username you entered is taken. Please enter a different username')
    
class LoginForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign In')