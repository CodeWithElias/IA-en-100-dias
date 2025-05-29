# 📅 Día 18: Validación de modelos

## 📌 ¿Qué es la validación de modelos?
Es el proceso de evaluar el rendimiento de un modelo de machine learning con datos que **no ha visto antes**, con el objetivo de estimar su capacidad de **generalización**. Es crucial para evitar **sobreajuste (overfitting)** o **subajuste (underfitting)**.

---

## 🔍 Técnicas de validación más comunes

### 1. Hold-Out
- Divide el conjunto de datos en dos partes: entrenamiento y prueba (por ejemplo 80/20).
- Simple, pero depende de qué datos caigan en cada parte.

### 2. Validación cruzada (Cross-Validation)
- Divide el conjunto en “k” partes iguales (llamadas folds).
- Se entrena el modelo con k-1 partes y se prueba con la restante.
- Repite el proceso k veces cambiando el fold de prueba.
- Finalmente se promedian los resultados.

#### ➕ Ventajas:
- Usa todos los datos para entrenamiento y prueba (en distintos momentos).
- Menos varianza en los resultados.

---

## 🔁 ¿Qué es K-Fold Cross-Validation?
- Técnica de validación cruzada en la que el conjunto se divide en **k subconjuntos (folds)**.
- Se entrena el modelo k veces, cada vez dejando un fold distinto como conjunto de prueba.
- Se calcula la media de las métricas de rendimiento (precisión, F1, etc.).

---

## 🧪 Ejemplo en Python

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
import numpy as np

# Cargamos el dataset Iris
X, y = load_iris(return_X_y=True)

# Creamos el modelo
modelo = LogisticRegression(max_iter=200)

# Definimos KFold con 5 particiones
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Aplicamos validación cruzada
resultados = cross_val_score(modelo, X, y, cv=kfold)

print("Resultados por fold:", resultados)
print("Precisión promedio:", np.mean(resultados))
```

---

## 📈 Interpretación
- Se entrena el modelo 5 veces.
- Cada vez se evalúa con un fold diferente.
- El resultado final es la media de los 5 resultados → una **estimación más confiable** de cómo se comportará el modelo con nuevos datos.

---

## ⚠️ ¿Por qué es importante?
- Evita depender de un único conjunto de prueba.
- Nos ayuda a elegir el mejor modelo y a ajustar sus hiperparámetros.
- Mide si el modelo está sobreajustando (si tiene rendimiento excelente solo en los datos de entrenamiento).