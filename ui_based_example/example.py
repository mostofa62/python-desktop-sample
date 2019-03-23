# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        MyDialog.setObjectName("MyDialog")
        MyDialog.resize(400, 300)
        self.saveButton = QtWidgets.QPushButton(MyDialog)
        self.saveButton.setGeometry(QtCore.QRect(140, 120, 111, 23))
        self.saveButton.setObjectName("saveButton")
        self.name = QtWidgets.QLineEdit(MyDialog)
        self.name.setGeometry(QtCore.QRect(70, 70, 241, 20))
        self.name.setAutoFillBackground(False)
        self.name.setInputMask("")
        self.name.setMaxLength(100)
        self.name.setObjectName("name")
        self.saveButton.clicked.connect(self.save_button_click)
        self.retranslateUi(MyDialog)
        QtCore.QMetaObject.connectSlotsByName(MyDialog)
		
    def save_button_click(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        name = self.name.value()
        msg.setText(name)
        

    def retranslateUi(self, MyDialog):
        _translate = QtCore.QCoreApplication.translate
        MyDialog.setWindowTitle(_translate("MyDialog", "Your Name Saver"))
        self.saveButton.setText(_translate("MyDialog", "Save Your  Name"))
        self.name.setPlaceholderText(_translate("MyDialog", "Provide your name"))

