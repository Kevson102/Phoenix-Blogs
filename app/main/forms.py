from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
  
  blog_title = StringField('Enter the blog title', validators=[Required()])
  author = StringField('Author\'s name', validators=[Required()])
  blog_content = TextAreaField('Enter the content of the Blog', validators=[Required()])
  submit = SubmitField('Post Blog')
  
  
class CommentForm(FlaskForm):
  comment_message = StringField('Leave a comment', validators=[Required()])
  submit = SubmitField('Post Comment')