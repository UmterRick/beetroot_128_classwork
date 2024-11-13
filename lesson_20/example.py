import requests


def add(a, b):
    return int(a) + int(b)


def divide(a, b):
    return a / b



def get_page_html(url):
    response = requests.get(url=url)
    print(f"Make request to URL={url}", response.status_code)
    return response.status_code # 200



def get_order_from_db_by_id(order_id):
    conn = "create_conn_with_db"
    order = db_request(conn, "orders", order_id)

    return order[1]

# code from library
def db_request(conn, table, obj_id):
    print("Go to database to get order", obj_id)
    ...
    ...
    return (obj_id, "Order 1", "My order", "2024-11-13")



def get_contact_name():
    name = input("Name:")

    return name

