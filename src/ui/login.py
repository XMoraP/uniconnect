from PyQt5 import QtCore, QtGui, QtWidgets
from ui.register import Ui_containerRegister


class Ui_ContainerLogin(object):
    def setupUi(self, ContainerLogin):
        ContainerLogin.setObjectName("ContainerLogin")
        ContainerLogin.resize(704, 500)
        ContainerLogin.setStyleSheet("")
        self.LoginPrincipal = QtWidgets.QFrame(ContainerLogin)
        self.LoginPrincipal.setGeometry(QtCore.QRect(0, 0, 711, 501))
        self.LoginPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.LoginPrincipal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginPrincipal.setObjectName("LoginPrincipal")
        self.logoSuperior = QtWidgets.QLabel(self.LoginPrincipal)
        self.logoSuperior.setGeometry(QtCore.QRect(20, 10, 51, 51))
        self.logoSuperior.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);")
        self.logoSuperior.setText("")
        self.logoSuperior.setObjectName("logoSuperior")
        self.fondoDegradado = QtWidgets.QLabel(self.LoginPrincipal)
        self.fondoDegradado.setGeometry(QtCore.QRect(40, 90, 621, 391))
        self.fondoDegradado.setStyleSheet("border-image: url(:/imagenes/FondoDegradado.png);\n"
"")
        self.fondoDegradado.setText("")
        self.fondoDegradado.setObjectName("fondoDegradado")
        self.subContainerLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.subContainerLogin.setGeometry(QtCore.QRect(400, 130, 201, 331))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.subContainerLogin.setFont(font)
        self.subContainerLogin.setStyleSheet("\n"
"background-color: rgb(252, 252, 252);\n"
"")
        self.subContainerLogin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.subContainerLogin.setText("")
        self.subContainerLogin.setObjectName("subContainerLogin")
        self.cajaUsuarioLogin = QtWidgets.QLineEdit(self.LoginPrincipal)
        self.cajaUsuarioLogin.setGeometry(QtCore.QRect(430, 260, 141, 21))
        self.cajaUsuarioLogin.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaUsuarioLogin.setObjectName("cajaUsuarioLogin")
        self.personasLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.personasLogin.setGeometry(QtCore.QRect(100, 140, 261, 221))
        self.personasLogin.setStyleSheet("border-image: url(:/imagenes/logoSinFondo.png);\n"
"background-color: transparent;\n"
"")
        self.personasLogin.setText("")
        self.personasLogin.setObjectName("personasLogin")
        self.cajaContrasennaLogin = QtWidgets.QLineEdit(self.LoginPrincipal)
        self.cajaContrasennaLogin.setGeometry(QtCore.QRect(430, 310, 141, 21))
        self.cajaContrasennaLogin.setAcceptDrops(True)
        self.cajaContrasennaLogin.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cajaContrasennaLogin.setObjectName("cajaContrasennaLogin")
        # Set echo mode to Password
        self.cajaContrasennaLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textoLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.textoLogin.setGeometry(QtCore.QRect(430, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.textoLogin.setFont(font)
        self.textoLogin.setStyleSheet("border-color: rgb(52, 136, 196);")
        self.textoLogin.setObjectName("textoLogin")
        self.iconoPersonaLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.iconoPersonaLogin.setGeometry(QtCore.QRect(470, 140, 61, 61))
        self.iconoPersonaLogin.setStyleSheet("border-image: url(:/imagenes/usuario (4).png);")
        self.iconoPersonaLogin.setText("")
        self.iconoPersonaLogin.setObjectName("iconoPersonaLogin")
        self.botonAceptarLogin = QtWidgets.QPushButton(self.LoginPrincipal)
        self.botonAceptarLogin.setGeometry(QtCore.QRect(440, 340, 111, 31))
        self.botonAceptarLogin.setMouseTracking(True)
        self.botonAceptarLogin.setStyleSheet("QPushButton{\n"
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
        self.botonAceptarLogin.setAutoDefault(False)
        self.botonAceptarLogin.setDefault(False)
        self.botonAceptarLogin.setObjectName("botonAceptarLogin")
        self.esloganLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.esloganLogin.setGeometry(QtCore.QRect(80, 350, 311, 16))
        self.esloganLogin.setStyleSheet("font: 75 13pt \"Arial\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.esloganLogin.setObjectName("esloganLogin")
        self.separadorLogin = QtWidgets.QLabel(self.LoginPrincipal)
        self.separadorLogin.setGeometry(QtCore.QRect(450, 380, 91, 21))
        self.separadorLogin.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(44, 102, 164);")
        self.separadorLogin.setObjectName("separadorLogin")
        self.iconoFBLogin = QtWidgets.QPushButton(self.LoginPrincipal)
        self.iconoFBLogin.setGeometry(QtCore.QRect(430, 400, 31, 21))
        self.iconoFBLogin.setStyleSheet("border-image: url(:/imagenes/facebook.png);\n"
"background-color: transparent;")
        self.iconoFBLogin.setText("")
        self.iconoFBLogin.setObjectName("iconoFBLogin")
        self.iconoGoogleLogin = QtWidgets.QPushButton(self.LoginPrincipal)
        self.iconoGoogleLogin.setGeometry(QtCore.QRect(480, 400, 31, 21))
        self.iconoGoogleLogin.setStyleSheet("border-image: url(:/imagenes/google.png);\n"
"background-color: transparent;")
        self.iconoGoogleLogin.setText("")
        self.iconoGoogleLogin.setObjectName("iconoGoogleLogin")
        self.iconoTwitterLogin = QtWidgets.QPushButton(self.LoginPrincipal)
        self.iconoTwitterLogin.setGeometry(QtCore.QRect(530, 400, 31, 21))
        self.iconoTwitterLogin.setStyleSheet("border-image: url(:/imagenes/twitter.png);\n"
"background-color: transparent;")
        self.iconoTwitterLogin.setText("")
        self.iconoTwitterLogin.setObjectName("iconoTwitterLogin")
        self.iconoVolverAtrasLogin = QtWidgets.QPushButton(self.LoginPrincipal)
        self.iconoVolverAtrasLogin.setGeometry(QtCore.QRect(650, 10, 31, 31))
        self.iconoVolverAtrasLogin.setStyleSheet("QPushButton{\n"
"border-image: url(:/imagenes/flecha-hacia-atras (1).png);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(230, 237, 253);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"    ")
        self.iconoVolverAtrasLogin.setText("")
        self.iconoVolverAtrasLogin.setObjectName("iconoVolverAtrasLogin")
        self.textoEnlaceRegistro = QtWidgets.QLabel(self.LoginPrincipal)
        self.textoEnlaceRegistro.setGeometry(QtCore.QRect(405, 438, 121, 20))
        self.textoEnlaceRegistro.setStyleSheet("font: 8pt \"Arial\";\n"
"color: rgb(112, 112, 112);")
        self.textoEnlaceRegistro.setObjectName("textoEnlaceRegistro")
        self.enlaceRegistrate = QtWidgets.QPushButton(self.LoginPrincipal)
        self.enlaceRegistrate.setGeometry(QtCore.QRect(525, 438, 61, 20))
        self.enlaceRegistrate.setStyleSheet("QPushButton{\n"
"    font: 75 8pt \"Arial\";\n"
"    text-decoration: underline;\n"
"    color: rgb(158, 158, 158);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(85, 0, 255);\n"
"}")
        self.enlaceRegistrate.setObjectName("enlaceRegistrate")
        self.fondoDegradado.raise_()
        self.logoSuperior.raise_()
        self.subContainerLogin.raise_()
        self.cajaUsuarioLogin.raise_()
        self.personasLogin.raise_()
        self.cajaContrasennaLogin.raise_()
        self.textoLogin.raise_()
        self.iconoPersonaLogin.raise_()
        self.botonAceptarLogin.raise_()
        self.esloganLogin.raise_()
        self.separadorLogin.raise_()
        self.iconoFBLogin.raise_()
        self.iconoGoogleLogin.raise_()
        self.iconoTwitterLogin.raise_()
        self.iconoVolverAtrasLogin.raise_()
        self.textoEnlaceRegistro.raise_()
        self.enlaceRegistrate.raise_()

        self.retranslateUi(ContainerLogin)
        QtCore.QMetaObject.connectSlotsByName(ContainerLogin)


    def retranslateUi(self, ContainerLogin):
        _translate = QtCore.QCoreApplication.translate
        ContainerLogin.setWindowTitle(_translate("ContainerLogin", "Form"))
        self.cajaUsuarioLogin.setPlaceholderText(_translate("ContainerLogin", "Usuario o email"))
        self.cajaContrasennaLogin.setPlaceholderText(_translate("ContainerLogin", "Contraseña"))
        self.textoLogin.setText(_translate("ContainerLogin", "Iniciar sesión"))
        self.botonAceptarLogin.setText(_translate("ContainerLogin", "Aceptar"))
        self.esloganLogin.setText(_translate("ContainerLogin", "\" Ordena tu mundo, desata tu potencial \""))
        self.separadorLogin.setText(_translate("ContainerLogin", "-------- O -------"))
        self.textoEnlaceRegistro.setText(_translate("ContainerLogin", "¿No tienes una cuenta?"))
        self.enlaceRegistrate.setText(_translate("ContainerLogin", "Registrate"))
