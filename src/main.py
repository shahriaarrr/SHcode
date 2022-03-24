from PyQt5.QtWidgets import *
from PyQt5 import uic

class GmailSender(QMainWindow):
    def __init__(self):
        super(GmailSender, self).__init__()
        uic.loadUi('SHcode.ui', self)
        self.show()

def main():
    app = QApplication([])
    window = GmailSender()
    app.exec_()

if __name__ == '__main__':
    main()