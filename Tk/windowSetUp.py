from tkinter import simpledialog
from events import *


class Root() :

    #The window constructure :
    #It Allow to create a window widget using tk, specifing the width, the height, the icon, title and bg color
    def __init__(self,iconPath,windowTitle,bgColor,wh,ww):
        self.window_height = wh
        self.window_width = ww
        self.window = Tk()
        self.window.iconbitmap(iconPath)
        self.window.title(windowTitle)
        self.window.config(bg=bgColor)
        self.window.winfo_width()


    def Dimensions(self):

        ###DIMENSIONS
        # The width and the height of the screen used :
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()

        # Centring the self :
        center_x = int(screen_w / 2 - self.window_width / 2)
        center_y = int(screen_h / 2 - self.window_height / 2)

        #To place the root widget and to modify its dimension we use geometry(widthxheight+-x+-y)
        self.window.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.window.minsize(self.window_width, self.window_height)

        return center_x, center_y
    
    def Padding(self, sets) :

        y_padding = self.window.winfo_screenheight() - (2 * sets[1]) - (5 * sets[2] * 2)
        self.window.configure(padx=sets[0], pady=y_padding)


    def ModeChanging(self):
        print(self.mode.get())

    def set_default_mode(self,mode:IntVar):
        self.mode.set(mode.get())  # Set Light mode as default
    
    def Menu(self):
        # THE WINDOW MENU :
        menuBar = Menu(self.window)

        fileMenu = Menu(menuBar, tearoff=0)  # tearoff=0 means that the file menu is attached to the menu bar
        fileMenu.add_command(label="New Concept", command=lambda:CreateNew(self.window)) #Lambda is used as wraper to allow passing argument
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.window.destroy)
        menuBar.add_cascade(label='File', menu=fileMenu)

        # TheView Menu
        viewMenu = Menu(menuBar, tearoff=0)
        modeSubMenu = Menu(menuBar, tearoff=0)
        self.mode = IntVar(value=1)  # Initialize mode variable

        modeSubMenu.add_checkbutton(label="Light", variable=self.mode, onvalue=1, command=lambda: self.ModeChanging())
        modeSubMenu.add_checkbutton(label="Dark", variable=self.mode, onvalue=2, command=lambda: self.ModeChanging())

        self.set_default_mode(IntVar(value=1))
        
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

        self.window.config(menu=menuBar)

class NewConcept(simpledialog.Dialog):
        def Customized(self):
            self.title="New Concept"
            
            self.entry = Entry(self)
            
            