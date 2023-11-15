# Implement user sessions in a Flask app to store and display user-specific data
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '1234'  # Set a secret key for session security

@app.route("/", methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # Get the user input from the form
        # using form input and result output of the 4th_project
        user_input = request.form.get('user_input')

        # Store user-specific data in the session
        session['user_data'] = user_input

        # Redirect to a new route to display user-specific data
        return redirect(url_for('display_data')) # generate url to an endpoint in this case display_data

    # Render the form template for GET requests
    return render_template('4th_project/form.html')

@app.route("/display_data")
def display_data():
    # Retrieve user-specific data from the session
    user_data = session.get('user_data')

    # Render a template to display user-specific data
    return render_template('4th_project/result.html', input=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
