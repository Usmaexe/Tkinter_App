import secrets
from tkinter import *

'''
def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)
'''

#This Method is used to clear the window
def frameClear(frame):
    frame.grid_remove()

def showCryptage(event,frame):
    frameClear(frame)


def showAi(event,frame):
    print("hello ai")

def showFiles(event,frame):
    print("hello fil")

def showPOO(event,frame):
    print("hello po")

def showTkinter(event,frame):
    print("hello tk")

def showAlgorithms(event,frame):
    print(event)


def OpenNew(window):
    window.destroy()
    window2 = Tk()
    print("Hello")
    window2.mainloop()