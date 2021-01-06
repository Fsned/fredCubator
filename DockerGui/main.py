#TestingStuffOut
import sys, os
import pathlib

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt5.QtCore import QSize    



class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        gridLayout = QGridLayout(self)

        self.uiComponents()
        
        #gridLayout.addWidget(self.productTitle, row = 0, column = 0)
        #gridLayout.addWidget(self.productComboBox, row = 0, column = 1)
#
        #gridLayout.addWidget(self.softwareVersionTitle, row = 1, column = 0)
        #gridLayout.addWidget(self.softwareVersionComboBox, row = 1, column = 1)
        centralWidget.setLayout(gridLayout) 
        

        self.show() 

    def uiComponents(self):

        possibleProducts = ["MiR100",
                            "MiR200",
                            "MiR250",
                            "MiR500",
                            "MiR1000",
                            "Fleet"]
                        
        self.productTitle = QLabel("Product", self)
        self.productTitle.setGeometry(200, 80, 225, 20)

        self.softwareVersionTitle = QLabel("Software version", self)
        self.softwareVersionTitle.setGeometry(200, 110, 225, 20)

        self.productComboBox = QComboBox(self)
        self.productComboBox.setGeometry(200, 100, 225, 30)
        self.productComboBox.addItems(possibleProducts)

        self.softwareVersionComboBox = QComboBox(self)
        self.softwareVersionComboBox.setGeometry(200, 150, 225, 30)

        # Populate combobox with files existing in the ~/Desktop/SW/3.CleanSimulators/-dir
        with os.scandir("/home/fsn/Desktop/SW/3.CleanSimulators/") as filesInSWDir:
            for entry in filesInSWDir:
                if entry.is_file() and ".mir" in entry.name :
                    self.softwareVersionComboBox.addItem(entry.name)

        #self.productTitle.setGeometry(200, 130, 225, 20)
        
        

        







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()

    sys.exit( app.exec_() )