# Implement notifications in a Flask app using web_sockets to notify users of updates
from flask import Flask,render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index():
   return render_template('main.html')

# you can implement feature to allow super user to only access the send_notification page
#@super_user
@app.route('/send_notification')
def send_notification():
   return render_template('send_notification.html')
   
@socketio.on('message')
def get_notification(notification):
   print("notification: ",notification)
   socketio.emit('notification',notification)



if __name__ == '__main__':
   socketio.run(app,debug=True)