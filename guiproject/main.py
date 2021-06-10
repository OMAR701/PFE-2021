# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from tkinter import *
from tkinter import filedialog
from skimage import io
# from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from pdfrw import PdfReader
import time


class Graph:
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    result = []

    def printPath(self, parent, j):
        # Base Case : If j is source
        if parent[j] == -1:
            print(j)
            self.result.append(j)
            return
        self.printPath(parent, parent[j])
        print(j)
        self.result.append(j)

    def printSolution(self, dist, parent):
        src = 0
        result2 = [[0 for i in range(len(dist))] for j in range(len(dist))]
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(0, len(dist)):
            self.result = []
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]))
            self.printPath(parent, i)
            result2[i] = self.result
        return result2

    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        result = self.printSolution(dist, parent)
        return result


def writemat(mat, nbr):
    filer = open("graphrbib.asy", "r")
    lignes = filer.readlines()
    filer.close()
    lignes[2] = "size(" + str(nbr * 2) + "cm);\n"
    lignes[3] = "\n"
    lignes[4] = "real[][] matadj={{"
    lignes[6] = "\n"
    lignes[7] = '\n'
    nbr = len(mat[0])
    for i in range(0, nbr - 1):
        for j in range(0, nbr - 1):
            lignes[4] += str(mat[i][j]) + ','
        lignes[4] += str(mat[i][nbr - 1]) + "},{"
    for j in range(0, nbr - 1):
        lignes[4] += str(mat[nbr - 1][j]) + ','
    lignes[4] += str(mat[nbr - 1][nbr - 1]) + "}};\n"
    filer = open("graphrbib.asy", "w")
    filer.writelines(lignes)
    filer.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -f pdf -noV  graphrbib.asy')


def writepath(to, test):
    filer = open("graphrbib.asy", "r")
    lignes = filer.readlines()
    filer.close()
    s = ["modif_s(gr,", ",s_penlab=fontsize(20pt)+black,s_penenv  = 3bp+black,s_fill=FillDraw(red));"]
    a = ["modif_a(gr,", ",a_pen=3bp+red,a_penlab=fontsize(20pt)+black, a_labfill = Fill(red));"]
    lignes[6] = ""
    lignes[7] = ""
    for i in range(0, len(test[to])):
        lignes[6] += s[0] + str(test[to][i]) + s[1]
    for i in range(0, len(test[to]) - 1):
        lignes[7] += a[0] + str(test[to][i]) + "," + str(test[to][i + 1]) + a[1]
    lignes[6] += "\n"
    lignes[7] += "\n"
    filer = open("graphrbib.asy", "w")
    lignes = filer.writelines(lignes)
    filer.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -f pdf -noV  graphrbib.asy')


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
    if os.path.exists("draw.png"):
        os.remove("draw.png")
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
    draw = ["include'bibliopile.asy';" + "\n", "settings.outformat='png';settings.render=2;\n", "pushList();" + "\n"]
    filew.writelines(draw)
    filew.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -noV  draw.asy')


def stackpop():
    draw = ["include'bibliopile.asy';" + "\n", "settings.outformat='png';settings.render=2;\n", "popList();" + "\n"]
    filew = open("draw.asy", "w")
    filew.writelines(draw)
    filew.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -noV draw.asy')


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
    rightFrame[6].place(x=190, y=0)
    rightFrame[7].place_forget()
    rightFrame[8].place_forget()
    rightFrame[9].place_forget()


def fileClick():
    rightFrame[7].place(x=190, y=0)
    rightFrame[6].place_forget()
    rightFrame[8].place_forget()
    rightFrame[9].place_forget()


def llClick():
    rightFrame[8].place(x=190, y=0)
    rightFrame[6].place_forget()
    rightFrame[7].place_forget()
    rightFrame[9].place_forget()


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
                    Spinbox(rightFrame[9], font=('Helvetica bold', 15), values=spinvalues, width=10))
                typesB[i].place(x=300, y=200 + i * 80)
                namesL.append(Label(rightFrame[9], text="le nom :", bg="#21222d", font=('Arial bold', 15), fg="white"))
                namesL[i].place(x=500, y=200 + i * 80)
                namesB.append(Entry(rightFrame[9], font=('Helvetica bold', 15), width=12))
                namesB[i].place(x=600, y=200 + i * 80)
            suivantB.place(x=750, y=500)

    else:
        errorLabel.configure(text="enter un nombre entier", fg="red")


def next():
    clr = open("testing.txt", "w")
    clr.writelines("0\n")
    clr.close()
    for i in range(len(typesL)):
        if str(typesB[i].get()) not in spinvalues:
            errorLabel.place(x=400, y=140)
            errorLabel.configure(text="type invalide", fg="red")
            types.clear()
            names.clear()
            return
        if str(namesB[i].get()) == "":
            errorLabel.place(x=400, y=140)
            errorLabel.configure(text="label vide !", fg="red")
            types.clear()
            names.clear()
            return
        for g in range(len(str(namesB[i].get()))):
            if str(namesB[i].get()[g]) not in ailph:
                errorLabel.place(x=400, y=140)
                errorLabel.configure(text="enter seulement des charatere", fg="red")
                types.clear()
                names.clear()
                return
        types.append(str(typesB[i].get()))
        names.append(str(namesB[i].get()))
    for i in range(len(names) - 1):
        if names[i] in names[(i + 1):len(names)]:
            errorLabel.place(x=400, y=140)
            errorLabel.configure(text="nom doit etre unique", fg="red")
            types.clear()
            names.clear()
            return
    errorLabel.place_forget()
    writestruct(len(typesL), names, types)
    for i in range(3):
        leftBtn[i + 6].place(x=25, y=150 + i * 75)
    pileClick()
    for i in range(len(names)):
        pileLabels.append(Label(rightFrame[6], text=names[i] + " :", bg="#21222d", font=('Arial bold', 15), fg="white"))
        pileLabels[i].place(x=50, y=100 + i * 60)
        pileButtons.append(Entry(rightFrame[6], font=('Helvetica bold', 15), width=12))
        pileButtons[i].place(x=220, y=100 + i * 60)


def preClick():
    names.clear()
    types.clear()
    rightFrame[9].place(x=190, y=0)
    for i in range(len(pileLabels)):
        pileLabels[i].destroy()
        pileButtons[i].destroy()
    pileLabels.clear()
    pileButtons.clear()
    for i in range(3):
        rightFrame[i + 6].place_forget()
        leftBtn[i + 6].place_forget()
    clr = open("testing.txt", "w")
    clr.writelines("0\n")
    clr.close()


def homeClick():
    mainFrame.pack(fill="both", expand="yes")
    btnFrames[0].pack_forget()
    btnFrames[2].pack_forget()
    btnFrames[1].pack_forget()


frames = 8
count = 0
anim = None


def animation(count):
    global anim
    im2 = loadgift[count]

    labelGif.configure(image=im2)
    tg_Gif.configure(image=im2)
    ar_Gif.configure(image=im2)
    new_Gif.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50, lambda: animation(count))


def loadingf():
    empiler["state"] = "disabled"
    depiler["state"] = "disabled"
    downShow["state"] = "disabled"
    animation(count)
    labelGif.place(x=100, y=430)


def testing():
    empiler["state"] = "normal"
    depiler["state"] = "normal"
    downShow["state"] = "normal"
    root.after_cancel(anim)
    labelGif.place_forget()
    for i in range(10):
        loadingFrm[i].place_forget()
    pileResult.configure(file="draw.png")
    labelP.configure(image=pileResult)
    labelP.pack(side=BOTTOM)


def empilerClick():
    values = []
    filer = open("testing.txt", "r")
    lignes = filer.readlines()
    filer.close()
    if int(lignes[0]) > 9:
        errorLabel3.configure(text="la pile est plein", fg="red")
        errorLabel3.place(x=300, y=400)
        return

    for i in range(len(types)):
        if str(types[i]) == "int":
            if not pileButtons[i].get().isdigit():
                errorLabel2.configure(text="nom doit etre unique", fg="red")
                errorLabel2.place(x=200, y=200)
                return
        if str(types[i]) == "real":
            try:
                float(pileButtons[i].get())
            except:
                errorLabel2.configure(text="nom doit etre unique", fg="red")
                errorLabel2.place(x=200, y=200)
                return

        values.append(str(pileButtons[i].get()))
    errorLabel2.place_forget()
    stack(names, types, values)
    errorLabel3.place_forget()

    root.after(0, loadingf)
    root.after(u, testing)


def depilerClick():
    filer = open("testing.txt", "r")
    lignes = filer.readlines()
    filer.close()
    if int(lignes[0]) == 0:
        errorLabel3.configure(text="la pile est vide", fg="red")
        errorLabel3.place(x=300, y=400)
        return
    stackpop()
    errorLabel3.place_forget()
    # time.sleep(0.5)

    root.after(0, loadingf)
    root.after(u, testing)


def file_save():
    img = io.imread("draw.png")
    fpath = filedialog.asksaveasfilename(defaultextension=".png")
    io.imsave(str(fpath), img)


def imputGF():
    line = []
    inpt = str(tg_lignentry.get())
    val = ""
    for i in range(len(str(inpt))):
        if inpt[i].isdigit():
            val += str(inpt[i])
        elif i > 0:
            try:
                if val != "":
                    line.append(int(val))
                    val = ""
            except:
                return
    if val != "":
        try:
            line.append(int(val))
        except:
            return
    return line


# -------------------------------NEW ------------------------------
def an_newtonclick():
    rightFrame[2].place(x=190, y=0)
    rightFrame[3].place_forget()
    rightFrame[4].place_forget()
    rightFrame[5].place_forget()


def new_loading():
    animation(count)
    new_Gif.place(x=270, y=430)


def new_newIdea():
    if os.path.exists("newtonpython-1.png"):
        root.after(0, newImgshow)
        return
    print("2")
    root.after(700, new_newIdea)


def new_newIdea2():
    if os.path.exists("newtonpython.pdf"):
        time.sleep(0.5)
        pdf = PdfReader('newtonpython.pdf')
        info = pdf.pages[0].MediaBox
        print(info[3])
        a = float(info[3])
        a = int(a)
        a1 = a
        print(info[2])
        b = float(info[2])
        b = int(b)
        b1 = b
        if a > b:
            a1 = 400
            b1 = int((400 * b) / a)
        else:
            b1 = 400
            a1 = int((400 * a) / b)
        os.popen(
            "pdftoppm  newtonpython.pdf newtonpython -png -scale-to-x " + str(int(b1)) + " -scale-to-y " + str(int(a1)))
        root.after(0, new_newIdea)
        return
    print("1")
    root.after(700, new_newIdea2)


def new_graphe():
    if os.path.exists("newtonpython-1.png"):
        os.remove("newtonpython-1.png")
    if os.path.exists("newtonpython.pdf"):
        os.remove("newtonpython.pdf")
    writefunct(str(new_spin.get()), str(new_spin_pr.get()))
    writenewton(str(new_iter_spin.get()), str(new_spin_epsilon.get()), str(new_spin_x0.get()))
    root.after(0, new_loading)
    root.after(0, new_newIdea2)


def writefunct(fct, fctprime):
    filr = open("new_edit.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[1] = "return " + str(fct) + ";\n"
    lignes[4] = "return " + str(fctprime) + ";\n"
    flew = open("new_edit.asy", "w")
    flew.writelines(lignes)
    flew.close()


def writenewton(a, b, c):
    filr = open("newtonpython.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[0] = " real x0=" + str(c) + "; \n"
    lignes[61] = "newton(f,fprime," + str(a) + "," + str(b) + "," + str(c) + ");\n"
    flew = open("newtonpython.asy", "w")
    flew.writelines(lignes)
    flew.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -f pdf -noV newtonpython.asy')


def newImgshow():
    new_Gif.place_forget()
    new_Img.clear()
    new_Img.append(PhotoImage(file="newtonpython-1.png"))
    new_label.configure(image=new_Img[0])
    new_label.place(x=10, y=10)


def writenew_tab(a, b, c):
    filr = open("new_tab.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[55] = "newton(f,fprime," + str(a) + "," + str(b) + "," + str(
        c) + ");settings.outformat='png';settings.render=2;\n"
    flew = open("new_tab.asy", "w")
    flew.writelines(lignes)
    flew.close()
    os.popen('asy -noV new_tab.asy')


def new_save():
    img = io.imread("newtonpython-1.png")
    fpath = filedialog.asksaveasfilename(defaultextension=".png")
    io.imsave(str(fpath), img)


# -------------------------------ARBRES-----------------------------

def arbreClick():
    rightFrame[1].place(x=190, y=0)
    rightFrame[0].place_forget()


def ar_newIdea():
    if os.path.exists("tree-1.png"):
        root.after(0, arImgShow)
        return
    print("2")
    root.after(700, ar_newIdea)


def ar_newIdea2():
    if os.path.exists("tree.pdf"):
        time.sleep(0.5)
        pdf = PdfReader('tree.pdf')
        info = pdf.pages[0].MediaBox
        print(info[3])
        a = float(info[3])
        a = int(a)
        a1 = a
        print(info[2])
        b = float(info[2])
        b = int(b)
        b1 = b
        if a > b:
            a1 = 400
            b1 = int((400 * b) / a)
        else:
            b1 = 400
            a1 = int((400 * a) / b)
        if len(ar_option) == 1:
            a1 /= 2
            b1 /= 2
        os.popen("pdftoppm  tree.pdf tree -png -scale-to-x " + str(int(b1)) + " -scale-to-y " + str(int(a1)))
        root.after(0, ar_newIdea)
        return
    print("1")
    root.after(700, ar_newIdea2)


def Arbreclick():
    rightFrame[1].place(x=190, y=0)
    rightFrame[0].pack_forget()


def addNoeud():
    if str(Spinarbre.get()) == "":
        ar_error.configure(text="Chemp obligatoire")
        ar_error.place(x=400, y=120)
        return
    ar_option.clear()
    if " " in str(Spinarbre.get()):
        ar_error.configure(text="Les espaces sont interdit")
        ar_error.place(x=400, y=120)
        return
    if os.path.exists("tree-1.png"):
        os.remove("tree-1.png")
    if os.path.exists("tree.pdf"):
        os.remove("tree.pdf")
    ar_error.place_forget()
    ar_suivant["state"] = "disabled"
    ar_Show["state"] = "disabled"
    ar_option.append(Spinarbre.get())
    writeNoeud(Spinarbre.get())
    cb.set(ar_option[-1])
    # ar_image.configure(file="tree.png")
    # ar_label.configure()
    cb.configure(values=ar_option)
    ar_father.place(x=90, y=200)
    cb.place(x=200, y=200)
    ar_child.place(x=90, y=300)
    ar_spin.place(x=200, y=300)
    ar_suivant.place(x=175, y=390)
    ar_Show.place(x=150, y=480)
    root.after(0, ar_loading)
    root.after(0, ar_newIdea2)


def ar_loading():
    animation(count)
    ar_Gif.place(x=350, y=390)


def addchild():
    a = ar_spin.get()
    b = cb.get()
    if str(ar_spin.get()) == "":
        ar_error.configure(text="Chemp obligatoire")
        ar_error.place(x=200, y=350)
        return
    if str(cb.get()) == "":
        ar_error.configure(text="Chemp obligatoire")
        ar_error.place(x=200, y=250)
        return
    if " " in str(cb.get()):
        ar_error.configure(text="Les espaces sont interdit")
        ar_error.place(x=200, y=250)
        return
    if " " in str(ar_spin.get()):
        ar_error.configure(text="Les espaces sont interdit")
        ar_error.place(x=200, y=350)
        return
    if b not in ar_option:
        ar_error.configure(text="Ce Noeud père n'existe pas")
        ar_error.place(x=200, y=250)
        return
    if a in ar_option:
        ar_error.configure(text="Ce Noeud Déja existe ")
        ar_error.place(x=200, y=350)
        return
    if os.path.exists("tree-1.png"):
        os.remove("tree-1.png")
    if os.path.exists("tree.pdf"):
        os.remove("tree.pdf")
    ar_suivant["state"] = "disabled"
    ar_Show["state"] = "disabled"
    ar_option.append(a)
    cb.set(ar_option[-1])
    ar_spin.delete(0, 'end')
    ar_error.place_forget()
    ar_error2.place_forget()
    cb.configure(values=ar_option)
    if os.path.exists("tree-1.png"):
        os.remove("tree-1.png")
    writeanyNoeud(a, b)
    root.after(0, ar_loading)
    root.after(0, ar_newIdea2)


def arImgShow():
    ar_suivant["state"] = "normal"
    ar_Show["state"] = "normal"
    root.after_cancel(anim)
    ar_Gif.place_forget()
    ar_Img.clear()
    ar_Img.append(PhotoImage(file="tree-1.png"))
    ar_result.place(x=500, y=150)
    ar_label.configure(image=ar_Img[0])
    ar_label.place(x=10, y=10)


def writeNoeud(Noeud1):
    lignes = []
    if str(Noeud1)[0].isdigit():
        lignes.append("TreeNode nbr" + str(Noeud1) + "= makeNode(" + str('"') + str(Noeud1) + str('"') + ");\n")
        lignes.append("draw(nbr" + str(Noeud1) + ",(0,0));")
    else:
        lignes.append("TreeNode " + str(Noeud1) + "= makeNode(" + str('"') + str(Noeud1) + str('"') + ");\n")
        lignes.append("draw(" + str(Noeud1) + ",(0,0));")
    flew = open("includingtree.asy", "w")
    flew.writelines(lignes)
    flew.close()
    os.popen(' "C:/Program Files (x86)/Asymptote/asy.exe" -f pdf -noV tree.asy')


def writeanyNoeud(Noeud1, father):
    filr = open("includingtree.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes.pop()
    if str(Noeud1)[0].isdigit():
        if str(father)[0].isdigit():
            lignes.append(
                "TreeNode nbr" + str(Noeud1) + " = makeNode(nbr" + str(father) + "," + str('"') + str(Noeud1) + str(
                    '"') + ");\n")

        else:
            lignes.append(
                "TreeNode nbr" + str(Noeud1) + " = makeNode(" + str(father) + "," + str('"') + str(Noeud1) + str(
                    '"') + ");\n")
    else:
        if str(father)[0].isdigit():
            lignes.append(
                "TreeNode " + str(Noeud1) + " = makeNode(nbr" + str(father) + "," + str('"') + str(Noeud1) + str(
                    '"') + ");\n")
        else:
            lignes.append("TreeNode " + str(Noeud1) + " = makeNode(" + str(father) + "," + str('"') + str(Noeud1) + str(
                '"') + ");\n")
    if str(ar_option[0]).isdigit():
        lignes.append("draw( nbr" + str(ar_option[0]) + ",(0,0));")
    else:
        lignes.append("draw( " + str(ar_option[0]) + ",(0,0));")

    flew = open("includingtree.asy", "w")
    flew.writelines(lignes)
    flew.close()
    os.popen('"C:/Program Files (x86)/Asymptote/asy.exe" -f pdf -noV tree.asy')


def ar_save():
    img = io.imread("tree-1.png")
    fpath = filedialog.asksaveasfilename(defaultextension=".png")
    io.imsave(str(fpath), img)


# -------------------------------- TG ---------------------------
def grapheClick():
    rightFrame[0].place(x=190, y=0)
    rightFrame[1].place_forget()


def tg_loading():
    tg_parcour["state"] = "disable"
    animation(count)
    tg_Gif.place(x=200, y=200)


def tg_newIdea():
    if os.path.exists("graphrbib-1.png"):
        root.after(0, tgImgShow)
        return
    root.after(700, tg_newIdea)


def tg_newIdea2():
    if os.path.exists("graphrbib.pdf"):
        time.sleep(0.5)
        pdf = PdfReader('graphrbib.pdf')
        info = pdf.pages[0].MediaBox
        print(info[3])
        a = float(info[3])
        a = int(a)
        a1 = a
        print(info[2])
        b = float(info[2])
        b = int(b)
        b1 = b
        if a > b:
            a1 = 400
            b1 = int((400 * b) / a)
        else:
            b1 = 400
            a1 = int((400 * a) / b)

        os.popen("pdftoppm  graphrbib.pdf graphrbib -png -scale-to-x " + str(b1) + " -scale-to-y " + str(a1))
        root.after(0, tg_newIdea)
        return
    root.after(700, tg_newIdea2)


def tgImgShow():
    tg_parcour["state"] = "normal"
    root.after_cancel(anim)
    tg_Gif.place_forget()
    tg_Img.clear()
    tg_Img.append(PhotoImage(file="graphrbib-1.png"))
    tg_result.place(x=550, y=150)
    tg_label.configure(image=tg_Img[0])
    tg_label.place(x=10, y=10)


def tg_valider():
    tg_result.place_forget()
    tg_leftframe.place_forget()
    tg_table.clear()
    global tg_i
    tg_i = 1
    global mat

    tg_table.append(int(tg_nbrSpingf.get()))
    mat = [[1] * tg_table[0]] * tg_table[0]
    if tg_table[0] == 1:
        tg_valid.place(x=270, y=35)
        tg_nextB.place_forget()
        tg_preB.place_forget()
    else:
        tg_valid.place_forget()
        tg_preB.place_forget()
        tg_nextB.place(x=270, y=35)
    tg_rightframe.place(x=500, y=60)
    tg_nbrlines.configure(text="ligne : " + str(tg_i))
    tg_nbrlinesRe.configure(text="ligne restant : " + str(tg_table[0] - tg_i))


def tg_valider2():
    if os.path.exists("graphrbib-1.png"):
        os.remove("graphrbib-1.png")
    if os.path.exists("graphrbib.pdf"):
        os.remove("graphrbib.pdf")
    tg_next()
    tg_Combox1.clear()
    tg_Combox2.clear()
    for i in range(tg_table[0]):
        tg_Combox1.append("S" + str(i))
        tg_Combox2.append("S" + str(i))
    tg_nbrDepart.configure(values=tg_Combox1)
    tg_nbrAllez.configure(values=tg_Combox2)
    tg_rightframe.place_forget()
    writemat(mat, tg_table[0])
    tg_leftframe.place(x=30, y=200)
    i = u
    root.after(0, tg_loading)
    root.after(0, tg_newIdea2)


def tg_next():
    global tg_i
    ln = imputGF()
    if tg_table[0] != len(ln):
        return
    i = tg_i - 1
    mat[i] = ln
    print(mat)
    tg_i += 1
    tg_nbrlines.configure(text="ligne : " + str(tg_i))
    tg_nbrlinesRe.configure(text="lignes restant: " + str(tg_table[0] - tg_i))
    tg_preB.place(x=300, y=56)
    tg_nextB.place(x=300, y=6)
    tg_rightframe.place(x=500, y=60)
    if tg_table[0] == tg_i:
        tg_valid.place(x=300, y=6)
        tg_nextB.place_forget()
        tg_preB.place(x=300, y=56)


def tg_pre():
    global tg_i
    tg_i -= 1
    tg_nbrlines.configure(text="ligne : " + str(tg_i))
    tg_nbrlinesRe.configure(text="lignes restant: " + str(tg_table[0] - tg_i))
    tg_valid.place_forget()
    tg_nextB.place(x=300, y=6)
    if tg_i == 1:
        tg_valid.place_forget()
        tg_preB.place_forget()
        tg_nextB.place(x=270, y=35)


def tg_valider3():
    if os.path.exists("graphrbib-1.png"):
        os.remove("graphrbib-1.png")
    if os.path.exists("graphrbib.pdf"):
        os.remove("graphrbib.pdf")
    g = Graph()
    global mat
    graph = mat
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0:
                graph[i][j] = 100000
    if tg_nbrDepart.get() not in tg_Combox1:
        return
    if tg_nbrAllez.get() not in tg_Combox2:
        return
    frm = int(tg_nbrDepart.get()[1])
    to = int(tg_nbrAllez.get()[1])
    test = g.dijkstra(graph, frm)
    poid = 0
    for i in range(len(test[to]) - 1):
        poid += mat[test[to][i]][test[to][i + 1]]
    print(poid)
    writepath(to, test)
    tg_leftframe.place(x=30, y=200)
    i = u
    root.after(0, tg_loading)
    root.after(0, tg_newIdea2)


root = Tk()
root.geometry("1200x605")
root.configure(bg='black', bd=0)
root.minsize(1200, 605)
root.maxsize(1200, 605)
global n
mainFrame = LabelFrame(root, bd=0)
mainFrame.pack(fill="both", expand="yes")
btnFrames = []
ailph = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
u = 3000
# _________________Main Frame ____________________
tgImg = PhotoImage(file="tg.png")
anImg = PhotoImage(file="an.png")
sdImg = PhotoImage(file="sd.png")
bgA = PhotoImage(file="bgA.png")
logo = PhotoImage(file="logo.png")
loadgif = PhotoImage(file="loadgif.gif", format="gif")
label = Label(mainFrame, image=bgA)
label.place(x=0, y=0)

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
pre = PhotoImage(file="pre.png")
empl = PhotoImage(file="empiler.png")
depl = PhotoImage(file="depiler.png")
down = PhotoImage(file="down.png")
loadgift = [PhotoImage(file="loadgif.gif", format=f"gif -index {i}") for i in range(8)]
loading = []
for i in range(10):
    loading.append(PhotoImage(file="loading" + str(i) + ".png"))
count = 0
anim = None
precedant = []
leftFrame = []
home = []
rightFrame = []
fixedRightFrame = []
leftBtn = []
btn = []
for i in range(3):
    btnFrames.append(LabelFrame(root))
    leftFrame.append(LabelFrame(btnFrames[i], width=300, height=600, bd=0, bg="#cbcbe5"))
    leftFrame[i].place(x=0, y=0)
    leftLabel = Label(leftFrame[i], image=sdBtnImg, bg="#cbcbe5", bd=0)
    leftLabel.place(x=0, y=0)
    home.append(
        Button(leftFrame[i], activebackground="#cbcbe5", bg="#cbcbe5", image=accueil, bd=0, height=100, width=100,
               command=homeClick))
    home[i].place(x=50, y=25)
    fixedRightFrame.append(LabelFrame(btnFrames[i], bg="#cbcbe5", width=1010, height=600, bd=0))
    fixedRightFrame[len(fixedRightFrame) - 1].place(x=190, y=0)
for i in range(2):
    rightFrame.append(LabelFrame(btnFrames[0], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame) - 1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame) - 1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
    btn.append(PhotoImage(file="btn" + str(i) + ".png"))
    leftBtn.append(
        Button(btnFrames[0], image=btn[i], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0))
    leftBtn[i].place(x=25, y=200 + i * 75)
for i in range(4):
    rightFrame.append(LabelFrame(btnFrames[1], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame) - 1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame) - 1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
    btn.append(PhotoImage(file="btn" + str(i + 2) + ".png"))
    leftBtn.append(
        Button(btnFrames[1], image=btn[i + 2], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0))
    leftBtn[i + 2].place(x=25, y=125 + i * 75)
for i in range(3):
    rightFrame.append(LabelFrame(btnFrames[2], bg="#cbcbe5", width=1010, height=600, bd=0))
    rightFrame[len(rightFrame) - 1].place(x=190, y=0)
    sdRbg = Label(rightFrame[len(rightFrame) - 1], image=rightImg, bg="#cbcbe5")
    sdRbg.pack()
    btn.append(PhotoImage(file="btn" + str(i + 6) + ".png"))
    leftBtn.append(
        Button(btnFrames[2], image=btn[i + 6], bg="#cbcbe5", activebackground="#cbcbe5", width=150, height=50, bd=0))
for i in range(3):
    precedant.append(
        Button(rightFrame[i + 6], bg="#21222d", activebackground="#21222d", fg="black", image=pre, width=150, height=50,
               bd=0, command=preClick))
    precedant[i].place(x=100, y=525)
leftBtn[0].configure(command=grapheClick)
leftBtn[1].configure(command=arbreClick)
leftBtn[2].configure(command=an_newtonclick)
leftBtn[6].configure(command=pileClick)
leftBtn[7].configure(command=fileClick)
leftBtn[8].configure(command=llClick)
rightFrame.append(LabelFrame(btnFrames[2], bg="#cbcbe5", width=1010, height=600, bd=0))
rightFrame[len(rightFrame) - 1].place(x=190, y=0)
sdRbg = Label(rightFrame[len(rightFrame) - 1], image=rightImg, bg="#cbcbe5")
sdRbg.pack()
# leftBtn[i + 6].place(x=25, y=150 + i * 75)

pileFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)
fileFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)
llFrame = LabelFrame(btnFrames[2], bg="#1fa0b8", width=1000, height=600, bd=0)

sdLabel = Label(rightFrame[9], text="création d'une structure de données :", bg="#21222d", font=('Arial bold', 25),
                fg="white")
sdLabel.place(x=200, y=20)
nbrLabel = Label(rightFrame[9], text="le nombre de paramètres :", bg="#21222d", font=('Arial bold', 15), fg="white")
nbrLabel.place(x=100, y=100)

nbrSpin = Spinbox(rightFrame[9], from_=1, to=3, font=('Helvetica bold', 15))
nbrSpin.bind('<Return>', clickEnter)
spinvalues = ["int", "real", "string"]
nbrSpin.place(x=400, y=100)
nbrButton = Button(rightFrame[9], image=valider, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                   command=clickNbrBtn)
nbrButton.place(x=750, y=85)
nextB = PhotoImage(file="nextB.png")
suivantB = Button(rightFrame[9], image=nextB, fg="white", bg="#21222d", activebackground="#21222d",
                  font=('Arial bold', 15), width=145, height=45, bd=0, command=next)
errorLabel = Label(rightFrame[9], text="", font=('Arial bold', 13), bg="#21222d")
errorLabel.place(x=400, y=140)
errorLabel2 = Label(rightFrame[6], text="", font=('Arial bold', 13), bg="#21222d", fg="red")
errorLabel2.place(x=200, y=200)
errorLabel3 = Label(rightFrame[6], text="", font=('Arial bold', 13), bg="#21222d", fg="red")
errorLabel3.place(x=200, y=200)
typesL = []
typesB = []
namesL = []
namesB = []
types = []
names = []

# _______________pile frame_________________
test = PhotoImage(width=0, height=0)

pileLabels = []
pileButtons = []
pileLabel = Label(rightFrame[6], text="Piles :", bg="#21222d", font=('Arial bold', 30), fg="white")
pileLabel.place(x=200, y=20)

pileResult = PhotoImage()
empiler = Button(rightFrame[6], bg="#21222d", fg="black", activebackground="#21222d", image=empl, width=150, height=50,
                 bd=0, command=empilerClick)
empiler.place(x=100, y=300)
depiler = Button(rightFrame[6], bg="#21222d", fg="black", activebackground="#21222d", image=depl, width=150, height=50,
                 bd=0, compound="c", command=depilerClick)
depiler.place(x=300, y=300)
showFrame = LabelFrame(rightFrame[6], bg="white", width=480, height=480, bd=0)
showFrame.place(x=500, y=500, anchor=SW)
downShow = Button(rightFrame[6], bg="#21222d", fg="black", activebackground="#21222d", image=down, width=200, height=70,
                  bd=0, compound="c", command=file_save)
downShow.place(x=640, y=515)
labelP = Label(showFrame, image=pileResult)
labelGif = Label(rightFrame[6], image="", bd=0, width=48, height=48)
labelTest = []
loadingFrm = []
for i in range(10):
    loadingFrm.append(Label(rightFrame[6], image=loading[i], bg="black"))
# labelP.pack(side=BOTTOM)

# ----------------------AN-Newton---------------------------------

new_Label = Label(rightFrame[2], text="La méthode de newton:", bg="#21222d", font=('Arial bold', 25),
                  fg="white")
new_Label.place(x=200, y=20)
new_func = Label(rightFrame[2], text="La fonction:", bg="#21222d", font=('Arial bold', 15), fg="white")
new_func.place(x=80, y=80)
new_spin = Entry(rightFrame[2], font=('Helvetica bold', 15), width=12)
new_spin.place(x=250, y=80)
new_func_pr = Label(rightFrame[2], text="La dérivée :", bg="#21222d", font=('Arial bold', 15), fg="white")
new_func_pr.place(x=80, y=150)
new_spin_pr = Entry(rightFrame[2], font=('Helvetica bold', 15), width=12)
new_spin_pr.place(x=250, y=150)
new_iter = Label(rightFrame[2], text="N° itérations:", bg="#21222d", font=('Arial bold', 15), fg="white")
new_iter.place(x=80, y=220)
new_iter_spin = Spinbox(rightFrame[2], from_=1, to=20, font=('Helvetica bold', 15), width=11)
new_iter_spin.place(x=250, y=220)
new_epsilon = Label(rightFrame[2], text="Epsilon:", bg="#21222d", font=('Arial bold', 15), fg="white")
new_epsilon.place(x=80, y=290)
new_spin_epsilon = Entry(rightFrame[2], font=('Helvetica bold', 15), width=12)
new_spin_epsilon.place(x=250, y=290)
new_x0 = Label(rightFrame[2], text="   X0  :", bg="#21222d", font=('Arial bold', 15), fg="white")
new_x0.place(x=80, y=360)
new_spin_x0 = Entry(rightFrame[2], font=('Helvetica bold', 15), width=12)
new_spin_x0.place(x=250, y=360)
new_show = Button(rightFrame[2], bg="#21222d", fg="black", activebackground="#21222d", image=empl, width=150, height=50,
                  bd=0, command=new_graphe)
new_show.place(x=100, y=430)
new_tab = Button(rightFrame[2], bg="#21222d", fg="black", activebackground="#21222d", image=depl, width=150, height=50,
                 bd=0, compound="c")
new_tab.place(x=350, y=430)
new_down = Button(rightFrame[2], bg="#21222d", fg="black", activebackground="#21222d", image=down, width=200, height=70,
                  bd=0, compound="c", command=new_save)
new_down.place(x=225, y=500)
new_result = LabelFrame(rightFrame[2], bg="white", height=420, width=420, bd=0)
new_result.place(x=550, y=110)

new_Img = []
new_Img.append(PhotoImage(file='newtonpython.png'))
new_label = Label(new_result, image=new_Img[0], bg="white", width=400, height=400, bd=0)
new_Gif = Label(rightFrame[2], image="", bd=0, width=48, height=48)
# ----------------Ar----------------------
ar_option = []
ArbreLabel = Label(rightFrame[1], text="création d'une Arbre :", bg="#21222d", font=('Arial bold', 25),
                   fg="white")
ArbreLabel.place(x=200, y=20)
nbrar = Label(rightFrame[1], text="le premier Noeud:", bg="#21222d", font=('Arial bold', 15), fg="white")
nbrar.place(x=100, y=80)

Spinarbre = Entry(rightFrame[1], font=('Helvetica bold', 15), width=12)
Spinarbre.place(x=400, y=80)
nbrButton = Button(rightFrame[1], image=valider, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                   command=addNoeud)
nbrButton.place(x=750, y=65)
ar_father = Label(rightFrame[1], text="father name:", bg="#21222d", font=('Arial bold', 12), fg="white")
cb = Combobox(rightFrame[1], values=ar_option, font=('Arial bold', 15), width=13)
ar_child = Label(rightFrame[1], text="child name:", bg="#21222d", fg="white", font=('Arial bold', 12))
ar_spin = Entry(rightFrame[1], font=('Helvetica bold', 15), width=14)
ar_next = PhotoImage(file="nextB.png")
ar_suivant = Button(rightFrame[1], image=nextB, fg="white", bg="#21222d", activebackground="#21222d",
                    font=('Arial bold', 15), width=145, height=45, bd=0, command=addchild)
ar_Show = Button(rightFrame[1], bg="#21222d", fg="black", activebackground="#21222d", image=down, width=200, height=70,
                 bd=0, compound="c", command=ar_save)
ar_error = Label(rightFrame[1], text="Ce Noeud Déja existe", bg="#21222d", fg="red")
ar_error2 = Label(rightFrame[1], text="Ce Noeud père n'existe pas ", bg="#21222d", fg="red")
ar_result = LabelFrame(rightFrame[1], bg="white", height=420, width=420, bd=0)
ar_result.place(x=500, y=150)
ar_Img = []
ar_Img.append(PhotoImage(file='tst.png'))
ar_label = Label(ar_result, image=ar_Img[0], bg="white", width=400, height=400, bd=0)
ar_Gif = Label(rightFrame[1], image="", bd=0, width=48, height=48)
# _______________TG_______________________

sdLabel = Label(rightFrame[0], text="creation d'un graphe :", bg="#21222d", font=('Arial bold', 20), fg="white")
sdLabel.place(x=300, y=20)
tg_nbrLabel = Label(rightFrame[0], text="nombre des sommets:", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_nbrLabel.place(x=40, y=110)
tg_nbrSpingf = Entry(rightFrame[0], font=('Helvetica bold', 17), width=6)
tg_nbrSpingf.place(x=210, y=110)
tg_rightframe = LabelFrame(rightFrame[0], bg="#21222d", height=150, width=500, bd=0)
tg_leftframe = LabelFrame(rightFrame[0], bg="#21222d", height=300, width=400, bd=0)
tg_i = 1
tg_nbrlines = Label(tg_rightframe, text="ligne " + str(tg_i) + " :", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_nbrlines.place(x=10, y=50)
tg_lignentry = Entry(tg_rightframe, font=('Helvetica bold', 17), width=12)
tg_lignentry.place(x=100, y=45)
tg_nbrlinesRe = Label(tg_rightframe, text="ligne restant :", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_nbrlinesRe.place(x=100, y=75)
tg_nbrButton = Button(rightFrame[0], image=valider, width=150, activebackground="#21222d", height=50, bd=0,
                      bg="#21222d", command=tg_valider)
tg_nbrButton.place(x=300, y=97)
tg_nextB = Button(tg_rightframe, image=nextB, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                  command=tg_next)
tg_nextB.place(x=300, y=6)
tg_preB = Button(tg_rightframe, image=pre, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                 command=tg_pre)
tg_preB.place(x=300, y=56)
tg_valid = Button(tg_rightframe, image=valider, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                  command=tg_valider2)
tg_valid.place(x=270, y=35)
tg_nbrLabel = Label(tg_leftframe, text="Parcour :", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_nbrLabel.place(x=30, y=100)
tg_depard = Label(tg_leftframe, text="Depart :", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_depard.place(x=120, y=100)
tg_Combox1 = []
tg_Combox2 = []
tg_nbrDepart = Combobox(tg_leftframe, font=('Helvetica bold', 17), width=6, values=tg_Combox1)
tg_nbrDepart.place(x=200, y=100)
tg_allez = Label(tg_leftframe, text="Vers :", bg="#21222d", font=('Arial bold', 12), fg="white")
tg_allez.place(x=120, y=150)
tg_nbrAllez = Combobox(tg_leftframe, font=('Helvetica bold', 17), width=6, values=tg_Combox2)
tg_nbrAllez.place(x=200, y=150)
tg_parcour = Button(tg_leftframe, image=valider, width=150, activebackground="#21222d", height=50, bd=0, bg="#21222d",
                    command=tg_valider3)
tg_parcour.place(x=165, y=200)
tg_table = []
tg_Img = []
tg_Img.append(PhotoImage(file='tst.png'))
tg_result = LabelFrame(rightFrame[0], bg="white", width=420, height=420, bd=0)
tg_label = Label(tg_result, image=tg_Img[0], bg="white", width=400, height=400, bd=0)
tg_Gif = Label(rightFrame[0], image="", bd=0, width=48, height=48)

# _____________home click____________________


root.mainloop()
