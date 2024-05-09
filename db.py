import os
import pymysql

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get_user(username):
    # do something with `username` in the database
    # if username is not registered in the database, return None
    return {"username": username}


def get_events(query):
    # get events from the database based on `query`
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT e.event_name, e.date_time, e.event_desc, e.venue_name, COALESCE(AVG(r.score), 0) as score FROM event e LEFT JOIN review r on e.event_name = r.event_name WHERE e.event_name like '%{query}%' GROUP BY e.event_name;")
        result = cursor.fetchall()
        return result


def get_artists(query):
    pass


def get_cities():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * from city")
        result = cursor.fetchall()
        return result


def get_upcoming_events():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT e.event_name, e.date_time, e.event_desc, e.venue_name FROM event e WHERE e.date_time > NOW() ORDER BY e.date_time;")
        result = cursor.fetchmany(3)
        return result


def get_tickets(username):
    # Get the tickets owned by the user
    return [{"price": 10000.0, "purchase_date": "2024-04-30",
             "username": "bryced", "event_name": "Eras Tour: Reefville", "event_desc": "Taylor Swift in her hometown!"}]


def insert_user(user):
    # Logic here to insert a new user into the database
    pass


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
