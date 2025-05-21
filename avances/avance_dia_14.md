
# 📅 Día 14: Random Forest en el Reto de 100 días de IA

## 🌲 ¿Qué es Random Forest?

Random Forest (Bosque Aleatorio) es un algoritmo de aprendizaje supervisado que combina múltiples árboles de decisión para obtener una predicción más robusta y precisa.

- Se basa en el principio del **ensamble learning**, específicamente del método **bagging**.
- Entrena múltiples árboles de decisión sobre subconjuntos aleatorios del conjunto de entrenamiento.
- Luego combina los resultados de cada árbol (por mayoría para clasificación, promedio para regresión).

---

## 🔍 ¿Por qué usar Random Forest?

- Reduce el sobreajuste (overfitting) comparado con un solo árbol.
- Mejora la precisión del modelo.
- Es robusto ante valores atípicos y datos faltantes.
- Muy utilizado en clasificación y regresión.

---

## 🧠 Comparación con Árboles de Decisión

| Característica        | Árbol de Decisión        | Random Forest             |
|-----------------------|--------------------------|---------------------------|
| Modelo                | Único árbol              | Conjunto de árboles       |
| Precisión             | Menor (puede sobreajustar)| Mayor precisión           |
| Interpretabilidad     | Alta                     | Media (menos interpretable)|
| Riesgo de sobreajuste| Alto                     | Bajo                      |

---

## 🔧 Implementación básica en Python

```python
# Importamos las bibliotecas necesarias
import numpy as np  # Para manejo de arreglos numéricos
import matplotlib.pyplot as plt  # Para graficar
from sklearn.ensemble import RandomForestClassifier  # Modelo de Random Forest para clasificación
from sklearn.model_selection import train_test_split  # Para dividir datos en entrenamiento y prueba
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # Métricas de evaluación

# Creamos los datos de entrada (edad del usuario) y las etiquetas (0 = no compró, 1 = compró)
x = np.array([
    [18], [20], [22], [25], [28], [30], [32], [35], [38], [40],
    [42], [45], [48], [50], [52], [55], [58], [60], [62], [65]
])
y = np.array([
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1,  # Datos donde se asume que edades mayores tienden a comprar más
    0, 0, 1, 1, 0, 0, 0, 1, 1, 1
])

# Dividimos los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Creamos un modelo de Random Forest con 100 árboles y profundidad máxima de 5
modelo = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
modelo.fit(x_train, y_train)  # Entrenamos el modelo con los datos de entrenamiento

# -------- Predicción simple para una nueva edad ----------
nueva_edad = [[29]]  # Queremos predecir si una persona de 29 años comprará
pred = modelo.predict(nueva_edad)  # Predicción de clase (0 o 1)
prob = modelo.predict_proba(nueva_edad)[0][1]  # Probabilidad de que compre (clase 1)

# Mostramos el resultado de la predicción
print(f"¿Una persona de 29 años comprará el producto? {'Sí' if pred[0] == 1 else 'No'}")
print(f"Probabilidad de compra: {prob:.2f}")  # Mostramos la probabilidad con 2 decimales

# -------- Evaluación del modelo ----------
y_pred = modelo.predict(x_test)  # Predecimos con los datos de prueba

# Imprimimos métricas de evaluación del modelo
print("\n--- Evaluación del modelo ---")
print("Accuracy:", accuracy_score(y_test, y_pred))  # Precisión: porcentaje de aciertos
print("Matriz de confusión:\n", confusion_matrix(y_test, y_pred))  # Muestra TP, FP, FN, TN
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))  # Precisión, recall y F1-score

# -------- Gráfica de probabilidades para un rango de edades ----------
x_range = np.linspace(18, 65, 100).reshape(-1, 1)  # Creamos un rango de edades entre 18 y 65
probs = modelo.predict_proba(x_range)[:, 1]  # Calculamos la probabilidad de compra para cada edad

# Graficamos los resultados
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
plt.plot(x_range, probs, label="Probabilidad de compra", color="green")  # Línea de probabilidad
plt.scatter(x, y, color="blue", label="Datos reales")  # Puntos originales del dataset
plt.xlabel("Edad")  # Etiqueta del eje X
plt.ylabel("Probabilidad de compra")  # Etiqueta del eje Y
plt.title("Probabilidad de compra vs Edad (Random Forest)")  # Título del gráfico
plt.legend()  # Muestra las leyendas
plt.grid(True)  # Agrega una cuadrícula al fondo
plt.show()  # Muestra la gráfica

```

---

## 📈 Evaluación del modelo

Puedes usar `.score()`, `confusion_matrix` o `classification_report` para evaluar el modelo en conjunto de prueba.

---

## 📚 Recursos útiles

- [Documentación oficial de Scikit-learn - Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
- [Video educativo sobre Random Forest (YouTube)](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)

---

## 🧪 Ejercicio sugerido

Entrena un modelo `RandomForestClassifier` con un conjunto de datos más grande. Luego:
1. Evalúa la precisión.
2. Compara con un árbol de decisión simple.
3. Visualiza la importancia de cada característica con `.feature_importances_`.

---

¡Sigue adelante con el reto! 🚀