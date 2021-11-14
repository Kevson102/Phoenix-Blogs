from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db, photos
from ..models import User, Blog, Comment
from .forms import BlogForm, CommentForm
from flask_login import login_required
from ..requests import get_random_quote

# Views
@main.route('/')
def index():
  '''
  Root page function that returns the index.html page
  '''
  random_quote = get_random_quote()
  title = "Welcome to Phoenix Blogs | TechBlogs"
  blogs = Blog.query.all()
  
  return render_template('index.html',title=title, blogs=blogs, quotes=random_quote)
###########################################################################

@main.route('/blog/content/<int:id>', methods = ['POST', 'GET'])
def blog_content(id):
  comments = Comment.query.all()
  blog = Blog.query.filter_by(id=id).all()
  
  return render_template('blog_content.html', blogs = blog, comments=comments)
###########################################################################

@main.route('/blogs/new_blog', methods = ['GET', 'POST'])
@login_required
def new_blog():
  blog_form = BlogForm()
  if blog_form.validate_on_submit():
    blog = Blog(blog_title = blog_form.blog_title.data, author = blog_form.author.data, blog_content = blog_form.blog_content.data)
    
    db.session.add(blog)
    db.session.commit()
    
    return redirect(url_for('main.index'))
  
  return render_template('new_blog.html', blog_form = blog_form)
###########################################################################

@main.route('/blog/content/comment', methods = ['GET', 'POST'])
def post_comment():
  comment_form = CommentForm()

  if comment_form.validate_on_submit():
    comment_message = comment_form.comment_message.data
    new_comment = Comment(comment_message = comment_message)
    
    db.session.add(new_comment)
    db.session.commit()
    
    return redirect(url_for('main.index'))
  return render_template('comments.html', comment_form = comment_form)

@main.route('/comment/delete/<int:id>')
@login_required
def delete(id):
  comment_to_delete = Comment.query.get(id)
  # db.session.delete(comment_to_delete)
  # db.session.commit()
  # return redirect(url_for('main.blog_content'))
  try:
    db.session.delete(comment_to_delete)
    db.session.commit()
    
    return redirect(url_for('main.index'))
  except:
    return "There was an error deleting the comment"
  

# @main.route('/blogs/blogpicture', methods = ['GET', 'POST'])
# def update_blog_display_pic(blogid):
#   blog = Blog.query.filter_by(id = blogid).first()
  
#   if 'photo' in request.files:
#     filename = photos.save(request.files['photo'])
#     path = f'photos/{filename}'
#     blog.blog_display_pic_path = path
#     db.session.commit()
    
#   return redirect(url_for(main.index))