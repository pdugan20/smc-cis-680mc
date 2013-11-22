#!/usr/local/bin/python3
# Patrick DUgan
# lab6.3.py  database functions
# Aug 1, 2011

print('Content-type:text/html\n')

import sqlite3
connection = sqlite3.connect('databasefile.db')
cursor = connection.cursor()

all = cursor.execute('SELECT * FROM users')
print('<html><p><b>Database Info :</b><br>')
for row in all:
    print('<br>' + str(row))
print('</html>')
