from flask import *
from models import *
from settings import *

app = Flask(__name__)

db.init_app(app)
app.config.from_object(Config)


