# Create a Flask app with a form that accepts user input and displays it

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def handle_form():
    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.form.get('user_input')
        # Render a template with the entered data
        context = {'input': user_input}
        return render_template('4th_project/result.html',**context)
    # Render the form template for GET requests
    return render_template('4th_project/form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)