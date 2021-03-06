from werkzeug.security import check_password_hash, generate_password_hash
from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255), unique=True, index = True)
  profile_pic_path = db.Column(db.String)
  user_bio = db.Column(db.String)
  pass_secure = db.Column(db.String(255))
  blogs = db.relationship('Blog', backref='user', lazy="dynamic")
  
  @property
  def password(self):
    raise AttributeError('You are not authorized to access password attribute')
  
  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)
  
  def __repr__(self):
    return f'User {self.username}'
  
class Blog(db.Model):
  __tablename__='blogs'
  
  id = db.Column(db.Integer, primary_key=True)
  blog_title = db.Column(db.String(500))
  author = db.Column(db.String(50))
  blog_display_pic_path = db.Column(db.String)
  blog_content = db.Column(db.String)
  date_posted = db.Column(db.DateTime, default = datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  comments = db.relationship('Comment', backref='comment', lazy="dynamic")
  
  def save_blog(self):
    db.session.add(self)
    db.session.commit()
  
  def __repr__(self):
    return f'Blog {self.blog_content}'
  
  
class Comment(db.Model):
  __tablename__='comments'
  
  id = db.Column(db.Integer, primary_key=True)
  comment_message = db.Column(db.String(1500))
  date_posted = db.Column(db.DateTime, default = datetime.utcnow)
  blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
  
  def __repr__(self):
    return f'Comment {self.comment_message}'
  
class Quote:
  '''
  This is a quote class that is used for defining a quote object
  '''
  def __init__(self, id, author, quote):
    '''
    Method that initializes the Quote object
    Args:
      id: The id of the quote
      author: The author of the quote
      quote: The quote statement
    '''
    self.id = id
    self.author = author
    self.quote = quote