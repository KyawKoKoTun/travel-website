from app import *
from .authentication import *

def render(*args ,**kwargs):
    blogs = Blog.queryAll()[:6]
    return render_template(*args, **kwargs, blogs_foot=blogs, signed_in = token_to_user(session.get('token')))