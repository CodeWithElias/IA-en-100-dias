# 🤖 Día 11: Regresión Lineal

Hoy exploramos uno de los modelos más esenciales del aprendizaje supervisado: **la regresión lineal**.

---

## 📘 ¿Qué es la regresión lineal?

La regresión lineal es una técnica estadística usada para **modelar la relación entre una variable dependiente (Y)** y **una o más variables independientes (X)**.

En su forma más simple (regresión lineal simple), busca ajustar una línea recta a los datos para predecir valores.

**Ecuación general:**

```
y = mx + b
```

Donde:  
- `y` = variable dependiente  
- `x` = variable independiente  
- `m` = pendiente de la recta  
- `b` = intercepto (ordenada al origen)

---

## 🎯 Objetivo

Predecir una variable continua basada en la relación lineal con una o más variables independientes.

---

## 📊 Ejemplo práctico

### Dataset de ejemplo:

| Horas de estudio | Calificación |
|------------------|--------------|
| 1                | 40           |
| 2                | 50           |
| 3                | 60           |
| 4                | 65           |
| 5                | 80           |

---

## 🔧 Implementación en Python

```python
#instalacion de scikit-learn
pip install scikit-learn 
# importaciones
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([40, 50, 60, 65, 80])

# Crear el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción
predicciones = modelo.predict(X)

# Visualización
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, predicciones, color='red', label='Modelo lineal')
plt.title("Regresión Lineal: Horas vs Calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.legend()
plt.grid(True)
plt.show()

# Coeficientes
print("Pendiente (m):", modelo.coef_[0])
print("Intercepto (b):", modelo.intercept_)
```

---

## 📈 ¿Cómo saber si nuestro modelo es bueno?

Se evalúa comúnmente usando el **coeficiente de determinación R²**.  
Este valor va de 0 a 1: cuanto más cercano a 1, mejor el modelo ajusta los datos.

```python
print("Score R²:", modelo.score(X, y))
```

---

## 🧠 Aplicaciones en IA

- Predicción de precios (casas, acciones, etc.)
- Modelado de series temporales
- Estimaciones continuas (temperatura, tráfico, ingresos)
- Componente base de modelos más complejos como redes neuronales

---

## 💡 Ejercicio sugerido

Implementa un modelo de regresión lineal para predecir el **precio de una casa** en función del número de habitaciones y metros cuadrados usando un conjunto de datos sintético.

---

## EXPLICACION DEL EJEMPLO PRACTICO

### 🔧 Ejemplo 1: Regresión Lineal Simple

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Creamos los datos de ejemplo
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Horas de estudio
y = np.array([40, 50, 60, 65, 80])           # Calificaciones obtenidas

# Creamos el modelo de regresión
modelo = LinearRegression()
modelo.fit(x, y)  # Entrenamos el modelo con nuestros datos

# Realizamos predicciones con el modelo entrenado
predicciones = modelo.predict(x)

# Visualización de los resultados
plt.scatter(x, y, color='blue', label='datos reales')   # Puntos originales
plt.plot(x, predicciones, color='red', label='modelo lineal')  # Línea de regresión
plt.title("Regresión lineal: horas vs calificaciones")
plt.xlabel("horas de estudio")
plt.ylabel("calificacion")
plt.legend()
plt.grid(True)
plt.show()

# Imprimimos los parámetros aprendidos por el modelo
print("Pendiente (m):", modelo.coef_[0])
print("Intercepto (b):", modelo.intercept_)
print("Score R2:", modelo.score(x, y))  # Evaluación del modelo
```

---

### 📊 Ejemplo 2: Regresión Lineal Múltiple (Ejercicio práctico)

**Escenario:** Predecir el ingreso anual de una persona basado en años de educación y experiencia laboral.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Variables independientes: [años educación, años experiencia]
X = np.array([
    [12, 1],
    [14, 2],
    [16, 4],
    [18, 5],
    [20, 7],
    [16, 3],
    [14, 5],
    [12, 2]
])

# Variable dependiente: ingreso en miles USD
y = np.array([30, 35, 50, 65, 80, 55, 48, 33])

# Creamos y entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción para una nueva persona con 17 años de educación y 6 de experiencia
nueva_persona = np.array([[17, 6]])
prediccion = modelo.predict(nueva_persona)

print("Ingreso estimado:", prediccion[0], "mil USD")

# Coeficientes y evaluación del modelo
print("Coeficientes:", modelo.coef_)         # Influencia de cada variable
print("Intercepto:", modelo.intercept_)       # Valor base sin experiencia ni educación
print("R² Score:", modelo.score(X, y))       # Calidad del ajuste
```

--- 

## 🎥 Recurso recomendado

[Regresión Lineal con Python](https://developers.google.com/machine-learning/crash-course/linear-regression?hl=es-419)

---

### 💡 Conclusión
La regresión lineal es una herramienta poderosa para encontrar relaciones entre variables y hacer predicciones numéricas. Saber usarla con múltiples variables te prepara para afrontar problemas reales en IA, ciencia de datos y negocios.

---

#100DiasDeIA #MachineLearning #RegresionLineal #AprendizajeSupervisado #PythonIA #CodeWithElias
