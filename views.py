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


@app.route('/blog/<id>')
def blog():
    return render_template('blog.html')


@app.route('/hotel/<id>')
def hotel():
    return render_template('hotel.html')