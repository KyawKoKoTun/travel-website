from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *
from app import *


admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Place, db.session))
admin.add_view(ModelView(Hotel, db.session))
admin.add_view(ModelView(Booking, db.session))
admin.add_view(ModelView(Attraction, db.session))
admin.add_view(ModelView(Blog, db.session))

