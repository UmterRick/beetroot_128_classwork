from datetime import datetime

import psycopg2

conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")

tables = {
    "authors": """
    CREATE TABLE IF NOT EXISTS public.authors (
    id SERIAL,
    name varchar(200),
    biography TEXT,
    birth_date timestamp,
    PRIMARY KEY (id)
    )
    """,
    "books": """
    CREATE TABLE IF NOT EXISTS public.books (
    id SERIAL,
    title varchar(200),
    pages int,
    author_id int,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES public.authors(id) ON DELETE CASCADE

    )
    """,
}

authors = [
    {
        "name": "Author_1",
        "biography": "asfndasdm984512asjfs caa",
        "birth_date": datetime(1937, 1,  20)
    },
    {
        "name": "Author_2",
        "biography": "asfndasdmascxscvsasjfs caa",
        "birth_date": datetime(1887, 1, 23)
    },
    {
        "name": "Author_3",
        "biography": "asfndasdmasjfdssdgegwr32542s caa",
        "birth_date": datetime(2007, 1, 1)
    },
    {
        "name": "Author_4",
        "biography": "asfndasdmasjfs caadafasfasas",
        "birth_date": datetime(1987, 1, 30)
    },
]

books = [
    ("Book_1", 100, 1),
    ("Book_2", 34, 1),
    ("Book_3", 100, 1),
    ("Book_4", 1, 2),
    ("Book_5", 100, 2),
    ("Book_6", 123, 2),
    ("Book_7", 100, 2),
    ("Book_8", 100, 2),
    ("Book_9", 100, 3),
    ("Book_10", 100, 3),
    ("Book_11", 100, 4),
    ("Book_12", 1200, 3),
    ("Book_13", 100, 2),
    ("Book_14", 100, 1),
    ("Book_15", 34, 1),
]

def create_tables():
    try:
        with conn.cursor() as cursor:
            for table_name, query in tables.items():
                cursor.execute(query)
                print(f"Create table '{table_name}'")
            conn.commit()
    except psycopg2.errors.Error:
        conn.rollback()




def create_authors():
    with conn.cursor() as cursor:
        cursor.executemany("INSERT INTO authors (name, biography, birth_date) VALUES (%(name)s, %(biography)s, %(birth_date)s)",
                           vars_list=authors)

    conn.commit()

def create_books():
    try:
        with conn.cursor() as cursor:
            cursor.executemany("INSERT INTO books (title, pages, author_id) VALUES (%s, %s, %s)",
                               vars_list=books)
        conn.commit()
    except psycopg2.errors.Error as exc:
        conn.rollback()
        raise exc



create_books()




