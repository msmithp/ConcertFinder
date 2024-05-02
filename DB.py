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
    pass


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
