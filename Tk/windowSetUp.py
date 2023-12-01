from tkinter import *
from tkinter import ttk
from events import *

# The width and the height of the window
window_width = int(400 * 2.4)
window_height = int(350 * 1.6)


#THINK ABOUT USING SELF
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

def fsu(window, defaultPadding, nbFrames, names, actions):
    frame0 = ttk.Frame(window)
    frame0.grid()

    # Dictionary to manage frames and buttons:
    frames = {}
    buttons = {}

    for i in range(nbFrames):
        name = f"frame_{i}"
        function_name = actions[i]

        my_lambda = lambda event, frame=frame0, func=function_name: globals()[func](event, frame)

        frames[name] = ttk.Frame(frame0, padding=defaultPadding)
        frames[name].grid(row=int((i / 2) + 1), column=(i % 2) + 1)
        label = ttk.Label(frames[name], text=f"{names[i]}").grid(row=1, column=1)
        buttons[name] = ttk.Button(frames[name], text="see more")
        buttons[name].bind('<Button-1>', my_lambda)
        buttons[name].grid(row=2, column=1)

    return window

