import sqlite3 #Import the SQLite3 module
try:
 #db = sqlite3.connect(':memory:')
 # Creates or opens a file called mydb with a SQLite3 DB
 db = sqlite3.connect('test')
 db.row_factory = sqlite3.Row
 # Get a cursor object
 cursor = db.cursor()
 # Check if table users does not exist and create it
 cursor.execute('''CREATE TABLE IF NOT EXISTS
				  users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
 # Commit the change
 db.commit()
 name1 = 'Andres'
 phone1 = '3366858'
 email1 = 'user@example.com'
 # A very secure password
 password1 = '12345'

 name2 = 'John'
 phone2 = '5557241'
 email2 = 'johndoe@example.com'
 password2 = 'abcdef'

 # Insert user 1
 cursor.execute('''INSERT INTO users(name, phone, email, password)
			  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
 print('First user inserted')
 
 # Insert user 2
 cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
 print('Second user inserted')
 
 db.commit()
 cursor.execute('''SELECT name, email, phone FROM users''')
 for row in cursor:
 # row['name'] returns the name column in the query, row['email'] returns email column.
  print('{0} : {1}, {2}'.format(row['name'], row['email'], row['phone']))
 # Catch the exception
except Exception as e:
 # Roll back any change if something goes wrong
 db.rollback()
 raise e
finally:
 # Close the db connection
 db.close()