from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_containerRegister(object):
    def setupUi(self, containerRegister):
        containerRegister.setObjectName("containerRegister")
        containerRegister.resize(707, 500)
        containerRegister.setStyleSheet("")
        self.principalRegister = QtWidgets.QFrame(containerRegister)
        self.principalRegister.setGeometry(QtCore.QRect(0, 0, 711, 501))
        self.principalRegister.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.principalRegister.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principalRegister.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principalRegister.setObjectName("principalRegister")
        self.logoRegister = QtWidgets.QLabel(self.principalRegister)
        self.logoRegister.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.logoRegister.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);")
        self.logoRegister.setText("")
        self.logoRegister.setObjectName("logoRegister")
        self.fondoAzulRegister = QtWidgets.QLabel(self.principalRegister)
        self.fondoAzulRegister.setGeometry(QtCore.QRect(40, 90, 621, 391))
        self.fondoAzulRegister.setStyleSheet("border-image: url(:/imagenes/FondoDegradado.png);\n"
"")
        self.fondoAzulRegister.setText("")
        self.fondoAzulRegister.setObjectName("fondoAzulRegister")
        self.cuadroPequennoRegistro = QtWidgets.QLabel(self.principalRegister)
        self.cuadroPequennoRegistro.setGeometry(QtCore.QRect(400, 120, 221, 341))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cuadroPequennoRegistro.setFont(font)
        self.cuadroPequennoRegistro.setStyleSheet("\n"
"background-color: rgb(252, 252, 252);\n"
"")
        self.cuadroPequennoRegistro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cuadroPequennoRegistro.setText("")
        self.cuadroPequennoRegistro.setObjectName("cuadroPequennoRegistro")
        self.cajaEmailRegister = QtWidgets.QLineEdit(self.principalRegister)
        self.cajaEmailRegister.setGeometry(QtCore.QRect(440, 220, 141, 21))
        self.cajaEmailRegister.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaEmailRegister.setObjectName("cajaEmailRegister")
        self.dibujoPersonasRegister = QtWidgets.QLabel(self.principalRegister)
        self.dibujoPersonasRegister.setGeometry(QtCore.QRect(100, 140, 261, 221))
        self.dibujoPersonasRegister.setStyleSheet("border-image: url(:/imagenes/logoSinFondo.png);\n"
"background-color: transparent;\n"
"")
        self.dibujoPersonasRegister.setText("")
        self.dibujoPersonasRegister.setObjectName("dibujoPersonasRegister")
        self.cajaContrasennaRegister = QtWidgets.QLineEdit(self.principalRegister)
        self.cajaContrasennaRegister.setGeometry(QtCore.QRect(440, 300, 141, 21))
        self.cajaContrasennaRegister.setAcceptDrops(True)
        self.cajaContrasennaRegister.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaContrasennaRegister.setObjectName("cajaContrasennaRegister")
        # set password to echo mode
        self.cajaContrasennaRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textoRegister = QtWidgets.QLabel(self.principalRegister)
        self.textoRegister.setGeometry(QtCore.QRect(450, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textoRegister.setFont(font)
        self.textoRegister.setStyleSheet("border-color: rgb(52, 136, 196);")
        self.textoRegister.setObjectName("textoRegister")
        self.iconoRegister = QtWidgets.QLabel(self.principalRegister)
        self.iconoRegister.setGeometry(QtCore.QRect(480, 120, 61, 61))
        self.iconoRegister.setStyleSheet("border-image: url(:/imagenes/agregar-usuario.png);")
        self.iconoRegister.setText("")
        self.iconoRegister.setObjectName("iconoRegister")
        self.botonAceptarRegister = QtWidgets.QPushButton(self.principalRegister)
        self.botonAceptarRegister.setGeometry(QtCore.QRect(450, 390, 111, 31))
        self.botonAceptarRegister.setMouseTracking(True)
        self.botonAceptarRegister.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(132, 205, 255, 255), stop:1 rgba(85, 74, 208, 255));\n"
"font: 75 9pt \"Arial\";\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgb(60, 193, 231);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"    \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.botonAceptarRegister.setAutoDefault(False)
        self.botonAceptarRegister.setDefault(False)
        self.botonAceptarRegister.setObjectName("botonAceptarRegister")
        self.esloganRegister = QtWidgets.QLabel(self.principalRegister)
        self.esloganRegister.setGeometry(QtCore.QRect(80, 350, 311, 16))
        self.esloganRegister.setStyleSheet("font: 75 13pt \"Arial\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.esloganRegister.setObjectName("esloganRegister")
        self.iconoVolverAtrasRegister = QtWidgets.QPushButton(self.principalRegister)
        self.iconoVolverAtrasRegister.setGeometry(QtCore.QRect(650, 10, 31, 31))
        self.iconoVolverAtrasRegister.setStyleSheet("QPushButton{\n"
"    border-image: url(:/imagenes/flecha-hacia-atras (1).png);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(230, 237, 253);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"    ")
        self.iconoVolverAtrasRegister.setText("")
        self.iconoVolverAtrasRegister.setObjectName("iconoVolverAtrasRegister")
        self.cajaUsuarioRegister = QtWidgets.QLineEdit(self.principalRegister)
        self.cajaUsuarioRegister.setGeometry(QtCore.QRect(440, 260, 141, 21))
        self.cajaUsuarioRegister.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaUsuarioRegister.setObjectName("cajaUsuarioRegister")
        self.cajaContrasenna2Register = QtWidgets.QLineEdit(self.principalRegister)
        self.cajaContrasenna2Register.setGeometry(QtCore.QRect(440, 340, 141, 21))
        self.cajaContrasenna2Register.setAcceptDrops(True)
        self.cajaContrasenna2Register.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaContrasenna2Register.setObjectName("cajaContrasenna2Register")
        # set password to echo mode
        self.cajaContrasenna2Register.setEchoMode(QtWidgets.QLineEdit.Password)
        self.termsCondicRegister = QtWidgets.QCheckBox(self.principalRegister)
        self.termsCondicRegister.setGeometry(QtCore.QRect(420, 370, 191, 18))
        self.termsCondicRegister.setStyleSheet("font: 75 8pt \"Arial\";\n"
"color: rgb(126, 126, 126);")
        self.termsCondicRegister.setObjectName("termsCondicRegister")
        self.enlaceInicioSesionRegister = QtWidgets.QLabel(self.principalRegister)
        self.enlaceInicioSesionRegister.setGeometry(QtCore.QRect(420, 440, 121, 16))
        self.enlaceInicioSesionRegister.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(141, 141, 141);")
        self.enlaceInicioSesionRegister.setObjectName("enlaceInicioSesionRegister")
        self.linkInicioSesionRegister = QtWidgets.QPushButton(self.principalRegister)
        self.linkInicioSesionRegister.setGeometry(QtCore.QRect(540, 437, 75, 23))
        self.linkInicioSesionRegister.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"Arial\";\n"
"text-decoration: underline;\n"
"color: rgb(130, 130, 130);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(85, 0, 255);\n"
"}")
        self.linkInicioSesionRegister.setObjectName("linkInicioSesionRegister")
        self.fondoAzulRegister.raise_()
        self.logoRegister.raise_()
        self.cuadroPequennoRegistro.raise_()
        self.cajaEmailRegister.raise_()
        self.dibujoPersonasRegister.raise_()
        self.cajaContrasennaRegister.raise_()
        self.textoRegister.raise_()
        self.iconoRegister.raise_()
        self.botonAceptarRegister.raise_()
        self.esloganRegister.raise_()
        self.iconoVolverAtrasRegister.raise_()
        self.cajaUsuarioRegister.raise_()
        self.cajaContrasenna2Register.raise_()
        self.termsCondicRegister.raise_()
        self.enlaceInicioSesionRegister.raise_()
        self.linkInicioSesionRegister.raise_()

        self.retranslateUi(containerRegister)
        QtCore.QMetaObject.connectSlotsByName(containerRegister)

    def retranslateUi(self, containerRegister):
        _translate = QtCore.QCoreApplication.translate
        containerRegister.setWindowTitle(_translate("containerRegister", "Form"))
        self.cajaEmailRegister.setPlaceholderText(_translate("containerRegister", "Email"))
        self.cajaContrasennaRegister.setPlaceholderText(_translate("containerRegister", "Contraseña"))
        self.textoRegister.setText(_translate("containerRegister", "Registrarse"))
        self.botonAceptarRegister.setText(_translate("containerRegister", "Aceptar"))
        self.esloganRegister.setText(_translate("containerRegister", "\" Ordena tu mundo, desata tu potencial \""))
        self.cajaUsuarioRegister.setPlaceholderText(_translate("containerRegister", "Nombre de usuario"))
        self.cajaContrasenna2Register.setPlaceholderText(_translate("containerRegister", "Confirmar contraseña"))
        self.termsCondicRegister.setText(_translate("containerRegister", "Acepto los términos y condiciones"))
        self.enlaceInicioSesionRegister.setText(_translate("containerRegister", "¿Ya tienes una cuenta?"))
        self.linkInicioSesionRegister.setText(_translate("containerRegister", "Iniciar sesión"))
