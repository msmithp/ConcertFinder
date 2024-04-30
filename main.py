# main.py controller
from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get_customers, create

app = Flask(__name__)

@app.route('/')
def login():
    if session["loggedin"]:
        return redirect(url_for("home"))

    user = get_user(request.form["username"])
    if user:
        session["username"] = user["username"]
        session["loggedin"] = True
        return redirect(url_for("home"))
    else:
        # invalid username message goes here
        pass

@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop("loggedin", None)
    return redirect(url_for('/'))

@app.route('/home')
def home():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return render_template("about.html")    

# @app.route('/display')
# def display():
#     customers = get_customers()
#     return render_template('display.html', customers = customers)

# #Single song
# @app.route('/songs/<int:id>/')
# def customer(id):
#     customer = get_one_customer(id)
#     return render_template('song.html', customer=customer)

# @app.route('/insert_form')
# def insert_form():
#     return render_template('insert.html')


@app.route('/add', methods=['POST'])
def add():
    create(request.form['customer_name'], request.form['customer_street'], request.form['customer_city'])
    return redirect(url_for('display'))

if __name__ == '__main__':
    app.run(debug=True)
