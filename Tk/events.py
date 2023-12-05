import secrets
from tkinter import *
from tkinter import ttk
from Help import helpFunctions
'''
def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)
'''

#This Method is used to clear the Window

#The removed frame is restored and we remove the return button
def frameReset(event,frame):
    frame.grid()
    event.widget.grid_remove()
    #To adjust the return Button we should use the padding method

#def frameRemove(frame):


# HERE WE REMOVE THE CURRENT FRAME THAT CONTAIN BUTTONS AND WE DISPLAY THE SHOW MORE OF A SPECIFIED MENU
def frameClear(frame):#frame = frame0 created in frameSetUp
    # REMOVING the current frame layout
    currentWindow = frame.winfo_toplevel()
    frame.grid_remove()
    
    # CREATING new frame layout
    newFrame = ttk.Frame(currentWindow)
    newFrame.grid(row=0,column=0)
    returnButton = ttk.Button(newFrame, text="return")
    returnButton.bind('<Button-1>', lambda event: frameReset(event,frame))#Lambda function make sure that the function isn't called directly
    returnButton.grid(row=1, column=1,sticky="NW")
    print(helpFunctions.stylename_elements_options(Grid))





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