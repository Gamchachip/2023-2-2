import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("이름적는거")   
        btn = QPushButton(text="매수", parent=self)
        btn.move(100, 100)
        btn.clicked.connect(self.buy)

    def buy(self):
        print('몽땅 매수')

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()


