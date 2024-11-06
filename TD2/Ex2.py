fichier = open("txt.txt", "r")
for ligne in fichier:
    ligne = ligne.rstrip("\r\n")
    print(ligne)
fichier.close()