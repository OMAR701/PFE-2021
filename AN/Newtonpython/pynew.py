from asymptote import *
import os


def writefunct(fct,fctprime):
    filr = open(__file__[:-8]+"edit.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[1] = "return " + str(fct) + ";\n"
    lignes[4] = "return " + str(fctprime) + ";\n"
    flew = open(__file__[:-8]+"edit.asy", "w")
    flew.writelines(lignes)
    flew.close()

def writenewton(a,b,c):
    filr = open(__file__[:-8] + "newtonpython.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[50] = "newton(f,fprime,"+str(a)+","+str(b)+","+str(c)+");\n"
    flew = open(__file__[:-8] + "an.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writenewton2(a,b,c):
    filr = open(__file__[:-8] + "tab.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[57] = "newton(f,fprime," + str(a) + "," + str(b) + "," + str(c) + ");\n"
    flew = open(__file__[:-8] + "tab.asy", "w")
    flew.writelines(lignes)
    flew.close()


print("entrer la fonction : ")
print(__file__)
x = input()
print(x)
print("entrer la fonction dérivé")
print(__file__)
xprime = str(input())
print("entrer x0 ")
a = input()
print("nombre d'ietation")
b = input()
print("taux d'erreur")
c = input()
writefunct(fct=x,fctprime=xprime)
writenewton(a,b,c)

os.system('cd '+__file__[:-8]+' && asy -f pdf -V newtonpython.asy')

print("do you want the tabel ")
choix = input()
if choix =="yes":
    writenewton2(b,c,a)
    os.system('cd ' + __file__[:-8] + ' && asy -f pdf -V tab.asy')

else:
    print("THX")

#g = asy()
#g.send("include '"+__file__[:-8]+"edit.asy'")
#g.send("include '"+__file__[:-8]+"an.asy'")
#g.send("decho("+str(a)+","+str(b)+","+str(c)+");")
