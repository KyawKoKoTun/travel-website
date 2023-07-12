from datetime import timedelta

class Config(object):
    SECRET_KEY = 'flask_740d9e58782809e59424751c9b5279af09e707febe831fec78ff1e2571f52b89'
    SESSION_PERMANENT = True
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database.db"
