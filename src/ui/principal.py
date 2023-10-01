from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(737, 445)
        Form.setStyleSheet("")
        self.backround = QtWidgets.QFrame(Form)
        self.backround.setGeometry(QtCore.QRect(0, 0, 711, 501))
        self.backround.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.backround.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backround.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backround.setObjectName("backround")
        self.logo = QtWidgets.QLabel(self.backround)
        self.logo.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.logo.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.fondoAzul = QtWidgets.QLabel(self.backround)
        self.fondoAzul.setGeometry(QtCore.QRect(40, 80, 621, 391))
        self.fondoAzul.setStyleSheet("border-image: url(:/imagenes/FondoDegradado.png);\n"
"")
        self.fondoAzul.setText("")
        self.fondoAzul.setObjectName("fondoAzul")
        self.labeluniconnect = QtWidgets.QLabel(self.backround)
        self.labeluniconnect.setGeometry(QtCore.QRect(100, 30, 81, 16))
        self.labeluniconnect.setStyleSheet("\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.labeluniconnect.setObjectName("labeluniconnect")
        self.iniciarsesion = QtWidgets.QPushButton(self.backround)
        self.iniciarsesion.setGeometry(QtCore.QRect(550, 30, 101, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/usuario (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iniciarsesion.setIcon(icon)
        self.iniciarsesion.setObjectName("iniciarsesion")
        self.titulo1 = QtWidgets.QLabel(self.backround)
        self.titulo1.setGeometry(QtCore.QRect(190, 110, 331, 31))
        self.titulo1.setStyleSheet("font: 87 8pt \"Neue Haas Grotesk Text Pro Blac\";\n"
"background-color: rgb(243, 242, 247);\n"
"font: 8pt \"Microsoft YaHei UI\";\n"
"\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.titulo1.setObjectName("titulo1")
        self.titulo2 = QtWidgets.QLabel(self.backround)
        self.titulo2.setGeometry(QtCore.QRect(250, 160, 221, 16))
        self.titulo2.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(243, 242, 247);")
        self.titulo2.setObjectName("titulo2")
        self.funcionalidades = QtWidgets.QLabel(self.backround)
        self.funcionalidades.setGeometry(QtCore.QRect(100, 190, 531, 231))
        self.funcionalidades.setStyleSheet("border-image: url(:/imagenes/funcionalidades.png);")
        self.funcionalidades.setText("")
        self.funcionalidades.setObjectName("funcionalidades")
        self.fondoAzul.raise_()
        self.logo.raise_()
        self.labeluniconnect.raise_()
        self.iniciarsesion.raise_()
        self.titulo1.raise_()
        self.titulo2.raise_()
        self.funcionalidades.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labeluniconnect.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">UniConnect</span></p><p><br/></p></body></html>"))
        self.labeluniconnect.setText(_translate("Form", "UniConnect"))
        self.iniciarsesion.setText(_translate("Form", "Iniciar sesión "))
        self.titulo1.setText(_translate("Form", "¡Bienvenid@ a UniConnect!"))
        self.titulo2.setText(_translate("Form", "Comparte tus dudas, resuelve las de otros​"))
