import sqlite3


class DatabaseConnection:
    def __init__(self):
        self.connection=None

    def __enter__(self):
        self.connection=sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
