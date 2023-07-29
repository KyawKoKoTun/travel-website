from flask import *
from models import *
from settings import *

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)


