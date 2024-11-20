import logging
from datetime import datetime
from threading import Timer


# from some library
class SSLConnection:
    def __init__(self):
        self.connections = []

    def connect(self, host, port, user, password):
        self.connections.append({
            "host": host,
            "port": port,
            "user_name": user,
            "pass": password,
        })
        print(f"Establish connection to {host}:{port}")
        return self

    def disconnect(self, user):
        for conn in self.connections:
            if conn["user_name"] == user:
                del conn
                print("Connection ended")
                return

    def execute(self, command):
        print(f"Execute {command}")
        return 0


# our code
class SSLContextManager:
    def __init__(self, host, port, user, password):
        self.connection = SSLConnection()
        self.conn_data = (host, port, user, password)

    def __enter__(self):
        conn = self.connection.connect(*self.conn_data)
        logging.warning(f"Create connection to {self.conn_data} at {datetime.now()}")
        return conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        error_message = "Exit from ContextManager"
        if exc_type == TimeoutError:
            error_message = f"Connection time expired 30s ({exc_val})"

        elif exc_type == ValueError:
            error_message = exc_val

        elif exc_type is not None:
            error_message = f"{exc_type}: {exc_val}"



        logging.warning(f"End connection with {self.conn_data} at {datetime.now()} Reason: {error_message}")
        self.connection.disconnect(self.conn_data[2])


with SSLContextManager("127.0.0.1", 5000, "admin", "pass1234") as connection:
    result = connection.execute("pwd")
    print()
    x = 10
    y = x / result

# connection = SSLConnection().connect("127.0.0.1", 5000, "admin", "pass1234")
#
#
# result = connection.execute("pwd")
# print()
# x = 10
# y = x / result
#
# connection.disconnect("admin")