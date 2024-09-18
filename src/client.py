from multiprocessing import connection, Process

with connection.Client("127.0.0.1:6006") as conn:
    while True:
        print(conn.recv())