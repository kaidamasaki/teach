import os

from flask import Flask, render_template
from flask_meld import Meld

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

meld = Meld()
meld.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.socketio.run(app, debug=True)
