# 🧠 Día 16: K-Vecinos más cercanos (KNN)

## 📌 ¿Qué es KNN?

**K-Nearest Neighbors (KNN)** es un algoritmo de aprendizaje supervisado utilizado tanto para **clasificación** como para **regresión**. Su funcionamiento se basa en un principio muy simple:

> “Para predecir la clase de un nuevo dato, busca los **K puntos más cercanos** en el conjunto de entrenamiento y clasifica según la mayoría.”

No hay fase de entrenamiento como tal en KNN. En cambio, **almacena todos los datos de entrenamiento** y utiliza la distancia para tomar decisiones en el momento de la predicción. Por eso, se le conoce como un **modelo perezoso (lazy learner)**.

## 🧭 ¿Cómo funciona?

1. **Elige el número de vecinos (K)**.
2. **Calcula la distancia** entre el nuevo punto y todos los puntos de entrenamiento.
3. **Selecciona los K vecinos más cercanos**.
4. **Clasifica o regresa** un valor en base a esos vecinos.

## 📐 Distancia Euclidiana

\[
d(A, B) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}
\]

## 📦 Ventajas de KNN

- Simple y fácil de implementar.
- No requiere suposiciones sobre los datos.
- Eficiente en conjuntos de datos pequeños.

## ⚠️ Desventajas

- Lento en predicción (requiere comparar con todos los datos).
- Sensible al ruido.
- Afectado por la dimensionalidad alta.

## 🧪 Implementación en Python

```python
# Importamos numpy para trabajar con arreglos numéricos
import numpy as np

# Importamos el clasificador KNN desde sklearn
from sklearn.neighbors import KNeighborsClassifier

# Importamos herramientas para dividir los datos
from sklearn.model_selection import train_test_split

# Importamos métricas para evaluar el modelo
from sklearn.metrics import classification_report, accuracy_score

# Creamos un conjunto de datos con 10 observaciones y 6 características cada una
X = np.array([
    [2, 4, 3, 5, 6, 7],
    [1, 2, 1, 2, 1, 2],
    [6, 5, 6, 4, 5, 5],
    [0, 1, 0, 1, 0, 1],
    [7, 8, 6, 5, 7, 8],
    [1, 0, 1, 1, 0, 1],
    [5, 5, 5, 5, 5, 5],
    [2, 1, 3, 2, 2, 1],
    [8, 7, 7, 6, 8, 7],
    [0, 0, 1, 0, 1, 0]
])

# Etiquetas de clase: 1 = riesgo alto, 0 = riesgo bajo
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

# Dividimos los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo KNN con 3 vecinos (k = 3)
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo con los datos de entrenamiento
modelo_knn.fit(X_train, y_train)

# Realizamos predicciones con los datos de prueba
y_pred = modelo_knn.predict(X_test)

# Calculamos y mostramos la precisión del modelo
print("Accuracy:", accuracy_score(y_test, y_pred))
# Output: Accuracy: 1.0 → Esto significa que el modelo acertó en el 100% de los casos de prueba.
# Nota: Con tan pocos datos de prueba (solo 2), este resultado puede no ser generalizable.

# Mostramos el reporte de clasificación completo
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
# El reporte muestra:
# - Precision: proporción de verdaderos positivos sobre positivos predichos.
# - Recall: proporción de verdaderos positivos sobre los positivos reales.
# - f1-score: media armónica entre precision y recall.
# En este caso, todos los valores son 1.00 porque el modelo clasificó correctamente los 2 ejemplos de prueba.
# Sin embargo, **debido al tamaño pequeño**, no debemos confiar ciegamente en estos resultados para casos reales.

# Definimos un nuevo paciente con 6 características para predecir su clase
nuevo_paciente = np.array([[4, 4, 4, 5, 5, 5]])

# Predecimos si el nuevo paciente es de riesgo alto (1) o bajo (0)
pred = modelo_knn.predict(nuevo_paciente)

# Mostramos el resultado de la predicción de forma comprensible
print(f"¿Predicción para nuevo paciente?: {'RIESGO ALTO' if pred[0] == 1 else 'RIESGO BAJO'}")
# En este caso, el modelo predice RIESGO ALTO, lo que indica que según sus vecinos más cercanos,
# este nuevo paciente se asemeja a casos clasificados como de riesgo alto.

# -------------------------------------
# VISUALIZACIÓN DE LOS DATOS CON KNN
# -------------------------------------

# Importamos la librería para graficar
import matplotlib.pyplot as plt

# Entrenamos un nuevo modelo KNN usando solo 2 características (las primeras) para poder visualizar
modelo_knn.fit(X_train[:, :2], y_train)

# Definimos la resolución del mapa de colores
h = .02

# Definimos el rango del eje x (feature 1)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1

# Definimos el rango del eje y (feature 2)
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Creamos una malla de puntos en el plano para evaluar el modelo en cada punto
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Usamos el modelo para predecir la clase en cada punto del plano
Z = modelo_knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)  # Reorganizamos los datos para graficar

# Mostramos las regiones del plano clasificadas por el modelo
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

# Dibujamos los puntos reales del conjunto de datos (solo 2 características)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')

# Añadimos títulos y etiquetas a los ejes
plt.title("Visualización de KNN (2 features)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Mostramos el gráfico
plt.show()

```

## 🧩 ¿Cómo elegir el valor de K?

- K pequeño → Sobreajuste.
- K grande → Subajuste.
- Usar validación cruzada para encontrar el mejor valor.
