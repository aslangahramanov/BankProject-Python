# DATABASE SETTINGS


import psycopg2


connection = psycopg2.connect(
        dbname="bank_db",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )



