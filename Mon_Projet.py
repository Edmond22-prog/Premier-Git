class Candidat (object):
    def __init__(self, ncin = None, nom = None, prenom = None, age = None, notes = [], decision = None):
        self.ncin = ncin
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.notes = notes
        self.decision = decision
        self.moyenne = sum(self.notes)/10

    def decision_finale (self):
        var = 0
        for i in range(10):
            if (self.notes[i] < 10):
                var += 1
        self.moyenne = sum(self.notes)/10
        if (self.moyenne >= 10):
            if (var == 0):
                return "Admis"
            else:
                return "Ajourné"
        else:
            return "Refusé"

def saisir ():
    "Saisie des informations d'un candidat avec réinitialisation de la liste"
    cand = Candidat()
    print("Saisie des informations du candidat...")
    cand.ncin = input("Entrer le numéro de CNI : ")
    cand.nom = input("Entrer le/les nom(s) : ")
    cand.prenom = input("Entrer le/les prénom(s) : ")
    while 1:
        try:
            cand.age = int(input("Entrer l'âge : "))
            break
        except:
            print("Entrer un âge valide s'il vous plaît !")
    print("Entrer les 10 notes : ")
    for i in range(10):
        while 1:
            try:
                note = float(input("Note "+str(i+1)+" : "))
                if (note <0 or note > 20):
                    raise ZeroDivisionError     # Sur cette ligne, on nomme l'erreur d'intervalle à ZeroDivisionError
                cand.notes.append(note)
                break
            except ZeroDivisionError:
                print("La note doit être comprise entre 0 et 20")
            except:
                print("Entrer une note valide s'il vous plaît !")
    cand.decision = cand.decision_finale()
    with open ("concours.txt", "w") as fichier:
        fichier.write("{} ; {} ; {} ; {} ; {} ; {}\n".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
    print("Enregistrement du candidat : ")
    print("{} ; {} ; {} ; {} ans ; {} ; {}".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
    print("Réussi !")

def ajouter():
    "Ajout de candidat dans la liste de concours"
    choix = "O"
    while (choix == "O"):
        choix = ""
        cand = Candidat()
        cand.notes = []
        print("Saisie des informations du candidat...")
        cand.ncin = input("Entrer le numéro de CNI : ")
        cand.nom = input("Entrer le/les nom(s) : ")
        cand.prenom = input("Entrer le/les prénom(s) : ")
        while 1:
            try:
                cand.age = int(input("Entrer l'âge : "))
                break
            except:
                print("Entrer un âge valide s'il vous plaît !")
        print("Entrer les 10 notes : ")
        for i in range(10):
            while 1:
                try:
                    note = float(input("Note "+str(i+1)+" : "))
                    if (note <0 or note > 20):
                        raise ZeroDivisionError     # Sur cette ligne, on nomme l'erreur d'intervalle à ZeroDivisionError
                    cand.notes.append(note)
                    break
                except ZeroDivisionError:
                    print("La note doit être comprise entre 0 et 20")
                except:
                    print("Entrer une note valide s'il vous plaît !")
        cand.decision = cand.decision_finale()
        try:
            fichier1 = open("concours.txt", "r")
        except:
            print("Impossible de lire, fichier introuvable. Vous devez d'abord faire l'opération Saisir.")
        else:
            fichier1.close()
            with open("concours.txt", "a") as fichier2:
                fichier2.write("{} ; {} ; {} ; {} ; {} ; {}\n".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
            print("Enregistrement du candidat : ")
            print("{} ; {} ; {} ; {} ans ; {} ; {}".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
            print("Réussi !")
        while (choix != "O"  and choix != "N"):
            choix = input("Voulez-vous encore ajouter un candidat ? O/N....")

def modifier():
    "Modifier les informations d'un candidat"
    try:
        fichier = open("concours.txt", "r")
    except:
        print("Impossible de lire, fichier introuvable. Vous devez d'abord faire l'opération Saisir.")
    else:
        i = 1
        list_fichier = fichier.readlines()
        for info in list_fichier:
            print (str(i)+" - "+info)
            i += 1
        size = len(list_fichier)
        fichier.close()
        '''print (size)'''
        while 1:
            try:
                num = int(input("Entrer le numéro de l'étudiant dont vous voulez modifier les données : "))
                if (num <= 0 or num > size):
                    raise ZeroDivisionError
                break
            except ZeroDivisionError:
                print("Le numéro entrée n'est pas valide !")
            except:
                print ("Entrer un numéro s'il vous plaît !")
        fichier = open ("concours.txt", "r")
        for x in range (1, size+1):
            import copy
            cand = Candidat()
            liste = copy.deepcopy(fichier.readline().split(" ; "))  # Liste des éléments d'une ligne
            cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision = liste[0], liste[1], liste[2], int(liste[3]), eval(liste[4]), liste[5]
            if (num == x):
                choix = menu_donnee()
                if (choix == 1):
                    cand.ncin = input("Entrer le nouveau numéro de CNI : ")
                elif (choix == 2):
                    cand.nom = input("Entrer le nouveau nom : ")
                elif (choix == 3):
                    cand.prenom = input("Entrer le nouveau prénom : ")
                elif (choix == 4):
                    while 1:
                        try:
                            cand.age = int(input("Entrer le nouvel âge : "))
                            break
                        except:
                            print("Entrer un âge valide s'il vous plaît !")
                elif (choix == 5):
                    print("Entrer les 10 nouvelles notes : ")
                    cand.notes.clear()
                    for i in range(10):
                        while 1:
                            try:
                                note = float(input("Note "+str(i+1)+" : "))
                                if (note <0 or note > 20):
                                    raise ZeroDivisionError      
                                cand.notes.append(note)
                                break
                            except ZeroDivisionError:
                                print("La note doit être comprise entre 0 et 20")
                            except:
                                print("Entrer une note valide s'il vous plaît !")
                    cand.decision = cand.decision_finale()
                else:
                    print ("Entrée non valide")
                with open ("temporaire.txt", "a") as fichier1:
                    fichier1.write("{} ; {} ; {} ; {} ; {} ; {}".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
                #break
            else:
                with open ("temporaire.txt", "a") as fichier1:
                    fichier1.write("{} ; {} ; {} ; {} ; {} ; {}".format(cand.ncin, cand.nom, cand.prenom, cand.age, cand.notes, cand.decision))
                continue
        fichier.close()
        import os
        os.remove("concours.txt")
        os.rename("temporaire.txt", "concours.txt")
        while 1:
            try:
                print ("Voulez-vous encore modifier les informations d'un candidat ?")
                print ("1. Oui\n2. Non")
                n = int(input("Votre choix : "))
            except ValueError:
                print("Entrer un nombre s'il vous plaît !")
            else:
                if (n == 1 or n == 2):
                    break
                else:
                    print ("Choix indisponible !")
        if (n == 1):
            modifier()
        else:
            print ("Fin  des modifications.")
        
def supprimerCandidat (ncin):
    "Supprime les informations du candidat dont le numéro de cni est entrée en paramètre, dans le fichier texte"
    try:
        fichier = open ("concours.txt", "r")
    except:
        print ("Impossible de lire le fichier. Fichier introuvable !")
    else:
        lignes = fichier.readlines()
        fichier.close()
        size = len(lignes)
        trouve, x = False, 1
        fichier = open ("concours.txt", "r")
        while (x <= size):
            import copy
            liste = copy.deepcopy(fichier.readline().split(" ; "))  # Liste des éléments d'une ligne
            cni, nom, prenom, age, notes, decision = liste[0], liste[1], liste[2], liste[3], liste[4], liste[5]
            x += 1
            if (cni == ncin):
                trouve = True
                continue
            else:
                with open ("tempo.txt", "a") as fichier2:
                    fichier2.write ("{} ; {} ; {} ; {} ; {} ; {}".format(cni, nom, prenom, age, notes, decision))
        fichier.close()
        if (trouve):
            print ("Suppréssion du candidat de numéro de CNI "+ncin+" effectué !")
        else:
            print ("Numéro de CNI introuvable dans la base de donnée !")
        import os
        os.remove("concours.txt")
        os.rename("tempo.txt", "concours.txt")

def admis ():
    "Génère une base de donnée des candidats admis"
    try:
        fichier = open ("concours.txt", "r")
        fichier2 = open ("admis.txt", "w")
        fichier2.close()
    except:
        print ("Impossible de lire le fichier. Fichier concours introuvable !")
    else:
        import os
        os.remove("admis.txt")
        lignes = fichier.readlines()
        fichier.close()
        size = len(lignes)
        fichier = open ("concours.txt", "r")
        for x in range (1, size+1):
            import copy
            liste = copy.deepcopy(fichier.readline().split(" ; "))  # Liste des éléments d'une ligne
            cni, nom, prenom, age, notes, decision = liste[0], liste[1], liste[2], liste[3], liste[4], liste[5]
            if (decision.find("Admis") == 0):       #Comparaison de 2 chaînes de caractères
                with open ("admis.txt", "a") as fichier2:
                    fichier2.write ("{} ; {} ; {} ; {} ; {} ; {}".format(cni, nom, prenom, age, notes, decision))
            else:
                continue
        fichier.close()
        fichier = open ("admis.txt", "r")
        lignes2 = fichier.readlines()
        size = len(lignes2)
        if (size == 0):
            print("Aucun candidat admis.")
        else:
            print ("Liste des candidats admis : ")
            for ligne in lignes2:
                print (ligne)
        fichier.close()

def attente ():
    "Génère une base de donnée des candidats mis en attente"
    try:
        fichier = open ("admis.txt", "r")
        fichier2 = open ("attente.txt", "w")
        fichier2.close()
    except:
        print ("Impossible de lire le fichier. Fichier introuvable !")
        print ("Vérifier si le fichier admis.txt existe.")
    else:
        import os
        os.remove("attente.txt")
        lignes = fichier.readlines()
        fichier.close()
        size = len(lignes)
        fichier = open ("admis.txt", "r")
        for x in range (1, size+1):
            import copy
            liste = copy.deepcopy(fichier.readline().split(" ; "))  # Liste des éléments d'une ligne
            cni, nom, prenom, age = liste[0], liste[1], liste[2], liste[3]
            if (int(age) > 20): 
                with open ("attente.txt", "a") as fichier2:
                    fichier2.write ("{} ; {} ; {}\n".format(cni, nom, prenom))
            else:
                continue
        fichier.close()
        fichier = open ("attente.txt", "r")
        lignes2 = fichier.readlines()
        size = len(lignes2)
        if (size == 0):
            print("Aucun candidat dans la file d'attente.")
        else:
            print ("Liste des candidats admis mis en attente : ")
            for ligne in lignes2:
                print (ligne)
        fichier.close()
    
def statistique (dec):
    "Détermine le pourcentage des candidats pour une décision"
    dec = dec.capitalize()
    try:
        f = open ("concours.txt", "r")
    except:
        print ("Impossile de lire le fichier. Fichier concours introuvable.")
    else:
        lignes = f.readlines()
        f.close()
        size = len(lignes)
        n = 0
        f = open ("concours.txt", "r")
        if (dec.find ("Admis") == 0):
            for x in range (1, size+1):
                import copy
                liste = copy.deepcopy(f.readline().split(" ; "))
                decision = liste[5]
                if (decision.find ("Admis") == 0):
                    n += 1
        elif (dec.find ("Ajourné") == 0):
            for x in range (1, size+1):
                import copy
                liste = copy.deepcopy(f.readline().split(" ; "))
                decision = liste[5]
                if (decision.find ("Ajourné") == 0):
                    n += 1
        elif (dec.find ("Refusé") == 0):
            for x in range (1, size+1):
                import copy
                liste = copy.deepcopy(f.readline().split(" ; "))
                decision = liste[5]
                if (decision.find ("Refusé") == 0):
                    n += 1
        else:
            print ("Mauvaise entrée de décision, impossible de calculer le pourcentage d'une telle décision !")
        f.close()
        return (n*100)/size            
    
def supprimer ():
    "Supprime du fichier admis.txt les candidats d'âge supérieur à 20"
    try:
        fichier = open ("admis.txt", "r")
    except:
        print ("Impossible de lire le fichier. Fichier introuvable !")
        print ("Vérifier si le fichier admis.txt existe.")
    else:
        lignes = fichier.readlines()
        fichier.close()
        size = len(lignes)
        fichier = open ("admis.txt", "r")
        for x in range (1, size+1):
            import copy
            liste = copy.deepcopy(fichier.readline().split(" ; "))  # Liste des éléments d'une ligne
            cni, nom, prenom, age, notes, decision = liste[0], liste[1], liste[2], liste[3], liste[4], liste[5]
            if (int(age) <= 20): 
                with open ("tempo.txt", "a") as fichier2:
                    fichier2.write ("{} ; {} ; {} ; {} ; {} ; {}".format(cni, nom, prenom, age, notes, decision))
            else:
                continue
        fichier.close()
        import os
        os.remove("admis.txt")
        os.rename("tempo.txt", "admis.txt")
        print ("Opération effectuée.")
    
def affiche_merite ():
    "Affiche les candidats par ordre de mérite"
    admis()
    f = open ("admis.txt", "r")
    lignes = f.readlines()
    f.close()
    size = len(lignes)
    f = open ("admis.txt", "r")
    candidat = []
    for x in range(1, size+1):
        import copy
        liste = copy.deepcopy(f.readline().split(" ; "))
        cand = Candidat (liste[0], liste[1], liste[2], int(liste[3]), eval(liste[4]), liste[5])
        candidat.append(cand)
    f.close()
    for i in range (len(candidat)):
        for j in range (i+1, len(candidat)-1):
            if (candidat[i].moyenne < candidat[j].moyenne):
                permutation (candidat[i], candidat[j])
    print ("\n\nAffichage des candidats par ordre de mérite :".upper())
    for i in range(len(candidat)):
        print (str(i+1)+"- "+candidat[i].nom+" "+candidat[i].prenom)
    
def recherche (cni):
    "Renvoi les informations du candidat dont on a entré le numéro de CNI"
    try:
        f = open ("concours.txt", "r")
    except:
        print ("Lecture impossible. Fichier introuvable !")
    else:
        lignes = f.readlines()
        f.close()
        size = len(lignes)
        f = open("concours.txt", "r")
        trouve = False
        for x in range (1, size+1):
            import copy
            liste = copy.deepcopy(f.readline().split(" ; "))
            ncin = liste[0]
            if (cni.find(ncin) == 0):
                trouve = True
                print ("Candidat trouvé : ")
                for elt in liste:
                    print (elt)
                break
        f.close()
        if (trouve == False):
            print ("Aucun candidat ne possède ce numéro de CNI.")
            
    
def menu_donnee ():
    "Menu des données à modifier, et renvoi le choix"
    print ("Quelle donnée voulez-vous modifier ?")
    print ("1. NCNI")
    print ("2. Nom")
    print ("3. Prénom")
    print ("4. Âge")
    print ("5. Notes")
    choix = int(input("Votre choix : "))
    return choix

def permutation (a = Candidat(), b = Candidat()):
    c = Candidat()
    # Attribution des données du candidat a au candidat b
    c.ncin = a.ncin
    c.nom = a.nom
    c.prenom = a.prenom
    c.age = a.age
    c.notes = a.notes
    c.decision = a.decision
    # Attribution des données du candidat b au candidat a
    a.ncin = b.ncin
    a.nom = b.nom
    a.prenom = b.prenom
    a.age = b.age
    a.notes = b.notes
    a.decision = b.decision
    # Attribution des données du candidat c au candidat b
    b.ncin = c.ncin
    b.nom = c.nom
    b.prenom = c.prenom
    b.age = c.age
    b.notes = c.notes
    b.decision = c.decision
    

# Programme principal :
if __name__ == "__main__":
    while 1:
        choix = 0
        print("\n")
        print ("==========|| MENU ||==========")
        print("1. Saisir")
        print("2. Ajouter")
        print("3. Modifier")
        print("4. Supprimer candidat de la base de donnée")
        print("5. Répertoire des candidats admis")
        print("6. Répertoire des candidats admis mis en attente")
        print("7. Pourcentage")
        print("8. Supprimer du fichier admis les candidats âgé de plus de 20 ans")
        print("9. Affichage des candidats admis par ordre de mérite")
        print("10. Recherche d'un candidat dans la base de donnée")
        choix = int(input("\nQuelle opération voulez-vous effectuer ?\n"))
        if (choix == 1):
            saisir()
        elif (choix == 2):
            ajouter()
        elif (choix == 3):
            modifier()
        elif (choix == 4):
            try:
                fichier = open ("concours.txt", "r")
            except:
                print ("Impossible de lire le fichier, car il est introuvable !")
            else:
                for ligne in fichier.readlines():
                    print (ligne)
                fichier.close()
            suppr_cand = input ("\nEntrer le numéro de CNI du candidat dont vous voulez supprimer les informations : ")
            supprimerCandidat (suppr_cand)
        elif (choix == 5):
            admis()
        elif (choix == 6):
            attente()
        elif (choix == 7):
            print ("\nVous voulez le pourcentage d'admis, d'ajourné ou de refusé")
            dec = input ("Votre réponse : ")
            print ("Le pourcentage de candidat "+dec+" est de "+str(statistique(dec))+" %")
        elif (choix == 8):
            supprimer()
        elif (choix == 9):
            affiche_merite()
        elif (choix == 10):
            cni = input ("\nEntrer le numéro de CNI du candidat recherché : ")
            recherche (cni)
        else:
            print("Aucune bonne entrée...")
        print ("\nVoulez-vous faire une autre opération ?\n1- Oui\n2- Non")
        choice = input("Décision : ")
        if (choice in ("1", "Oui", "oui", "Yes", "yes", "O", "o", "y", "Y")):
            continue
        else:
            print ("Fin du programme.")
            break
            






















    
        
