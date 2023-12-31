from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Query:
    @classmethod
    def queryOne(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs)[0]
        except:
            return None
    
    @classmethod
    def queryAll(cls, **kwargs):
        return list(cls.query.filter_by(**kwargs).all())


class User(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(100))
    password = db.Column(db.String(100))
    nrc = db.Column(db.String(255))
    birthday = db.Column(db.String(100))
    bookings = db.relationship('Booking', backref='user', lazy=True)
    token = db.Column(db.String(100), unique=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return f"{self.name} - {self.nrc} - {self.birthday}"


class Place(db.Model, Query):
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
    fact1 = db.Column(db.Text)
    fact2 = db.Column(db.Text)
    fact3 = db.Column(db.Text)
    history = db.Column(db.Text)
    hotels = db.relationship('Hotel', backref='place', lazy=True)
    attractions = db.relationship('Attraction', backref='place', lazy=True)
    plane = db.Column(db.Text, nullable=True)
    car = db.Column(db.Text, nullable=True)
    train = db.Column(db.Text, nullable=True)
    ship = db.Column(db.Text, nullable=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __repr__(self):
        return self.name



class Hotel(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    price = db.Column(db.Integer)
    name = db.Column(db.String(100))
    location = db.Column(db.String(200))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    bookings = db.relationship('Booking', backref='hotel', lazy=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __repr__(self):
        return self.name


class Booking(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(100))
    duration = db.Column(db.Integer, default=1)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))



class Attraction(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    title = db.Column(db.String(100))
    image1 = db.Column(db.String(100))
    image2 = db.Column(db.String(100))
    image3 = db.Column(db.String(100))
    text1 = db.Column(db.Text)
    text2 = db.Column(db.Text)
    text3 = db.Column(db.Text)
    text4 = db.Column(db.Text)
    comments = db.relationship('Comment', backref='attraction', lazy=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    

class Comment(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    attraction_id = db.Column(db.Integer, db.ForeignKey('attraction.id'), nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=True)

    text = db.Column(db.Text)


class Blog(db.Model, Query):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    to_do = db.Column(db.Boolean)
    image1 = db.Column(db.String(100))
    image2 = db.Column(db.String(100))
    image3 = db.Column(db.String(100))
    text1 = db.Column(db.Text)
    text2 = db.Column(db.Text)
    text3 = db.Column(db.Text)
    text4 = db.Column(db.Text)
    comments = db.relationship('Comment', backref='blog', lazy=True)

