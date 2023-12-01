from tkinter import *
from events import *
def SetUp(window):
	# THE WINDOW MENU :
    menuBar = Menu(window)

    fileMenu = Menu(menuBar, tearoff=0)  # tearoff=0 means that the file menu is attached to the menu bar
    fileMenu.add_command(label="New Concept",command=lambda:OpenNew(window)) #Lambda is used as wraper to allow passing argument
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=window.destroy)
    menuBar.add_cascade(label='File', menu=fileMenu)

    # TheView Menu
    viewMenu = Menu(menuBar, tearoff=0)
    modeSubMenu = Menu(menuBar, tearoff=0)
    modeSubMenu.add_command(label="Light")
    modeSubMenu.add_command(label="Dark")
    viewMenu.add_cascade(label='Mode', menu=modeSubMenu)

    menuBar.add_cascade(label='View', menu=viewMenu)

    # The edit Menu
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_cascade(label='Preferences')
    editMenu.add_cascade(label='Full Screen')

    menuBar.add_cascade(label='Edit', menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add(CASCADE, label="Documentation")
    helpMenu.add(CASCADE, label="Who Am I?")
    menuBar.add_cascade(label='Help', menu=helpMenu)
    menuBar.config(bg="#ff2220")

    window.config(menu=menuBar)

    return window