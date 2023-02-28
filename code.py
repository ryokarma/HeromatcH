# afficher mot random parmis une liste
import random

word_list = ["mot1", "mot2", "mot3", "mot4", ...]

random_word = random.choice(word_list)

print(random_word)


# aller chercher mots dans fichier texte pour inclure dans une liste
with open("nom_du_fichier.txt", "r") as file:
    word_list = file.read().split()

print(word_list)

#Vous pouvez également utiliser une boucle for pour parcourir la liste et construire une nouvelle liste sans l'élément que vous souhaitez supprimer :

liste = [1, 2, 3, 4, 5]
nouvelle_liste = [x for x in liste if x != 3]
print(nouvelle_liste)
#Sortie :
#[1, 2, 4, 5]

