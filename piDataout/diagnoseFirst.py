# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnoseFirst.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from diagnoseSecond import Ui_secondPage
from datetime import datetime
import os.path



class Ui_firstPage(object):
    def open2(self):
        
        #print (data2)

        data2 = [
            str(self.lineEdit_1.text()),
            str(self.lineEdit_2.text()),
            str(self.lineEdit_4.text()),
            str(self.lineEdit_5.text())
            ]
       
        
        f = open("patient.txt", "w+")

        for line in data2:
            # write line to output file
            f.write(line)
            f.write("\n")

        self.window=QtWidgets.QDialog() 
        self.ui = Ui_secondPage()
        self.ui.setupUi(self.window) #setupUi as in other program
        self.window.showFullScreen()
        

    def setupUi(self, firstPage):
        firstPage.setObjectName("firstPage")
        firstPage.resize(480, 800)
        firstPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        firstPage.setIconSize(QtCore.QSize(70, 70))
        self.centralwidget = QtWidgets.QWidget(firstPage)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(260, 180, 181, 31))
        self.lineEdit_1.setStyleSheet("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.nationality = QtWidgets.QLabel(self.centralwidget)
        self.nationality.setGeometry(QtCore.QRect(40, 310, 61, 61))
        self.nationality.setText("")
        self.nationality.setPixmap(QtGui.QPixmap(":/newPrefix/nationality.png"))
        self.nationality.setScaledContents(True)
        self.nationality.setObjectName("nationality")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(40, 410, 61, 61))
        self.id.setText("")
        self.id.setPixmap(QtGui.QPixmap(":/newPrefix/ID.png"))
        self.id.setScaledContents(True)
        self.id.setObjectName("id")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(40, 190, 61, 61))
        self.name.setText("")
        self.name.setPixmap(QtGui.QPixmap(":/newPrefix/name.png"))
        self.name.setScaledContents(True)
        self.name.setObjectName("name")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 230, 181, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 320, 181, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 420, 181, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 710, 470, 60))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/nav1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.continue1 = QtWidgets.QPushButton(self.centralwidget)
        self.continue1.setGeometry(QtCore.QRect(140, 530, 200, 52))
        self.continue1.setStyleSheet("background-color: rgb(157, 195, 230);\n"
"font: 20pt \"Arial Rounded MT Bold\";\n"
"border-radius: 15px;\n"
"color: rgb(46, 117, 182);\n"
"\n"
"\n"
"")
        self.continue1.setAutoDefault(False)
        self.continue1.setDefault(True)
        self.continue1.setFlat(False)
        self.continue1.setObjectName("continue1")
        self.personal_details = QtWidgets.QLabel(self.centralwidget)
        self.personal_details.setGeometry(QtCore.QRect(20, 45, 420, 60))
        self.personal_details.setStyleSheet("background-color: transparent;\n"
"font: 38pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.personal_details.setObjectName("personal_details")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(120, 170, 101, 41))
        self.name_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.name_2.setObjectName("name_2")
        self.surname = QtWidgets.QLabel(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(120, 220, 111, 41))
        self.surname.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.surname.setObjectName("surname")
        self.nationality_2 = QtWidgets.QLabel(self.centralwidget)
        self.nationality_2.setGeometry(QtCore.QRect(120, 315, 131, 41))
        self.nationality_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.nationality_2.setObjectName("nationality_2")
        self.id_2 = QtWidgets.QLabel(self.centralwidget)
        self.id_2.setGeometry(QtCore.QRect(120, 420, 131, 41))
        self.id_2.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"Arial Rounded MT Bold\";\n"
"color: rgb(46, 117, 182);\n"
"")
        self.id_2.setObjectName("id_2")
        firstPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(firstPage)
        self.statusbar.setObjectName("statusbar")
        firstPage.setStatusBar(self.statusbar)

        self.retranslateUi(firstPage)
        
        self.continue1.clicked.connect(self.open2)
        self.continue1.clicked.connect(firstPage.close)
        
        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        _translate = QtCore.QCoreApplication.translate
        firstPage.setWindowTitle(_translate("firstPage", "MainWindow"))
        self.continue1.setText(_translate("firstPage", "CONTINUE"))
        self.personal_details.setText(_translate("firstPage", " Personal details"))
        self.name_2.setText(_translate("firstPage", "Name"))
        self.surname.setText(_translate("firstPage", "Surame"))
        self.nationality_2.setText(_translate("firstPage", "Nationality"))
        self.id_2.setText(_translate("firstPage", "ID Number"))

import First_page_file

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstPage = QtWidgets.QMainWindow()
    ui = Ui_firstPage()
    ui.setupUi(firstPage)
    firstPage.show()
    sys.exit(app.exec_())

