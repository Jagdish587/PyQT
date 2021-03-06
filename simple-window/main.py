# This Python file uses the following encoding: utf-8


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Sample App")
        label = QLabel("This is a simple text !")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        button = QPushButton("Press Me!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

