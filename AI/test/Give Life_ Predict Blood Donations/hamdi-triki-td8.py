# -*- coding: utf-8 -*-
"""
Created on Mon May  6 04:24:12 2024

@author: Hamdi
"""
from sklearn import metrics
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm




transfusion = pd.read_csv('transfusion.data')
print(transfusion.head())


target = pd.DataFrame(transfusion["whether he/she donated blood in March 2007"], columns=["whether he/she donated blood in March 2007"])
print(target.head())







def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    epsilon = 1e-10  # Small constant to avoid division by zero
    mask = y_true != 0  # Mask to filter out zero true values
    return np.mean(np.abs((y_true[mask] - y_pred[mask]) / (y_true[mask] + epsilon))) * 100


def predict(x):
    return model.slope * x + model.intercept

def regression(X,Y):
    
    print("--------------------------------------------------")
    model = sm.OLS(Y, X).fit()
    # Évaluation du modèle
    prediction = model.predict(X) 

    model.summary()
    mae= metrics.mean_absolute_error(Y,prediction)
    mse = metrics.mean_squared_error(Y,prediction)
    mape = mean_absolute_percentage_error(Y,prediction)

    print("Mean Absolute Error " ,  mae)
    print("Mean Square Error " , mse)
    print("Mean Absolute Percentage Error " , mape)
    fitLine =  prediction
    plt.scatter(X, Y)
    plt.plot(X, fitLine, c='r')
    plt.show()
    model.predict(0.05)
    print("--------------------------------------------------\n\n")
## 3. Régression Linéaire avec statsmodels v1
print("## 3. Régression Linéaire avec statsmodels")
print('regression for x= Frequency (times)',)
X = transfusion["Frequency (times)"]
Y = target["whether he/she donated blood in March 2007"]   
regression(X, Y)

print('regression for x= Recency (months)',)
X = transfusion["Recency (months)"]
Y = target["whether he/she donated blood in March 2007"]
regression(X, Y)  
print('regression for x= Monetary (c.c. blood) ',)
X = transfusion["Monetary (c.c. blood)"]
Y = target["whether he/she donated blood in March 2007"]
regression(X, Y)  
print('regression for x= Time (months)',)
X = transfusion["Time (months)"]
Y = target["whether he/she donated blood in March 2007"]
regression(X, Y)  

"""------------------------------------------------------------------"""
#7. Entraînez un nouveau modèle de régression linéaire avec seulement les attributs les plus dominants sélectionnés.
dominant_attributes = ["Frequency (times)", "Monetary (c.c. blood)"]

# Training new regression model with selected dominant attributes
print("Training new regression model with selected dominant attributes:")
X_selected = transfusion[dominant_attributes]
model_selected = sm.OLS(Y, X_selected).fit()

# Evaluating the new model
print("\nSummary of Model with Selected Dominant Attributes:")
print(model_selected.summary())

# Plotting regression lines for selected dominant attributes
for feature in dominant_attributes:
    X = transfusion[feature]
    plt.scatter(X, Y)
    plt.plot(X, model_selected.predict(X_selected), c='r')
    plt.xlabel(feature)
    plt.ylabel("whether he/she donated blood in March 2007")
    plt.title(f"Regression for {feature}")
    plt.show()











