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

