# main.py controller
from flask import Flask, redirect, request, url_for, render_template, session, jsonify
from db import get_user, get_events, get_upcoming_events, get_tickets, insert_user, get_cities, insert_review, get_reviews, get_all_events
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # very secure

 
@app.context_processor
def utility_processor():
    def format_datetime(dt):
        # get day and hour as decimal value
        day = int(dt.strftime("%d"))
        hr = int(dt.strftime("%I"))

        # return formatted datetime
        return dt.strftime(f"%a %b {day}, %Y, {hr}:%M %p")

    def format_date(d):
        # get day as decimal value
        day = int(d.strftime("%d"))

        # return formatted date
        return d.strftime(f"%a %b {day}, %Y")

    def cities():
        return get_cities()

    def all_events():
        return get_all_events()

    return dict(format_datetime=format_datetime, format_date=format_date, cities=cities, all_events=all_events)


@app.route('/')
def root():
    session["loggedin"] = False

    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # no message by default
    msg = None
    user = None

    # if user input something...
    if request.method == 'POST':
        user = get_user(request.form["username"])
        if not user:
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
        if get_user(new_user["username"]):
            msg = "Username is already taken"
        else:
            insert_user(new_user["username"], new_user["birthday"], new_user["city"], new_user["bio"])
            return redirect(url_for("login"))

    return render_template("create_account.html", msg=msg, user=new_user)


@app.route("/review", methods=['GET', 'POST'])
def review():
    if request.method == 'POST' and session["loggedin"]:
        review = request.form
        insert_review(session["username"], review["score"], review["event"], review["text"])

        reviews=get_reviews(review["event"])
        return render_template("list_reviews.html", event_name=review["event"], reviews=reviews)
    
    return render_template("review.html")


@app.route('/search_reviews')
def search_reviews():
    return render_template("search_reviews.html")


@app.route('/review_search', methods=['POST'])
def do_review_search():
    event_name = request.form["event"]
    reviews = get_reviews(event_name)
    return render_template("list_reviews.html", event_name=event_name, reviews=reviews)


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
    events = get_events(query, session["username"] if session["loggedin"] else None)
    return render_template('list_events.html', query=query, events=events)


if __name__ == '__main__':
    app.run(debug=True)
