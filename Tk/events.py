import secrets
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