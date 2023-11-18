from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret1234'
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for simplicity (update in production)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
