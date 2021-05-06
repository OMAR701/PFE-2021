from asymptote import *
import os


def writefunct(fct):
    filr = open(__file__[:-8]+"edit.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[1] = "return " + str(fct) + ";\n"
    flew = open(__file__[:-8]+"edit.asy", "w")
    flew.writelines(lignes)
    flew.close()


print("entrer la function : ")
x = str(input())
print(x)
print("entrer a et b ")
a = input()
b = input()
writefunct(fct=x)
#os.system('cd '+__file__[:-8]+' && asy -f pdf -V an.asy')
g = asy()
g.send("include '"+__file__[:-8]+"edit.asy'")
g.send("include '"+__file__[:-8]+"an.asy'")
g.send("mygraph("+str(a)+","+str(b)+");")
