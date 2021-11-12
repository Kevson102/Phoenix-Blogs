from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db

# Views
@main.route('/')
def index():
  '''
  Root page function that returns the index.html page
  '''
  
  return render_template('index.html',)