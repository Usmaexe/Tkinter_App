import secrets
from tkinter import *

'''
def hoverHandling(event):
    list=[chr(c) for c in range(97,123)]
    word=''.join(secrets.choice(list) for _ in range(5))
    button.config(text=word)
'''

#This Method is used to clear the Window
def frameClear(frame):
    frame.grid_remove()


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