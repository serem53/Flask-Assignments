#Build a Flask app with static HTML pages and navigate between them.
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>this is my home page</h1>"

@app.route("/about")
def about_page():
    return "<h1>this is my about page<h1>"

@app.route("/settings")
def settings_page():
    return "<h1>this is my settings page</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
