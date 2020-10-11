# This Python file uses the following encoding: utf-8


import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()

        widgets = [QCheckBox,
        QComboBox,
        QDateEdit,
        QDateTimeEdit,
        QDial,
        QDoubleSpinBox,
        QFontComboBox,
        QLCDNumber,
        QLabel,
        QLineEdit,
        QProgressBar,
        QPushButton,
        QRadioButton,
        QSlider,
        QSpinBox,
        QTimeEdit]

        for w in widgets:
            layout.addWidget(w())


            widget = QWidget()
            widget.setLayout(layout)

            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

