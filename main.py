from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from mydesign import Ui_MainWindow
from mainForm import Ui_MainWindowForm
import sys
from test import CompileParsed

class mainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainForm, self).__init__()
        self.ui = Ui_MainWindowForm()
        self.ui.setupUi(self)

        cp = CompileParsed.compile()
        for driver in cp:
            self.ui.comboBox.addItem(driver['name'])
            self.ui.comboBoxTeam.addItem(driver['team'])
            self.ui.comboBoxDate.addItem(driver['birth_date'])

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mainForm = mainForm()

        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.passwordEdit.text() == 'pass':
            self.window().hide()
            self.mainForm.show()
            # QMessageBox.about(self, "Title", "Message")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())