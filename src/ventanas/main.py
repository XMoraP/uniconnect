import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from ui_homepage import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        # Connect signals and slots here if needed

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

