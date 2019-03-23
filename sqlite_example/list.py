import sqlite3 #Import the SQLite3 module

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('test')
db.row_factory = sqlite3.Row
# Get a cursor object
cursor = db.cursor()
cursor.execute('''SELECT name, email, phone FROM users''')
for row in cursor:
 # row['name'] returns the name column in the query, row['email'] returns email column.
 print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))

# Close the db connection
db.close()