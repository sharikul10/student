  # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup(object):

	def addUser(self):
		f_name = self.lineEdit_5.text()
		l_name = self.lineEdit_6.text()
		u_name = self.lineEdit.text()
		p_name = self.lineEdit_2.text()
		e_name = self.lineEdit_4.text()


		db=pymysql.connect(host="localhost",user="root",passwd="rutu",db="project") 
		if (db.open):
			print ("connected")
		else:
			print ("Not connected")

		cursor=db.cursor()
		sql="insert into stud values ('%s','%s','%s','%s','%s')" % (f_name,l_name,u_name,p_name,e_name)
		cursor.execute(sql)
		result = cursor.fetchall()
		cursor.close()
		db.commit()
		db.close()
		signup.close()

		
		
	"""
		with open('iris.csv', 'w') as csvfile:
			fieldnames = ['first_name', 'last_name','usrname','password','Email']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			writer.writeheader()
			writer.writerow({'first_name': f_name, 'last_name': l_name,'usrname': u_name,'password': p_name,'Email': e_name})
	"""

	def setupUi(self, signup):
		signup.setObjectName("signup")
		signup.resize(914, 836)
		self.centralwidget = QtWidgets.QWidget(signup)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, 0, 911, 801))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("Pictures/s2.jpg"))
		self.label.setObjectName("label")
		self.username = QtWidgets.QLabel(self.centralwidget)
		self.username.setGeometry(QtCore.QRect(170, 300, 211, 31))
		self.username.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.username.setObjectName("username")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(214, 50, 541, 101))
		self.label_3.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";")
		self.label_3.setObjectName("label_3")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(480, 300, 221, 31))
		self.lineEdit.setObjectName("lineEdit")
		self.password = QtWidgets.QLabel(self.centralwidget)
		self.password.setGeometry(QtCore.QRect(220, 370, 171, 31))
		self.password.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.password.setObjectName("password")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(480, 370, 221, 31))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(480, 440, 221, 31))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.password1 = QtWidgets.QLabel(self.centralwidget)
		self.password1.setGeometry(QtCore.QRect(120, 440, 281, 31))
		self.password1.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.password1.setObjectName("password1")
		self.email = QtWidgets.QLabel(self.centralwidget)
		self.email.setGeometry(QtCore.QRect(220, 510, 181, 31))
		self.email.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.email.setObjectName("email")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(480, 510, 221, 31))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.create = QtWidgets.QPushButton(self.centralwidget)
		self.create.setGeometry(QtCore.QRect(350, 620, 161, 71))
		self.create.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
		"background-color: rgb(0, 157, 235);")
		self.create.setObjectName("create")
		self.fname = QtWidgets.QLabel(self.centralwidget)
		self.fname.setGeometry(QtCore.QRect(170, 170, 211, 31))
		self.fname.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.fname.setObjectName("fname")
		self.lname = QtWidgets.QLabel(self.centralwidget)
		self.lname.setGeometry(QtCore.QRect(170, 230, 211, 31))
		self.lname.setStyleSheet("\n"
		"font: 75 16pt \"MS Shell Dlg 2\";\n"
		"")
		self.lname.setObjectName("lname")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_5.setGeometry(QtCore.QRect(480, 170, 221, 31))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_6.setGeometry(QtCore.QRect(480, 230, 221, 31))
		self.lineEdit_6.setObjectName("lineEdit_6")
		signup.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(signup)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 26))
		self.menubar.setObjectName("menubar")
		signup.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(signup)
		self.statusbar.setObjectName("statusbar")
		signup.setStatusBar(self.statusbar)

		self.retranslateUi(signup)
		QtCore.QMetaObject.connectSlotsByName(signup)
		self.create.clicked.connect(self.addUser)
		

	def retranslateUi(self, signup):
		_translate = QtCore.QCoreApplication.translate
		signup.setWindowTitle(_translate("signup", "MainWindow"))
		self.username.setText(_translate("signup", "          USERNAME"))
		self.label_3.setText(_translate("signup", "CREATE NEW ACCOUNT"))
		self.password.setText(_translate("signup", "   PASSWORD"))
		self.password1.setText(_translate("signup", "RE-ENTER PASSWORD "))
		self.email.setText(_translate("signup", "       E-MAIL ID"))
		self.create.setText(_translate("signup", "CREATE"))
		self.fname.setText(_translate("signup", "        FIRST NAME"))
		self.lname.setText(_translate("signup", "         LAST NAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup = QtWidgets.QMainWindow()
    ui = Ui_signup()
    ui.setupUi(signup)
    signup.show()
    sys.exit(app.exec_())

