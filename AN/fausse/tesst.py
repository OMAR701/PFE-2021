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
def writedecho(a,b,c,f):
    filr = open(__file__[:-8] + "an.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[35] = "faussposition(f,"+str(a)+","+str(b)+","+str(c)+","+str(d)+");\n"
    flew = open(__file__[:-8] + "an.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writedecho2(a,b,c,f):
    filr = open(__file__[:-8] + "faussetab.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[59] = "fausseposition(f," + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + ");\n"
    flew = open(__file__[:-8] + "faussetab.asy", "w")
    flew.writelines(lignes)
    flew.close()
print("entrer la fonction : ")
print(__file__)
x = str(input())
print("entrer an et bn")
a = input()
b = input()
print("nombre d'ietation")
c = input()
print("taux d'erreur")
d = input()
writefunct(fct=x)
writedecho(a,b,c,d)
os.system('cd '+__file__[:-8]+' && asy -f pdf -V an.asy')
print("do you want the tabel of iterations")
choix = input()
if choix=="yes":
    writedecho2(a, b, c, d)
    os.system('cd ' + __file__[:-8] + ' && asy -f pdf -V faussetab.asy')
else :
    print("THX")
#g = asy()
#g.send("include '"+__file__[:-8]+"edit.asy'")
#g.send("include '"+__file__[:-8]+"an.asy'")
#g.send("decho("+str(a)+","+str(b)+","+str(c)+");")
