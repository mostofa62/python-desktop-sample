import sys

from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('picdb')
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\n"
                "This example needs SQLite support. Please read the Qt SQL "
                "driver documentation for information how to build it.\n\n"
                "Click Cancel to exit.",
                QMessageBox.Cancel)
        return False

    query = QSqlQuery()
    return query.exec_('''CREATE TABLE IF NOT EXISTS imgTable
        (id INTEGER primary key AUTOINCREMENT, filename TEXT, imagedata BLOB)''')

		

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        vbox = QVBoxLayout(self)

        self.load_btn = QPushButton("Select Image")
        self.combo = QComboBox()
        self.label = QLabel()
        self.model = QSqlTableModel()
        self.model.setTable("imgTable")
        self.model.select()
        self.combo.setModel(self.model)
        self.combo.setModelColumn(1)
        vbox.addWidget(self.load_btn)
        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)
        self.load_btn.clicked.connect(self.load_image)
        self.combo.currentIndexChanged.connect(self.on_change_select)

    def on_change_select(self, row):
        ix = self.combo.model().index(row, 2)
        pix = QPixmap()
        pix.loadFromData(ix.data())
        self.label.setPixmap(pix)

    def load_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', QDir.currentPath(), "Image files (*.jpg, *.gif, *.png)")
        if fname:
            self.saveImage(fname)

    def saveImage(self, filename):
        file = QFile(filename)
        if not file.open(QIODevice.ReadOnly):
            return
        ba = file.readAll()
        name = QFileInfo(filename).fileName()
        record = self.model.record()
        record.setValue("filename", name)
        record.setValue("imagedata", ba)

        if self.model.insertRecord(-1, record):
            self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not createConnection():
        sys.exit(-1)
    w = Widget()
    w.show()
    sys.exit(app.exec_())