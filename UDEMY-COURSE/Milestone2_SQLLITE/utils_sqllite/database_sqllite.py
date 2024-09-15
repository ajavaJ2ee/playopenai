import json
import sqlite3

from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection() as connection:
        cursor=connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')



def add_book(name,author):
    with DatabaseConnection() as connection:
        cursor=connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (name,author))
        print(f'Books with {name} is added')

def get_all_books():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name':row[0],'author':row[1],'read':row[2]}  for row in cursor.fetchall()]
        return books


def mark_book_as_read(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1  WHERE name=?',(name,))



def delete_book(name):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books  WHERE name=?', (name,))



