from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, 
QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, 
QTextEdit, QVBoxLayout, QWidget, QMainWindow, QFrame, QDateEdit)
from PyQt5.QtCore import Qt, QRect
import sys

import budgetDB

from datetime import datetime, date
 





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

        self.beginDateBox = QDateEdit()
        self.beginDateLabel = QLabel("Begin date")
        self.layout.addWidget(self.beginDateLabel, 3,0)
        self.layout.addWidget(self.beginDateBox, 3, 1)

        self.endDateBox = QDateEdit()
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
        self.showDBPostsButton.clicked.connect(lambda : self.clicked())
        self.layout.addWidget(self.showDBPostsButton)
        
        
    def textbox_text_changed(self): 
        self.echo_label.setText(self.textbox.text()) 

    def addPost(self, name, postAmount, yearlyTransactions, beginDate, endDate):
        
        if int(postAmount) >= 0:
            table = "income_posts"
        else:
            table = "expense_posts"

        monthlyAmount = int(postAmount) * int(yearlyTransactions) / 12
        
        
        endDate == ""

        todayDate = datetime.now()
        todayDate = date.today()

        post = (name, postAmount, monthlyAmount, yearlyTransactions, todayDate, beginDate, endDate)
        postID = budgetDB.createPost(db, table, post)



    def clicked(self):
        
        result = budgetDB.fetchAllPosts(db, "income_posts")
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
            if a == "id":
                continue

            self.postObjectsLabels.append(QLabel(str(a) + '\n' + str(postObject[a])))
            self.frame.layout.addWidget(self.postObjectsLabels[-1], 0, enum)
        

        self.deleteButton = QPushButton("Delete post")
        self.deleteButton.clicked.connect(lambda : self.deletePost(db, postObject['id']))
        self.frame.layout.addWidget(self.deleteButton, 0, 8)


        window.addPostToUI(self)






    def labelClicked(self, text):
        print (text)

    def deletePost(self, database, postID):
        print ("Destroying ID: " + str(postID))
        budgetDB.deletePost(db, "income_posts", str(postID))
        self.frame.destroy()

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

        self.inputWidget = inputPostWidget()
        self.layout.addWidget(self.inputWidget)
        self.loadExistingPosts()

    def loadExistingPosts(self):

        # Get all existing posts from database in a niceself.layout.addWidget((oldPost(a)).frame) format
        existingPosts = budgetDB.fetchAllPosts(db, "income_posts")
        # destroy existing 'old posts' from the ui
        #eh?

        # call the oldPost(postObject) on all db posts, and add it to the layout
        for a in existingPosts:
            #self.renderedPosts.append(oldPost(a))
            #self.layout.addWidget
            self.layout.addWidget((oldPost(a)).frame)

    def addPostToUI(self, postObject):
        self.layout.addWidget(postObject.frame)


        
  
if __name__ == '__main__':

    db = budgetDB.initDatabase("budgetDB.db")

    app = QApplication([]) 
  
    window = MainWindow() 
    window.show() 
  
    sys.exit(app.exec_()) 
