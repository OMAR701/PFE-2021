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

def writedecho(a,b,c):
    filr = open(__file__[:-8] + "an.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[42] = "pointfixe(g,"+str(a)+","+str(b)+","+str(c)+");\n"
    flew = open(__file__[:-8] + "an.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writedecho2(a,b,c):
    filr = open(__file__[:-8] + "pointfixe.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[56] = "pointfixe(g," + str(a) + "," + str(b) + "," + str(c) + ");\n"
    flew = open(__file__[:-8] + "pointfixe.asy", "w")
    flew.writelines(lignes)
    flew.close()
print("entrer la fonction : ")
print(__file__)
x = str(input())
print(x)
print("entrer x0 ")
a = input()

print("nombre d'ietation")
c = input()
print("Entrer le taux d'erreur")
b = input()
writefunct(fct=x)
writedecho(a,c,b)
os.system('cd '+__file__[:-8]+' && asy -f pdf -V an.asy')
print("do you want the tabel")
choix = input()
if choix=="yes":
    writedecho2(c,b,a)
    os.system('cd ' + __file__[:-8] + ' && asy -f pdf -V pointfixe.asy')
else :
    print("THX")
#g = asy()
#g.send("include '"+__file__[:-8]+"edit.asy'")
#g.send("include '"+__file__[:-8]+"an.asy'")
#g.send("decho("+str(a)+","+str(b)+","+str(c)+");")
