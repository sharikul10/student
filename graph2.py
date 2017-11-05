# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from graph3 import  Ui_graph3
import graph3 as g2


MGMT=0

class Ui_graph2(object):

	def __init__(self):
		self.management=0
		
	def openwindow(self):
		self.window=QtWidgets.QMainWindow()
		self.ui= Ui_graph3()
		self.ui.setupUi(self.window)
		self.window.show()

	def val3(self):
		if(self.rb33.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb34.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb35.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb36.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb37.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb38.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb39.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb40.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb41.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb42.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb43.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb44.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb45.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb46.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb47.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb48.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb49.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb50.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb51.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb52.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb53.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb54.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb55.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb56.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb57.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb58.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb59.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb60.isChecked() == True):
			self.management =self.management+ 0
		if(self.rb61.isChecked() == True):
			self.management =self.management+ 3
		if(self.rb62.isChecked() == True):
			self.management =self.management+ 2
		if(self.rb63.isChecked() == True):
			self.management =self.management+ 1
		if(self.rb64.isChecked() == True):
			self.management =self.management+ 0
		global MGMT
		MGMT = self.management
		print(self.management)


	def setupUi(self, graph2):
		graph2.setObjectName("graph2")
		graph2.resize(1035, 1023)
		self.centralwidget = QtWidgets.QWidget(graph2)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(-30, -50, 1101, 1081))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("Documents/CyT83yY.jpg"))
		self.label.setObjectName("label")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(530, 240, 541, 31))
		self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_5.setObjectName("label_5")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 30, 541, 31))
		self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 240, 541, 31))
		self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_3.setObjectName("label_3")
		self.gb1_10 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_10.setGeometry(QtCore.QRect(600, 490, 301, 141))
		self.gb1_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_10.setTitle("")
		self.gb1_10.setObjectName("gb1_10")
		self.rb53 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb53.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb53.setObjectName("rb53")
		self.rb56 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb56.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb56.setObjectName("rb56")
		self.rb55 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb55.setGeometry(QtCore.QRect(10, 80, 191, 20))
		self.rb55.setObjectName("rb55")
		self.rb54 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb54.setGeometry(QtCore.QRect(10, 50, 151, 20))
		self.rb54.setObjectName("rb54")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(540, 450, 541, 16))
		self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(530, 660, 541, 31))
		self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_8.setObjectName("label_8")
		self.gb1_9 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_9.setGeometry(QtCore.QRect(600, 290, 301, 141))
		self.gb1_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_9.setTitle("")
		self.gb1_9.setObjectName("gb1_9")
		self.rb45 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb45.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb45.setObjectName("rb45")
		self.rb48 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb48.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb48.setObjectName("rb48")
		self.rb47 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb47.setGeometry(QtCore.QRect(10, 80, 201, 20))
		self.rb47.setObjectName("rb47")
		self.rb46 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb46.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb46.setObjectName("rb46")
		self.gb1_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_4.setGeometry(QtCore.QRect(100, 80, 301, 141))
		self.gb1_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_4.setTitle("")
		self.gb1_4.setObjectName("gb1_4")
		self.rb33 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb33.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb33.setObjectName("rb33")
		self.rb36 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb36.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb36.setObjectName("rb36")
		self.rb35 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb35.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb35.setObjectName("rb35")
		self.rb34 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb34.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb34.setObjectName("rb34")
		self.gb1_5 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_5.setGeometry(QtCore.QRect(90, 290, 301, 141))
		self.gb1_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_5.setTitle("")
		self.gb1_5.setObjectName("gb1_5")
		self.rb41 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb41.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb41.setObjectName("rb41")
		self.rb44 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb44.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb44.setObjectName("rb44")
		self.rb43 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb43.setGeometry(QtCore.QRect(10, 80, 191, 20))
		self.rb43.setObjectName("rb43")
		self.rb42 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb42.setGeometry(QtCore.QRect(10, 50, 131, 20))
		self.rb42.setObjectName("rb42")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(10, 440, 541, 31))
		self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_6.setObjectName("label_6")
		self.gb1_8 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_8.setGeometry(QtCore.QRect(600, 80, 301, 141))
		self.gb1_8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_8.setTitle("")
		self.gb1_8.setObjectName("gb1_8")
		self.rb37 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb37.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb37.setObjectName("rb37")
		self.rb40 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb40.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb40.setObjectName("rb40")
		self.rb39 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb39.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb39.setObjectName("rb39")
		self.rb38 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb38.setGeometry(QtCore.QRect(10, 50, 141, 20))
		self.rb38.setObjectName("rb38")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(510, 30, 551, 31))
		self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_4.setObjectName("label_4")
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(10, 660, 541, 31))
		self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_9.setObjectName("label_9")
		self.gb1_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_6.setGeometry(QtCore.QRect(90, 490, 301, 141))
		self.gb1_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_6.setTitle("")
		self.gb1_6.setObjectName("gb1_6")
		self.rb49 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb49.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb49.setObjectName("rb49")
		self.rb52 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb52.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb52.setObjectName("rb52")
		self.rb51 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb51.setGeometry(QtCore.QRect(10, 80, 191, 20))
		self.rb51.setObjectName("rb51")
		self.rb50 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb50.setGeometry(QtCore.QRect(10, 50, 121, 20))
		self.rb50.setObjectName("rb50")
		self.gb1_7 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_7.setGeometry(QtCore.QRect(90, 720, 301, 141))
		self.gb1_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_7.setTitle("")
		self.gb1_7.setObjectName("gb1_7")
		self.rb57 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb57.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb57.setObjectName("rb57")
		self.rb60 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb60.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb60.setObjectName("rb60")
		self.rb59 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb59.setGeometry(QtCore.QRect(10, 80, 201, 20))
		self.rb59.setObjectName("rb59")
		self.rb58 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb58.setGeometry(QtCore.QRect(10, 50, 131, 20))
		self.rb58.setObjectName("rb58")
		self.gb1_11 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_11.setGeometry(QtCore.QRect(600, 720, 301, 141))
		self.gb1_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_11.setTitle("")
		self.gb1_11.setObjectName("gb1_11")
		self.rb61 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb61.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb61.setObjectName("rb61")
		self.rb64 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb64.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb64.setObjectName("rb64")
		self.rb63 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb63.setGeometry(QtCore.QRect(10, 80, 181, 20))
		self.rb63.setObjectName("rb63")
		self.rb62 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb62.setGeometry(QtCore.QRect(10, 50, 171, 20))
		self.rb62.setObjectName("rb62")
		self.nextpage1 = QtWidgets.QPushButton(self.centralwidget)
		self.nextpage1.setGeometry(QtCore.QRect(440, 890, 151, 51))
		self.nextpage1.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);\n"
		"background-color: rgb(125, 62, 0);")
		self.nextpage1.setObjectName("nextpage1")
		graph2.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(graph2)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 26))
		self.menubar.setObjectName("menubar")
		graph2.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(graph2)
		self.statusbar.setObjectName("statusbar")
		graph2.setStatusBar(self.statusbar)

		self.retranslateUi(graph2)
		QtCore.QMetaObject.connectSlotsByName(graph2)
		self.nextpage1.clicked.connect(self.openwindow)
		self.nextpage1.clicked.connect(self.val3)

	def retranslateUi(self, graph2):
		_translate = QtCore.QCoreApplication.translate
		graph2.setWindowTitle(_translate("graph2", "MainWindow"))
		self.label_5.setText(_translate("graph2", "   12.  Supervise, hire, and mentor others."))
		self.label_2.setText(_translate("graph2", "9.  Help people during a natural disaster or emergency."))
		self.label_3.setText(_translate("graph2", "11.  A career that takes less than 2 years of education."))
		self.rb53.setText(_translate("graph2", "  Very interested"))
		self.rb56.setText(_translate("graph2", "  Not interested"))
		self.rb55.setText(_translate("graph2", "  Slightly interested"))
		self.rb54.setText(_translate("graph2", "  Interested"))
		self.label_7.setText(_translate("graph2", "   14.  Teach people new skills."))
		self.label_8.setText(_translate("graph2", "     16.  Teach a large group how to do something."))
		self.rb45.setText(_translate("graph2", "  Very interested"))
		self.rb48.setText(_translate("graph2", "  Not interested"))
		self.rb47.setText(_translate("graph2", "  Slightly interested"))
		self.rb46.setText(_translate("graph2", "  Interested"))
		self.rb33.setText(_translate("graph2", "  Very interested"))
		self.rb36.setText(_translate("graph2", "  Not interested"))
		self.rb35.setText(_translate("graph2", "  Slightly interested"))
		self.rb34.setText(_translate("graph2", "  Interested"))
		self.rb41.setText(_translate("graph2", "  Very interested"))
		self.rb44.setText(_translate("graph2", "  Not interested"))
		self.rb43.setText(_translate("graph2", "  Slightly interested"))
		self.rb42.setText(_translate("graph2", "  Interested"))
		self.label_6.setText(_translate("graph2", "13.  Develop lesson plans for classes."))
		self.rb37.setText(_translate("graph2", "  Very interested"))
		self.rb40.setText(_translate("graph2", "  Not interested"))
		self.rb39.setText(_translate("graph2", "  Slightly interested"))
		self.rb38.setText(_translate("graph2", "  Interested"))
		self.label_4.setText(_translate("graph2", "   10.  Ensure federal, state, and local laws are abided by."))
		self.label_9.setText(_translate("graph2", "15.  Prepare a press release or commercial."))
		self.rb49.setText(_translate("graph2", "  Very interested"))
		self.rb52.setText(_translate("graph2", "  Not interested"))
		self.rb51.setText(_translate("graph2", "  Slightly interested"))
		self.rb50.setText(_translate("graph2", "  Interested"))
		self.rb57.setText(_translate("graph2", "  Very interested"))
		self.rb60.setText(_translate("graph2", "  Not interested"))
		self.rb59.setText(_translate("graph2", "  Slightly interested"))
		self.rb58.setText(_translate("graph2", "  Interested"))
		self.rb61.setText(_translate("graph2", "  Very interested"))
		self.rb64.setText(_translate("graph2", "  Not interested"))
		self.rb63.setText(_translate("graph2", "  Slightly interested"))
		self.rb62.setText(_translate("graph2", "  Interested"))
		self.nextpage1.setText(_translate("graph2", "NEXT PAGE"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph2 = QtWidgets.QMainWindow()
    ui = Ui_graph2()
    ui.setupUi(graph2)
    graph2.show()
    sys.exit(app.exec_())

