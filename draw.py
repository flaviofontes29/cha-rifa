from desing import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import random


class Draw(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.button_drawn_number.clicked.connect(self.drawn_number)

    def drawn_number(self):
        number = random.randint(1, 100)
        self.Label_drawn_number.setText(str(number))


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    draw = Draw()
    draw.show()
    qt.exec()

