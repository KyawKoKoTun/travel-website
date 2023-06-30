from datetime import timedelta
import os
from dotenv import load_dotenv


class Config(object):

    SECRET_KEY = 'flask_740d9e58782809e59424751c9b5279af09e707febe831fec78ff1e2571f52b89'
    SESSION_PERMANENT = True
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)

    def __init__(self):
        load_dotenv()
        self.SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
