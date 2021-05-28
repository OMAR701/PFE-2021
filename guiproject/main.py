# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import font
from tkDocViewer
from tkPDFViewer import tkPDFViewer as pdf

root = Tk()
root.geometry("1210x605")
root.configure(bg='black')
root.minsize(1210, 605)
root.maxsize(1210, 605)

mainFrame = LabelFrame(root)
mainFrame.pack(fill="both", expand="yes")
tgFrame = LabelFrame(root)
tgFrame.pack(fill="both", expand="yes")
tgFrame.pack_forget()
anFrame = LabelFrame(root)
anFrame.pack(fill="both", expand="yes")
anFrame.pack_forget()
sdFrame = LabelFrame(root)
sdFrame.pack(fill="both", expand="yes")
sdFrame.pack_forget()

# _________________Main Frame ____________________
tgImg = PhotoImage(file="tg.png")
anImg = PhotoImage(file="an.png")
sdImg = PhotoImage(file="sd.png")
bgA = PhotoImage(file="bgA.png")
label = Label(mainFrame, image=bgA)
label.place(x=0, y=0)


def tgClick():
    mainFrame.pack_forget()
    sdFrame.pack_forget()
    anFrame.pack_forget()
    tgFrame.pack(fill="both", expand="yes")


def anClick():
    mainFrame.pack_forget()
    sdFrame.pack_forget()
    tgFrame.pack_forget()
    anFrame.pack(fill="both", expand="yes")


def sdClick():
    mainFrame.pack_forget()
    tgFrame.pack_forget()
    anFrame.pack_forget()
    sdFrame.pack(fill="both", expand="yes")


tg = Button(mainFrame, image=tgImg, borderwidth=0, height=195, width=195, compound="c", command=tgClick)
an = Button(mainFrame, image=anImg, bd=0, height=195, width=195, compound="c", command=anClick)
sd = Button(mainFrame, image=sdImg, bd=0, height=195, width=195, compound="c", command=sdClick)
an.place(x=500, y=200)
tg.place(x=200, y=200)
sd.place(x=800, y=200)
# ___________________________________________________

# _________________SD frame _________________________

sdBtnFrame = LabelFrame(sdFrame,width=210, height=600,bd=0)
sdBtnFrame.place(x=0,y=0)
sdBtnFrame.pack(side=LEFT)
sdBtnImg = PhotoImage(file="sdBtnFrame.png")
sdBtnLabel = Label(sdBtnFrame,image=sdBtnImg)
sdBtnLabel.pack()
rightImg = PhotoImage(file="rightImg.png")
pileFrame = LabelFrame(sdFrame,width=1000, height=600,bd=0)
pileFrame.pack()
pileImg = Label(pileFrame,image=rightImg)
pileImg.pack()
fileFrame = LabelFrame(sdFrame,width=1000, height=600,bd=0)
fileFrame.pack_forget()
fileImg = Label(fileFrame,image=rightImg)
fileImg.pack()
llFrame = LabelFrame(sdFrame,width=1000, height=600,bd=0)
llFrame.pack_forget()
llImg = Label(llFrame,image=rightImg)
llImg.pack()
test = PhotoImage(width=0,height=0)
def pileClick():
    pileFrame.pack()
    fileFrame.pack_forget()
    llFrame.pack_forget()
def fileClick():
    fileFrame.pack()
    pileFrame.pack_forget()
    llFrame.pack_forget()
def llClick():
    llFrame.pack()
    pileFrame.pack_forget()
    fileFrame.pack_forget()

pilesImg = PhotoImage(file="piles.png")
pileBtn = Button(sdBtnFrame,image=pilesImg, bd=0, height=36, width=146, compound="c",command=pileClick)
filesImg = PhotoImage(file="files.png")
fileBtn = Button(sdBtnFrame,image=filesImg, bd=0, height=36, width=146, compound="c",command=fileClick)
llImg = PhotoImage(file="llBtn.png")
llBtn = Button(sdBtnFrame,image=llImg, bd=0, height=36, width=146, compound="c",command=llClick)
pileBtn.place(x=30,y=150)
fileBtn.place(x=30,y=250)
llBtn.place(x=30,y=350)
#__________________piles frames______________________
pileLabel = Label(pileFrame,text="Piles :",bg="#1fa0b8",font=('Arial bold',30),fg="white")
pileLabel.place(x=460,y=10)
nbrLabel = Label(pileFrame,text="le nombre de paramètres :",bg="#1fa0b8",font=('Arial bold',15),fg="white")
nbrLabel.place(x=100,y=100)
def clickEnter(event):
    clickNbrBtn()
def clickNbrBtn():
    a=nbrSpin.get()
    if a.isdigit():
        a=int(a)
        if a>3 or a<1:
            errorLabel.configure(text="enter un nombre entre 1 et 3",fg="red")
        else:
            errorLabel.configure(text="", fg="red")
            for i in range(len(typesL)):
                typesL[i].destroy()
                typesB[i].destroy()
                namesL[i].destroy()
                namesB[i].destroy()
            typesL.clear()
            typesB.clear()
            namesL.clear()
            namesB.clear()
            for i in range(int(a)):
                typesL.append( Label(pileFrame,text="le type :",bg="#1fa0b8",font=('Arial bold',15),fg="white"))
                typesL[i].place(x=200,y=200+i*80)
                typesB.append(Spinbox(pileFrame, font=('Helvetica bold',15),values=["int","real","string"],width=10))
                typesB[i].place(x=300,y=200 + i * 80)
                namesL.append(Label(pileFrame, text="le nom :", bg="#1fa0b8", font=('Arial bold', 15), fg="white"))
                namesL[i].place(x=500, y=200 + i * 80)
                namesB.append(Entry(pileFrame,font=('Helvetica bold',15),width=12))
                namesB[i].place(x=600,y=200+i*80)

    else:
        errorLabel.configure(text="enter un nombre entier", fg="red")
nbrSpin = Spinbox(pileFrame, from_=1,to=3,font=('Helvetica bold',15))
nbrSpin.bind('<Return>',clickEnter)
nbrSpin.place(x=400,y=100)
validerB = PhotoImage(file="valider.png")
nbrButton = Button(pileFrame,image=validerB,width=145,height=45,bd=0,command=clickNbrBtn)
nbrButton.place(x=700,y=95)
nextB = PhotoImage(file="nextB.png")
suivantB = Button(pileFrame,image=nextB,fg="white",bg="#ea8b10",font=('Arial bold',15),width=145,height=45,bd=0,command=clickNbrBtn)
suivantB.place(x=700,y=500)
errorLabel = Label(pileFrame,text="",font=('Arial bold',13),bg="#1fa0b8")
errorLabel.place(x=400,y=140)
typesL=[]
typesB=[]
namesL=[]
namesB=[]
#_______________pdf_______________________
v1 = pdf.ShowPdf()
v2 = v1.pdf_view(pileFrame,pdf_location = r"location", width = 100, height = 100)
v2.place(x=400,y=10)
# _____________home click____________________
def homeClick():
    mainFrame.pack(fill="both", expand="yes")
    sdFrame.pack_forget()
    anFrame.pack_forget()
    tgFrame.pack_forget()


frames = [sdBtnFrame, anFrame, tgFrame]
accueil = PhotoImage(file="Accueil.png")
for i in range(3):
    home = Button(sdBtnFrame, image=accueil, bd=0, height=38, width=148, compound="c",command=homeClick,borderwidth=0)
    home.place(x=30, y=50)
# ______________________________________________


root.mainloop()
