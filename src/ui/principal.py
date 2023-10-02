from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(900, 600)
        main.setStyleSheet("")
        self.mainFrame = QtWidgets.QFrame(main)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.logoLabel = QtWidgets.QLabel(self.mainFrame)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.logoLabel.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.backgroundLabel = QtWidgets.QLabel(self.mainFrame)
        self.backgroundLabel.setGeometry(QtCore.QRect(70, 90, 781, 481))
        self.backgroundLabel.setStyleSheet("border-image: url(:/imagenes/FondoDegradado.png);\n"
"")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.uniConnectLabel = QtWidgets.QLabel(self.mainFrame)
        self.uniConnectLabel.setGeometry(QtCore.QRect(100, 30, 131, 21))
        self.uniConnectLabel.setStyleSheet("font: 75 18pt \"Arial\";\n"
"\n"
"")
        self.uniConnectLabel.setObjectName("uniConnectLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.mainFrame)
        self.welcomeLabel.setGeometry(QtCore.QRect(280, 110, 331, 31))
        self.welcomeLabel.setStyleSheet("font: 87 8pt \"Neue Haas Grotesk Text Pro Blac\";\n"
"background-color: rgb(243, 242, 247);\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"font: 75 20pt \"Arial\";")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.slangLabel = QtWidgets.QLabel(self.mainFrame)
        self.slangLabel.setGeometry(QtCore.QRect(300, 150, 291, 16))
        self.slangLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Arial\";\n"
"background-color: transparent;")
        self.slangLabel.setObjectName("slangLabel")
        self.informationLabel = QtWidgets.QLabel(self.mainFrame)
        self.informationLabel.setGeometry(QtCore.QRect(180, 220, 571, 261))
        self.informationLabel.setStyleSheet("border-image: url(:/imagenes/funcionalidades.png);\n"
"border-radius: 25px;")
        self.informationLabel.setText("")
        self.informationLabel.setObjectName("informationLabel")
        self.loginButton = QtWidgets.QPushButton(self.mainFrame)
        self.loginButton.setGeometry(QtCore.QRect(740, 30, 121, 31))
        self.loginButton.setMouseTracking(True)
        self.loginButton.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(132, 205, 255, 255), stop:1 rgba(85, 74, 208, 255));\n"
"font: 75 9pt \"Arial\";\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(60, 193, 231);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.backgroundLabel.raise_()
        self.logoLabel.raise_()
        self.uniConnectLabel.raise_()
        self.welcomeLabel.raise_()
        self.slangLabel.raise_()
        self.informationLabel.raise_()
        self.loginButton.raise_()

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.uniConnectLabel.setToolTip(_translate("main", "<html><head/><body><p><span style=\" font-weight:600;\">UniConnect</span></p><p><br/></p></body></html>"))
        self.uniConnectLabel.setText(_translate("main", "UniConnect"))
        self.welcomeLabel.setText(_translate("main", "¡Bienvenid@ a UniConnect!"))
        self.slangLabel.setText(_translate("main", "\"Comparte tus dudas, resuelve las de otros​\""))
        self.loginButton.setText(_translate("main", "Iniciar sesión"))
