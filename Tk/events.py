import secrets
from tkinter import *
from tkinter import ttk

'''
def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)
'''

#This Method is used to clear the Window

def frameReset(frame):
    frame.grid()

def frameClear(frame):
    #frame = frame0 created in frameSetUp

    # REMOVING the current frame layout
    currentWindow = frame.winfo_toplevel()
    frame.grid_remove()

    # CREATING new frame layout
    newFrame = ttk.Frame(currentWindow)
    newFrame.grid()
    returnButton = ttk.Button(newFrame,text="return")
    returnButton.bind('<Button-1>',func = frameReset(frame))
    returnButton.grid(row=1, column=1, padx=10, pady=20)





def showCryptage(event,frame):
    frameClear(frame)


def showAi(event,frame):
    frameClear(frame)


def showFiles(event,frame):
    frameClear(frame)


def showPOO(event,frame):
    frameClear(frame)


def showTkinter(event,frame):
    frameClear(frame)

def showAlgorithms(event,frame):
    frameClear(frame)


def OpenNew(window):
    window.destroy()
    window2 = Tk()
    print("Hello")
    window2.mainloop()