from sys import argv
import os

def aide():
    print("# -----\n# argument invalide ou non présent.\n# donnez un chemin d'accès valide en argument.\n# -----")

def affiche(dir):
    return(os.listdir(dir))

if __name__=='__main__':
    if len(argv) == 1:
        aide()
    else :
        if os.path.exists(argv[1]) == True:
            print(affiche(argv[1]))
        else:
            aide()