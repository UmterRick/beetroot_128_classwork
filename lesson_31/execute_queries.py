import psycopg2

conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM contacts WHERE id=13")
    result = cursor.fetchone()

name = "Vlad"
phone = 66811651
city = "Kharkiv"
with conn.cursor() as cursor:
    cursor.execute(
        query=f"INSERT INTO contacts (name, phone_number, city) VALUES (%(c_name)s, %(c_phone)s, %(c_city)s)",
        vars={"c_name": name, "c_phone": phone, "c_city": city}
    )

    conn.commit()
# print(result)
# for record in result:
#     print(record)
