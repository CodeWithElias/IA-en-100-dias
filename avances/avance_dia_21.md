# 📘 Día 21: Introducción a las Redes Neuronales

## 🤖 ¿Qué es una red neuronal artificial?

Una red neuronal artificial (RNA) es un **modelo computacional inspirado en el cerebro humano**. Se compone de **nodos (neuronas)** organizados en capas y conectados entre sí. Estas redes pueden aprender patrones complejos a partir de datos.

## 🧱 Estructura básica de una red neuronal

1. **Capa de entrada**: recibe los datos (inputs).
2. **Capas ocultas**: procesan la información mediante funciones no lineales.
3. **Capa de salida**: entrega la predicción final.

Cada conexión entre neuronas tiene un **peso**, que indica la importancia de esa señal. El objetivo del entrenamiento es **ajustar estos pesos** para minimizar el error.

## ⚙️ Funcionamiento general

1. **Propagación hacia adelante (forward pass)**: los datos pasan de entrada a salida activando neuronas.
2. **Cálculo del error**: se compara la salida con la respuesta esperada.
3. **Retropropagación (backpropagation)**: el error se propaga hacia atrás y se ajustan los pesos con base en el gradiente descendente.
4. **Iteración**: se repite el proceso muchas veces (épocas) para mejorar.

## 🧠 ¿Por qué funcionan?

Gracias a su capacidad para modelar funciones no lineales, las RNA pueden:
- Reconocer imágenes
- Procesar lenguaje natural
- Predecir series temporales
- Clasificar datos complejos

## 🔣 Funciones clave en las redes neuronales

- **Función de activación**: introduce no linealidad. Ejemplos:
  - `ReLU (Rectified Linear Unit)`
  - `Sigmoid`
  - `tanh`

- **Función de pérdida**: mide qué tan lejos está la predicción del valor real.
  - `categorical_crossentropy` (clasificación multiclase)
  - `mean_squared_error` (regresión)

## 🧪 Implementación básica en Python (con Keras)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Cargar datos
X, y = load_iris(return_X_y=True)
y_cat = to_categorical(y)  # Convertimos etiquetas a one-hot

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2, random_state=42)

# Crear modelo
modelo = Sequential()
modelo.add(Dense(10, input_shape=(4,), activation='relu'))  # Capa oculta
modelo.add(Dense(3, activation='softmax'))  # Capa de salida para 3 clases

# Compilar
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar
modelo.fit(X_train, y_train, epochs=50, verbose=0)

# Evaluar
loss, acc = modelo.evaluate(X_test, y_test)
print(f"Precisión en test: {acc:.2f}")
```

## 📚 Datos importantes

- Las redes neuronales **aprenden mejor con muchos datos**.
- Si son muy profundas pueden sobreajustarse, por eso se usan técnicas como:
  - Regularización (L2)
  - Dropout
  - Batch Normalization

## 📺 Recurso recomendado

🎥 [Redes neuronales explicadas visualmente - StatQuest (YouTube)](https://www.youtube.com/watch?v=aircAruvnKk)
