from PyQt5 import QtCore, QtGui, QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import requests
from bs4 import BeautifulSoup

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        res = requests.get('http://ergast.com/api/f1/2008')
        bs = BeautifulSoup(res.content, 'html.parser')
        for i in bs.racetable:
            print(i)
        self.ui.lineEdit.setText(bs.location['lat'])
        self.ui.label.adjustSize()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())