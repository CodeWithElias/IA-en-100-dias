# 📅 Día 12: Regresión Logística

## 🎯 Objetivo del Día
Comprender la **regresión logística**, cómo se diferencia de la regresión lineal, y su uso principal: **clasificación binaria**.

---

## 🧠 ¿Qué es la Regresión Logística?

La **regresión logística** es un modelo de aprendizaje supervisado que se utiliza para predecir la **probabilidad** de que una instancia pertenezca a una clase específica. A diferencia de la regresión lineal, **la variable objetivo (Y)** en regresión logística es **categórica**, generalmente binaria (0 o 1, sí o no, positivo o negativo, etc.).

---

## 📊 ¿En qué se diferencia de la regresión lineal?

| Característica              | Regresión Lineal          | Regresión Logística            |
|----------------------------|---------------------------|---------------------------------|
| Tipo de salida             | Continua (números reales) | Probabilidad entre 0 y 1        |
| Función utilizada          | Recta                     | Función sigmoide (logística)    |
| Aplicación principal       | Predicción numérica       | Clasificación binaria           |

---

## 🧮 La Función Sigmoide

La función **sigmoide** es una curva en forma de "S" que convierte cualquier número real en un valor entre 0 y 1:

\[
f(x) = 1 / ( 1 + e^x )
\]

Donde `y = m*x + b` (como en regresión lineal).

---

## 🧪 Ejemplo en Python: Clasificación de aprobado/suspenso

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Datos: Horas de estudio vs Aprobado (1) o Reprobado (0)
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])  # Etiquetas binarias

# Creamos y entrenamos el modelo
modelo = LogisticRegression()
modelo.fit(x, y)

# Predicción de probabilidades
x_test = np.linspace(0, 7, 100).reshape(-1, 1)
probabilidades = modelo.predict_proba(x_test)[:, 1]

# Gráfica de la curva sigmoide
plt.plot(x_test, probabilidades, color='green', label='Curva sigmoide')
plt.scatter(x, y, color='red', label='Datos reales')
plt.xlabel("Horas de estudio")
plt.ylabel("Probabilidad de aprobar")
plt.title("Regresión Logística")
plt.legend()
plt.grid(True)
plt.show()

# Predicción de un nuevo dato
nueva_hora = 3.5
prob = modelo.predict_proba([[nueva_hora]])[0][1]
print(f"Probabilidad de aprobar con {nueva_hora} horas de estudio: {prob:.2f}")
```

## 🧩 ¿Qué aprende el modelo?
El modelo ajusta una función logística a los datos, aprendiendo los parámetros óptimos (m y b) que mejor separan las clases 0 y 1.

## ✅ ¿Dónde se aplica la regresión logística?
- Detección de spam
- Diagnóstico médico (enfermo / sano)
- Clasificación de sentimientos
- Predicción de abandono de clientes
- Recomendación de productos (comprar / no comprar)

## 📌 Recomendaciones para profundizar
- Probar con más datos y características.
- Aplicar evaluación con matrices de confusión.
- Explorar regularización (L1 y L2).
- Visualizar los coeficientes del modelo.

## 🎥 Recurso recomendado

[Regresión Lineal con Python](https://developers.google.com/machine-learning/crash-course/logistic-regression?hl=es-419)
