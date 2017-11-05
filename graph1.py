# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import graph3 as g1
from graph2 import Ui_graph2
ACAD=0

class Ui_grpah1(object):

    
	def __init__(self):
		self.acad=0


	def openwindow(self):
		self.window=QtWidgets.QMainWindow()
		self.ui= Ui_graph2()
		self.ui.setupUi(self.window)
		self.window.show()
		
	def val2(self):
		
		if(self.rb1.isChecked() == True):
			self.acad =self.acad+3
		if(self.rb2.isChecked() == True):
			self.acad =self.acad+2
		if(self.rb3.isChecked() == True):
			self.acad =self.acad+1
		if(self.rb4.isChecked() == True):
			self.acad =self.acad+0
		if(self.rb5.isChecked() == True):
			self.acad =self.acad+3
		if(self.rb6.isChecked() == True):
			self.acad =self.acad+2
		if(self.rb7.isChecked() == True):
			self.acad =self.acad+1
		if(self.rb8.isChecked() == True):
			self.acad =self.acad+0
		if(self.rb9.isChecked() == True):
			self.acad =self.acad+3
		if(self.rb10.isChecked() == True):
			self.acad =self.acad+2
		if(self.rb11.isChecked() == True):
			self.acad =self.acad+1
		if(self.rb12.isChecked() == True):
			self.acad =self.acad+0
		if(self.rb13.isChecked() == True):
			self.acad =self.acad+ 3
		if(self.rb14.isChecked() == True):
			self.acad =self.acad+ 2
		if(self.rb15.isChecked() == True):
			self.acad =self.acad+ 1
		if(self.rb16.isChecked() == True):
			self.acad =self.acad+ 0
		if(self.rb17.isChecked() == True):
			self.acad =self.acad+ 3
		if(self.rb18.isChecked() == True):
			self.acad =self.acad+ 2
		if(self.rb19.isChecked() == True):
			self.acad =self.acad+ 1
		if(self.rb20.isChecked() == True):
			self.acad =self.acad+ 0
		if(self.rb21.isChecked() == True):
			self.acad =self.acad+ 3
		if(self.rb22.isChecked() == True):
			self.acad =self.acad+ 2
		if(self.rb23.isChecked() == True):
			self.acad =self.acad+ 1
		if(self.rb24.isChecked() == True):
			self.acad =self.acad+ 0
		if(self.rb25.isChecked() == True):
			self.acad =self.acad+ 3
		if(self.rb26.isChecked() == True):
			self.acad =self.acad+ 2
		if(self.rb27.isChecked() == True):
			self.acad =self.acad+ 1
		if(self.rb28.isChecked() == True):
			self.acad =self.acad+ 0
		if(self.rb29.isChecked() == True):
			self.acad =self.acad+ 3
		if(self.rb30.isChecked() == True):
			self.acad =self.acad+ 2
		if(self.rb31.isChecked() == True):
			self.acad =self.acad+ 1
		if(self.rb32.isChecked() == True):
			self.acad =self.acad+ 0			
		global ACAD
		ACAD = self.acad
		print (ACAD)
		
	def setupUi(self, grpah1):
		grpah1.setObjectName("grpah1")
		grpah1.resize(991, 1023)
		self.centralwidget = QtWidgets.QWidget(grpah1)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, -50, 991, 1021))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("Documents/CyT83yY.jpg"))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(420, 10, 191, 71))
		self.label_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_2.setObjectName("label_2")
		self.gb1_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_4.setGeometry(QtCore.QRect(80, 130, 301, 141))
		self.gb1_4.setTitle("")
		self.gb1_4.setObjectName("gb1_4")
		self.rb1 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb1.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb1.setObjectName("rb1")
		self.rb4 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb4.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb4.setObjectName("rb4")
		self.rb3 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb3.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb3.setObjectName("rb3")
		self.rb2 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb2.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb2.setObjectName("rb2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(30, 290, 541, 21))
		self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(20, 90, 541, 21))
		self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_4.setObjectName("label_4")
		self.gb1_2 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_2.setGeometry(QtCore.QRect(80, 530, 301, 141))
		self.gb1_2.setTitle("")
		self.gb1_2.setObjectName("gb1_2")
		self.rb20 = QtWidgets.QRadioButton(self.gb1_2)
		self.rb20.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb20.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb20.setObjectName("rb20")
		self.rb17 = QtWidgets.QRadioButton(self.gb1_2)
		self.rb17.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb17.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb17.setObjectName("rb17")
		self.rb18 = QtWidgets.QRadioButton(self.gb1_2)
		self.rb18.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb18.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb18.setObjectName("rb18")
		self.rb19 = QtWidgets.QRadioButton(self.gb1_2)
		self.rb19.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb19.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb19.setObjectName("rb19")
		self.gb1_3 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_3.setGeometry(QtCore.QRect(80, 730, 301, 141))
		self.gb1_3.setTitle("")
		self.gb1_3.setObjectName("gb1_3")
		self.rb28 = QtWidgets.QRadioButton(self.gb1_3)
		self.rb28.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb28.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb28.setObjectName("rb28")
		self.rb25 = QtWidgets.QRadioButton(self.gb1_3)
		self.rb25.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb25.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb25.setObjectName("rb25")
		self.rb26 = QtWidgets.QRadioButton(self.gb1_3)
		self.rb26.setGeometry(QtCore.QRect(10, 50, 131, 20))
		self.rb26.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb26.setObjectName("rb26")
		self.rb27 = QtWidgets.QRadioButton(self.gb1_3)
		self.rb27.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb27.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb27.setObjectName("rb27")
		self.gb1 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1.setGeometry(QtCore.QRect(80, 330, 301, 141))
		self.gb1.setTitle("")
		self.gb1.setObjectName("gb1")
		self.rb12 = QtWidgets.QRadioButton(self.gb1)
		self.rb12.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb12.setObjectName("rb12")
		self.rb11 = QtWidgets.QRadioButton(self.gb1)
		self.rb11.setGeometry(QtCore.QRect(10, 80, 171, 20))
		self.rb11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb11.setObjectName("rb11")
		self.rb9 = QtWidgets.QRadioButton(self.gb1)
		self.rb9.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb9.setObjectName("rb9")
		self.rb10 = QtWidgets.QRadioButton(self.gb1)
		self.rb10.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb10.setObjectName("rb10")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(30, 480, 541, 31))
		self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_6.setObjectName("label_6")
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(40, 690, 541, 31))
		self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_9.setObjectName("label_9")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(560, 90, 551, 21))
		self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_5.setObjectName("label_5")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(550, 690, 541, 31))
		self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_8.setObjectName("label_8")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(520, 290, 541, 21))
		self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_7.setObjectName("label_7")
		self.label_10 = QtWidgets.QLabel(self.centralwidget)
		self.label_10.setGeometry(QtCore.QRect(520, 485, 541, 31))
		self.label_10.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_10.setObjectName("label_10")
		self.gb1_5 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_5.setGeometry(QtCore.QRect(620, 130, 301, 141))
		self.gb1_5.setTitle("")
		self.gb1_5.setObjectName("gb1_5")
		self.rb5 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb5.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb5.setObjectName("rb5")
		self.rb8 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb8.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb8.setObjectName("rb8")
		self.rb7 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb7.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb7.setObjectName("rb7")
		self.rb6 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb6.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb6.setObjectName("rb6")
		self.gb1_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_6.setGeometry(QtCore.QRect(620, 330, 301, 141))
		self.gb1_6.setTitle("")
		self.gb1_6.setObjectName("gb1_6")
		self.rb13 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb13.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb13.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb13.setObjectName("rb13")
		self.rb16 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb16.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb16.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb16.setObjectName("rb16")
		self.rb15 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb15.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb15.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb15.setObjectName("rb15")
		self.rb14 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb14.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb14.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb14.setObjectName("rb14")
		self.gb1_7 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_7.setGeometry(QtCore.QRect(620, 530, 301, 141))
		self.gb1_7.setTitle("")
		self.gb1_7.setObjectName("gb1_7")
		self.rb21 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb21.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb21.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb21.setObjectName("rb21")
		self.rb24 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb24.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb24.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb24.setObjectName("rb24")
		self.rb23 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb23.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb23.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb23.setObjectName("rb23")
		self.rb22 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb22.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb22.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb22.setObjectName("rb22")
		self.gb1_8 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_8.setGeometry(QtCore.QRect(620, 730, 301, 141))
		self.gb1_8.setTitle("")
		self.gb1_8.setObjectName("gb1_8")
		self.rb29 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb29.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb29.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb29.setObjectName("rb29")
		self.rb32 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb32.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb32.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb32.setObjectName("rb32")
		self.rb31 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb31.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb31.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb31.setObjectName("rb31")
		self.rb30 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb30.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb30.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.rb30.setObjectName("rb30")
		self.nextpage = QtWidgets.QPushButton(self.centralwidget)
		self.nextpage.setGeometry(QtCore.QRect(430, 890, 151, 51))
		self.nextpage.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);\n"
		"background-color: rgb(125, 62, 0);")
		self.nextpage.setObjectName("nextpage")
		grpah1.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(grpah1)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 26))
		self.menubar.setObjectName("menubar")
		grpah1.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(grpah1)
		self.statusbar.setObjectName("statusbar")
		grpah1.setStatusBar(self.statusbar)

		self.retranslateUi(grpah1)
		QtCore.QMetaObject.connectSlotsByName(grpah1)
		self.nextpage.clicked.connect(self.val2)
		self.nextpage.clicked.connect(self.openwindow)

	def retranslateUi(self, grpah1):
		_translate = QtCore.QCoreApplication.translate
		grpah1.setWindowTitle(_translate("grpah1", "MainWindow"))
		self.label_2.setText(_translate("grpah1", "LETS START !!"))
		self.rb1.setText(_translate("grpah1", "  Very interested"))
		self.rb4.setText(_translate("grpah1", "  Not interested"))
		self.rb3.setText(_translate("grpah1", "  Slightly interested"))
		self.rb2.setText(_translate("grpah1", "  Interested"))
		self.label_3.setText(_translate("grpah1", "3.  Motivate and help others fulfill their goals."))
		self.label_4.setText(_translate("grpah1", "1.  Code a website, mobile app, or software program."))
		self.rb20.setText(_translate("grpah1", "  Not interested"))
		self.rb17.setText(_translate("grpah1", "  Very interested"))
		self.rb18.setText(_translate("grpah1", "  Interested"))
		self.rb19.setText(_translate("grpah1", "  Slightly interested"))
		self.rb28.setText(_translate("grpah1", "  Not interested"))
		self.rb25.setText(_translate("grpah1", "  Very interested"))
		self.rb26.setText(_translate("grpah1", "  Interested"))
		self.rb27.setText(_translate("grpah1", "  Slightly interested"))
		self.rb12.setText(_translate("grpah1", "  Not interested"))
		self.rb11.setText(_translate("grpah1", "  Slightly interested"))
		self.rb9.setText(_translate("grpah1", "  Very interested"))
		self.rb10.setText(_translate("grpah1", "  Interested"))
		self.label_6.setText(_translate("grpah1", " 5.  Learn computer software programs."))
		self.label_9.setText(_translate("grpah1", "7. Understand world events or politics."))
		self.label_5.setText(_translate("grpah1", " 2.  Learn how the body functions."))
		self.label_8.setText(_translate("grpah1", "8.  Teach a large group how to do something."))
		self.label_7.setText(_translate("grpah1", "    4.  Discover why chemicals react to one another."))
		self.label_10.setText(_translate("grpah1", "    6.  Take care of people even strangers."))
		self.rb5.setText(_translate("grpah1", "  Very interested"))
		self.rb8.setText(_translate("grpah1", "  Not interested"))
		self.rb7.setText(_translate("grpah1", "  Slightly interested"))
		self.rb6.setText(_translate("grpah1", "  Interested"))
		self.rb13.setText(_translate("grpah1", "  Very interested"))
		self.rb16.setText(_translate("grpah1", "  Not interested"))
		self.rb15.setText(_translate("grpah1", "  Slightly interested"))
		self.rb14.setText(_translate("grpah1", "  Interested"))
		self.rb21.setText(_translate("grpah1", "  Very interested"))
		self.rb24.setText(_translate("grpah1", "  Not interested"))
		self.rb23.setText(_translate("grpah1", "  Slightly interested"))
		self.rb22.setText(_translate("grpah1", "  Interested"))
		self.rb29.setText(_translate("grpah1", "  Very interested"))
		self.rb32.setText(_translate("grpah1", "  Not interested"))
		self.rb31.setText(_translate("grpah1", "  Slightly interested"))
		self.rb30.setText(_translate("grpah1", "  Interested"))
		self.nextpage.setText(_translate("grpah1", "NEXT PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    grpah1 = QtWidgets.QMainWindow()
    ui = Ui_grpah1()
    ui.setupUi(grpah1)
    grpah1.show()
    sys.exit(app.exec_())

