from tkinter import *
root=Tk()
root.geometry("1000x1000")
test=LabelFrame(root,bg="yellow",width=500,height=500)
def fr():
    test.place(x=0, y=0)

bt=Button(root,text="clique ici!",command=fr)
bt.pack()
root.mainloop()