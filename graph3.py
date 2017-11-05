# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt

class Ui_graph3(object):

	def data1(self):
		def f(v):
			ans=(v/24)*100
			return ans

		def data_graph():

			from graph2 import MGMT
			from graph1 import ACAD

			print(ACAD,"is acad")
			y = [ACAD,MGMT,self.creativity]
			y = [f(i) for i in y]	
			x = range(3)
			width = 1/1.5
			plt.bar(x,y,width,color='blue')

			print(x)
			print(y)
			plt.legend()
			plt.show()

		data_graph()

	def __init__(self):
		self.creativity=0
	
	def openwindow(self):
		self.window=QtWidgets.QMainWindow()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.window.show()
	
	def val4(self):
		if(self.rb65.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb66.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb67.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb68.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb69.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb70.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb71.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb72.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb73.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb74.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb75.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb76.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb77.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb78.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb79.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb80.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb81.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb82.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb83.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb84.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb85.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb86.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb87.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb88.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb89.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb90.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb91.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb92.isChecked() == True):
			self.creativity=self.creativity+ 0
		if(self.rb93.isChecked() == True):
			self.creativity=self.creativity+ 3
		if(self.rb94.isChecked() == True):
			self.creativity=self.creativity+ 2
		if(self.rb95.isChecked() == True):
			self.creativity=self.creativity+ 1
		if(self.rb96.isChecked() == True):
			self.creativity=self.creativity+ 0
			
		
		print(self.creativity)
		
	def setupUi(self, graph3):
		graph3.setObjectName("graph3")
		graph3.resize(1085, 1023)
		self.centralwidget = QtWidgets.QWidget(graph3)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, -40, 1101, 1071))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("Documents/CyT83yY.jpg"))
		self.label.setObjectName("label")
		self.gb1_5 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_5.setGeometry(QtCore.QRect(650, 90, 301, 141))
		self.gb1_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_5.setTitle("")
		self.gb1_5.setObjectName("gb1_5")
		self.rb69 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb69.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb69.setObjectName("rb69")
		self.rb72 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb72.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb72.setObjectName("rb72")
		self.rb71 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb71.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb71.setObjectName("rb71")
		self.rb70 = QtWidgets.QRadioButton(self.gb1_5)
		self.rb70.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb70.setObjectName("rb70")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(520, 250, 541, 41))
		self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_5.setObjectName("label_5")
		self.gb1_8 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_8.setGeometry(QtCore.QRect(100, 520, 301, 141))
		self.gb1_8.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_8.setTitle("")
		self.gb1_8.setObjectName("gb1_8")
		self.rb81 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb81.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb81.setObjectName("rb81")
		self.rb84 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb84.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb84.setObjectName("rb84")
		self.rb83 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb83.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb83.setObjectName("rb83")
		self.rb82 = QtWidgets.QRadioButton(self.gb1_8)
		self.rb82.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb82.setObjectName("rb82")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(590, 680, 541, 31))
		self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_8.setObjectName("label_8")
		self.gb1_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_6.setGeometry(QtCore.QRect(100, 300, 301, 141))
		self.gb1_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_6.setTitle("")
		self.gb1_6.setObjectName("gb1_6")
		self.rb73 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb73.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb73.setObjectName("rb73")
		self.rb76 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb76.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb76.setObjectName("rb76")
		self.rb75 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb75.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb75.setObjectName("rb75")
		self.rb74 = QtWidgets.QRadioButton(self.gb1_6)
		self.rb74.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb74.setObjectName("rb74")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(20, 40, 541, 31))
		self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(30, 250, 541, 41))
		self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_3.setObjectName("label_3")
		self.gb1_10 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_10.setGeometry(QtCore.QRect(100, 730, 301, 141))
		self.gb1_10.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_10.setTitle("")
		self.gb1_10.setObjectName("gb1_10")
		self.rb89 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb89.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb89.setObjectName("rb89")
		self.rb92 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb92.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb92.setObjectName("rb92")
		self.rb91 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb91.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb91.setObjectName("rb91")
		self.rb90 = QtWidgets.QRadioButton(self.gb1_10)
		self.rb90.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb90.setObjectName("rb90")
		self.gb1_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_4.setGeometry(QtCore.QRect(100, 90, 301, 141))
		self.gb1_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_4.setTitle("")
		self.gb1_4.setObjectName("gb1_4")
		self.rb65 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb65.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb65.setObjectName("rb65")
		self.rb68 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb68.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb68.setObjectName("rb68")
		self.rb67 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb67.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb67.setObjectName("rb67")
		self.rb66 = QtWidgets.QRadioButton(self.gb1_4)
		self.rb66.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb66.setObjectName("rb66")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(520, 39, 561, 31))
		self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_4.setObjectName("label_4")
		self.gb1_11 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_11.setGeometry(QtCore.QRect(650, 730, 301, 141))
		self.gb1_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_11.setTitle("")
		self.gb1_11.setObjectName("gb1_11")
		self.rb93 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb93.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb93.setObjectName("rb93")
		self.rb96 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb96.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb96.setObjectName("rb96")
		self.rb95 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb95.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb95.setObjectName("rb95")
		self.rb94 = QtWidgets.QRadioButton(self.gb1_11)
		self.rb94.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb94.setObjectName("rb94")
		self.gb1_9 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_9.setGeometry(QtCore.QRect(650, 510, 301, 141))
		self.gb1_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_9.setTitle("")
		self.gb1_9.setObjectName("gb1_9")
		self.rb85 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb85.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb85.setObjectName("rb85")
		self.rb88 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb88.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb88.setObjectName("rb88")
		self.rb87 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb87.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb87.setObjectName("rb87")
		self.rb86 = QtWidgets.QRadioButton(self.gb1_9)
		self.rb86.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb86.setObjectName("rb86")
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(40, 680, 541, 31))
		self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_9.setObjectName("label_9")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(30, 460, 541, 41))
		self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_6.setObjectName("label_6")
		self.gb1_7 = QtWidgets.QGroupBox(self.centralwidget)
		self.gb1_7.setGeometry(QtCore.QRect(650, 300, 301, 141))
		self.gb1_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.gb1_7.setTitle("")
		self.gb1_7.setObjectName("gb1_7")
		self.rb77 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb77.setGeometry(QtCore.QRect(10, 20, 151, 20))
		self.rb77.setObjectName("rb77")
		self.rb80 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb80.setGeometry(QtCore.QRect(10, 110, 151, 20))
		self.rb80.setObjectName("rb80")
		self.rb79 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb79.setGeometry(QtCore.QRect(10, 80, 161, 20))
		self.rb79.setObjectName("rb79")
		self.rb78 = QtWidgets.QRadioButton(self.gb1_7)
		self.rb78.setGeometry(QtCore.QRect(10, 50, 95, 20))
		self.rb78.setObjectName("rb78")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(550, 470, 541, 21))
		self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);")
		self.label_7.setObjectName("label_7")
		self.finish = QtWidgets.QPushButton(self.centralwidget)
		self.finish.setGeometry(QtCore.QRect(460, 890, 151, 51))
		self.finish.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
		"color: rgb(255, 255, 255);\n"
		"background-color: rgb(125, 62, 0);")
		self.finish.setObjectName("finish")
		graph3.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(graph3)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1085, 26))
		self.menubar.setObjectName("menubar")
		graph3.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(graph3)
		self.statusbar.setObjectName("statusbar")
		graph3.setStatusBar(self.statusbar)

		self.retranslateUi(graph3)
		QtCore.QMetaObject.connectSlotsByName(graph3)
		self.finish.clicked.connect(self.val4)
		self.finish.clicked.connect(self.data1)

	def retranslateUi(self, graph3):
		_translate = QtCore.QCoreApplication.translate
		graph3.setWindowTitle(_translate("graph3", "MainWindow"))
		self.rb69.setText(_translate("graph3", "  Very interested"))
		self.rb72.setText(_translate("graph3", "  Not interested"))
		self.rb71.setText(_translate("graph3", "  Slightly interested"))
		self.rb70.setText(_translate("graph3", "  Interested"))
		self.label_5.setText(_translate("graph3", "   20.  Write a blog post, magazine article, or novel."))
		self.rb81.setText(_translate("graph3", "  Very interested"))
		self.rb84.setText(_translate("graph3", "  Not interested"))
		self.rb83.setText(_translate("graph3", "  Slightly interested"))
		self.rb82.setText(_translate("graph3", "  Interested"))
		self.label_8.setText(_translate("graph3", "    24.  Learn about human behavior."))
		self.rb73.setText(_translate("graph3", "  Very interested"))
		self.rb76.setText(_translate("graph3", "  Not interested"))
		self.rb75.setText(_translate("graph3", "  Slightly interested"))
		self.rb74.setText(_translate("graph3", "  Interested"))
		self.label_2.setText(_translate("graph3", "  17. Critique art, music, or performances."))
		self.label_3.setText(_translate("graph3", "19.  Promote or market a brand new product."))
		self.rb89.setText(_translate("graph3", "  Very interested"))
		self.rb92.setText(_translate("graph3", "  Not interested"))
		self.rb91.setText(_translate("graph3", "  Slightly interested"))
		self.rb90.setText(_translate("graph3", "  Interested"))
		self.rb65.setText(_translate("graph3", "  Very interested"))
		self.rb68.setText(_translate("graph3", "  Not interested"))
		self.rb67.setText(_translate("graph3", "  Slightly interested"))
		self.rb66.setText(_translate("graph3", "  Interested"))
		self.label_4.setText(_translate("graph3", " 18. Work as a performer, costume designer, or background artist."))
		self.rb93.setText(_translate("graph3", "  Very interested"))
		self.rb96.setText(_translate("graph3", "  Not interested"))
		self.rb95.setText(_translate("graph3", "  Slightly interested"))
		self.rb94.setText(_translate("graph3", "  Interested"))
		self.rb85.setText(_translate("graph3", "  Very interested"))
		self.rb88.setText(_translate("graph3", "  Not interested"))
		self.rb87.setText(_translate("graph3", "  Slightly interested"))
		self.rb86.setText(_translate("graph3", "  Interested"))
		self.label_9.setText(_translate("graph3", "23.  Work with my hands."))
		self.label_6.setText(_translate("graph3", "21.  Work that is physical (keeps my body active)."))
		self.rb77.setText(_translate("graph3", "  Very interested"))
		self.rb80.setText(_translate("graph3", "  Not interested"))
		self.rb79.setText(_translate("graph3", "  Slightly interested"))
		self.rb78.setText(_translate("graph3", "  Interested"))
		self.label_7.setText(_translate("graph3", "    22.  Design works of art for others to enjoy."))
		self.finish.setText(_translate("graph3", "FINISH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graph3 = QtWidgets.QMainWindow()
    ui = Ui_graph3()
    ui.setupUi(graph3)
    graph3.show()
    sys.exit(app.exec_())

