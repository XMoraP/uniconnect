import sys
from PyQt5.QtWidgets import QApplication
from login import Ui_Form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.setupUi(window)
    window.show()
    sys.exit(app.exec_())