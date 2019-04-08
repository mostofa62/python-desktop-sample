from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal
class LinkLabel(QLabel):
 changedValue = pyqtSignal(int)
 linkId=None;
 def __init__(self, parent=None):
  QLabel.__init__(self, parent)
  self.setStyleSheet("QLabel { background-color:rgba(232, 12, 12, 50); border: 1px solid rgba(188, 188, 188, 250); color:rgba(0,0,0,255); }")
  
 def mousePressEvent(self, event):
  #print(self.linkId)
  self.changedValue.emit(self.linkId)