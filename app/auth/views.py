from flask import render_template, redirect, url_for
from . import auth
from ..models import User
from .forms import RegistrationForm
from .. import db

@auth.route('/login')
def login():
  return render_template('auth/login.html')

@auth.route('/register', methods = ["GET", "POST"])
def register():
  registration_form = RegistrationForm()
  if registration_form.validate_on_submit():
    user = User(email = registration_form.email.data, username = registration_form.username.data, pass_secure = registration_form.password.data)
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))
  title = "Create New Account"
  return render_template('auth/register.html', registration_form = registration_form, title=title)