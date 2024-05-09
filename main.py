# main.py controller
from flask import Flask, redirect, request, url_for, render_template, session, jsonify
from db import get_user, get_events, get_artists, get_upcoming_events, get_tickets, insert_user, get_cities
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # very secure


@app.context_processor
def utility_processor():
    def format_datetime(dt):
        # get day and hour as decimal value
        day = int(dt.strftime("%d"))
        hr = int(dt.strftime("%I"))

        # return formatted date
        return dt.strftime(f"%a %b {day}, %Y, {hr}:%M %p")

    def cities():
        return get_cities()

    return dict(format_datetime=format_datetime, cities=cities)


@app.route('/')
def root():
    session["loggedin"] = False

    # return render_template('login.html')
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # no message by default
    msg = None
    user = None

    # if user input something...
    if request.method == 'POST':
        user = get_user(request.form["username"])
        if user["username"] != "username":  # replace with actual logic
            msg = "Invalid login"
        else:
            session["username"] = user["username"]
            session["loggedin"] = True
            return redirect(url_for("home"))

    return render_template("login.html", msg=msg, user=user)


@app.route("/create_account", methods=['GET', 'POST'])
def create_account():
    # no message by default
    msg = None
    new_user = None

    # if user input something...
    if request.method == 'POST':
        new_user = request.form
        if new_user["username"] != "username":  # replace with actual logic to test if username is taken
            msg = "Username is already taken"
        else:
            insert_user(new_user)
            return redirect(url_for("login"))

    return render_template("create_account.html", msg=msg, user=new_user)


@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop("loggedin", None)
    return redirect("/")


@app.route('/home')
def home():
    upcoming = get_upcoming_events()
    if session["loggedin"]:
        tickets = get_tickets(session["username"])
    else:
        tickets = None

    return render_template("index.html", upcoming=upcoming, tickets=tickets)


@app.route('/search_events')
def search_events():
    return render_template("search_events.html")


@app.route('/event_search', methods=['POST'])
def do_event_search():
    query = request.form["query"]
    events = get_events(query)
    return render_template('list_events.html', query=query, events=events)


@app.route('/account')
def account():
    return render_template("account.html")

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


# @app.route('/add', methods=['POST'])
# def add():
#     create(request.form['customer_name'], request.form['customer_street'], request.form['customer_city'])
#     return redirect(url_for('display'))


if __name__ == '__main__':
    app.run(debug=True)
