# Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"Hello, {username}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post ID: {post_id}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)
