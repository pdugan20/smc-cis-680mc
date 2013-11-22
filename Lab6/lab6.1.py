#!/usr/local/bin/python3
# Patrick DUgan
# lab6.1.py  database functions
# Aug 1, 2011

print('Content-type:text/html\n')

import sqlite3
connection = sqlite3.connect('databasefile.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('CREATE TABLE users (id integer primary key, first_name string, last_name string, color string)')
cursor.execute('INSERT INTO users values(null, ?, ?, ?)', ('joe','smith', 'red'))
cursor.execute('INSERT INTO users values(null, ?, ?, ?)', ('mary','jones', 'green'))
cursor.execute('INSERT INTO users values(null, ?, ?, ?)', ('tom', 'brown', 'blue'))
connection.commit()

all = cursor.execute('SELECT * FROM users')
print('<html><p><b>Database Info :</b><br>')
for row in all:
    print('<br>' + str(row))
print('</html>')

connection.close()

