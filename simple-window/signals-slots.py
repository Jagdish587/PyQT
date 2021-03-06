# This Python file uses the following encoding: utf-8


import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,  QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        button.setChecked(self.button_is_checked)
        self.setCentralWidget(button)

    def the_button_was_clicked(self, checked):
        print("checked value ",checked)
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

