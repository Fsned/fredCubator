from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel, QLineEdit, 
QPushButton, QTextEdit, QVBoxLayout, QWidget, QMainWindow, QFrame, QDateEdit, QDoubleSpinBox)
from PyQt5.QtCore import Qt, QRect
import sys

import budgetDB

from datetime import date
 










class inputPostWidget(QWidget): 
  
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.layout.setColumnStretch(1, 3)
  
        self.inputLabel = QLabel("Input Postname")
        self.textbox = QLineEdit() 
        self.layout.addWidget(self.inputLabel, 0,0)
        self.layout.addWidget(self.textbox, 0, 1)

        self.postAmountBox = QLineEdit()
        self.postAmountLabel = QLabel("Post amount")
        self.layout.addWidget(self.postAmountLabel, 1,0)
        self.layout.addWidget(self.postAmountBox, 1, 1)

        self.yearlyTxBox = QLineEdit()
        self.yearlyTxLabel = QLabel("Yearly transactions")
        self.layout.addWidget(self.yearlyTxLabel, 2,0)
        self.layout.addWidget(self.yearlyTxBox, 2, 1)

        self.beginDateBox = QDateEdit(date.today())
        self.beginDateLabel = QLabel("Begin date")
        self.layout.addWidget(self.beginDateLabel, 3,0)
        self.layout.addWidget(self.beginDateBox, 3, 1)

        self.endDateBox = QDateEdit(date.today())
        self.endDateLabel = QLabel("End date")
        self.layout.addWidget(self.endDateLabel, 4,0)
        self.layout.addWidget(self.endDateBox, 4, 1)

        self.addPostButton = QPushButton()
        self.addPostButton.setText("Add post")
        self.addPostButton.clicked.connect(lambda : self.addPost(  self.textbox.text(), 
                                                                   self.postAmountBox.text(),
                                                                   self.yearlyTxBox.text(),
                                                                   self.beginDateBox.text(),
                                                                   self.endDateBox.text()))
        
        self.layout.addWidget(self.addPostButton)
        self.showDBPostsButton = QPushButton()
        self.showDBPostsButton.setText("print DB Entries")
        self.showDBPostsButton.clicked.connect(lambda : self.showDBEntriesClicked())
        self.layout.addWidget(self.showDBPostsButton)
        
        


    def textbox_text_changed(self): 
        self.echo_label.setText(self.textbox.text()) 




    def addPost(self, name, postAmount, yearlyTransactions, beginDate, endDate):
        monthlyAmount = (int(postAmount) * int(yearlyTransactions)) / 12
        todayDate = date.today()
        post = (name, postAmount, monthlyAmount, yearlyTransactions, todayDate, beginDate, endDate)
        postID = budgetDB.createPost(db, post)
        postObject = budgetDB.fetchSpecificPost(db, postID)
        postObject = oldPost(postObject)
        window.addPostToUI(postObject)




    def showDBEntriesClicked(self):
        result = budgetDB.fetchAllPosts(db)
        for a in result:
            print (a)













class oldPost(QWidget): 

    def __init__(self, postObject): 
        super().__init__() 
        
        self.frame = QFrame()
        self.frame.layout = QGridLayout()
        self.frame.setLayout(self.frame.layout)

        if int(postObject['postAmount']) >= 0:
            self.frame.setStyleSheet("background-color: green")
        else:
            self.frame.setStyleSheet("background-color: red")

        self.postObjectsLabels = []

        for enum, a in enumerate(postObject):
            if a == "id" or a == "addedDate":
                continue

            self.postObjectsLabels.append(QLabel(str(a) + '\n' + str(postObject[a])))
            self.postObjectsLabels[-1].setAlignment(Qt.AlignCenter)
            self.frame.layout.addWidget(self.postObjectsLabels[-1], 0, enum)


        self.deleteButton = QPushButton("X")
        self.deleteButton.clicked.connect(lambda : self.deletePost(db, postObject['id']))
        self.frame.layout.addWidget(self.deleteButton, 0, 8)



    def labelClicked(self, text):
        print (text)



    def deletePost(self, database, postID):
        print ("Destroying ID: " + str(postID))
        budgetDB.deletePost(db, str(postID))
        self.setParent(None)
        window.reloadExistingPosts()

















class MainWindow(QMainWindow):
  
    def __init__(self, parent = None): 
        super().__init__(parent) 
        self.init_gui()

    def init_gui(self): 
        self.renderedPosts = []
        self.window = QWidget() 
        self.layout = QGridLayout() 
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

        self.postFrame = QFrame()
        self.postFrame.layout = QVBoxLayout()
        self.postFrame.setLayout(self.postFrame.layout)

        self.inputWidget = inputPostWidget()
        self.layout.addWidget(self.inputWidget)
        self.layout.addWidget(self.postFrame)

        self.reloadExistingPosts()

    def reloadExistingPosts(self):
        for i in reversed(range(self.postFrame.layout.count())): 
            self.postFrame.layout.itemAt(i).widget().setParent(None)

        existingPosts = budgetDB.fetchAllPosts(db)
        for a in existingPosts:
            self.addPostToUI(oldPost(a))

    def addPostToUI(self, postObject):
        self.postFrame.layout.addWidget(postObject.frame)


        
  
if __name__ == '__main__':

    db = budgetDB.initDatabase("budgetDB.db")
    app = QApplication([]) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_()) 
