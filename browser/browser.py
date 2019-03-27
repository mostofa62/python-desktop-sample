# coding: utf-8

import sys
import os
# import site
# site.addsitedir('/usr/local/lib/python2.7/site-packages')
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import * 

app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()
#view.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
#view.page().fullScreenRequested.connect(QWebEngineFullScreenRequest.accept)
# view.settings().setAttribute(QtWebEng.QWebSettings.LocalContentCanAccessRemoteUrls, True)

# f = open('html/test.html', 'r')
#
# html = f.read()
# f.close()

# print(os.path.abspath(__file__))
# path = os.path.abspath(__file__)
# print()

# view.setHtml(html)
# view.setHtml(html, baseUrl=QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))))

# view.setUrl()
# view.set
# view.load(QtCore.QUrl('http://'))
#print(os.path.split(os.path.abspath(__file__))[0]+r'\site\index.html')
view.load(QtCore.QUrl().fromLocalFile(
    os.path.split(os.path.abspath(__file__))[0]+r'\site\index.html'
))

view.show()
sys.exit(app.exec_())
