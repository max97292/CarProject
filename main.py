from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mydesign import Ui_MainWindow
from searchForm import Ui_SearchWindow
import sys
from test import CompileParsed

class searchForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(searchForm, self).__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        nationality = []
        cp = CompileParsed.compile()
        for driver in cp:
            if driver['nationality'] not in nationality:
                nationality.append(driver['nationality'])
        self.ui.comboBoxNationality.addItems(nationality)

class loginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.searchForm = searchForm()

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.passwordEdit.text() == 'pass':
            self.window().hide()
            self.searchForm.show()
            # QMessageBox.about(self, "Title", "Message")


app = QtWidgets.QApplication([])
application = loginForm()
application.show()

sys.exit(app.exec())