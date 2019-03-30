# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from CategoryWindow import Ui_CategoyWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 18))
        self.menubar.setObjectName("menubar")
        self.menuCategories = QtWidgets.QMenu(self.menubar)
        self.menuCategories.setObjectName("menuCategories")
        self.menuPosts = QtWidgets.QMenu(self.menubar)
        self.menuPosts.setObjectName("menuPosts")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.catList = QtWidgets.QAction(MainWindow)
        self.catList.setObjectName("catList")
        self.catNew = QtWidgets.QAction(MainWindow)
        self.catNew.setObjectName("catNew")
        self.postList = QtWidgets.QAction(MainWindow)
        self.postList.setObjectName("postList")
        self.postNew = QtWidgets.QAction(MainWindow)
        self.postNew.setObjectName("postNew")
        self.menuCategories.addAction(self.catList)
        self.menuCategories.addAction(self.catNew)
        self.menuPosts.addAction(self.postList)
        self.menuPosts.addAction(self.postNew)
        self.menubar.addAction(self.menuCategories.menuAction())
        self.menubar.addAction(self.menuPosts.menuAction())
        #call new category menu actions
        self.catNew.triggered.connect(MainWindow.showNewCategory)
        self.catList.triggered.connect(MainWindow.showListCategory)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HomeWindow"))
        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))
        self.menuPosts.setTitle(_translate("MainWindow", "Posts"))
        self.catList.setText(_translate("MainWindow", "List"))
        self.catNew.setText(_translate("MainWindow", "New"))
        self.postList.setText(_translate("MainWindow", "List"))
        self.postNew.setText(_translate("MainWindow", "New"))    
	

