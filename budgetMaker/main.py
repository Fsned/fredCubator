from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, 
QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, 
QTextEdit, QVBoxLayout, QWidget, QMainWindow, QFrame)
from PyQt5.QtCore import Qt
import sys

import budgetDB
 
 

class inputPostWidget(QWidget):
    def __init__(self, parent=None):
        super(inputPostWidget, self).__init__()

        self.layout = QVBoxLayout()
        self.inputLine = QLineEdit()
        self.layout.addWidget(self.inputLine)
        self.inputLine.setAlignment(Qt.AlignCenter)
        self.inputLine.setStyleSheet("background-color: green")

        #self.layout.show()








class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(85, 87, 83)")
        self.resize(550, 650)
        self.layout = QHBoxLayout()

        self.inputBoxFrame = QFrame(self)
        self.inputBoxFrame.setStyleSheet("background-color: white")
        self.inputBoxFrame.resize(550, 50)
        
        self.inputWidget = inputPostWidget(parent=self.inputBoxFrame)

        self.layout.addWidget(self.inputBoxFrame)
        self.layout.addWidget(self.inputWidget)
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
