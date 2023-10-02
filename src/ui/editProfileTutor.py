from PyQt5 import QtCore, QtGui, QtWidgets
import ui.imagenes.resorces_rc


class Ui_containerEditProfileTutor(object):
    def setupUi(self, containerEditProfileTutor):
        containerEditProfileTutor.setObjectName("containerEditProfileTutor")
        containerEditProfileTutor.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(containerEditProfileTutor.sizePolicy().hasHeightForWidth())
        containerEditProfileTutor.setSizePolicy(sizePolicy)
        containerEditProfileTutor.setStyleSheet("")
        self.editProfileTutorFrame = QtWidgets.QFrame(containerEditProfileTutor)
        self.editProfileTutorFrame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.editProfileTutorFrame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.editProfileTutorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.editProfileTutorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.editProfileTutorFrame.setObjectName("editProfileTutorFrame")
        self.bar = QtWidgets.QWidget(self.editProfileTutorFrame)
        self.bar.setGeometry(QtCore.QRect(0, 0, 61, 601))
        self.bar.setStyleSheet("background-color: rgb(249, 235, 211);\n"
"\n"
"\n"
"")
        self.bar.setObjectName("bar")
        self.homeButton = QtWidgets.QPushButton(self.bar)
        self.homeButton.setGeometry(QtCore.QRect(20, 110, 24, 24))
        self.homeButton.setMaximumSize(QtCore.QSize(200, 100))
        self.homeButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/imagenes/home.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.homeButton.setText("")
        self.homeButton.setIconSize(QtCore.QSize(10, 5))
        self.homeButton.setObjectName("homeButton")
        self.subjectsButton = QtWidgets.QPushButton(self.bar)
        self.subjectsButton.setGeometry(QtCore.QRect(20, 150, 24, 24))
        self.subjectsButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/imagenes/open-book.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.subjectsButton.setText("")
        self.subjectsButton.setObjectName("subjectsButton")
        self.userButton = QtWidgets.QPushButton(self.bar)
        self.userButton.setGeometry(QtCore.QRect(20, 70, 24, 24))
        self.userButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/imagenes/usuario (4).png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.userButton.setText("")
        self.userButton.setObjectName("userButton")
        self.logoLabel = QtWidgets.QLabel(self.bar)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.logoLabel.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.exitButton = QtWidgets.QPushButton(self.bar)
        self.exitButton.setGeometry(QtCore.QRect(10, 560, 31, 31))
        self.exitButton.setStyleSheet("QPushButton{\n"
"  \n"
"    border-image: url(:/imagenes/cross.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.editProfileLabel = QtWidgets.QLabel(self.editProfileTutorFrame)
        self.editProfileLabel.setGeometry(QtCore.QRect(100, 20, 191, 41))
        self.editProfileLabel.setStyleSheet("font: 75 18pt \"Arial\";\n"
"color: rgb(44, 32, 172);")
        self.editProfileLabel.setObjectName("editProfileLabel")
        self.emailBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.emailBox.setGeometry(QtCore.QRect(120, 300, 141, 21))
        self.emailBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.emailBox.setObjectName("emailBox")
        self.gradeBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.gradeBox.setGeometry(QtCore.QRect(320, 300, 141, 21))
        self.gradeBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.gradeBox.setObjectName("gradeBox")
        self.nameBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.nameBox.setGeometry(QtCore.QRect(120, 250, 141, 21))
        self.nameBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.nameBox.setObjectName("nameBox")
        self.passwordBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.passwordBox.setGeometry(QtCore.QRect(120, 360, 141, 21))
        self.passwordBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.passwordBox.setObjectName("passwordBox")
        self.lastNameBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.lastNameBox.setGeometry(QtCore.QRect(320, 250, 141, 21))
        self.lastNameBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lastNameBox.setObjectName("lastNameBox")
        self.cameraLabel = QtWidgets.QLabel(self.editProfileTutorFrame)
        self.cameraLabel.setGeometry(QtCore.QRect(140, 90, 91, 81))
        self.cameraLabel.setStyleSheet("border-image: url(:/imagenes/camara.png);")
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.addPhotoButton = QtWidgets.QPushButton(self.editProfileTutorFrame)
        self.addPhotoButton.setGeometry(QtCore.QRect(290, 120, 101, 21))
        self.addPhotoButton.setMouseTracking(True)
        self.addPhotoButton.setStyleSheet("QPushButton{\n"
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
        self.addPhotoButton.setAutoDefault(False)
        self.addPhotoButton.setDefault(False)
        self.addPhotoButton.setObjectName("addPhotoButton")
        self.saveButton = QtWidgets.QPushButton(self.editProfileTutorFrame)
        self.saveButton.setGeometry(QtCore.QRect(650, 460, 111, 31))
        self.saveButton.setMouseTracking(True)
        self.saveButton.setStyleSheet("QPushButton{\n"
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
        self.saveButton.setAutoDefault(False)
        self.saveButton.setDefault(False)
        self.saveButton.setObjectName("saveButton")
        self.confirmPasswordBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.confirmPasswordBox.setGeometry(QtCore.QRect(320, 360, 141, 21))
        self.confirmPasswordBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.confirmPasswordBox.setText("")
        self.confirmPasswordBox.setObjectName("confirmPasswordBox")
        self.updateDataLabel = QtWidgets.QLabel(self.editProfileTutorFrame)
        self.updateDataLabel.setGeometry(QtCore.QRect(120, 190, 151, 41))
        self.updateDataLabel.setStyleSheet("font: 75 13pt \"Arial\";")
        self.updateDataLabel.setObjectName("updateDataLabel")
        self.dataBox = QtWidgets.QLabel(self.editProfileTutorFrame)
        self.dataBox.setGeometry(QtCore.QRect(590, 140, 231, 291))
        self.dataBox.setStyleSheet("background-color: rgb(197, 245, 255);\n"
"border-bottom-color: rgb(45, 33, 173);\n"
"gridline-color: rgb(44, 32, 172);\n"
"border-radius: 30px;")
        self.dataBox.setText("")
        self.dataBox.setObjectName("dataBox")
        self.currentDataLabel = QtWidgets.QLabel(self.editProfileTutorFrame)
        self.currentDataLabel.setGeometry(QtCore.QRect(640, 100, 121, 41))
        self.currentDataLabel.setStyleSheet("font: 75 13pt \"Arial\";\n"
"background-color: transparent;")
        self.currentDataLabel.setObjectName("currentDataLabel")
        self.subjectsBox = QtWidgets.QLineEdit(self.editProfileTutorFrame)
        self.subjectsBox.setGeometry(QtCore.QRect(120, 420, 141, 21))
        self.subjectsBox.setStyleSheet("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.subjectsBox.setObjectName("subjectsBox")

        self.retranslateUi(containerEditProfileTutor)
        QtCore.QMetaObject.connectSlotsByName(containerEditProfileTutor)

    def retranslateUi(self, containerEditProfileTutor):
        _translate = QtCore.QCoreApplication.translate
        containerEditProfileTutor.setWindowTitle(_translate("containerEditProfileTutor", "Form"))
        self.editProfileLabel.setText(_translate("containerEditProfileTutor", "Editar perfil Tutor"))
        self.emailBox.setPlaceholderText(_translate("containerEditProfileTutor", "email"))
        self.gradeBox.setPlaceholderText(_translate("containerEditProfileTutor", "Grado"))
        self.nameBox.setPlaceholderText(_translate("containerEditProfileTutor", "Nombre de usuario"))
        self.passwordBox.setPlaceholderText(_translate("containerEditProfileTutor", "Contraseña"))
        self.lastNameBox.setPlaceholderText(_translate("containerEditProfileTutor", "Apellido"))
        self.addPhotoButton.setText(_translate("containerEditProfileTutor", "Agregar foto"))
        self.saveButton.setText(_translate("containerEditProfileTutor", "Guardar"))
        self.confirmPasswordBox.setPlaceholderText(_translate("containerEditProfileTutor", "Confirmar contraseña"))
        self.updateDataLabel.setText(_translate("containerEditProfileTutor", "Actualizar datos"))
        self.currentDataLabel.setText(_translate("containerEditProfileTutor", "Datos actuales"))
        self.subjectsBox.setPlaceholderText(_translate("containerEditProfileTutor", "Asignaturas"))
