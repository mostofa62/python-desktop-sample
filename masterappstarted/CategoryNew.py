# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CategoryNew.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoryNewOrUpdate(object):    

    def setupUi(self, CategoryNewOrUpdate):
        CategoryNewOrUpdate.setObjectName("CategoryNewOrUpdate")
        CategoryNewOrUpdate.resize(400, 300)
        self.catName = QtWidgets.QLineEdit(CategoryNewOrUpdate)
        self.catName.setGeometry(QtCore.QRect(90, 40, 201, 20))
        self.catName.setObjectName("catName")
        self.saveOrUpdateCat = QtWidgets.QPushButton(CategoryNewOrUpdate)
        self.saveOrUpdateCat.setGeometry(QtCore.QRect(150, 130, 56, 17))
        self.saveOrUpdateCat.setObjectName("saveOrUpdateCat")
        self.catDesc = QtWidgets.QLineEdit(CategoryNewOrUpdate)
        self.catDesc.setGeometry(QtCore.QRect(90, 80, 201, 20))
        self.catDesc.setObjectName("catDesc")
		
		#save Data
        self.saveOrUpdateCat.clicked.connect(CategoryNewOrUpdate.saveOrUpdateCat)

        self.retranslateUi(CategoryNewOrUpdate)
        QtCore.QMetaObject.connectSlotsByName(CategoryNewOrUpdate)

    def retranslateUi(self, CategoryNewOrUpdate):
        _translate = QtCore.QCoreApplication.translate
        CategoryNewOrUpdate.setWindowTitle(_translate("CategoryNewOrUpdate", "Category"))
        self.catName.setPlaceholderText(_translate("CategoryNewOrUpdate", "Provide Category Name"))
        self.saveOrUpdateCat.setText(_translate("CategoryNewOrUpdate", "Save"))
        self.catDesc.setPlaceholderText(_translate("CategoryNewOrUpdate", "Provide Category Description"))


