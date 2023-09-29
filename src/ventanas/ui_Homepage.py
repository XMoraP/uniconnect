# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomepagevOYqUn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(455, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backround = QFrame(self.centralwidget)
        self.backround.setObjectName(u"backround")
        self.backround.setStyleSheet(u"\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.backround.setFrameShape(QFrame.StyledPanel)
        self.backround.setFrameShadow(QFrame.Raised)
        self.Boton2 = QFrame(self.backround)
        self.Boton2.setObjectName(u"Boton2")
        self.Boton2.setGeometry(QRect(280, 20, 48, 44))
        self.Boton2.setFrameShape(QFrame.StyledPanel)
        self.Boton2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Boton2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.Boton2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u"../imagenes/mensajes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.Boton2_2 = QFrame(self.backround)
        self.Boton2_2.setObjectName(u"Boton2_2")
        self.Boton2_2.setGeometry(QRect(327, 20, 61, 44))
        self.Boton2_2.setFrameShape(QFrame.StyledPanel)
        self.Boton2_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Boton2_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.Boton2_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u"../imagenes/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.backround)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 41, 21))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../imagenes/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.frame = QFrame(self.backround)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 20, 48, 44))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u"../imagenes/ajustes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.frame_2 = QFrame(self.backround)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 101, 151))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.backround)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

