#  Build a Flask app that updates data in real-time using WebSocket connections.
#This is an example of how to build a Flask application with WebSockets for real-time data update.

from flask import Flask,render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

#Define Routes
@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('connect')
def handle_connect():
   print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
   print ("Client disconnected")

@socketio.on('message')
def handle_update_data(data):
   print(data)
   socketio.emit('update_data',data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
