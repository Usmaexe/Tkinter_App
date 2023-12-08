import tkinter as tk
from tkinter import Canvas
from tkinter import messagebox
window=tk.Tk()
window.title("abc")
window.geometry('200x200')
lb = tk.Label(window,text="premier exemple",font=("Arial",20))
lb.pack()
asaisie = tk.Entry(); bsaisie=tk.Entry(); asaisie.pack() ; bsaisie.pack();
laba=tk.Label(window,text="a");laba.place(x=10,y=30);

def somme():
    a=int(asaisie.get()); b = int(bsaisie.get());
    if(x.get()==1):
     messagebox.showinfo("msg",a+b);
    else:
        return messagebox.showinfo("abc","confirmez")
bt=tk.Button(window,text="somme",
             command=lambda : somme() )
x=tk.IntVar()
cb = tk.Checkbutton(window, text='confirmer',variable=x,onvalue=1,offvalue=0);
cb.pack();bt.pack()
lbsomme=tk.Label(window, text=""); lbsomme.pack();
def effacer():
    asaisie.delete(0,tk.END)
    bsaisie.delete(0,tk.END)
    asaisie.insert(0,"123")
bteff=tk.Button(window,text="effacer", command=lambda : effacer() )
bteff.bind("<Double-Button-1>",lambda event : window.quit())
bteff.pack()
s=tk.StringVar(value="ine1");
tk.Radiobutton(window,text="ine1",variable=s,value="ine1").pack();
tk.Radiobutton(window,text="ine2",variable=s,value="ine2").pack();
bteff=tk.Button(window,text="choix", command=lambda : effacer() )
compteur = tk.IntVar(value=0);
lbc=tk.Label(window, text="0"); lbc.pack()
def miseajourcompteur ():
    compteur.set(compteur.get()+1)
    lbc.config(text=compteur.get())
    window.after(1000,miseajourcompteur)
miseajourcompteur()
w = Canvas(window, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)
window.mainloop()