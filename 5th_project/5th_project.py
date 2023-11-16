#Design a Flask app with proper error handling for 404 and 500 errors

from flask import Flask, render_template,abort

app = Flask(__name__)

# Sample route that triggers a 404 error
@app.route('/')
def home():
    # Simulate a 404 error by using abort(404)
    abort(404)

# Custom error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Sample route that triggers a 500 error
@app.route('/error')
def trigger_error():
    # This will raise a RuntimeError to simulate a 500 error
    raise RuntimeError("Simulating a 500 Internal Server Error")

# Custom error handler for 500 Internal Server Error
@app.errorhandler(RuntimeError)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
