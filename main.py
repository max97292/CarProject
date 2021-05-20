from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from loginForm import Ui_LoginWindow
from searchForm import Ui_SearchWindow
from mainForm import Ui_MainWindow
import sys
from test import CompileParsed


# class mainForm(QtWidgets.QMainWindow):
#     def init(self):
#         super(mainForm, self).init()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)


class searchForm(QtWidgets.QMainWindow):
    def init(self):
        super(searchForm, self).init()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        nationality = []
        cp = CompileParsed.compile()
        for driver in cp:
            if driver['nationality'] not in nationality:
                nationality.append(driver['nationality'])
        self.ui.comboBoxNationality.addItems(nationality)

    #     self.ui.pushButtonSubmit.clicked.connect(self.btnClicked)
    #
    # def btnClicked(self):
    #     self.window().hide()
    #     self.mainForm.show()


class loginForm(QtWidgets.QMainWindow):
    def init(self):
        super(loginForm, self).init()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonLogin.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.lineEditPassword.text() == 'pass':
            self.window().hide()
            self.searchForm.show()
            # QMessageBox.about(self, "Title", "Message")


app = QtWidgets.QApplication([])
application = loginForm()
application.show()

sys.exit(app.exec())