# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from tkinter import *
from tkPDFViewer import tkPDFViewer


def writestruct(nbr, names, types):
    filer = open("edited.asy", "r")
    lignes = filer.readlines()
    filer.close()
    lignes[0] = "int nbr=" + str(nbr) + ";\n"
    lignes[1] = "string[] names={" + '"'
    l = [3, 7, 9, 13, 20, 23, 30]
    for i in l:
        lignes[i] = ""
    for i in range(int(nbr)):
        if i < nbr - 1:
            lignes[1] += names[i] + '"' + "," + '"'
        lignes[3] += types[i] + "  " + names[i] + ";"
        lignes[7] += types[i] + "[]" + names[i] + ";"
        lignes[9] += names[i] + "[i]=m[i]." + names[i] + ";"
        lignes[13] += "write(f," + names[i] + ");"
        lignes[20] += "for(int i=0;i<dim;++i){" + names[i] + "[i]=f.line();}"
        lignes[23] += "t." + names[i] + "=" + names[i] + "[i];"
        lignes[30] += "t[" + str(i) + "]=(string)s." + names[i] + ";"

    for i in l:
        lignes[i] += "\n"
    lignes[1] += names[nbr - 1] + '"' + "};\n"
    lignes[19] = lignes[7]
    filew = open("edited.asy", "w")
    filew.writelines(lignes)
    filew.close()


def stack(names, types, values):
    filer = open("bibliopile.asy", "r")
    lignes = filer.readlines()
    filer.close()
    lignes[4] = ""
    for i in range(len(names)):
        lignes[4] += "t." + names[i] + "="
        if types[i] == "string":
            lignes[4] += '"' + values[i] + '"' + ";"
        elif types[i] == "char":
            lignes[4] += '"' + values[i][0] + '"' + ";"
        else:
            lignes[4] += values[i] + ";"
    lignes[4] += "\n"
    filew = open("bibliopile.asy", "w")
    filew.writelines(lignes)
    filew.close()
    filew = open("draw.asy", "w")
    draw = ["include'bibliopile.asy';" + "\n", "pushList();" + "\n"]
    filew.writelines(draw)
    filew.close()
    os.system('"C:/Program Files/asymptote/asy.exe"  -f pdf -noV ' + __file__[:-7] + 'draw.asy')


root = Tk()
root.geometry("1200x605")
root.configure(bg='black',bd=0)
root.minsize(1200, 605)
root.maxsize(1200, 605)
global n
mainFrame = LabelFrame(root,bd=0)
mainFrame.pack(fill="both", expand="yes")
btnFrames = []

# _________________Main Frame ____________________
tgImg = PhotoImage(file="tg.png")
anImg = PhotoImage(file="an.png")
sdImg = PhotoImage(file="sd.png")
bgA = PhotoImage(file="bgA.png")
logo = PhotoImage(file="logo.png")
label = Label(mainFrame, image=bgA)
label.place(x=0, y=0)


def tgClick():
    mainFrame.pack_forget()
    btnFrames[2].pack_forget()
    btnFrames[1].pack_forget()
    btnFrames[0].pack(fill="both", expand="yes")


def anClick():
    mainFrame.pack_forget()
    btnFrames[2].pack_forget()
    btnFrames[0].pack_forget()
    btnFrames[1].pack(fill="both", expand="yes")


def sdClick():
    mainFrame.pack_forget()
    btnFrames[0].pack_forget()
    btnFrames[1].pack_forget()
    btnFrames[2].pack(fill="both", expand="yes")


def pileClick():
    pileFrame.pack()
    fileFrame.pack_forget()
    llFrame.pack_forget()
    rightFrame[9].pack_forget()


def fileClick():
    fileFrame.pack()
    pileFrame.pack_forget()
    llFrame.pack_forget()
    rightFrame[9].pack_forget()


def llClick():
    llFrame.pack()
    pileFrame.pack_forget()
    fileFrame.pack_forget()
    rightFrame[9].pack_forget()


def clickEnter(event):
    clickNbrBtn()


def clickNbrBtn():
    a = nbrSpin.get()
    if a.isdigit():
        a = int(a)
        if a > 3 or a < 1:
            errorLabel.configure(text="enter un nombre entre 1 et 3", fg="red")
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
                typesL.append(Label(rightFrame[9], text="le type :", bg="#21222d", font=('Arial bold', 15), fg="white"))
                typesL[i].place(x=200, y=200 + i * 80)
                typesB.append(
                    Spinbox(rightFrame[9], font=('Helvetica bold', 15), values=["int", "real", "string"], width=10))
                typesB[i].place(x=300, y=200 + i * 80)
                namesL.append(Label(rightFrame[9], text="le nom :", bg="#21222d", font=('Arial bold', 15), fg="white"))
                namesL[i].place(x=500, y=200 + i * 80)
                namesB.append(Entry(rightFrame[9], font=('Helvetica bold', 15), width=12))
                namesB[i].place(x=600, y=200 + i * 80)
            suivantB.place(x=700, y=500)

    else:
        errorLabel.configure(text="enter un nombre entier", fg="red")


def next():
    for i in range(len(typesL)):
        types.append(str(typesB[i].get()))
        names.append(str(namesB[i].get()))
    writestruct(len(typesL), names, types)
    for i in range(3):
        leftBtn[i + 6].place(x=25, y=150 + i * 75)
    pileClick()
    for i in range(len(names)):
        pileLabels.append(Label(pileFrame, text=names[i] + " :", bg="#1fa0b8", font=('Arial bold', 15), fg="white"))
        pileLabels[i].place(x=50, y=100 + i * 60)
        pileButtons.append(Entry(pileFrame, font=('Helvetica bold', 15), width=12))
        pileButtons[i].place(x=220, y=100 + i * 60)

def preClick():
    names.clear()
    types.clear()
    for i in range(len(pileLabels)):
        pileLabels[i].destroy()
        pileButtons[i].destroy()
    pileLabels.clear()
    pileButtons.clear()
    pileFrame.pack_forget()
    fileFrame.pack_forget()
    llFrame.pack_forget()
    for i in range(3):
        leftBtn[i+6].place_forget()
    rightFrame[9].pack()

def homeClick():
    mainFrame.pack(fill="both", expand="yes")
    btnFrames[0].pack_forget()
    btnFrames[2].pack_forget()
    btnFrames[1].pack_forget()

tg = Button(mainFrame, image=tgImg, bg="#cbcbe5", activebackground="#cbcbe5", borderwidth=0, height=195, width=195,
            compound="c", command=tgClick)
an = Button(mainFrame, image=anImg, bg="#cbcbe5", activebackground="#cbcbe5", bd=0, height=195, width=195, compound="c",
            command=anClick)
sd = Button(mainFrame, image=sdImg, bg="#cbcbe5", activebackground="#cbcbe5", bd=0, height=195, width=195, compound="c",
            command=sdClick)
an.place(x=500, y=200)
tg.place(x=200, y=200)
sd.place(x=800, y=200)
# ___________________________________________________

# _________________SD frame _________________________
sdBtnImg = PhotoImage(file="sdBtnFrame.png")
accueil = PhotoImage(file="Accueil.png")
rightImg = PhotoImage(file="rightImg.png")
valider = PhotoImage(file="valider.png")
leftFrame=[]
home=[]
rightFrame=[]
leftBtn = []
btn =[]
for i in range(3):
    btnFrames.append(LabelFrame(root))
    leftFrame.append(LabelFrame(btnFrames[i], width=300, height=600, bd=0,bg="#cbcbe5"))
    leftFrame[i].place(x=0, y=0)
    leftLabel = Label(leftFrame[i], image=sdBtnImg,bg="#cbcbe5",bd=0)
    leftLabel.place(x=0,y=0)
    home.append(Button(leftFrame[i],activebackground="#cbcbe5",bg="#cbcbe5", image=accueil, bd=0, height=100, width=100, command=homeClick))
    home[i].place(x=50, y=25)
for i in range(2):
    rightFrame.append(LabelFrame(btnFrames[0], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame)-1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame)-1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
    btn.append(PhotoImage(file="btn"+str(i)+".png"))
    leftBtn.append(Button(btnFrames[0],image=btn[i],bg="#cbcbe5",activebackground="#cbcbe5",width=150,height=50,bd=0))
    leftBtn[i].place(x=25,y=200+i*75)
for i in range(4):
    rightFrame.append(LabelFrame(btnFrames[1], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame)-1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame)-1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
    btn.append(PhotoImage(file="btn" + str(i+2) + ".png"))
    leftBtn.append(Button(btnFrames[1], image=btn[i+2], bg="#cbcbe5",activebackground="#cbcbe5", width=150, height=50, bd=0))
    leftBtn[i+2].place(x=25, y=125 + i * 75)
for i in range(4):
    rightFrame.append(LabelFrame(btnFrames[2], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame)-1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame)-1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
btn.append(PhotoImage(file="btn6.png"))
leftBtn.append(Button(btnFrames[2], image=btn[6], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0, command=pileClick))
btn.append(PhotoImage(file="btn7.png"))
leftBtn.append(Button(btnFrames[2], image=btn[7], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0, command=fileClick))
btn.append(PhotoImage(file="btn8.png"))
leftBtn.append(Button(btnFrames[2], image=btn[8], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0, command=llClick))
    #leftBtn[i + 6].place(x=25, y=150 + i * 75)

pileFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)
fileFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)
llFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)


"""
pileBtn.place(x=30,y=150)
fileBtn.place(x=30,y=250)
llBtn.place(x=30,y=350)
"""
# pileLabel = Label(rightFrame,text="Piles :",bg="#1fa0b8",font=('Arial bold',30),fg="white")
# pileLabel.place(x=460,y=10)
sdLabel = Label(rightFrame[9], text="création d'une structure de données :", bg="#21222d", font=('Arial bold', 25),fg="white")
sdLabel.place(x=150, y=10)
nbrLabel = Label(rightFrame[9], text="le nombre de paramètres :", bg="#21222d", font=('Arial bold', 15), fg="white")
nbrLabel.place(x=100, y=100)



nbrSpin = Spinbox(rightFrame[9], from_=1, to=3, font=('Helvetica bold', 15))
nbrSpin.bind('<Return>', clickEnter)
nbrSpin.place(x=400, y=100)
nbrButton = Button(rightFrame[9], image=valider, width=150, height=50, bd=0,bg="#21222d", command=clickNbrBtn)
nbrButton.place(x=700, y=95)
nextB = PhotoImage(file="nextB.png")
suivantB = Button(rightFrame[9], image=nextB, fg="white", bg="#ea8b10", font=('Arial bold', 15), width=145, height=45, bd=0,
                  command=next)
errorLabel = Label(rightFrame[9], text="", font=('Arial bold', 13), bg="#21222d")
errorLabel.place(x=400, y=140)
typesL = []
typesB = []
namesL = []
namesB = []
types = []
names = []



# _______________pile frame_________________
test = PhotoImage(width=0, height=0)
precedant = Button(pileFrame, bg="red", fg="black", text="precedant", image=test, width=140, height=40, bd=0,
                   compound="c", command=preClick)
precedant.place(x=10, y=530)
pileLabels = []
pileButtons = []
pileLabel = Label(pileFrame, text="Piles :", bg="#1fa0b8", font=('Arial bold', 30), fg="white")
pileLabel.place(x=200, y=20)
v1=[]
v2=[]
v1.append(tkPDFViewer.ShowPdf())
v2.append(v1[len(v1)-1].pdf_view(pileFrame, pdf_location=r"exee.pdf", width=50, height=35))
v2[len(v2)-1].place(x=500, y=10)
def empilerClick():
    values = []
    for i in range(len(types)):
        values.append(str(pileButtons[i].get()))
    stack(names, types, values)
    v1.append(tkPDFViewer.ShowPdf())
    v2.append(v1[len(v1) - 1].pdf_view(pileFrame, pdf_location=r"draw.pdf", width=50, height=35))
    v2[len(v2) - 1].place(x=400, y=10)
empiler = Button(pileFrame, bg="red", fg="black", text="Empiler", image=test, width=140, height=40, bd=0, compound="c",
                 command=empilerClick)
empiler.place(x=10, y=400)
# _______________pdf_______________________

# _____________home click____________________




# ______________________________________________


root.mainloop()
