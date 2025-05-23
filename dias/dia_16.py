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

# Etiquetas: 1 = riesgo alto, 0 = riesgo bajo
y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

# Dividimos los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo KNN con k=3 vecinos
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el modelo con los datos de entrenamiento
modelo_knn.fit(X_train, y_train)

# Realizamos predicciones con los datos de prueba
y_pred = modelo_knn.predict(X_test)

# Mostramos la precisión del modelo
print("Accuracy:", accuracy_score(y_test, y_pred))

# Mostramos el reporte de clasificación (precisión, recall, etc.)
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))

# Definimos un nuevo paciente con 6 características para predecir su clase
nuevo_paciente = np.array([[4, 4, 4, 5, 5, 5]])

# Predecimos el riesgo del nuevo paciente
pred = modelo_knn.predict(nuevo_paciente)

# Mostramos la predicción de forma legible
print(f"¿Predicción para nuevo paciente?: {'RIESGO ALTO' if pred[0] == 1 else 'RIESGO BAJO'}")

# Importamos la librería para graficar
import matplotlib.pyplot as plt

# Entrenamos el modelo solo con las dos primeras características para visualización
modelo_knn.fit(X_train[:, :2], y_train)

# Definimos el paso para la malla del gráfico
h = .02

# Obtenemos los valores mínimos y máximos del primer feature
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# Obtenemos los valores mínimos y máximos del segundo feature
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Creamos una malla de puntos en 2D
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predecimos la clase para cada punto de la malla
Z = modelo_knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)  # Ajustamos la forma para graficar

# Mostramos las regiones de decisión
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

# Dibujamos los puntos originales
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')

# Títulos y etiquetas del gráfico
plt.title("Visualización de KNN (2 features)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Mostramos el gráfico
plt.show()
