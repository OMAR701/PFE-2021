from asymptote import*
import os

def writeNoeud(Noeud1):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[1] = str(Noeud1)+"\n"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()
def writelast():
   with open('edit.asy','r') as firstfile , open('including.asy','a')as secondfile:
       for line in firstfile:
           secondfile.write(line)

def deletcontent():
    a_file =open("including.asy","r")
    liens = a_file.readlines()
    a_file.close()
    new_file = open("including.asy","w")
    for line in liens:
        if line.strip("\n") =="walo":
            new_file.write(line)
            new_file.close()
def writeanyNoeud(Noeud1,i):
    filr = open("including.asy", "r")
    lignes = filr.readlines()
    filr.close()
    lignes[i] = ","+str(Noeud1)+"\n );"
    flew = open("including.asy", "w")
    flew.writelines(lignes)
    flew.close()



stop = "yes"
i=1
while stop == "yes":
    if i==1:
       print("Enter the root")
       c = input()
       writeNoeud(c)
       i=i+1
    else:
        print("Enter the Noeud")
        d = input()
        writeanyNoeud(d,i)
        print("do you want to continue")
        stop = input()
        i=i+1
os.system(' asy -f pdf -V tree.asy')
deletcontent()
writelast()
#writelast()
#os.system('cd '+__file__[:-8]+' && asy -f pdf -V arbre.asy')
