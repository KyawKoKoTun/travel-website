from app import *
from .authentication import *

def render(*args ,**kwargs):
    return render_template(*args, **kwargs, signed_in = token_to_user(session.get('token')))