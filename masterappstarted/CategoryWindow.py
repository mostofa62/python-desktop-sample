# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CategoryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoyWindow(object):
    def setupUi(self, CategoyWindow):
        CategoyWindow.setObjectName("CategoyWindow")
        CategoyWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CategoyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CatTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.CatTableWidget.setGeometry(QtCore.QRect(40, 40, 441, 441))
        self.CatTableWidget.setObjectName("CatTableWidget")
        self.CatTableWidget.setColumnCount(0)
        self.CatTableWidget.setRowCount(0)
        CategoyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CategoyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        CategoyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CategoyWindow)
        self.statusbar.setObjectName("statusbar")
        CategoyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CategoyWindow)
        QtCore.QMetaObject.connectSlotsByName(CategoyWindow)

    def retranslateUi(self, CategoyWindow):
        _translate = QtCore.QCoreApplication.translate
        CategoyWindow.setWindowTitle(_translate("CategoyWindow", "Categories"))


