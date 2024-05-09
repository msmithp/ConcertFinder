# import os
# import pymysql
# from flask import jsonify

# db_user = os.environ.get('CLOUD_SQL_USERNAME')
# db_password = os.environ.get('CLOUD_SQL_PASSWORD')
# db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
# db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def get_user(username):
    # do something with `username` in the database
    # if username is not registered in the database, return None
    return {"username": username}


def get_events(query):
    # get events from the database based on `query`
    return [{"event_name": "The Day of Reckoning", "date_time": "2024-12-22 19:00:00",
             "event_desc": "Beethoven reanimates at the 9:30 Club", "venue_name": "The 9:30 Club"},
            {"event_name": "District of Columbiachella", "date_time": "2024-04-12 10:00:00",
             "event_desc": "It’s like Coachella but even worse somehow", "venue_name": "The 9:30 Club"},
            {"event_name": "All-American Closed Mic", "date_time": "2024-11-05 12:00:00",
             "event_desc": "This replaced the election, no one was voting anyways", "venue_name": "The White House"},
            {"event_name": "Eras Tour: Reefville", "date_time": "2024-06-19 18:00:00",
             "event_desc": "Taylor Swift in her hometown!", "venue_name": "The Ocean"}]


def get_artists(query):
    pass


def get_cities():
    return ({"city_name": "Frederick", "country": "United States of America", "latitude": 39.4143, "longitude": 77.4105},
            {"city_name": "Reefville", "country": "United States of America", "latitude": -48.8766, "longitude": -123.3933})


def get_upcoming_events():
    # This should return the 3 events with the soonest date_time attribute
    return [{"event_name": "The Day of Reckoning", "date_time": "2024-12-22 19:00:00",
             "event_desc": "Beethoven reanimates at the 9:30 Club", "venue_name": "The 9:30 Club"},
            {"event_name": "District of Columbiachella", "date_time": "2024-04-12 10:00:00",
             "event_desc": "It’s like Coachella but even worse somehow", "venue_name": "The 9:30 Club"},
            {"event_name": "All-American Closed Mic", "date_time": "2024-11-05 12:00:00",
             "event_desc": "This replaced the election, no one was voting anyways", "venue_name": "The White House"}]


def get_tickets(username):
    # Get the tickets owned by the user
    return [{"price": 10000.0, "purchase_date": "2024-04-30",
             "username": "bryced", "event_name": "Eras Tour: Reefville", "event_desc": "Taylor Swift in her hometown!"}]


def insert_user(user):
    # Logic here to insert a new user into the database
    pass


# def open_connection():
#     unix_socket = '/cloudsql/{}'.format(db_connection_name)
#     try:
#         if os.environ.get('GAE_ENV') == 'standard':
#             conn = pymysql.connect(user=db_user,
#                                    password=db_password,
#                                    unix_socket=unix_socket,
#                                    db=db_name,
#                                    cursorclass=pymysql.cursors.DictCursor
#                                    )
#     except pymysql.MySQLError as e:
#         return e
#     return conn

# def get_customers():
#     conn = open_connection()
#     with conn.cursor() as cursor:
#         cursor.execute("select * from customers;")
#         result = cursor.fetchall()
#         return result

# def create(name, street, city):
#     conn = open_connection()
#     with conn.cursor() as cursor:
#         cursor.execute('INSERT INTO customer (customer_name, customer_street, customer_city) VALUES(%s, %s, %s)',
#                        (name, street, city))
#     conn.commit()
#     conn.close()
