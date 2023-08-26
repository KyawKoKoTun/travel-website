from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import *
from app import *

class CustomBookingView(ModelView):
    column_list = ['hotel', 'user', 'date']  # Include 'date' for displaying in list view

    # Customize column formatters to show user.nrc and user.birthday
    column_formatters = {
        'user': lambda v, c, m, p: f"{m.user.name} - {m.user.nrc} - {m.user.birthday}"
    }
    form_columns = ['hotel', 'user', 'date']  # Include 'date' in the form for adding/editing bookings

    # To make the 'user' field show 'nrc' and 'name' attributes
    column_auto_select_related = True
    column_auto_select_related_filters = ['user.nrc', 'user.birthday']

    # Customize the single model view to show user.nrc and user.birthday
    column_details_list = ['hotel', 'user.name', 'user.nrc', 'user.birthday', 'date']

admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Place, db.session))
admin.add_view(ModelView(Hotel, db.session))
admin.add_view(ModelView(Attraction, db.session))
admin.add_view(ModelView(Blog, db.session))
admin.add_view(CustomBookingView(Booking, db.session))  # Use the custom view here
admin.add_view(ModelView(Comment, db.session))
