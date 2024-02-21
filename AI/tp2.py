import numpy as np

# 1. Importez numpy comme np et affichez le numéro de version.
print("1. NumPy version:", np.__version__)


# 2. Créez un tableau 1D « arr » de nombres de 0 à 9.
arr = np.arange(10)
print("2. Tableau 1D arr:", arr)


# 3. Extraire tous les nombres impairs de arr
odd_numbers = arr[arr % 2 != 0]
print("3. Nombres impairs de arr:", odd_numbers)


# 4. Remplacez tous les nombres impairs dans arr par -1.
arr[arr % 2 != 0] = -1
print("4. Tableau arr avec nombres impairs remplacés par -1:", arr)


# 5. Remplacez tous les nombres impairs dans arr par -1 sans changer arr.
arr = np.arange(10)
arr_with_neg_ones = np.where(arr % 2 != 0, -1, arr)
print("5. Tableau original arr:", arr)
print("   Tableau avec nombres impairs remplacés par -1 sans changer arr:", arr_with_neg_ones)


# 6. Convertir le tableau arr en un tableau 2D avec 2 lignes.
arr_2d = arr.reshape(2, -1)
print("6. Tableau 2D avec 2 lignes:", arr_2d)

# 7. À partir du tableau 1D arr, supprimez tous les éléments présents dans le tableau b.
arr = np.array([1,2,3,4,5,6,7,8,9])
b = np.array([8,9,10,11,12])
arr = np.setdiff1d(arr, b)
print("7. Tableau arr après suppression des éléments présents dans b:", arr)

# 8. Inverser les lignes d'un tableau 2D arr.
arr = np.arange(9).reshape(3,3)
arr_inv_rows = np.flip(arr, axis=0)
print("8. Tableau 2D avec lignes inversées:", arr_inv_rows)

# 9. Inverser les colonnes d'un tableau 2D arr.
arr_inv_cols = np.flip(arr, axis=1)
print("9. Tableau 2D avec colonnes inversées:", arr_inv_cols)

# 10. Imprimez rand_arr en supprimant la notation scientifique.
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True)
print("10. Tableau rand_arr sans notation scientifique:\n", rand_arr)

# 11. Importez le jeu de données iris en conservant le texte intact.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype=None, names=('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'))
print("11. Jeu de données iris:\n", iris[:3])

# 12. Extrayez la colonne de texte 'species' du tableau 1D iris importé.
species_column = iris['species']
print("12. Colonne 'species' du tableau 1D iris:\n", species_column)

# 13. Trouver la moyenne, la médiane et l'écart-type de « sepallength » de l'iris (1ère colonne).
sepallength = iris['sepallength']
mean_sepallength = np.mean(sepallength)
median_sepallength = np.median(sepallength)
std_sepallength = np.std(sepallength)
print("13. Moyenne de sepallength:", mean_sepallength)
print("    Médiane de sepallength:", median_sepallength)
print("    Écart-type de sepallength:", std_sepallength)
