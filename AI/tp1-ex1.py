import random

# Générer une liste aléatoire de 100 éléments entre 1 et 100
random_list = [random.randint(1, 100) for _ in range(100)]


# 1. Afficher les éléments inférieurs à 20 dans la liste aléatoire
elements_below_20 = [element for element in random_list if element < 20]
print("1. Éléments inférieurs à 20 :", elements_below_20)



# 2. Créer une nouvelle liste avec les éléments inférieurs à 20 et l'afficher
new_list_below_20 = list(filter(lambda x: x < 20, random_list))
print("\n \n 2. Nouvelle liste avec éléments inférieurs à 20 :", new_list_below_20)


# 3. Demander à l'utilisateur un nombre et renvoyer les éléments inférieurs à ce nombre
user_number = int(input("\n \n 3. Entrez un nombre : "))
elements_below_user_number = [element for element in random_list if element < user_number]
print(f"\t Éléments inférieurs à {user_number} :", elements_below_user_number)


# 4. Trouver et afficher les indices des éléments inférieurs à 20 dans la liste d'origine
indices_below_20 = [index for index, element in enumerate(random_list) if element < 20]
print("\n \n 4. Indices des éléments inférieurs à 20 :", indices_below_20)


# 5. Implémenter une fonction pour filtrer les éléments inférieurs au seuil
def filter_below_threshold(lst, threshold):
    return [element for element in lst if element < threshold]

new_list = filter_below_threshold(random_list, 20)
print("\n \n 5. Nouvelle liste avec la fonction filter_below_threshold :", new_list)


# 6. Utiliser une fonction lambda pour filtrer les éléments inférieurs à un seuil donné (k = 20)
filtered_list_lambda = list(filter(lambda x: x < 20, random_list))
print("\n \n 6. Liste filtrée avec une fonction lambda :", filtered_list_lambda)


# 7. Calculer la somme des éléments inférieurs à 20 dans la liste d'origine
sum_below_20 = sum(element for element in random_list if element < 20)
print("\n \n 7. Somme des éléments inférieurs à 20 :", sum_below_20)
