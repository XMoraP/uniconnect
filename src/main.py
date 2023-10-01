import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.principal import Ui_Form
import ui.imagenes.resources_rc

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
