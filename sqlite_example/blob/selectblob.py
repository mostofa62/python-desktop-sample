import sqlite3
import os.path
from IPython.core.display import Image

def create_or_open_db(db_file):
 db_is_new = not os.path.exists(db_file)
 conn = sqlite3.connect(db_file)
 if db_is_new:
  print('Creating schema')
  sql = '''create table if not exists PICTURES(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   PICTURE BLOB,
   TYPE TEXT,
   FILE_NAME TEXT);'''
  conn.execute(sql) # shortcut for conn.cursor().execute(sql)
 else:
  print('Schema exists\n')
 return conn

def extract_picture(cursor, picture_id):
 sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
 param = {'id': picture_id}
 cursor.execute(sql, param)
 ablob, ext, afile = cursor.fetchone()
 filename = afile + ext
 with open(filename, 'wb') as output_file:
  output_file.write(ablob)
 return filename

conn = create_or_open_db('picdb')
cur = conn.cursor()
filename = extract_picture(cur, 1)
cur.close()
conn.close()
Image(filename='./'+filename)