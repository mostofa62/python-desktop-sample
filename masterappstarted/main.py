import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem, QMessageBox
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
  try:
   sql = '''INSERT INTO Categories
   (NAME, DESC)
   VALUES(?, ?);'''
   conn.execute(sql,[catname, catdesc]) 
   conn.commit()
   QMessageBox.information(QMessageBox(),'Successful','Category is added successfully to the database.')
   self.close()
  except Exception:
   QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')


class CategoryListWindow(QMainWindow):
 def __init__(self):
  super().__init__()
  self.ui = Ui_CategoyWindow()  
  self.ui.setupUi(self)
  #load data to table widget
  sql='''SELECT *FROM Categories'''
  result = conn.execute(sql)
  #setting to tablewidget
  self.ui.CatTableWidget.setRowCount(0)
  self.ui.CatTableWidget.setColumnCount(3)
  self.ui.CatTableWidget.setHorizontalHeaderLabels(("Id.", "Name", "Descriptiom"))
  #end setting to tablewidget
  for row_number, row_data in enumerate(result):
   self.ui.CatTableWidget.insertRow(row_number)
   for column_number, data in enumerate(row_data):
    self.ui.CatTableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
  #end load data to table widget
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
 
