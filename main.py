from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mydesign import Ui_MainWindow
from mainForm import Ui_MainWindowForm
import sys
import requests
from bs4 import BeautifulSoup

class mainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.ui = Ui_MainWindowForm()
        self.ui.setupUi(self)
        res = requests.get('http://ergast.com/api/f1/drivers')
        bs = BeautifulSoup(res.content, 'html.parser')

        drivers = bs.find_all('driver')

        for driver in drivers:
            name = driver.find('givenname').text
            sur_name = driver.find('familyname').text
            self.ui.comboBox.addItem(name + " " + sur_name)
            # print(name, sur_name)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)


    def btnClicked(self):
        if self.ui.passwordEdit.text() == 'pass':
            # QMessageBox.about(self, "Title", "Message")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindowForm()
            self.ui.setupUi(self.window)
            self.window.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())