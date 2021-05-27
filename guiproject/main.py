# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import font

root = Tk()
root.geometry("1200x600")
root.configure(bg='white')
root.minsize(1200, 600)
root.maxsize(1200, 600)
pixelVirtual = PhotoImage(width=0, height=0)
an=Button(root,text="Analyse \n Numerique",image=pixelVirtual,fg="white",bg="#1929DB",height=200,width=200,compound="c",bd=0)
an['font'] =  font.Font(family='Helvetica', size=20, weight='bold')
tg=Button(root,text="Theorie de Grapge",image=pixelVirtual,height=200,width=200,compound="c")
sd=Button(root,text="Structure de Donnee",image=pixelVirtual,height=200,width=200,compound="c")
#an.grid(row=0,column=0)
#tg.grid(row=0,column=1)
#sd.grid(row=0,column=2)
an.place(x=500,y=200)
tg.place(x=200,y=200)
sd.place(x=800,y=200)
root.mainloop()