# 🧠 Día 13: Árboles de Decisión

## 🌳 ¿Qué es un Árbol de Decisión?
Un **árbol de decisión** es un algoritmo de aprendizaje supervisado utilizado tanto para clasificación como para regresión. Representa decisiones en forma de un árbol con nodos que se dividen en función de características específicas.

## 🧪 ¿Cómo funciona?
1. El árbol divide los datos en subconjuntos según el valor de una característica.
2. Estas divisiones continúan de forma recursiva hasta que se cumplen ciertos criterios (como profundidad máxima o número mínimo de muestras).
3. Las hojas del árbol representan la decisión final o predicción.

## 📈 Ventajas
- Fácil de interpretar y visualizar.
- No requiere escalado de características.
- Funciona tanto con variables categóricas como numéricas.

## ⚠️ Desventajas
- Propensos al sobreajuste si no se controlan.
- Pueden ser inestables ante pequeños cambios en los datos.

---

## 🧑‍💻 Implementación en Python

```python
# Importamos las bibliotecas necesarias
import numpy as np  # Para trabajar con arreglos numéricos
from sklearn.tree import DecisionTreeClassifier, plot_tree  # Para usar el modelo de árbol de decisión y visualizarlo
import matplotlib.pyplot as plt  # Para crear gráficos

# Creamos los datos de entrenamiento:
# x representa las horas de estudio de distintos estudiantes
# y representa si aprobaron (1) o no (0)
x = np.array([[1], [2], [3], [4], [5], [6]])  # Características (input)
y = np.array([0, 0, 0, 1, 1, 1])              # Etiquetas (output)

# Creamos el modelo de árbol de decisión
# max_depth=6 limita la profundidad del árbol para evitar sobreajuste
# random_state=0 asegura que los resultados sean reproducibles
modelo = DecisionTreeClassifier(max_depth=6, random_state=0)

# Entrenamos el modelo con nuestros datos
modelo.fit(x, y)

# Visualizamos gráficamente el árbol de decisión entrenado
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plot_tree(
    modelo, 
    filled=True,  # Colorea las hojas según la clase predicha
    feature_names=["Horas de estudio"],  # Nombre de la variable
    class_names=["No Aprueba", "Aprueba"]  # Etiquetas de salida
)
plt.title("Árbol de Decisión: Aprobación según horas de estudio")
plt.show()

# Ahora realizamos una predicción con un nuevo dato:
# Queremos saber si un estudiante que estudia 3.5 horas aprueba
nueva_hora = [[3.5]]  # Entrada nueva
prediccion = modelo.predict(nueva_hora)  # El modelo predice 0 (no aprueba) o 1 (aprueba)

# Mostramos el resultado de forma legible
print(f"¿Aprueba con 3.5h de estudio? {'Sí' if prediccion[0] == 1 else 'No'}")

```

---

## 💡 Ejercicio Propuesto
Crea un árbol de decisión que clasifique si una persona aprueba un examen considerando **dos variables**: horas de estudio y cantidad de horas dormidas la noche anterior.

1. Genera un conjunto de datos ficticios.
2. Entrena un modelo de árbol de decisión.
3. Visualiza el árbol.
4. Realiza predicciones con nuevos datos.

---

## 📦 Requisitos
```bash
pip install scikit-learn matplotlib
```

---
