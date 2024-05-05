# db.py model
import os
# import pymysql
# from flask import jsonify

# db_user = os.environ.get('CLOUD_SQL_USERNAME')
# db_password = os.environ.get('CLOUD_SQL_PASSWORD')
# db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
# db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def get_user(username):
    # do something with `dummy` in the database
    # if username is not registered in the database, return None
    return {"username": username}


def get_events(query):
    # return [("The Day of Reckoning", "2024-12-22 19:00:00", "Beethoven reanimates at the 9:30 Club", "The 9:30 Club"),
    #         ("District of Columbiachella", "2024-4-12 10:00:00", "It’s like Coachella but even worse somehow", "The 9:30 Club"),
    #         ("All-American Closed Mic", "2024-11-05 12:00:00", "This replaced the election, no one was voting anyways", "The White House"),
    #         ("Eras Tour: Reefville", "2024-06-19 18:00:00", "Taylor Swift in her hometown!", "The Ocean"),
    #         ("Eras Tour: Reefville", "2024-06-19 18:00:00", "Taylor Swift in her hometown!", "The Ocean")]

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
