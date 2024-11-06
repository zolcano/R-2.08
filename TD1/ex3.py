from sys import argv
import os

def aide():
    print("# -----\n# argument invalide ou non présent.\n# donnez un chemin d'accès valide en argument.\n# -----")

def recherche(dossier):
    listeDossiers = []
    listeFichiers = []
    liste = os.listdir(dossier)
    for i in range(len(liste)):
        print(liste[i]+'/')
        if os.path.exists(dossier+liste[i]+'/') :
            listeDossiers.append(dossier + liste[i] + '/')
        else :
            listeFichiers.append(dossier + liste[i])
    return(listeDossiers, listeFichiers)

if __name__ == '__main__':
    if len(argv) == 1:
        aide()
    else:
        listeDossiers, listeFichiers = recherche(argv[1])

        print(f"-----\n## liste des Dossiers : ## \n{listeDossiers}\n-----")
        print(f"## liste des Fichiers : ## \n{listeFichiers}\n-----")