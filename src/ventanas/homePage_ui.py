# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Yolal\ing_soft\Practica-Ing.software\src\ventanas\homePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.barra = QtWidgets.QWidget(self.widget)
        self.barra.setGeometry(QtCore.QRect(0, 0, 61, 281))
        self.barra.setStyleSheet("background-color: rgb(249, 235, 211);\n"
"\n"
"\n"
"")
        self.barra.setObjectName("barra")
        self.boton_usuario = QtWidgets.QPushButton(self.barra)
        self.boton_usuario.setGeometry(QtCore.QRect(20, 110, 21, 21))
        self.boton_usuario.setMaximumSize(QtCore.QSize(200, 100))
        self.boton_usuario.setStyleSheet("\n"
"border-image: url(imagenes/usuario (4).png);")
        self.boton_usuario.setText("")
        self.boton_usuario.setIconSize(QtCore.QSize(10, 5))
        self.boton_usuario.setObjectName("boton_usuario")
        self.botonasignaturas = QtWidgets.QPushButton(self.barra)
        self.botonasignaturas.setGeometry(QtCore.QRect(20, 150, 21, 21))
        self.botonasignaturas.setStyleSheet("\n"
"border-image: url(imagenes/open-book.png);")
        self.botonasignaturas.setText("")
        self.botonasignaturas.setObjectName("botonasignaturas")
        self.botonhome = QtWidgets.QPushButton(self.barra)
        self.botonhome.setGeometry(QtCore.QRect(20, 70, 21, 21))
        self.botonhome.setStyleSheet("border-image: url(imagenes/home.png);")
        self.botonhome.setText("")
        self.botonhome.setObjectName("botonhome")
        self.logo = QtWidgets.QLabel(self.barra)
        self.logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.logo.setStyleSheet("\n"
"border-image: url(imagenes/logoUniConnect.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.Botonsalir = QtWidgets.QPushButton(self.barra)
        self.Botonsalir.setGeometry(QtCore.QRect(15, 240, 31, 31))
        self.Botonsalir.setStyleSheet("border-image: url(imagenes/cross.png);")
        self.Botonsalir.setText("")
        self.Botonsalir.setObjectName("Botonsalir")
        self.barra_arriba = QtWidgets.QWidget(self.widget)
        self.barra_arriba.setGeometry(QtCore.QRect(100, 10, 321, 41))
        self.barra_arriba.setObjectName("barra_arriba")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import res_rc
