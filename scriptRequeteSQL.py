from mysql.connector import connect
from mysql.connector import Error
from subprocess import call
from menu import *

config = {
    'host':'127.0.0.1',
    'user':'root',
    'database':'LemGUI',
    'password':'6wdGPPpOe!'
}
try:
    dbConnect = connect(**config)
except Error:
    print("Error, please verify your connexion ")
curseur = dbConnect.cursor()
exi=1
dejaExecuter = dict()

def cleanTerminal():
    call('clear')

def printSelect(x):
    print("votre choix est l'option ",x,"\n")
    curseur.execute(requete[x])
    print("Votre selection est: \n")
    for elmt in curseur.fetchall():
        print(list(elmt),"\n")
    print("\n\n")
    

descRequeteCopy = descRequete.copy()
while exi>0:
    for key in descRequete.keys():
        print(key,':',descRequete[key],"\n")
    choix = input("QUE DESIREZ VOUS ? \n")
    if choix not in ["E","e","R","r","Q","q"]:
        n = int(choix)
        dejaExecuter.update({n:descRequete[n]})
        cleanTerminal()
        printSelect(n)
        del descRequete[n]
    elif choix in ["E","e"]:
        dejaExecuter.update({"R|r": descRequete["R|r"]})
        dejaExecuter.update({"Q|q":descRequete['Q|q']})
        exi=-1
        exi_e = 1
        cleanTerminal()
        while exi_e > 0:
            for key1 in dejaExecuter.keys():
                print(key1,':',dejaExecuter[key1],"\n")
            choix2 = input("QUE DESIREZ VOUS ? \n")
            if choix2 not in ["R","r","Q","q"]:
                m = int(choix2)
                cleanTerminal()
                printSelect(m)
            elif choix2 in ['R','r']:
                exi_e = -1
                descRequete = descRequeteCopy
                cleanTerminal()
                exi = 1
            elif choix2 in ['Q','q']:
                exi_e = -2
                cleanTerminal()
                print("Bye")
                choix = choix2
    elif choix in ['R','r']:
        descRequete = descRequeteCopy
        dejaExecuter.clear()
        cleanTerminal()
        exi = 1
    elif choix in ["Q","q"]:
        exi=-2
        cleanTerminal()
        print("Bye")
dbConnect.close()
