import sys
import os
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from py_toggle import PyToggle

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #resixe window
        self.resize(500, 500)

        #Create Container and Layout
        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222 }")
        self.layout = QVBoxLayout()

        self.toggle = PyToggle(animation_curve=QEasingCurve.OutBounce)


        self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)


        #Set general widget
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        #Show Window
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
