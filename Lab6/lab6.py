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

------------------------------------------------------------------------
Visible Divider
------------------------------------------------------------------------

#!/usr/local/bin/python3
# Patrick DUgan
# lab6.2.py  database functions
# Aug 1, 2011

import sqlite3
import cgitb
import cgi

def form_input():
  print('<html>')
  print('<form action="" method="post" accept-charset="utf-8">')
  print('<p>')
  print('<label for="first_name">First name</label><br>')
  print('<input type="text" name="first_name" value="" id="first_name">')
  print('</p>')
  print('<p>')
  print('<label for="last_name">Last name</label><br>')
  print('<input type="text" name="last_name" value="" id="last_name">')
  print('</p>')
  print('<p>')
  print('<label for="color">Favorite color</label><br>')
  print('<input type="text" name="color" value="" id="color">')
  print('</p>')
  print('<p>')
  print('<input type="submit" name="submit" value="Fave it!">')
  print('</p>')
  print('</form>')
  print('</html>')

try:
  print('Content-type:text/html\n')
  form_input()

  form = cgi.FieldStorage()
  errors = []

  if form.has_key('first_name') and form["first_name"].value.strip != '':
    first_name = form["first_name"].value
  else:
    errors.append('First name missing')

  if form.has_key('last_name') and form["last_name"].value.strip != '':
    last_name = form["last_name"].value
  else:
    errors.append('Last name missing')

  if form.has_key('color') and form["color"].value.strip != '':
    color = form["color"].value
  else:
    errors.append('Last name missing')
  if errors:
    print("<ul><li>", "</li><li>".join(errors), "</li></ul>")
  else:
    '''Since there are no errors we can insert the data into the db.'''
    cursor.execute('INSERT INTO users values(null, ?, ?, ?)',(first_name, last_name, color))
    cursor.commit()

  # connection = sqlite3.connect('databasefile.db')
  # cursor = connection.cursor()
  # cursor.execute('DROP TABLE IF EXISTS users')
  # cursor.execute('CREATE TABLE users (id integer primary key, first_name string, last_name string)')
  # cursor.execute('INSERT INTO users values(null, ?, ?)', ('first','last'))
  # all = cursor.execute('SELECT * FROM users')
  # for row in all:
    # print(row)

except Exception as e:
    print('Content-type:text/html\n')
    print(e)

------------------------------------------------------------------------
Visible Divider
------------------------------------------------------------------------

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


