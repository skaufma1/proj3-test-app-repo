from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from sqlalchemy import desc
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_site.db'

# Creating an object of SQLAlchemy, based on the Flask object
db = SQLAlchemy(app)

# This migration step can be done before or after the schema specs in classes
migrate = Migrate(app, db)

# Table specs. Each table has its own class
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    datetime = db.Column(db.String(20), unique=False, nullable=False)

    # Predefined function definition - for allowing the printing of the objects = records
    # __repr__ can do the same function as __str__
    def __str__(self):
        return f"Name: {self.name}, DateTime: {self.datetime}"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/success/<name>")
def success(name):
    return render_template("success.html", name=name)

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form.get("name")

        # insert a datetime value into the table
        now = datetime.now()
        formatted_date = now.strftime('%d-%m-%Y %H:%M')
        print(f"DateTime = {formatted_date}")

        # We call the table class - to create an object, for a record of the table
        p = Profile(name=user, datetime=formatted_date)
        # Saving the table object = record in the DB
        db.session.add(p)
        db.session.commit()

        return redirect(url_for('success', name=user))
    else:
        # user = request.form.get("name", "DEVBOSS")
        return render_template("login.html")

@app.route("/home")
def homepage():
    return render_template("login.html")

@app.route('/results_popup')
def show_results():
    # Retrieve all data from SQLite table
    users_data = Profile.query.order_by(desc(Profile.datetime)).all()
    print(users_data)
    # Pass data to template
    return render_template('results_popup.html', users_data=users_data)

if __name__ == "__main__":
    app.run(debug=True)
