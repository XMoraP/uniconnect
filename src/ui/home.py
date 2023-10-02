from PyQt5 import QtCore, QtGui, QtWidgets
import ui.imagenes.resorces_rc


class Ui_ContainerHome(object):
    def setupUi(self, ContainerHome):
        ContainerHome.setObjectName("ContainerHome")
        ContainerHome.resize(1002, 616)
        ContainerHome.setStyleSheet("\"\"")
        self.frameHome = QtWidgets.QFrame(ContainerHome)
        self.frameHome.setGeometry(QtCore.QRect(0, 0, 1011, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHome.sizePolicy().hasHeightForWidth())
        self.frameHome.setSizePolicy(sizePolicy)
        self.frameHome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameHome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHome.setObjectName("frameHome")
        self.bar = QtWidgets.QWidget(self.frameHome)
        self.bar.setGeometry(QtCore.QRect(0, 0, 61, 621))
        self.bar.setStyleSheet("background-color: rgb(249, 235, 211);")
        self.bar.setObjectName("bar")
        self.userButton = QtWidgets.QPushButton(self.bar)
        self.userButton.setGeometry(QtCore.QRect(20, 110, 24, 24))
        self.userButton.setMaximumSize(QtCore.QSize(200, 100))
        self.userButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/imagenes/home.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.userButton.setObjectName("userButton")
        self.subjectsButton = QtWidgets.QPushButton(self.bar)
        self.subjectsButton.setGeometry(QtCore.QRect(20, 150, 24, 24))
        self.subjectsButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/imagenes/open-book.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.subjectsButton.setObjectName("subjectsButton")
        self.homeButton = QtWidgets.QPushButton(self.bar)
        self.homeButton.setGeometry(QtCore.QRect(20, 70, 24, 24))
        self.homeButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/imagenes/usuario (4).png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.homeButton.setObjectName("homeButton")
        self.logoLabel = QtWidgets.QLabel(self.bar)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.logoLabel.setStyleSheet("border-image: url(:/imagenes/logoUniConnect.png);")
        self.logoLabel.setObjectName("logoLabel")
        self.exitButton = QtWidgets.QPushButton(self.bar)
        self.exitButton.setGeometry(QtCore.QRect(10, 570, 31, 31))
        self.exitButton.setStyleSheet("QPushButton{\n"
"border-image: url(:/imagenes/cross.png);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frameHome)
        self.calendarWidget.setGeometry(QtCore.QRect(170, 210, 421, 231))
        self.calendarWidget.setStyleSheet("font: 10pt;\n"
"color: rgb(44, 188, 230);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.listView = QtWidgets.QListView(self.frameHome)
        self.listView.setGeometry(QtCore.QRect(650, 240, 311, 192))
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.saveButton = QtWidgets.QPushButton(self.frameHome)
        self.saveButton.setGeometry(QtCore.QRect(730, 450, 151, 21))
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
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(60, 193, 231);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.addTaskButton = QtWidgets.QPushButton(self.frameHome)
        self.addTaskButton.setGeometry(QtCore.QRect(850, 200, 111, 21))
        self.addTaskButton.setMouseTracking(True)
        self.addTaskButton.setStyleSheet("QPushButton{\n"
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
        self.addTaskButton.setObjectName("addTaskButton")
        self.barLabel = QtWidgets.QLabel(self.frameHome)
        self.barLabel.setGeometry(QtCore.QRect(60, 80, 941, 51))
        self.barLabel.setStyleSheet("border-image: url(:/imagenes/FondoDegradado.png);\n"
"font: 75 18pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.barLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.barLabel.setObjectName("barLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.frameHome)
        self.welcomeLabel.setGeometry(QtCore.QRect(80, 20, 141, 31))
        self.welcomeLabel.setStyleSheet("font: 75 20pt \"Arial\";\n"
"color: rgb(45, 33, 173);")
        self.welcomeLabel.setObjectName("welcomeLabel")

        self.retranslateUi(ContainerHome)
        QtCore.QMetaObject.connectSlotsByName(ContainerHome)

    def retranslateUi(self, ContainerHome):
        _translate = QtCore.QCoreApplication.translate
        self.saveButton.setText(_translate("ContainerHome", "Guardar"))
        self.addTaskButton.setText(_translate("ContainerHome", "Agregar tarea"))
        self.barLabel.setText(_translate("ContainerHome", "Calendario de tareas"))
        self.welcomeLabel.setText(_translate("ContainerHome", "Bienvenido"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContainerHome = QtWidgets.QWidget()
    ui = Ui_ContainerHome()
    ui.setupUi(ContainerHome)
    ContainerHome.show()
    sys.exit(app.exec_()) """