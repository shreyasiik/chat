from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message received: ' + msg)
    emit('response', msg, broadcast=True)  # Send message to all clients

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
