#. Integrate a SQLite database with Flask to perform CRUD operations on a list of items
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
    items = Item.query.all()
    return render_template('2nd_project/index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = Item(name=request.form['item_name'])
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    item_to_delete = Item.query.get(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
    
# Ensure the app context is pushed so that db.create_all() works
with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)