from app import *
from utils import *


@app.errorhandler(404)
def resource_not_found(e):
    return render_template('404.html')

@app.route('/')
def main():
    return render('home.html')


@app.route('/visa')
def visa():
    return render('visa.html')


@app.route('/how-to-travel')
def how_to_travel():
    return render('how-to-travel.html')


@app.route('/place/<int:id>')
def place(id):
    place = Place.queryOne(id=id)
    if place:
        attractions = Attraction.queryAll(place_id=place.id)
        hotels = Hotel.queryAll(place_id=place.id)
        return render('place.html', place=place, attractions=attractions, hotels=hotels)
    else:
        return render_template('404.html')


@app.route('/place/name/<name>')
def place_by_name(name):
    place = Place.queryOne(name=name)
    if place:
        attractions = Attraction.queryAll(place_id=place.id)
        hotels = Hotel.queryAll(place_id=place.id)
        return render('place.html', place=place, attractions=attractions, hotels=hotels)
    else:
        return render_template('404.html')


@app.route('/places')
def places():
    places = Place.queryAll()
    return render('blogs.html', title='Places to visit in Myanmar', blogs=places)


@app.route('/blog/<int:id>')
def blog(id):
    blog = Blog.queryOne(id=id)
    blogs = []
    for b in Blog.queryAll():
        if b.to_do == blog.to_do and b.title != blog.title:
            blogs.append(b)
    return render('blog.html', blog=blog, blogs=blogs)


@app.route('/attraction')
def attraction():
    attraction = Attraction.queryOne()
    attractions = []
    for a in Attraction.queryAll():
        if a.place_id == attraction.place_id and a.name != attraction.name:
            attractions.append(a)
    return render('blog.html', blog=attraction, blogs=attractions, attractions=True)


@app.route('/blogs')
def blogs():
    blogs = Blog.queryAll(to_do=False)
    return render('blogs.html', title='Blogs about Myanmar', blogs=blogs)


@app.route('/to_dos')
def to_dos():
    to_dos = Blog.queryAll(to_do=True)
    return render('blogs.html', title='Things to do in Myanmar', blogs=to_dos)


@app.route('/hotel/<int:id>')
def hotel(id):
    hotel = Hotel.queryOne(id=id)
    return render('hotel.html', hotel=hotel)


@app.route('/book/<int:id>/<month>/<day>/<year>')
def book(id, month, day, year):
    booking = Booking(user_id=token_to_user(
        session['token']).id, hotel_id=id, date=f"{day} {month} {year}")
    db.session.add(booking)
    db.session.commit()
    return jsonify({
        'status': 'booked'
    })


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render('login.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user = User.queryOne(email=email, password=generate_sha256_hash(password))
        if user:
            session['token'] = user.token
            return redirect('/')
        else:
            return render('login.html', message="Please enter valid credentials.")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render('register.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User.queryOne(email=email)
        if not user:
            if validate_email(email):
                if len(password) > 4:
                    token = generate_sha256_hash(email)
                    user = User(name=name, email=email,
                                password=generate_sha256_hash(password), token=token)
                    db.session.add(user)
                    db.session.commit()
                    session['token'] = token
                    return redirect('/')
                else:
                    return render('register.html', message='Please choose a stronger password.')
            else:
                return render('register.html', message='Please enter a valid email.')
        else:
            return render('register.html', message='User email already exists.')


@app.route('/logout')
def logout():
    session['token'] = None
    return redirect('/')


@app.route('/profile')
def profile():
    user = token_to_user(session.get('token'))
    if user:
        bookings = []
        for booking in Booking.queryAll():
            if booking.user_id == user.id:
                bookings.append(
                    [booking, Hotel.queryOne(id=booking.hotel_id)])
        return render('profile.html', bookings=bookings)
    else:
        return redirect('/login')
