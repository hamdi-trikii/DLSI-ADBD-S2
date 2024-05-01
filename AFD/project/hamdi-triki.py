import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Initialisation des variables globales
donnees = None  # Les données brutes
donnees_imputees = None  # Les données avec les valeurs manquantes imputées
donnees_normalisees = None  # Les données normalisées

def ouvrir_fichier():
    """Fonction pour ouvrir le fichier CSV et charger les données."""
    global donnees
    chemin_fichier = filedialog.askopenfilename()  # Demander à l'utilisateur de choisir un fichier
    donnees = pd.read_csv(chemin_fichier)  # Charger les données depuis le fichier CSV

def effectuer_pretraitement():
    """Fonction pour effectuer le prétraitement des données."""
    global donnees, donnees_imputees, donnees_normalisees

    # Nombre d'observations et de caractéristiques
    nb_observations, nb_caracteristiques = donnees.shape
    print("Nombre d'observations:", nb_observations)
    print("Nombre de caractéristiques:", nb_caracteristiques)
    
    # Sélectionner les colonnes numériques
    colonnes_numeriques = donnees.select_dtypes(include=[np.number]).columns
    
    # Imputer les valeurs manquantes avec la moyenne pour les colonnes numériques
    imputeurs = SimpleImputer(strategy='mean')
    donnees_imputees = donnees.copy()
    donnees_imputees[colonnes_numeriques] = imputeurs.fit_transform(donnees[colonnes_numeriques])
    
    # Convertir les caractéristiques catégorielles en entiers
    encodeur_label = LabelEncoder()
    for colonne in donnees_imputees.columns:
        if donnees_imputees[colonne].dtype == 'object':
            donnees_imputees[colonne] = encodeur_label.fit_transform(donnees_imputees[colonne])
    
    # Normaliser les données
    normaliseur = StandardScaler()
    donnees_normalisees = normaliseur.fit_transform(donnees_imputees)
    
    # Afficher la matrice de corrélation
    matrice_correlation = donnees_imputees.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation")
    plt.show()
    most_correlated_pairs =  matrice_correlation.unstack().sort_values(key=lambda x: abs(x), ascending=False)


    most_correlated_pairs = most_correlated_pairs[most_correlated_pairs.index.get_level_values(0) != most_correlated_pairs.index.get_level_values(1)]


    top_correlated_pairs = most_correlated_pairs.head(3)

    print("Paires de variables les plus corrélées:")
    print(top_correlated_pairs)

def afficher_resultats_acp():
    """Fonction pour afficher les résultats de l'Analyse en Composantes Principales (ACP)."""
    global donnees_normalisees

    acp = PCA()
    acp.fit(donnees_normalisees)

    # Valeurs propres
    valeurs_propres = acp.explained_variance_
    ratio_variance_explicite = acp.explained_variance_ratio_

    # Eboulis des valeurs propres
    plt.plot(range(1, len(valeurs_propres) + 1), valeurs_propres, marker='o')
    plt.title("Eboulis des valeurs propres")
    plt.xlabel("Composantes principales")
    plt.ylabel("Valeurs propres")
    plt.show()

    # Pourcentage de variance expliquée
    variance_explicite_cumulative = ratio_variance_explicite.cumsum()
    print("Pourcentage d'inertie expliqué par les composantes:")
    print(variance_explicite_cumulative)

    # Matrice de saturation
    loadings = acp.components_.T * np.sqrt(acp.explained_variance_)
    matrice_saturation = pd.DataFrame(loadings, columns=[f"PC{i+1}" for i in range(len(valeurs_propres))], index=donnees_imputees.columns)
    print("Matrice de saturation des variables:")
    print(matrice_saturation)

    # Cercle de corrélation
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    cercle = plt.Circle((0,0), 1, color='blue', fill=False)
    ax.add_artist(cercle)
    for idx, (x, y) in enumerate(zip(acp.components_[0, :], acp.components_[1, :])):
        plt.plot([0, x], [0, y], color='k')
        plt.text(x, y, donnees_imputees.columns[idx], fontsize='9')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.title("Cercle de corrélation")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()

def afficher_resultats_regroupement():
    """Fonction pour afficher les résultats des méthodes de regroupement."""
    global donnees_normalisees

    # K-means
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(donnees_normalisees)
    etiquettes_cluster_kmeans = kmeans.labels_
    silhouette_kmeans = silhouette_score(donnees_normalisees, etiquettes_cluster_kmeans)
    print("Coefficient de silhouette pour K-means:", silhouette_kmeans)

    # Résultats de K-means
    plt.scatter(donnees_normalisees[:, 0], donnees_normalisees[:, 1], c=etiquettes_cluster_kmeans, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', s=300, c='red', label='Centroïdes')
    plt.title("Résultats de K-means")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.legend()
    plt.show()

    # Classification Ascendante Hiérarchique (CAH)
    agglomerative = AgglomerativeClustering(n_clusters=2)
    agglomerative.fit(donnees_normalisees)
    etiquettes_cluster_cah = agglomerative.labels_
    # Calcul du coefficient de silhouette pour CAH
    silhouette_cah = silhouette_score(donnees_normalisees, etiquettes_cluster_cah)
    print("Coefficient de silhouette pour CAH:", silhouette_cah)

    # Résultats de CAH
    plt.scatter(donnees_normalisees[:, 0], donnees_normalisees[:, 1], c=etiquettes_cluster_cah, cmap='viridis')
    plt.title("Résultats de la CAH")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()

    # Comparaison des résultats
    # Comparaison des coefficients de silhouette
    if silhouette_kmeans > silhouette_cah:
        print("K-means a un meilleur coefficient de silhouette.")
    elif silhouette_kmeans < silhouette_cah:
        print("CAH a un meilleur coefficient de silhouette.")
    else:
        print("Les deux méthodes ont des coefficients de silhouette égaux.")

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(donnees_normalisees[:, 0], donnees_normalisees[:, 1], c=etiquettes_cluster_kmeans, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', s=300, c='red', label='Centroïdes')
    plt.title("Résultats de K-means")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(donnees_normalisees[:, 0], donnees_normalisees[:, 1], c=etiquettes_cluster_cah, cmap='viridis')
    plt.title("Résultats de la CAH")
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    plt.tight_layout()
    plt.show()

# Création de l'interface graphique
racine = tk.Tk()
racine.title("Système de reconnaissance de la maladie des poumons")

# Fonction pour charger le fichier et effectuer les prétraitements
def charger_et_pretraiter():
    ouvrir_fichier()
    effectuer_pretraitement()
    # Afficher un message de confirmation
    lbl_confirmation.config(text="Prétraitement terminé avec succès !")

# Fonction pour afficher les résultats de l'ACP
def afficher_acp():
    afficher_resultats_acp()

# Fonction pour afficher les résultats des méthodes de regroupement
def afficher_regroupement():
    afficher_resultats_regroupement()

# Style pour les boutons
btn_style = {"padx": 10, "pady": 5, "bg": "#7371fc", "fg": "white", "font": ("Arial", 14)}

# Titre
lbl_title = tk.Label(racine, text="Système de reconnaissance de la maladie des poumons", font=("Arial", 16, "bold"))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

# Bouton pour charger et prétraiter les données
btn_charger_pretraiter = tk.Button(racine, text="Charger et prétraiter les données", command=charger_et_pretraiter, **btn_style)
btn_charger_pretraiter.grid(row=1, column=0, padx=5, pady=5)

# Bouton pour afficher les résultats de l'ACP
btn_afficher_acp = tk.Button(racine, text="Afficher les résultats de l'ACP", command=afficher_acp, **btn_style)
btn_afficher_acp.grid(row=2, column=0, padx=5, pady=5)

# Bouton pour afficher les résultats des méthodes de regroupement
btn_afficher_regroupement = tk.Button(racine, text="Afficher les résultats du regroupement", command=afficher_regroupement, **btn_style)
btn_afficher_regroupement.grid(row=3, column=0, padx=5, pady=5)

# Message de confirmation
lbl_confirmation = tk.Label(racine, text="", font=("Arial", 12))
lbl_confirmation.grid(row=4, column=0, columnspan=2, pady=5)

racine.mainloop()

