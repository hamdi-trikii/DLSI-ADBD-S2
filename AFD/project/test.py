import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

data = None
data_imputed = None
data_normalized = None

def open_file():
    global data
    filepath = filedialog.askopenfilename()
    data = pd.read_csv(filepath)

def perform_preprocessing():
    global data, data_imputed, data_normalized

    n_observations, n_features = data.shape
    print("Nombre d'observations:", n_observations)
    print("Nombre de caractéristiques:", n_features)
    
    # List of numeric columns
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    
    # Appliquer mean imputation seulement aux colonnes numériques
    imputer = SimpleImputer(strategy='mean')
    data_imputed = data.copy()
    data_imputed[numeric_columns] = imputer.fit_transform(data[numeric_columns])
    
    # Convertir les caractéristiques de type chaîne de caractères en entiers
    label_encoder = LabelEncoder()
    for column in data_imputed.columns:
        if data_imputed[column].dtype == 'object':
            data_imputed[column] = label_encoder.fit_transform(data_imputed[column])
    
    # Normaliser les données
    scaler = StandardScaler()
    data_normalized = scaler.fit_transform(data_imputed)
    
    # Afficher la matrice de corrélation
    correlation_matrix = data_imputed.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation")
    plt.show()

def display_pca_results():
    global data_normalized

    pca = PCA()
    pca.fit(data_normalized)

    # Interpréter les valeurs propres
    eigenvalues = pca.explained_variance_
    explained_variance_ratio = pca.explained_variance_ratio_

    # Afficher les valeurs propres
    plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker='o')
    plt.title("Eboulis des valeurs propres")
    plt.xlabel("Composantes principales")
    plt.ylabel("Valeurs propres")
    plt.show()

    # Pourcentage d'inertie expliqué
    cumulative_variance_ratio = explained_variance_ratio.cumsum()
    print("Pourcentage d'inertie expliqué par les composantes:")
    print(cumulative_variance_ratio)

    # Afficher la saturation des variables
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
    loading_matrix = pd.DataFrame(loadings, columns=[f"PC{i+1}" for i in range(len(eigenvalues))], index=data_imputed.columns)
    print("Matrice de saturation des variables:")
    print(loading_matrix)

    # Tracer le cercle de corrélation
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    circle = plt.Circle((0,0), 1, color='blue', fill=False)
    ax.add_artist(circle)
    for idx, (x, y) in enumerate(zip(pca.components_[0, :], pca.components_[1, :])):
        plt.plot([0, x], [0, y], color='k')
        plt.text(x, y, data_imputed.columns[idx], fontsize='9')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.title("Cercle de corrélation")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()

def display_clustering_results():
    global data_normalized

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(data_normalized)
    cluster_labels = kmeans.labels_

    # Afficher les résultats de K-means
    plt.scatter(data_normalized[:, 0], data_normalized[:, 1], c=cluster_labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', s=300, c='red', label='Centroïdes')
    plt.title("Résultats de K-means")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.legend()
    plt.show()

    # Appliquer l'algorithme Classification Ascendante Hiérarchique (CAH)
    agglomerative = AgglomerativeClustering(n_clusters=2)
    agglomerative.fit(data_normalized)
    agglomerative_labels = agglomerative.labels_

    # Afficher les résultats de CAH
    plt.scatter(data_normalized[:, 0], data_normalized[:, 1], c=agglomerative_labels, cmap='viridis')
    plt.title("Résultats de la CAH")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.show()

    # Comparer les résultats des deux algorithmes de clustering
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(data_normalized[:, 0], data_normalized[:, 1], c=cluster_labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='*', s=300, c='red', label='Centroïdes')
    plt.title("Résultats de K-means")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(data_normalized[:, 0], data_normalized[:, 1], c=agglomerative_labels, cmap='viridis')
    plt.title("Résultats de la CAH")
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    plt.tight_layout()
    plt.show()

# Créer l'interface graphique
root = tk.Tk()
root.title("Système de reconnaissance de la maladie des poumons")

# Boutons pour importer le fichier et effectuer les prétraitements
btn_load_file = tk.Button(root, text="Importer la base de données", command=open_file)
btn_load_file.pack()

btn_preprocess = tk.Button(root, text="Effectuer les prétraitements", command=perform_preprocessing)
btn_preprocess.pack()

# Boutons pour afficher les résultats de l'ACP et des méthodes de regroupement
btn_display_pca = tk.Button(root, text="Afficher les résultats de l'ACP", command=display_pca_results)
btn_display_pca.pack()

btn_display_clustering = tk.Button(root, text="Afficher les résultats du clustering", command=display_clustering_results)
btn_display_clustering.pack()

root.mainloop()
