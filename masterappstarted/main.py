import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem, QMessageBox, QVBoxLayout, QHBoxLayout
from MainWindow import Ui_MainWindow
from CategoryNew import Ui_CategoryNewOrUpdate
from CategoryWindow import Ui_CategoyWindow
from Mostofa.LinkLabel import LinkLabel
# web view
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView

# db related
import sqlite3
import os.path

from PyQt5.QtCore import pyqtSlot

# database

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
  conn.execute(sql)  # shortcut for conn.cursor().execute(sql)
  sql = '''create table if not exists Posts(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   NAME VARCHAR NOT NULL,
   DESC TEXT,
   CategoryId INTEGER NOT NULL,
   FOREIGN KEY(CategoryId) REFERENCES Categories(ID)
   );'''
  conn.execute(sql)
 else:
  print('Schema exists\n')
 return conn

# end database


class CategoryNewWindow(QWidget):

 def __init__(self):
  super().__init__()
  self.ui = Ui_CategoryNewOrUpdate()
  self.ui.setupUi(self)
  self.show()
 
 def make_connection(self, labelObject):
  labelObject.changedValue.connect(self.setCatName)
 @pyqtSlot(int)
 def setCatName(self, val):
  self.ui.catName.setText(str(val))
 def saveOrUpdateCat(self):
  catname = self.ui.catName.text()
  catdesc = self.ui.catDesc.text()
  print(catdesc)
  print(catname)
  try:
   sql = '''INSERT INTO Categories
   (NAME, DESC)
   VALUES(?, ?);'''
   conn.execute(sql, [catname, catdesc])
   conn.commit()
   QMessageBox.information(QMessageBox(), 'Successful',
                           'Category is added successfully to the database.')
   self.close()
  except Exception:
   QMessageBox.warning(QMessageBox(), 'Error',
                       'Could not add student to the database.')


class CategoryListWindow(QMainWindow):

 def __init__(self):
  super().__init__()
  self.ui = Ui_CategoyWindow()
  self.ui.setupUi(self)
  # load data to table widget
  sql = '''SELECT *FROM Categories'''
  result = conn.execute(sql)
  # setting to tablewidget
  self.ui.CatTableWidget.setRowCount(0)
  self.ui.CatTableWidget.setColumnCount(3)
  self.ui.CatTableWidget.setHorizontalHeaderLabels(
      ("Id.", "Name", "Descriptiom"))
  # end setting to tablewidget
  for row_number, row_data in enumerate(result):
   self.ui.CatTableWidget.insertRow(row_number)
   for column_number, data in enumerate(row_data):
    self.ui.CatTableWidget.setItem(
        row_number, column_number, QTableWidgetItem(str(data)))
  # end load data to table widget
  self.show()


class AppWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        centralWidget = QWidget()
        #centralWidget.resize(200,300)			
        layout = QVBoxLayout()		
        hbox = QHBoxLayout()
        hbox.addLayout(layout)
        #hbox.addStretch(1)
        anotherwidget = CategoryNewWindow()
        hbox.addWidget(anotherwidget)
        centralWidget.setLayout(hbox)
        self.setCentralWidget(centralWidget)
        sql = 'SELECT *FROM Categories LIMIT 0,2'
        result = conn.execute(sql)
        i=20;
        for row in result:
         l = LinkLabel()
         l.linkId=row[0]
         l.setText(row[1])
         l.setGeometry(QtCore.QRect(150, i, 200, 20))
         anotherwidget.make_connection(l)
         i=i+20
         layout.addWidget(l)
		
        self.show()
    def showNewCategory(self,conn):
     # self.hide()
     self.catNew = 	CategoryNewWindow()
     self.catNew.show()
    def showListCategory(self):
     self.catList = CategoryListWindow()
     self.catList.show()
 
app = QApplication(sys.argv)
conn = create_or_open_db('db')
w = AppWindow()
sys.exit(app.exec_())
 
