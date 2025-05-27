# 🇬🇧 English Version

# 🎾 Perceptron from Scratch for Tennis Match Prediction

This project implements a **Perceptron model** from scratch using Python and NumPy, to predict if **Player A will win a tennis match** based on features from the CSV file `tennis_matches.csv`.

No machine learning libraries like Scikit-Learn are used for training, as the entire model (weights, bias, training) is manually coded to deeply understand its functioning.

## 📚 Description

The model uses data such as the match surface (pre-converted to binary variables) and other match features. The perceptron algorithm adjusts weights and bias on each iteration by comparing the prediction to the actual value. Performance is evaluated using `accuracy_score` and `confusion_matrix`.

## 🧰 Technologies Used

- Python 3.x
- NumPy
- pandas
- scikit-learn (only for evaluation metrics)

## ⚙️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/ehm435/tennis-match-predictor-perceptron.git
   cd tennis-match-predictor-perceptron
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure `tennis_matches.csv` is in the same directory**. The CSV should include columns like:
   - `surface_hard`
   - `surface_clay`
   - `surface_grass`
   - `other_features...`
   - `winner` (1 for Player A win, 0 otherwise)

## ▶️ How to Run

Run the main script from terminal:

```bash
python tennis-match-predictor-perceptron.py
```

The script will train the model, show the weight evolution, and evaluate it with standard metrics.

## 💡 Example Output

```
Training Perceptron model...
Iteration 1: Global Error = 5
Iteration 2: Global Error = 3
...
Model Evaluation:
Accuracy: 0.85
Confusion Matrix:
[[20  5]
 [ 3 22]]
```

## 🚀 Possible Improvements

- Add cross-validation
- Visualize error evolution per iteration
- Implement Early Stopping
- Add preprocessing pipeline
- Extend model for multiclass classification (e.g., predict among more than two players)

---


---

# 🇪🇸 Versión en Español

# 🎾 Perceptrón desde cero para partidos de tenis

Este proyecto implementa desde cero, con Python y NumPy, un modelo de **Perceptrón** para predecir si el **Jugador A ganará un partido de tenis**, a partir de características extraídas del archivo CSV `tennis_matches.csv`.

No se utilizan librerías de machine learning como Scikit-Learn, ya que todo el modelo (pesos, sesgo, entrenamiento) está programado manualmente para entender a fondo su funcionamiento.

## 📚 Descripción

El modelo recibe datos como la superficie del partido (convertida previamente a variables binarias) y otras características relevantes del encuentro. A través del algoritmo del perceptrón, se ajustan los pesos y el sesgo en cada iteración comparando la predicción con el valor real. El rendimiento se evalúa mediante `accuracy_score` y `confusion_matrix`.

## 🧰 Tecnologías utilizadas

- Python 3.x
- NumPy
- pandas
- scikit-learn (solo para métricas de evaluación)

## ⚙️ Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/ehm435/tennis-match-predictor-perceptron.git
   cd tennis-match-predictor-perceptron
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Asegúrate de tener el archivo `tennis_matches.csv` en el mismo directorio**. El CSV debe contener columnas como:
   - `surface_hard`
   - `surface_clay`
   - `surface_grass`
   - `other_features...`
   - `winner` (donde 1 indica victoria del jugador A, y 0 lo contrario)

## ▶️ Cómo ejecutar

Desde consola, ejecuta el script principal:

```bash
python tennis-match-predictor-perceptron.py
```

El script entrenará el modelo, mostrará la evolución de pesos y finalmente evaluará el rendimiento con métricas estándar.

## 💡 Ejemplo de uso

```
Entrenando modelo Perceptrón...
Iteración 1: Error global = 5
Iteración 2: Error global = 3
...
Evaluación del modelo:
Accuracy: 0.85
Matriz de confusión:
[[20  5]
 [ 3 22]]
```

## 🚀 Posibles mejoras

- Añadir validación cruzada (cross-validation)
- Visualizar la evolución del error por iteración
- Implementar Early Stopping
- Añadir un pipeline para preprocesamiento automático del dataset
- Adaptar el modelo para clasificación multiclase (Ej: predicción del ganador entre más de dos jugadores)

---


