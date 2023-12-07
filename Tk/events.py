import subprocess
from tkinter import *
from tkinter import ttk
from frameExercices import FrameBuilder
#from frameSetUp import FrameBuilder


'''
def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)
'''

#This Method is used to clear the Window

#The removed frame is restored and we remove the return button
def frameReset(event,frame,newFrame):
    frame.grid()
    newFrame.remove()
    event.widget.grid_remove()
    #To adjust the return Button we should use the padding method

#def frameRemove(frame):


# HERE WE REMOVE THE CURRENT FRAME THAT CONTAIN BUTTONS AND WE DISPLAY THE SHOW MORE OF A SPECIFIED MENU
def frameClear(frame):#frame = frame0 created in frameSetUp
    # REMOVING the current frame layout
    currentWindow = frame.winfo_toplevel()
    frame.grid_remove()
    
    


def showCryptage(event,frame,window):
    output = subprocess.check_output(["ls","Cryptographie"],shell=True)
    exos=list((output.decode('utf-8')).split('\n'))
    exos.remove("")
    exos.remove("__pycache__")
    #print(exos)
    frameClear(frame)
    
    # CREATING new frame layout
    newFrame = ttk.Frame(window.window)
    newFrame.grid(row=0,column=0)
    returnButton = ttk.Button(newFrame, text="Return")
    returnButton.grid(row=1, column=1,sticky="NW")
    #(self,w,defaultPadding, nbFrames,content, names, actions)
    cryptageFrame = FrameBuilder(window, 10, len(exos), "Cryptographie",exos)
    returnButton.bind('<Button-1>', lambda event: frameReset(event,frame,cryptageFrame))#Lambda function make sure that the function isn't called directly
    

def showAi(event, frame, win):
    frameClear(frame)
def showFiles(event,frame, win):
    frameClear(frame)


def showPOO(event,frame, win):
    frameClear(frame)


def showTkinter(event,frame, win):
    frameClear(frame)

def showAlgorithms(event,frame, win):
    frameClear(frame)


def OpenNew(window):
    window.destroy()
    window2 = Tk()
    print("Hello")
    window2.mainloop()