# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registersZpidq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src import imagenes

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(707, 500)
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 711, 501))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 10, 51, 51))
        self.logo.setStyleSheet(u"border-image: url(../imagenes/logoUniConnect.png);")
        self.fondoAzul = QLabel(self.frame)
        self.fondoAzul.setObjectName(u"fondoAzul")
        self.fondoAzul.setGeometry(QRect(40, 90, 621, 391))
        self.fondoAzul.setStyleSheet(u"border-image: url(../imagenes/FondoDegradado.png);\n"
"")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 120, 221, 341))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"\n"
"background-color: rgb(252, 252, 252);\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(440, 220, 141, 21))
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
        self.lineEdit_2.setGeometry(QRect(440, 300, 141, 21))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 180, 121, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border-color: rgb(52, 136, 196);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 120, 61, 61))
        self.label_6.setStyleSheet(u"border-image: url(../imagenes/agregar-usuario.png);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 390, 111, 31))
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
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(440, 260, 141, 21))
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(440, 340, 141, 21))
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setStyleSheet(u"background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(420, 370, 191, 18))
        self.checkBox.setStyleSheet(u"font: 75 8pt \"Arial\";\n"
"color: rgb(126, 126, 126);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 440, 121, 16))
        self.label.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(141, 141, 141);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 437, 75, 23))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"font: 75 8pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(130, 130, 130);\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: rgb(85, 0, 255);\n"
"}")
        self.fondoAzul.raise_()
        self.logo.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.checkBox.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText("")
        self.fondoAzul.setText("")
        self.label_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.label_4.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Registrarse", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\" Ordena tu mundo, desata tu potencial \"", None))
        self.pushButton_5.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Nombre de usuario", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmar contrase\u00f1a", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Acepto los t\u00e9rminos y condiciones", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u00bfYa tienes una cuenta?", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

