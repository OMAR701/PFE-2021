from asymptote import*
import os

def writeNoeud(Noeud1):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[0] = "TreeNode "+str(Noeud1)+" = makeNode("+str('"')+str(Noeud1)+str('"')+");\n"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writelast():
   with open('edit.asy','r') as firstfile , open('including.asy','a')as secondfile:
       for line in firstfile:
           secondfile.write(line)

def deletcontent(i):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[i] = "\\n"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writeanyNoeud(Noeud1,i,father):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[i] = "TreeNode "+str(Noeud1)+" = makeNode("+str(father)+","+str('"')+str(Noeud1)+str('"')+");\n"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()

def drawing(c,i):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[i] = "draw("+str(c)+",(0,0));"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()


stop = "yes"
i=0
while stop == "yes":
    if i==0:
       print("Enter the value")
       c = str(input())
       writeNoeud(c)
       i=i+1
    else:
         print("Enter the Noeud")
         d = str(input())
         print("Enter the father")
         m = str(input())
         writeanyNoeud(d,i,m)
         i = i + 1
         print("do you want to continue")
         stop = input()
         if stop != "yes":
             drawing(c,i)

#deletcontent()
os.system(' asy -f pdf -V tree.asy')

#writelast()
#os.system('cd '+__file__[:-8]+' && asy -f pdf -V arbre.asy')
