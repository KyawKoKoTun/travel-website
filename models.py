from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    bookings = db.relationship('Booking', backref='user', lazy=True)
    token = db.Column(db.String(100), unique=True)


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    image1 = db.Column(db.String(200))
    image2 = db.Column(db.String(200))
    image3 = db.Column(db.String(200))
    description = db.Column(db.Text)
    text1 = db.Column(db.Text)
    text2 = db.Column(db.Text)
    text3 = db.Column(db.Text)
    text4 = db.Column(db.Text)
    reachable = db.relationship('Reachable', backref='place', lazy=True)
    hotels = db.relationship('Hotel', backref='place', lazy=True)
    attractions = db.relationship('Attraction', backref='place', lazy=True)


class Reachable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(1))


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    bookings = db.relationship('Booking', backref='hotel', lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200))
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    text1 = db.Column(db.Text)
    text2 = db.Column(db.Text)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    image1 = db.Column(db.String(200))
    image2 = db.Column(db.String(200))
    image3 = db.Column(db.String(200))
    text1 = db.Column(db.Text)
    text2 = db.Column(db.Text)
    text3 = db.Column(db.Text)
    text4 = db.Column(db.Text)
