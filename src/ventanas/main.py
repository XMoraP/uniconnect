import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_ContainerLogin

class ContainerLogin(QMainWindow, Ui_ContainerLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContainerLogin()
    window.show()
    sys.exit(app.exec_())
