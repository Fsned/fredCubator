from PyQt5.QtGui import QVBoxLayout, QHBoxLayout, QIcon
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton, QWidget, QMainWindow
from PyQt5.QtCore import Qt
import sys
 
 

class inputPostWidget(QWidget):
    def __init__(self, parent=None):
        super(inputPostWidget, self).__init__()

        self.layout = QVBoxLayout()

        self.inputLine = QLineEdit()






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()

        self.inputBoxFrame = QFrame(self)
        self.inputBoxFrame.setStyleSheet("background-color: blue")
        self.inputBoxFrame.resize(800, 60)

        

        self.layout.addWidget(self.inputBoxFrame)

        self.show()
        



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Frame"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:brown')
        hbox = QHBoxLayout()
        btn1 = QPushButton( "Click Me")
        btn1.setStyleSheet("color:white")
        btn1.setStyleSheet("background-color:green")
        frame =QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)
        hbox.addWidget(frame)
        hbox.addWidget(btn1)
        self.setLayout(hbox)
        self.show()
 
 
 
App = QApplication(sys.argv)

mainWindow = MainWindow()

sys.exit(App.exec())
