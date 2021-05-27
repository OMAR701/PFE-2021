from asymptote import *
import time
import os
def writestruct( nbr, names, types):
    filer = open("edited.asy", "r")
    lignes = filer.readlines()
    filer.close()
    lignes[0] = "int nbr="+str(nbr)+";\n"
    lignes[1] = "string[] names={"+'"'
    l = [3,7,9,13,20,23,30]
    for i in l:
        lignes[i]=""
    for i in range(int(nbr)):
        if i<nbr-1:
            lignes[1] +=names[i]+'"'+","+'"'
        lignes[3] += types[i]+"  "+names[i]+";"
        lignes[7] += types[i]+"[]"+names[i]+";"
        lignes[9] += names[i]+"[i]=m[i]."+names[i]+";"
        lignes[13] += "write(f,"+names[i]+");"
        lignes[20] += "for(int i=0;i<dim;++i){"+names[i]+"[i]=f.line();}"
        lignes[23] += "t."+names[i]+"="+names[i]+"[i];"
        lignes[30] += "t["+str(i)+"]=(string)s."+names[i]+";"

    for i in l:
        lignes[i] += "\n"
    lignes[1] += names[nbr-1]+'"'+"};\n"
    lignes[19] = lignes[7]
    filew = open("edited.asy", "w")
    filew.writelines(lignes)
    filew.close()
def executeasy():
    os.system("asy draw.asy")
def stack(etat,names,types,values):
    filer = open("bibliopile.asy", "r")
    lignes = filer.readlines()
    filer.close()
    lignes[4]=""
    for i in range(len(names)):
        lignes[4] += "t."+names[i]+"="
        if types[i]=="string":
            lignes[4] += '"'+values[i]+'"'+";"
        elif types[i]=="char":
            lignes[4] += '"' + values[i][0] + '"' + ";"
        else:
            lignes[4] +=values[i]+";"
    lignes[4]+="\n"
    filew = open("bibliopile.asy", "w")
    filew.writelines(lignes)
    filew.close()
    filew = open("draw.asy", "w")
    draw = ["include'bibliopile.asy';"+"\n","pushList();"+"\n"]
    filew.writelines(draw)
    filew.close()
    os.system("asy -V draw.asy")
def stackpop():
    draw = ["include'bibliopile.asy';" + "\n", "popList();" + "\n"]
    filew = open("draw.asy", "w")
    filew.writelines(draw)
    filew.close()
    executeasy()



print("le nombre des paramètres :")
nbr = int(input())
names = []
types = []
values = []
for i in range(nbr):
    print(" paramètres %d :" % (i + 1))
    print("    type : ")
    types.append(str(input()))
    print("    name : ")
    names.append(str(input()))
writestruct(nbr=nbr,names=names,types=types)
while True:
    print("1- push ")
    print("2- pop ")
    print("0- quit")
    s=int(input())
    if s == 1:
        for i in range(int(nbr)):
            print(names[i]+" : ")
            values.append(input())
        stack(s,names=names,types=types,values=values)
        values=[]
    elif s == 2:
            stackpop()
            values = []

    else:
        break

