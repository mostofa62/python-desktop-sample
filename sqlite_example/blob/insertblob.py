import sqlite3
import os.path


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

def insert_picture(conn, picture_file):
 with open(picture_file, 'rb') as input_file:
  ablob = input_file.read()
  base=os.path.basename(picture_file)
  afile, ext = os.path.splitext(base)
  sql = '''INSERT INTO PICTURES
  (PICTURE, TYPE, FILE_NAME)
  VALUES(?, ?, ?);'''
  conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
  conn.commit()

	
#conn = create_or_open_db('picdb.sqlite')
conn = create_or_open_db('picdb')
picture_file = "./pictures/Chrysanthemum.jpg"
insert_picture(conn, picture_file)
conn.close()