# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginzBjWPv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(704, 500)
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 711, 501))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 51, 51))
        self.label.setStyleSheet(u"border-image: url(../imagenes/logoUniConnect.png);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 621, 391))
        self.label_2.setStyleSheet(u"border-image: url(../imagenes/FondoDegradado.png);\n"
"")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 130, 201, 331))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"\n"
"background-color: rgb(252, 252, 252);\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(430, 260, 141, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 140, 261, 221))
        self.label_4.setStyleSheet(u"border-image: url(../imagenes/logoSinFondo.png);\n"
"background-color: transparent;\n"
"")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(430, 310, 141, 21))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 210, 151, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border-color: rgb(52, 136, 196);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 140, 61, 61))
        self.label_6.setStyleSheet(u"border-image: url(../imagenes/usuario (4).png);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 340, 111, 31))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(132, 205, 255, 255), stop:1 rgba(85, 74, 208, 255));\n"
"font: 75 9pt \"Arial\";\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(255, 255, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"	background-color: rgb(60, 193, 231);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setAutoDefault(False)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 350, 311, 16))
        self.label_7.setStyleSheet(u"font: 75 13pt \"Arial\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(450, 380, 91, 21))
        self.label_8.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(44, 102, 164);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 400, 31, 21))
        self.pushButton_2.setStyleSheet(u"border-image: url(../imagenes/facebook.png);\n"
"background-color: transparent;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(480, 400, 31, 21))
        self.pushButton_3.setStyleSheet(u"border-image: url(../imagenes/google.png);\n"
"background-color: transparent;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(530, 400, 31, 21))
        self.pushButton_4.setStyleSheet(u"border-image: url(../imagenes/twitter.png);\n"
"background-color: transparent;")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(650, 10, 31, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"border-image: url(:/images/flecha-hacia-atras (1).png);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(230, 237, 253);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(405, 438, 121, 20))
        self.label_9.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(112, 112, 112);")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(525, 438, 61, 20))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	font: 75 8pt \"Arial\";\n"
"	text-decoration: underline;\n"
"	color: rgb(158, 158, 158);\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(85, 0, 255);\n"
"}")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_9.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi(Form)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario o email", None))
        self.label_4.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Iniciar sesi\u00f3n", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\" Ordena tu mundo, desata tu potencial \"", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"-------- O -------", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u00bfNo tienes una cuenta?", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Registrate", None))
    # retranslateUi

