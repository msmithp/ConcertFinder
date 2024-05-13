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
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT username \
                        FROM account \
                        WHERE username = %s", (username))
        result = cursor.fetchone()
        return result


def get_events(search_query, username):
    # get events from the database based on `search_query`
    conn = open_connection()
    with conn.cursor() as cursor:
        if username:  # if user is logged in, get distance
            cursor.execute("SELECT e.event_name, e.date_time, e.event_desc, e.venue_name, COALESCE(AVG(r.score), 0) as score, \
                                haversine(user_city.latitude, user_city.longitude, venue_city.latitude, venue_city.longitude) as distance \
                            FROM venue v, city venue_city, account a, city user_city, event e LEFT JOIN review r ON e.event_name = r.event_name \
                            WHERE  e.venue_name = v.venue_name \
                                AND v.city_name = venue_city.city_name \
                                AND a.city_name = user_city.city_name \
                                AND a.username = %s \
                                AND e.event_name like CONCAT('%%', %s, '%%') \
                            GROUP BY e.event_name, distance \
                            ORDER BY e.date_time;", (username, search_query))
        else:  # if user is not logged in, don't get distance
            cursor.execute("SELECT e.event_name, e.date_time, e.event_desc, e.venue_name, COALESCE(AVG(r.score), 0) as score \
                    FROM event e LEFT JOIN review r on e.event_name = r.event_name WHERE \
                    e.event_name like CONCAT('%%', %s, '%%') \
                    GROUP BY e.event_name;", (search_query))

        result = cursor.fetchall()
        return result


def get_cities():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * from city")
        result = cursor.fetchall()
        return result


def get_all_events():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT event_name FROM event")
        result = cursor.fetchall()
        return result


def get_upcoming_events():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT e.event_name, e.date_time, e.event_desc, e.venue_name \
                        FROM event e \
                        WHERE e.date_time > NOW() \
                        ORDER BY e.date_time;")
        result = cursor.fetchmany(3)
        return result


def get_tickets(username):
    # Get the tickets owned by the user
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT e.event_name, e.event_desc, t.purchase_date, t.price \
                        FROM event e, ticket t, account a \
                        WHERE a.username = t.username AND t.event_name = e.event_name AND a.username = %s \
                        GROUP BY t.purchase_id \
                        ORDER BY t.purchase_date desc;", (username))
        result = cursor.fetchall()
        return result


def insert_user(username, birthday, city, bio):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO account (username, acc_birth_date, join_date, acc_bio, city_name) \
                        VALUES (%s, %s, CURRENT_DATE(), %s, %s);", (username, birthday, bio, city))
        conn.commit()
        conn.close()


def insert_review(username, score, event, text):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO review (score, review_date, review_text, event_name, username) \
                        VALUES (%s, CURRENT_DATE(), %s, %s, %s)", (score, text, event, username))
        conn.commit()
        conn.close()


def get_reviews(event_name):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT r.username, r.score, r.event_name, r.review_text, r.review_date \
                        FROM review r \
                        WHERE r.event_name = %s", (event_name))
        result = cursor.fetchall()
        return result
