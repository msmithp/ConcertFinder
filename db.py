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
        cursor.execute(f"SELECT username \
                        FROM account \
                        WHERE username = '{username}'")
        result = cursor.fetchone()
        return result


def get_events(search_query, username):
    # get events from the database based on `search_query`
    query = ""
    if username:  # if logged in, get distances
        query = f"SELECT e.event_name, e.date_time, e.event_desc, e.venue_name, COALESCE(AVG(r.score), 0) as score, \
                    haversine(user_city.latitude, user_city.longitude, venue_city.latitude, venue_city.longitude) as distance \
                FROM venue v, city venue_city, account a, city user_city, event e LEFT JOIN review r ON e.event_name = r.event_name \
                WHERE  e.venue_name = v.venue_name \
                    AND v.city_name = venue_city.city_name \
                    AND a.city_name = user_city.city_name \
                    AND a.username = '{username}' \
                    AND e.event_name like '%{search_query}%' \
                GROUP BY e.event_name, distance \
                ORDER BY e.date_time;"
    else:  # if not logged in, don't get distances
        query = f"SELECT e.event_name, e.date_time, e.event_desc, e.venue_name, COALESCE(AVG(r.score), 0) as score \
                    FROM event e LEFT JOIN review r on e.event_name = r.event_name WHERE \
                    e.event_name like '%{search_query}%' \
                    GROUP BY e.event_name;"

    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
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
        cursor.execute(f"SELECT e.event_name, e.event_desc, t.purchase_date, t.price \
                        FROM event e, ticket t, account a \
                        WHERE a.username = t.username AND t.event_name = e.event_name AND a.username = '{username}' \
                        GROUP BY t.purchase_id \
                        ORDER BY t.purchase_date desc;")
        result = cursor.fetchall()
        return result


def insert_user(username, birthday, city, bio):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO account (username, acc_birth_date, join_date, acc_bio, city_name) \
                        VALUES ('{username}', '{birthday}', CURRENT_DATE(), '{bio}', '{city}');")
        conn.commit()
        conn.close()
