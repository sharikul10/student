# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Ui_signup
from graph1 import Ui_grpah1

class Ui_MainWindow(object):


	def openwindow(self):
		self.window=QtWidgets.QMainWindow()
		self.ui= Ui_signup()
		self.ui.setupUi(self.window)
		self.window.show()
	
	
	def clickwindow(self):
		self.window=QtWidgets.QMainWindow()
		self.ui= Ui_grpah1()
		self.ui.setupUi(self.window)
		self.window.show()
		
		
		
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1068, 834)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(-370, -10, 1691, 781))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("Pictures/172206.jpg"))
		self.label.setObjectName("label")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(340, 90, 481, 81))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(34)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("font: 75 34pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_3.setObjectName("label_3")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(280, 220, 551, 331))
		self.label_5.setStyleSheet("background-color: rgba(255, 255, 255,25);")
		self.label_5.setText("")
		self.label_5.setObjectName("label_5")
		self.login = QtWidgets.QPushButton(self.centralwidget)
		self.login.setGeometry(QtCore.QRect(390, 480, 131, 51))
		font = QtGui.QFont()
		font.setFamily("Microsoft YaHei UI")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.login.setFont(font)
		self.login.setStyleSheet("font: 75 14pt \"Microsoft YaHei UI\";\n"
		"background-color: rgb(255, 255, 255);")
		self.login.setObjectName("login")
		self.username = QtWidgets.QLabel(self.centralwidget)
		self.username.setGeometry(QtCore.QRect(300, 290, 231, 31))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(24)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.username.setFont(font)
		self.username.setStyleSheet("font: 14pt \"Open Sans\";\n"
		"font: 75 24pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.username.setObjectName("username")
		self.password = QtWidgets.QLabel(self.centralwidget)
		self.password.setGeometry(QtCore.QRect(310, 380, 211, 41))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(24)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.password.setFont(font)
		self.password.setStyleSheet("color: rgb(255, 255, 255);\n"
		"font: 75 24pt \"MS Shell Dlg 2\";")
		self.password.setObjectName("password")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(610, 290, 211, 31))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(610, 390, 211, 31))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.signup = QtWidgets.QPushButton(self.centralwidget)
		self.signup.setGeometry(QtCore.QRect(590, 480, 131, 51))
		self.signup.setStyleSheet("font: 75 14pt \"Microsoft YaHei UI\";\n"
		"background-color: rgb(255, 255, 255);")
		self.signup.setObjectName("signup")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.signup.clicked.connect(self.openwindow)
		self.login.clicked.connect(self.clickwindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label_3.setText(_translate("MainWindow", "KNOW YOURSELF"))
		self.login.setText(_translate("MainWindow", "LOGIN"))
		self.username.setText(_translate("MainWindow", "USERNAME"))
		self.password.setText(_translate("MainWindow", "PASSWORD"))
		self.signup.setText(_translate("MainWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

