import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.principal import Ui_Form
from ui.login import Ui_ContainerLogin
from ui.register import Ui_containerRegister
import ui.imagenes.resorces_rc

class RegisterWindow(QMainWindow, Ui_containerRegister):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class LoginWindow(QMainWindow, Ui_ContainerLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the "Registrate" button's click event to open the registration window and close the login window
        self.enlaceRegistrate.clicked.connect(self.open_register_window)

    def open_register_window(self):
        self.close()  # Close the login window
        self.register_window = RegisterWindow()
        self.register_window.show()  # Show the registration window

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
