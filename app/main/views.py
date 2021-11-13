from flask import render_template, redirect, url_for, abort, request
from . import main
from .. import db, photos
from ..models import User, Blog, Comment
from .forms import BlogForm

# Views
@main.route('/')
def index():
  '''
  Root page function that returns the index.html page
  '''
  title = "Welcome to Phoenix Blogs | TechBlogs"
  blogs = Blog.query.all()
  
  return render_template('index.html',title=title, blogs=blogs)

@main.route('/blog/content/<int:id>', methods = ['POST', 'GET'])
def blog_content(id):
  blog = Blog.query.filter_by(id=id).all()
  
  return render_template('blog_content.html', blogs = blog)

@main.route('/blogs/new_blog', methods = ['GET', 'POST'])
def new_blog():
  blog_form = BlogForm()
  if blog_form.validate_on_submit():
    blog = Blog(blog_title = blog_form.blog_title.data, author = blog_form.author.data, blog_content = blog_form.blog_content.data)
    
    db.session.add(blog)
    db.session.commit()
    
    return redirect(url_for('main.index'))
  
  return render_template('new_blog.html', blog_form = blog_form)


# @main.route('/blogs/blogpicture', methods = ['GET', 'POST'])
# def update_blog_display_pic(blogid):
#   blog = Blog.query.filter_by(id = blogid).first()
  
#   if 'photo' in request.files:
#     filename = photos.save(request.files['photo'])
#     path = f'photos/{filename}'
#     blog.blog_display_pic_path = path
#     db.session.commit()
    
#   return redirect(url_for(main.index))