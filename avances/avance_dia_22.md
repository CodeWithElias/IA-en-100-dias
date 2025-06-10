
# 📘 Día 22: Perceptrón y Funciones de Activación

## 🧠 ¿Qué es un Perceptrón?
El **perceptrón** es el bloque básico de las redes neuronales artificiales. Fue propuesto por **Frank Rosenblatt en 1958** y es considerado el precursor del aprendizaje profundo.

Se basa en una idea simple:
- Recibe varias **entradas**.
- Cada entrada tiene un **peso** asignado.
- Calcula una **suma ponderada** de las entradas.
- Pasa ese valor por una **función de activación**.
- Genera una **salida binaria** (0 o 1).

## ⚙️ Arquitectura del Perceptrón

```
x1 ----\
        \        
x2 -----> (∑ x*w + b) ---> función de activación ---> salida (0 o 1)
        /
x3 ----/
```

- **x1, x2, x3**: Entradas.
- **w**: Pesos.
- **b**: Sesgo (bias).
- **Función de activación**: Decide si la neurona "se activa" o no.

## 🧪 Fórmula matemática

```
y = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)
```

- Donde `f` es la función de activación (por ejemplo: escalón, sigmoide, ReLU).
- `y` es la salida del perceptrón.

## 🔥 Funciones de Activación

Las funciones de activación permiten a las redes neuronales **introducir no linealidad**, algo crucial para resolver problemas complejos.

### 1. Función Escalón (Step Function)
```python
f(x) = 1 si x > 0, sino 0
```
- Uso original en perceptrones.
- No apta para redes profundas (no diferenciable).

### 2. Sigmoide
```python
f(x) = 1 / (1 + e^(-x))
```
- Rango: (0, 1).
- Útil para problemas de clasificación binaria.
- Problema: puede saturarse (gradientes pequeños).

### 3. Tanh (Tangente hiperbólica)
```python
f(x) = tanh(x)
```
- Rango: (-1, 1).
- Mejor que la sigmoide en redes profundas.

### 4. ReLU (Rectified Linear Unit)
```python
f(x) = max(0, x)
```
- Muy popular en redes neuronales profundas.
- Rápido y eficiente.
- Problema: algunas neuronas pueden “morir” (si siempre reciben valores negativos).

### 5. Softmax
- Generaliza la sigmoide a múltiples clases.
- Se usa en la **última capa** de una red para clasificación multiclase.

## 📊 ¿Por qué son importantes estas funciones?
- **Linealidad ≠ Aprendizaje complejo**
- Sin activaciones no lineales, la red neuronal es solo una regresión lineal.
- Las funciones de activación permiten que la red **represente relaciones no lineales**.

## 🧪 Ejemplo en Python (usando ReLU)

```python
import numpy as np  # Importamos la librería NumPy para operaciones numéricas

# ---------------------------
# Definición de la entrada de la neurona
# ---------------------------
X = np.array([1.2, -0.7, 3.0])         # Vector de características (entradas) de la neurona
pesos = np.array([0.5, -1.2, 0.8])     # Pesos sinápticos correspondientes a cada entrada
sesgo = 0.1                            # Término de sesgo (bias), desplazamiento del umbral

# ---------------------------
# Cálculo de la suma ponderada
# ---------------------------
# Se calcula el producto punto entre las entradas y los pesos, y se le suma el sesgo
z = np.dot(X, pesos) + sesgo
print(f"Suma ponderada (z): {z}")     # Mostramos el resultado intermedio

# ---------------------------
# Definición de la función de activación ReLU
# ---------------------------
def relu(x):
    """
    Función de activación ReLU (Rectified Linear Unit).
    Si x es positivo, devuelve x; si es negativo, devuelve 0.
    """
    return max(0, x)

# ---------------------------
# Aplicamos ReLU a la suma ponderada
# ---------------------------
salida = relu(z)
print(f"Salida de la neurona: {salida}")  # Mostramos el resultado final tras la activación

```

## 📚 Recursos recomendados:
- 🎥 [Explicación del Perceptrón - StatQuest (YouTube)](https://www.youtube.com/watch?v=ntKn5TPHHAk)
- 📘 [Libro: Neural Networks and Deep Learning - Michael Nielsen](http://neuralnetworksanddeeplearning.com/chap1.html)