from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QWidget, QMainWindow, QFrame)

from PyQt5.QtCore import Qt

import sqlite3
from sqlite3 import Error

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
 
 
 
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def startDb(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or Nonedatabase
    """

    # Create connection to a file, if it exists.
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # Create a table for incomes if it doesn't exist
    sql_create_incomePosts_table = """ CREATE TABLE IF NOT EXISTS income_posts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        post_amount,
                                        monthly_amount,
                                        yearly_transactions,
                                        added_date text,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_expensePosts_table = """ CREATE TABLE IF NOT EXISTS expense_posts (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        post_amount,
                                        monthly_amount,
                                        yearly_transactions,
                                        added_date text,
                                        begin_date text,
                                        end_date text
                                    ); """         

    create_table(conn, sql_create_incomePosts_table)
    create_table(conn, sql_create_expensePosts_table)


    return conn





db = startDb("budgetDatabase.db")



App = QApplication(sys.argv)

mainWindow = MainWindow()

sys.exit(App.exec())
