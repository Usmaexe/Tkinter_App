from tkinter import *
from tkinter import ttk
from events import *

# The width and the height of the window
window_width = int(400 * 2.4)
window_height = int(350 * 1.6)
def SetUp():
	#Creating a window widget and labeling it
    window = Tk()
    window.iconbitmap("Assets/windowLogo.ico")
    window.title("Python's Concepts")
    window.config(bg="#ffffff")

    ###DIMENSIONS

    #The width and the height of the screen used :
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    #Centring the window :
    center_x = int(screen_w/2 - window_width/2)
    center_y = int(screen_h/2 - window_height/2)


    return window,center_x,center_y

def Dimensions(window,center_x,center_y):

    #To place the root widget and to modify its dimension we use geometry(widthxheight+-x+-y)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.minsize(window_width,window_height)

    return window

def Padding(window,sets) :

    y_padding = window.winfo_screenheight() - (2 * sets[1]) - (sets[2] * sets[3] * 2)
    window.configure(padx=sets[0], pady=y_padding)

    return window

def fsu(window,defaultPadding=30):
    # Creating a ttk frame and adding it to the window with the grid(geometry manager similar to pack)
    # FRAME_1
    frame = ttk.Frame(window, padding=defaultPadding)
    frame.grid(row=1, column=1)
    label = ttk.Label(frame, text="Cryptage").grid(row=1, column=1)
    button = ttk.Button(frame, text="see more")
    button.bind('<Button-1>', showCryptage)
    button.grid(row=2, column=1)

    # FRAME_2
    frame2 = ttk.Frame(window, padding=defaultPadding)
    frame2.grid(row=1, column=2)
    label = ttk.Label(frame2, text="Ai").grid(row=1, column=1)
    button = ttk.Button(frame2, text="see more")
    button.bind('<Button-1>', showAi)
    button.grid(row=2, column=1)

    # FRAME_3
    frame3 = ttk.Frame(window, padding=defaultPadding)
    frame3.grid(row=2, column=1)
    label = ttk.Label(frame3, text="POO").grid(row=1, column=1)
    button = ttk.Button(frame3, text="see more")
    button.bind('<Button-1>', showPOO)
    button.grid(row=2, column=1)

    # FRAME_4
    frame4 = ttk.Frame(window, padding=defaultPadding)
    frame4.grid(row=2, column=2)
    label = ttk.Label(frame4, text="FILES").grid(row=1, column=1)
    button = ttk.Button(frame4, text="see more")
    button.bind('<Button-1>', showFiles)
    button.grid(row=2, column=1)

    # FRAME_5
    frame5 = ttk.Frame(window, padding=defaultPadding)
    frame5.grid(row=3, column=1)
    label = ttk.Label(frame5, text="TKINTER").grid(row=1, column=1)
    button = ttk.Button(frame5, text="see more")
    button.bind('<Button-1>', showTkinter)
    button.grid(row=2, column=1)

    # FRAME_6
    frame6 = ttk.Frame(window, padding=defaultPadding)
    frame6.grid(row=3, column=2)
    label = ttk.Label(frame6, text="ALGORITHMS").grid(row=1, column=1)
    button = ttk.Button(frame6, text="see more")
    button.bind('<Button-1>', showAlgos)
    button.grid(row=2, column=1)

    return window