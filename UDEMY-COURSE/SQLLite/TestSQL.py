import sqlite3

connection= sqlite3.connect('data.db')
cursor=connection.cursor()
cursor.execute('')
connection.commit()
connection.close()


