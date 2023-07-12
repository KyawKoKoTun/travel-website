from app import app
from views import *
from admin import *

if __name__ == '__main__':
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=80,
        )
