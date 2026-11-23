def inverseBinaire(binaire):
    
    inverseB = ''                # On initialise les variables.
    nb = 0
    
    for bit in binaire:
        if bit != '0':
            inverseB += '0'
        else:
            inverseB += '1'
        nb += 1
    
    return inverseB, nb


while True:
    binaire = input("Code en Binaire à inverser: ")    #Permet de quitter la fonction si l'utilisateur le souhaite.
    if binaire == '':
        break
    else:
        inverseBinaire(binaire)         #On appele la fonction.
        print("Le code binaire " + binaire + " dont les bits sont inversés devient " + inverseBinaire(binaire)[0] + " et contient " + str(inverseBinaire(binaire)[1]) + " bits")
    