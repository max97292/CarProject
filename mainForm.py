# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 632)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("formula-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 20, 481, 41))
        self.textEdit.setStyleSheet("QTextEdit { background: rgb(170, 255, 255)}")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButtonReset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReset.setGeometry(QtCore.QRect(330, 540, 161, 41))
        self.pushButtonReset.setStyleSheet("QPushButton{background: rgb(255, 255, 127)}")
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(191, 244, 256, 33))
        self.textEdit_5.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(191, 163, 256, 33))
        self.textEdit_4.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.lineEditWin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditWin.setGeometry(QtCore.QRect(454, 249, 137, 22))
        self.lineEditWin.setReadOnly(True)
        self.lineEditWin.setObjectName("lineEditWin")
        self.lineEditBio = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBio.setGeometry(QtCore.QRect(454, 209, 137, 22))
        self.lineEditBio.setReadOnly(True)
        self.lineEditBio.setObjectName("lineEditBio")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(191, 284, 256, 34))
        self.textEdit_7.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(191, 446, 256, 34))
        self.textEdit_6.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.lineEditPodiums = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPodiums.setGeometry(QtCore.QRect(454, 452, 137, 22))
        self.lineEditPodiums.setReadOnly(True)
        self.lineEditPodiums.setObjectName("lineEditPodiums")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(191, 203, 256, 34))
        self.textEdit_12.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_12.setReadOnly(True)
        self.textEdit_12.setObjectName("textEdit_12")
        self.lineEditFastestLap = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFastestLap.setGeometry(QtCore.QRect(454, 330, 137, 22))
        self.lineEditFastestLap.setReadOnly(True)
        self.lineEditFastestLap.setObjectName("lineEditFastestLap")
        self.lineEditPoints = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPoints.setGeometry(QtCore.QRect(454, 290, 137, 22))
        self.lineEditPoints.setReadOnly(True)
        self.lineEditPoints.setObjectName("lineEditPoints")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(191, 325, 256, 33))
        self.textEdit_11.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_11.setReadOnly(True)
        self.textEdit_11.setObjectName("textEdit_11")
        self.lineEditChampionship = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditChampionship.setGeometry(QtCore.QRect(454, 371, 137, 22))
        self.lineEditChampionship.setReadOnly(True)
        self.lineEditChampionship.setObjectName("lineEditChampionship")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(191, 406, 256, 33))
        self.textEdit_8.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_8.setReadOnly(True)
        self.textEdit_8.setObjectName("textEdit_8")
        self.lineEditTeam = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTeam.setGeometry(QtCore.QRect(454, 128, 137, 22))
        self.lineEditTeam.setReadOnly(True)
        self.lineEditTeam.setObjectName("lineEditTeam")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(191, 81, 256, 34))
        self.textEdit_2.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(454, 87, 137, 22))
        self.lineEditName.setReadOnly(True)
        self.lineEditName.setObjectName("lineEditName")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(191, 122, 256, 34))
        self.textEdit_3.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.lineEditEntries = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEntries.setGeometry(QtCore.QRect(454, 411, 137, 22))
        self.lineEditEntries.setReadOnly(True)
        self.lineEditEntries.setObjectName("lineEditEntries")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(191, 365, 256, 34))
        self.textEdit_9.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_9.setReadOnly(True)
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(191, 487, 256, 33))
        self.textEdit_10.setStyleSheet("QTextEdit { background:rgb(170, 255, 255)}")
        self.textEdit_10.setReadOnly(True)
        self.textEdit_10.setObjectName("textEdit_10")
        self.lineEditNationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNationality.setGeometry(QtCore.QRect(454, 492, 137, 22))
        self.lineEditNationality.setReadOnly(True)
        self.lineEditNationality.setObjectName("lineEditNationality")
        self.lineEditDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDate.setGeometry(QtCore.QRect(454, 170, 137, 22))
        self.lineEditDate.setReadOnly(True)
        self.lineEditDate.setObjectName("lineEditDate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditName, self.lineEditTeam)
        MainWindow.setTabOrder(self.lineEditTeam, self.lineEditBio)
        MainWindow.setTabOrder(self.lineEditBio, self.lineEditWin)
        MainWindow.setTabOrder(self.lineEditWin, self.lineEditPoints)
        MainWindow.setTabOrder(self.lineEditPoints, self.lineEditFastestLap)
        MainWindow.setTabOrder(self.lineEditFastestLap, self.lineEditChampionship)
        MainWindow.setTabOrder(self.lineEditChampionship, self.lineEditEntries)
        MainWindow.setTabOrder(self.lineEditEntries, self.lineEditPodiums)
        MainWindow.setTabOrder(self.lineEditPodiums, self.pushButtonReset)
        MainWindow.setTabOrder(self.pushButtonReset, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit_11)
        MainWindow.setTabOrder(self.textEdit_11, self.textEdit_7)
        MainWindow.setTabOrder(self.textEdit_7, self.textEdit_8)
        MainWindow.setTabOrder(self.textEdit_8, self.textEdit_5)
        MainWindow.setTabOrder(self.textEdit_5, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_6)
        MainWindow.setTabOrder(self.textEdit_6, self.textEdit_9)
        MainWindow.setTabOrder(self.textEdit_9, self.textEdit_10)
        MainWindow.setTabOrder(self.textEdit_10, self.textEdit_12)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Biography</span></p></body></html>"))
        self.pushButtonReset.setText(_translate("MainWindow", "Back to search form"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Win:</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Date of birth:</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Points:</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Podiums:</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">BIO:</span></p></body></html>"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Fastest Lap:</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Entries:</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Name:</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Team:</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Championship:</span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Nationality:</span></p></body></html>"))
