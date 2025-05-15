# Día 10: Introducción al Aprendizaje Automático

## ¿Qué es el Aprendizaje Automático?

El **Aprendizaje Automático (Machine Learning, ML)** es una rama de la inteligencia artificial que permite a las máquinas aprender de los datos y tomar decisiones sin ser programadas explícitamente para cada tarea.

El enfoque central del ML es **desarrollar modelos matemáticos y estadísticos que puedan generalizar patrones a partir de datos**.

---

## Tipos de Aprendizaje Automático

### 1. Aprendizaje Supervisado

- Los datos están etiquetados: cada entrada tiene una salida conocida.
- El objetivo es aprender una función que, a partir de una entrada, prediga la salida.
- Ejemplos:
  - Clasificación (spam vs no spam).
  - Regresión (predecir el precio de una casa).

**Algoritmos comunes:**
#### Regresión Lineal
Predice un valor numérico continuo.
Ejemplo: predecir el precio de una casa según tamaño y ubicación.

#### Regresión Logística
Clasifica ejemplos en dos o más clases.
Ejemplo: detectar si un correo es spam o no.

#### Árboles de Decisión
Modelo jerárquico que divide los datos con reglas simples.
Fácil de interpretar, pero puede sobreajustar.

#### Random Forest
Conjunto de árboles de decisión. Mejora precisión y reduce sobreajuste.

#### K-Nearest Neighbors (KNN)
Clasifica un dato según los k vecinos más cercanos.
Simple pero puede ser costoso con grandes volúmenes.

#### Support Vector Machines (SVM)
Encuentra el mejor límite (hiperplano) que separa clases.
Muy eficaz para clasificación binaria.

#### Redes Neuronales Artificiales
Inspiradas en el cerebro humano. Capaces de capturar patrones complejos.
Usadas en deep learning (aprendizaje profundo).
---

### 2. Aprendizaje No Supervisado

- No hay etiquetas, solo se proveen los datos de entrada.
- El objetivo es descubrir estructuras ocultas, agrupaciones o patrones.
- Ejemplos:
  - Agrupamiento (clustering) de clientes por comportamiento.
  - Reducción de dimensionalidad para visualización.

**Algoritmos comunes:**
#### K-Means Clustering
Agrupa datos en k grupos con características similares.

#### DBSCAN
Detecta agrupaciones basadas en densidad. Resistente al ruido.

#### PCA (Análisis de Componentes Principales)
Técnica de reducción de dimensionalidad. Útil para visualización.

#### Autoencoders
Red neuronal que aprende a comprimir y descomprimir datos.
Usado para reducción de ruido o detección de anomalías.
---

### 3. Aprendizaje por Refuerzo (Avanzado)

- Un agente aprende tomando acciones en un entorno para maximizar una recompensa acumulada.
- Usado en juegos, robótica, sistemas de recomendación.

---

## Aplicaciones del Aprendizaje Automático

- Reconocimiento de voz e imagen.
- Recomendaciones personalizadas (Netflix, Spotify).
- Detección de fraudes.
- Diagnóstico médico.
- Autos autónomos.

---

## Conceptos Clave

- **Datos de entrenamiento**: conjunto de datos usados para entrenar el modelo.
- **Datos de prueba**: conjunto separado para validar la capacidad del modelo.
- **Overfitting (sobreajuste)**: cuando el modelo memoriza en lugar de generalizar.
- **Underfitting (subajuste)**: cuando el modelo no logra capturar patrones.

---

## Recursos adicionales

- Curso básico de ML en [Google Developers](https://developers.google.com/machine-learning/crash-course)

---

## Ejercicio propuesto

**Simula un conjunto de datos etiquetados de frutas con características como peso y color. Usa un algoritmo de clasificación simple (como KNN) para predecir la fruta basada en esos atributos.**

(Este ejercicio se desarrollará en el Día 11).

---

