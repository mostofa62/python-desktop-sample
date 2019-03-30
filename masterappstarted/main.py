import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from MainWindow import Ui_MainWindow
from CategoryNew import Ui_CategoryNewOrUpdate
from CategoryWindow import Ui_CategoyWindow

#db related
import sqlite3
import os.path


#database

def create_or_open_db(db_file):
 db_is_new = not os.path.exists(db_file)
 conn = sqlite3.connect(db_file)
 if db_is_new:
  print('Creating schema')
  sql = '''create table if not exists Categories(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME VARCHAR NOT NULL,
   DESC TEXT
   );'''
  conn.execute(sql) # shortcut for conn.cursor().execute(sql)
  sql = '''create table if not exists Posts(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME VARCHAR NOT NULL,
   DESC TEXT,
   CategoryId INTEGER NOT NULL,
   FOREIGN KEY(CategoryId) REFERENCES Categories(ID)
   );'''
 else:
  print('Schema exists\n')
 return conn

#end database

class CategoryNewWindow(QWidget):
 def __init__(self):
  super().__init__()
  self.ui = Ui_CategoryNewOrUpdate()
  self.ui.setupUi(self)
  self.show()
 def saveOrUpdateCat(self):
  catname = self.ui.catName.text()
  catdesc = self.ui.catDesc.text()
  print(catdesc)
  print(catname)
  sql = '''INSERT INTO Categories
  (NAME, DESC)
  VALUES(?, ?);'''
  conn.execute(sql,[catname, catdesc]) 
  conn.commit()


class CategoryListWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.ui = Ui_CategoyWindow()
  self.ui.setupUi(self)
  self.show()  

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    def showNewCategory(self,conn):
     #self.hide()
     self.catNew = 	CategoryNewWindow()
     self.catNew.show()
    def showListCategory(self):
     self.catList = CategoryListWindow()
     self.catList.show()
 
app = QApplication(sys.argv)
conn = create_or_open_db('db')
w = AppWindow()
sys.exit(app.exec_())
 