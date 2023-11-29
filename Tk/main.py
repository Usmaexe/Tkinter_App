import secrets
from tkinter import *
from tkinter import ttk
from helpFunctions import stylename_elements_options as styleOp

def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)

def showCryptage(event):
    print("hello")

def showAi(event):
    print("hello ai")

def showFiles(event):
    print("hello fil")

def showPOO(event):
    print("hello po")

def showTkinter(event):
    print("hello tk")

def showAlgos(event):
    print(event)


def OpenNew(window):
    window.destroy()
    window2 = Tk()
    print("Hello")
    window2.mainloop()


if __name__ == "__main__" :
    #Creating a window widget and labeling it
    window = Tk()
    window.iconbitmap("./windowLogo.ico")
    window.title("Python's Concepts")
    window.config(bg="#ffffff")

    # THE WINDOW MENU :
    menuBar = Menu(window)

    fileMenu = Menu(menuBar, tearoff=0)  # tearoff=0 means that the file menu is attached to the menu bar
    fileMenu.add_command(label="New Concept")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=window.destroy)
    menuBar.add_cascade(label='File', menu=fileMenu)


    #TheViewMenu
    viewMenu = Menu(menuBar, tearoff=0)
    modeSubMenu = Menu(menuBar, tearoff=0)
    modeSubMenu.add_command(label="Light")
    modeSubMenu.add_command(label="Dark")
    viewMenu.add_cascade(label='Mode',menu=modeSubMenu)

    menuBar.add_cascade(label='View', menu=viewMenu)

    #The edit Menu
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


    ###DIMENSIONS
    #The width and the height of the window
    window_width = int(400*2.4)
    window_height = int(350*1.6)
    f_padding=50
    nbFrames = 5

    #The width and the height of the screen used :
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    #Centring the window :
    center_x = int(screen_w/2 - window_width/2)
    center_y = int(screen_h/2 - window_height/2)

    #To place the root widget and to modify its dimension we use geometry(widthxheight+-x+-y)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.minsize(window_width,window_height)

    #Creating a ttk frame and adding it to the window with the grid(geometry manager similar to pack)
    #FRAME_1
    frame = ttk.Frame(window,padding=f_padding)
    frame.grid(row=1,column=1)
    label = ttk.Label(frame,text="Cryptage").grid(row=1,column=1)
    button = ttk.Button(frame, text="see more")
    button.bind('<Button-1>',showCryptage)
    button.grid(row=2, column=1)


    #FRAME_2
    frame2 = ttk.Frame(window,padding=f_padding,)
    frame2.grid(row=1,column=2)
    label = ttk.Label(frame2,text="Ai").grid(row=1,column=1)
    button = ttk.Button(frame2, text="see more")
    button.bind('<Button-1>',showAi)
    button.grid(row=2, column=1)

    
    #FRAME_3
    frame3 = ttk.Frame(window,padding=f_padding)
    frame3.grid(row=2,column=1)
    label = ttk.Label(frame3,text="POO").grid(row=1,column=1)
    button =ttk.Button(frame3, text="see more")
    button.bind('<Button-1>',showPOO)
    button.grid(row=2, column=1)

    #FRAME_4
    frame4 = ttk.Frame(window,padding=f_padding)
    frame4.grid(row=2,column=2)
    label = ttk.Label(frame4,text="FILES").grid(row=1,column=1)
    button =ttk.Button(frame4, text="see more")
    button.bind('<Button-1>',showFiles)
    button.grid(row=2, column=1)

    #FRAME_5
    frame5 = ttk.Frame(window,padding=f_padding)
    frame5.grid(row=3,column=1)
    label = ttk.Label(frame5,text="TKINTER").grid(row=1,column=1)
    button = ttk.Button(frame5, text="see more")
    button.bind('<Button-1>',showTkinter)
    button.grid(row=2, column=1)

    #FRAME_6
    frame6 = ttk.Frame(window,padding=f_padding)
    frame6.grid(row=3,column=2)
    label = ttk.Label(frame6,text="ALGORITHMS").grid(row=1,column=1)
    button =ttk.Button(frame6, text="see more")
    button.bind('<Button-1>',showAlgos)
    button.grid(row=2, column=1)

    #Specifing the internal padding of the window :
    y_padding = window.winfo_screenheight()-(2*center_y)-(nbFrames*f_padding*2)
    window.configure(padx=center_x,pady=y_padding)

    #CREATING A STYLE :
    style = ttk.Style()
    style.configure('TLabel',font=('Roboto',14),background="white")
    style.configure('TButton',font=('Roboto',10))
    style.configure('TFrame', background="white")

    styleOp('TFrame')

    window.mainloop()

