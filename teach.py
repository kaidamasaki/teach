from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send

app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('ping')
def on_create(data):
    print("********************************************************************************")
    print("In Ping")
    print(data)
    print("********************************************************************************")

    emit('pong', {"message": "Hello from Python!"})

if __name__ == '__main__':
    socketio.run(app)
