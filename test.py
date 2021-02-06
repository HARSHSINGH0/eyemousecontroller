from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,1366,768)
        self.setWindowTitle("Eye Mouse Handler")
        self.initUI()
    def initUI(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(200,200)
        

        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()
    def update(self):
        self.label.adjustSize()
def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    
    
    win.show()
    sys.exit(app.exec_())
window()