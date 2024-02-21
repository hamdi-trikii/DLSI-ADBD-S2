import json
"""


# 1. Créez un dictionnaire contenant les noms et les anniversaires des personnes.
birthday_dict = {
    "Albert Einstein": "14/03/1879",
    "Benjamin Franklin": "17/01/1706",
    "Ada Lovelace": "10/12/1815"
}

# 2. Demandez à l'utilisateur d'entrer un nom.
print("Bienvenue dans le dictionnaire d'anniversaire. Nous connaissons les anniversaires de :")
for name in birthday_dict:
    print("\t *",name)

user_input = input("\nDe qui voulez-vous connaître l'anniversaire ? \n \n")

# 3. Recherchez dans le dictionnaire l'anniversaire associé à ce nom et affichez-le.
if user_input in birthday_dict:
    print(f"L'anniversaire de {user_input} est le {birthday_dict[user_input]}.")
else:
    print(f"Nous ne connaissons pas l'anniversaire de {user_input}.")


"""
"""PARTIE 2:"""

"""
# 1. Chargez le dictionnaire d'anniversaire à partir d'un fichier JSON.
with open("birthday_data.json", "r") as file:
    birthday_dict = json.load(file)
print(birthday_dict)
# 2. Demandez à l'utilisateur d'ajouter un nouveau nom et son anniversaire.
new_name = input("\n \n Entrez le nom du nouveau scientifique : ")
new_birthday = input("Entrez la date d'anniversaire (format : JJ/MM/AAAA) : ")

# 3. Mettez à jour le fichier JSON avec le nouveau nom et l'anniversaire.
birthday_dict[new_name] = new_birthday

with open("birthday_data.json", "w") as file:
    json.dump(birthday_dict, file)

print("Le dictionnaire a été mis à jour avec le nouveau nom et l'anniversaire.")


"""
"""PARTIE 3:"""

# 1. Chargez le fichier JSON contenant les anniversaires des scientifiques.
with open("birthday_data.json", "r") as file:
    birthday_dict = json.load(file)

# 2. Parcourez les anniversaires, extrayez les mois et comptez combien de scientifiques ont un anniversaire chaque mois.
months_count = {}
for name, birthday in birthday_dict.items():
    month = birthday.split('/')[1]
    if month in months_count:
        months_count[month] += 1
    else:
        months_count[month] = 1

# 3. Affichez le nombre de scientifiques ayant un anniversaire pour chaque mois.
for month, count in months_count.items():
    print(f"{month}: {count} scientifique(s)")




"""PARTIE 4:"""

import matplotlib.pyplot as plt

# 1. Chargez le fichier JSON contenant les anniversaires des scientifiques.
with open("birthday_data.json", "r") as file:
    birthday_dict = json.load(file)

# 2. Parcourez les anniversaires, extrayez les mois et stockez-les dans une liste.
months_list = [birthday.split('/')[1] for birthday in birthday_dict.values()]

# 3. Utilisez la bibliothèque Matplotlib pour tracer un histogramme montrant la distribution des anniversaires par mois.
plt.hist(months_list, bins=range(1, 14), edgecolor='black', alpha=0.7)
plt.xlabel('Mois')
plt.ylabel('Nombre de scientifiques')
plt.title('Distribution des anniversaires par mois')
plt.xticks(range(1, 13))
plt.show()

