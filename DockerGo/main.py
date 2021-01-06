from tkinter import *
from tkinter import ttk
import random

mainWindow = Tk()

mainWindow.geometry('400x600')
mainWindow.title('MegaUltimateSuperSim V0.1')


menubar = Menu(mainWindow)
productString = StringVar()
versionString = StringVar()





def newProductWindow():

    topWindow = Toplevel(mainWindow)
    topWindow.geometry('305x105')

    newSimFrame = LabelFrame(topWindow, text = 'Setup new simulator')
    newSimFrame.grid(row = 0, column = 0)


    startSimButton = Button(newSimFrame, text = 'Start simulator', command = lambda : startSim())
    startSimButton.grid(row = 3, column = 0, columnspan = 8)

    productList = [ 'MiR100',
                    'MiR200',
                    'MiR250',
                    'MiR500',
                    'MiR1000',
                    'MiRFleet']

    versionList = [ '2.7.9',
                    '2.8.3',
                    '2.10.2.3']
    

    chooseProductLabel = Label(newSimFrame, text = 'Choose a product')

    chooseProductLabel.grid(row = 0, column = 0)
    productComboBox = ttk.Combobox(newSimFrame, values = productList, textvariable = productString)
    productComboBox.grid(row = 0, column = 1)

    chooseVersionLabel = Label(newSimFrame, text = 'Choose a version')
    chooseVersionLabel.grid(row = 1, column = 0)
    versionComboBox = ttk.Combobox(newSimFrame, values = versionList, textvariable = versionString)
    versionComboBox.grid(row = 1, column = 1)

    topWindow.mainloop()

def doNothing():
    print ("Hello!")


createMenu = Menu(menubar, tearoff = 0)
createMenu.add_command(label = 'Product Simulator', command = lambda : newProductWindow())
createMenu.add_command(label = 'Troubleshooting tool', command = lambda : doNothing)
createMenu.add_separator()
createMenu.add_command(label="Exit", command=mainWindow.quit)

createLabel = Label(text = '+', fg = 'green', font = 'arial 16 bold')
menubar.add_cascade(label='+', menu=createMenu,)

mainWindow.config(menu=menubar)

amountOfSims = 0


def startSim():
    global amountOfSims
    print ("Starting simulator")
    print ("Product: " + productString.get())
    print ("Version: " + versionString.get())

    amountOfSims += 1
    simObject = simulatorObject(mainWindow, False, 400, 50)
    simObject.frame.grid(row = 1 + amountOfSims)



#def newProductWindow():




class simulatorObject:
    def __init__(self, parentFrame, propagate, width, height):
        labelTemplate = [   'Status: ',
                            'Product: ',
                            'Version: ',
                            'IP: ']

        self.frame = LabelFrame(parentFrame, text = 'Johnny ' + str(random.randint(1 , 9)), width = 400)
        
        self.fillerFrame = Frame(self.frame, width = 300)
        self.fillerFrame.grid(row = 8, column = 0, columnspan = 10)
        
        self.statusFrame = Frame(self.frame, bg = 'green', width = 10, height = 60)
        self.statusFrame.grid(row = 0, rowspan = 3, column = 0, sticky = W)

        self.status = Label(self.frame, text = 'Initializing')
        self.status.grid(row = 0, column = 2, sticky = E)

        self.stopButton = Button(self.frame, text = 'Kill', command = lambda : self.stopSim())
        self.stopButton.grid(row = 0, column = 4)
        for enum, a in enumerate(labelTemplate):
            Label(self.frame, text = a).grid(row = enum, sticky = W, column = 1)

        ipString = ""
        for a in range(4):
            ipString += str(random.randint(0, 254)) + "."

        self.ip = Label(self.frame, text = ipString)
        self.ip.grid(row = 1, column = 2, sticky = E)

        if propagate:
            self.frame.grid_propagate(0)
        else:
            self.frame.grid_propagate(1)

    def stopSim(self):
        self.frame.destroy()






mainWindow.mainloop()
