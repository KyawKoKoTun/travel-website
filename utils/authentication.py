from models import *
from app import *


def token_to_user(token):
    with app.app_context():
        try:
            user = User.query.filter_by(token=token)[0]
            return user
        except:
            return None
