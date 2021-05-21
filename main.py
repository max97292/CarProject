from PyQt5 import QtWidgets
from loginForm import Ui_LoginWindow
from searchForm import Ui_SearchWindow
from mainForm import Ui_MainWindow
import sys
from test import CompileParsed


class mainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class searchForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(searchForm, self).__init__()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        nationality = []
        cp = CompileParsed.compile(5)
        for driver in cp:
            if driver['nationality'] not in nationality:
                nationality.append(driver['nationality'])
        self.ui.comboBoxNationality.addItems(nationality)

        self.ui.pushButtonSubmit.clicked.connect(self.onSubmit)

    def onSubmit(self):
        self.mainform = mainForm()
        self.hide()
        self.mainform.show()


class loginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginForm, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonLogin.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.lineEditPassword.text() == 'pass':
            self.searchform = searchForm()
            self.window().hide()
            self.searchform.show()


app = QtWidgets.QApplication([])
application = loginForm()
application.show()

sys.exit(app.exec())