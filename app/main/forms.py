from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
  blog_title = StringField('Enter the blog title', validators=[Required()])
  
  blog_content = StringField('Enter the content of the Blog', validators=[Required()])
  