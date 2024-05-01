# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


"""3.1. La phase de préparation de données:"""

'''***************Prétraitement :**********************'''
data= pd.read_csv("cancer_des_poumons.csv")

print("le nombre des observations dans la base est : ",data.shape[0])
print("le nombre des caractéristiques dans la base est : ",data.shape[1])
data['GENDER'].fillna(data['GENDER'].mode()[0], inplace=True)

numeric_columns = data.select_dtypes(include=['number']).columns
if data.isna().values.any():
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
    print("Les valeurs manquantes ont été remplacées par la moyenne de chaque colonne.")
else:
    print("Il n'y a pas de valeurs manquantes dans la base de données.")


'''*************Transformations :***************'''

means = data[numeric_columns].mean()
stds = data[numeric_columns].std()

if all(abs(means) < 1e-8) and all(abs(stds - 1) < 1e-8):
    print("la base est déjà normalisée  (centrée-réduite).")
else:
    print("la base n'est pas normalisée. Effectuer la normalisation...")

    # Normalize the dataset (centering and scaling)
    normalized_data = (data[numeric_columns] - means) / stds

    # Update original DataFrame with normalized data
    data[numeric_columns] = normalized_data

    print("Normalisation terminée.")


correlation_matrix = data[numeric_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Matrix')
plt.show()


most_correlated_pairs = correlation_matrix.unstack().sort_values(key=lambda x: abs(x), ascending=False)


most_correlated_pairs = most_correlated_pairs[most_correlated_pairs.index.get_level_values(0) != most_correlated_pairs.index.get_level_values(1)]


top_correlated_pairs = most_correlated_pairs.head(3)

print("Top correlated variable pairs:")
print(top_correlated_pairs)



"""3.2. La phase d’extraction des caractéristiques"""

# Apply PCA to the normalized dataset
pca = PCA(n_components=len(numeric_columns))  # Keep all components
pca.fit(normalized_data)

# Get the eigenvalues
eigenvalues = pca.explained_variance_

# Print eigenvalues and their interpretation
print("Eigenvalues:")
for i, eigenvalue in enumerate(eigenvalues, start=1):
    print(f"Eigenvalue {i}: {eigenvalue:.4f}")

# Plot the explained variance ratio
plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o', linestyle='-')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance Ratio')
plt.grid(True)
plt.show()




# Determine the number of principal components to retain
cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
components_to_retain = np.argmax(cumulative_variance_ratio >= 0.95) + 1

print(f"Number of principal components to retain to explain 95% of the variance: {components_to_retain}")





# Get the principal components (loadings)
loadings = pca.components_

# Create a DataFrame to store the loadings
loadings_df = pd.DataFrame(loadings, columns=numeric_columns)

# Plot the correlation circle
plt.figure(figsize=(8, 8))
sns.heatmap(loadings_df, cmap='coolwarm', annot=True, fmt=".2f", annot_kws={"size": 10}, square=True, cbar=False)
plt.title('Variable Loadings')
plt.show()

# Plot the correlation circle with lines to the origin and a unit circle
plt.figure(figsize=(8, 8))
plt.scatter(loadings[0, :], loadings[1, :], alpha=0.7)
for i in range(len(numeric_columns)):
    plt.text(loadings[0, i], loadings[1, i], numeric_columns[i], fontsize=10)
    plt.plot([0, loadings[0, i]], [0, loadings[1, i]], color='k', linestyle='--', linewidth=0.5)
circle = plt.Circle((0, 0), 1, color='b', fill=False)
plt.gca().add_patch(circle)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('PC1 ({}%)'.format(int(pca.explained_variance_ratio_[0]*100)))
plt.ylabel('PC2 ({}%)'.format(int(pca.explained_variance_ratio_[1]*100)))
plt.title('Correlation Circle')
plt.grid()
plt.show()











