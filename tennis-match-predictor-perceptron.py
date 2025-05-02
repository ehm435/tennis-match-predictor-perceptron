import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('tennis_matches.csv')
df = pd.get_dummies(df, columns=['surface'])
X = df.drop('A_wins', axis=1)
y = df['A_wins']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Convertimos a arrays NumPy con tipo float
X_train = X_train.to_numpy(dtype=np.float64)
X_test = X_test.to_numpy(dtype=np.float64)
y_train = y_train.to_numpy()
# Inicialización
W = np.zeros(X_train.shape[1])  # Un peso por cada feature
b = 0                           # Sesgo
lr = 0.01                       # Tasa de aprendizaje
epochs = 2000                   # Cuántas vueltas damos al dataset

# Entrenamiento
for epoch in range(epochs):
    for xi, yi in zip(X_train, y_train):
        z = np.dot(W, xi) + b               # Producto punto + sesgo
        y_pred = 1 if z >= 0 else 0         # Activación escalón
        error = yi - y_pred                 # Diferencia con valor real
        W += lr * error * xi                # Ajustar pesos
        b += lr * error                     # Ajustar sesgo

# Evaluación
test_preds = [(1 if np.dot(W, xi) + b >= 0 else 0) for xi in X_test]
print('Perceptron accuracy:', accuracy_score(y_test, test_preds))
print('Confusion matrix:\n', confusion_matrix(y_test, test_preds))

