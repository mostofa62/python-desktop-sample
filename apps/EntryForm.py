# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EntryForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1024, 800)
        font = QtGui.QFont()
        font.setUnderline(False)
        Main.setFont(font)
        Main.setAutoFillBackground(False)
        self.entryForm = QtWidgets.QWidget(Main)
        self.entryForm.setGeometry(QtCore.QRect(150, 140, 781, 441))
        self.entryForm.setObjectName("entryForm")
        self.titleLabel = QtWidgets.QLabel(self.entryForm)
        self.titleLabel.setGeometry(QtCore.QRect(210, 60, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.title = QtWidgets.QLineEdit(self.entryForm)
        self.title.setGeometry(QtCore.QRect(210, 90, 401, 20))
        self.title.setObjectName("title")
        self.description = QtWidgets.QTextEdit(self.entryForm)
        self.description.setGeometry(QtCore.QRect(210, 190, 401, 91))
        self.description.setObjectName("description")
        self.descriptionLabel = QtWidgets.QLabel(self.entryForm)
        self.descriptionLabel.setGeometry(QtCore.QRect(210, 160, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.saveButton = QtWidgets.QPushButton(self.entryForm)
        self.saveButton.setGeometry(QtCore.QRect(510, 320, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Entry Form"))
        self.titleLabel.setText(_translate("Main", "Title"))
        self.descriptionLabel.setText(_translate("Main", "Description"))
        self.saveButton.setText(_translate("Main", "Save"))
		

 


