# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(329, 700)
        MainWindow.setMinimumSize(QtCore.QSize(329, 700))
        MainWindow.setMaximumSize(QtCore.QSize(329, 700))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(110, 20, 141, 61))
        self.title_label.setMinimumSize(QtCore.QSize(141, 61))
        self.title_label.setMaximumSize(QtCore.QSize(61, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.amy_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.amy_button.setGeometry(QtCore.QRect(31, 111, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.amy_button.setFont(font)
        self.amy_button.setAutoExclusive(True)
        self.amy_button.setObjectName("amy_button")
        self.joseph_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.joseph_button.setGeometry(QtCore.QRect(31, 142, 127, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.joseph_button.setFont(font)
        self.joseph_button.setAutoExclusive(True)
        self.joseph_button.setObjectName("joseph_button")
        self.jenny_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.jenny_button.setGeometry(QtCore.QRect(31, 173, 112, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.jenny_button.setFont(font)
        self.jenny_button.setAutoExclusive(True)
        self.jenny_button.setObjectName("jenny_button")
        self.ben_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.ben_button.setGeometry(QtCore.QRect(31, 204, 107, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ben_button.setFont(font)
        self.ben_button.setAutoExclusive(True)
        self.ben_button.setObjectName("ben_button")
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(20, 250, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.result_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.result_button.setGeometry(QtCore.QRect(190, 250, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result_button.setFont(font)
        self.result_button.setObjectName("result_button")
        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(20, 350, 281, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_label.setFont(font)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.results_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.results_label.setGeometry(QtCore.QRect(110, 320, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.results_label.setFont(font)
        self.results_label.setObjectName("results_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting Project"))
        self.title_label.setText(_translate("MainWindow", "VOTE!"))
        self.amy_button.setText(_translate("MainWindow", "Amy Dane"))
        self.joseph_button.setText(_translate("MainWindow", "Joseph Strong"))
        self.jenny_button.setText(_translate("MainWindow", "Jenny Apple"))
        self.ben_button.setText(_translate("MainWindow", "Ben Dianca"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.result_button.setText(_translate("MainWindow", "VIEW RESULTS"))
        self.results_label.setText(_translate("MainWindow", "RESULTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())