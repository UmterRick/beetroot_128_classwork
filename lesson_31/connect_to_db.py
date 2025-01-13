# import sqlite3
# pip install psycopg2
# pip install psycopg2-binary
import os
import psycopg2



if __name__ == "__main__":
    # WITH PARAMS
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port="5432",
        user="postgres",
        password="postgres",
        database="postgres"
    )

    # WITH URL
    # URL = postgresql://user:password@host:port/db_name
    connection_2 = psycopg2.connect(os.getenv("DB_URL"))

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM public.users")
    print(cursor.fetchall())
