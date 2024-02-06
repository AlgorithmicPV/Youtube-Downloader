import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow  # Import the generated UI class

class MyApplication(QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()

        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals and slots, add application logic here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())