import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from ui.principal import Ui_Form
from ui.login import Ui_ContainerLogin
from ui.register import Ui_containerRegister
import ui.imagenes.resources_rc

class LoginWindow(QMainWindow, Ui_ContainerLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.iniciarsesion.clicked.connect(self.open_login_window)

    def open_login_window(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
