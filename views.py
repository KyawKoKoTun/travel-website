from app import *


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/bagan')
def bagan():
    return render_template('place.html')


@app.route('/place/<id>')
def place():
    return render_template('place.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html', title='Blogs about Myanmar')


@app.route('/to_dos')
def to_dos():
    return render_template('blogs.html', title='Things to do in Myanmar')


@app.route('/places')
def places():
    return render_template('blogs.html', title='Places to visit in Myanmar')


@app.route('/hotel')
def hotel():
    return render_template('hotel.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html', signed_in = True)
