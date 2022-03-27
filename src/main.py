from PyQt5.QtWidgets import *
from PyQt5 import uic

class SHcode(QMainWindow):
    def __init__(self):
        super(SHcode, self).__init__()
        uic.loadUi('SHcode.ui', self)
        self.show()

        self.setWindowTitle("SHcode")

def main():
    app = QApplication([])
    window = SHcode()
    app.exec_()

if __name__ == '__main__':
    main()
