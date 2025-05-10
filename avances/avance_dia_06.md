# 🤖 Día 6: Principios de Álgebra Lineal para IA

## 🧮 Introducción al Álgebra Lineal

El álgebra lineal es un pilar fundamental en inteligencia artificial. Permite representar datos, realizar operaciones numéricas y aplicar transformaciones en modelos matemáticos.

---

## 🔹 Vectores

Un **vector** es una secuencia ordenada de números. Se puede representar como una lista unidimensional.

```python
# Vector en Python
vector = [1, 2, 3]
```

### Operaciones con vectores

- **Suma de vectores**:
```python
a = [1, 2, 3]
b = [4, 5, 6]
suma = [x + y for x, y in zip(a, b)]  # [5, 7, 9]
```

- **Multiplicación por escalar**:
```python
escalar = 2
producto = [escalar * x for x in a]  # [2, 4, 6]
```

- **Producto punto (dot product)**:
```python
dot = sum(x * y for x, y in zip(a, b))  # 32
```

---

## 🔹 Matrices

Una **matriz** es una colección bidimensional de números, representada en Python como una lista de listas.

```python
# Matriz 2x2
matriz = [[1, 2],
          [3, 4]]
```

### Operaciones con matrices

- **Suma de matrices**:
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
suma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
```

- **Multiplicación por escalar**:
```python
escalar = 2
producto = [[escalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
```

- **Multiplicación de matrices**:
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
producto = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
```

---

## 🤖 Aplicaciones en IA

- Los vectores representan características de datos.
- Las matrices modelan relaciones y transformaciones (como los pesos de redes neuronales).
- Permiten optimizar funciones, aplicar transformaciones lineales y trabajar con datos en múltiples dimensiones.

---

## 💡 Ejercicios prácticos

### 1. Suma de dos vectores
```python
a = [2, 4, 6]
b = [1, 3, 5]
resultado = [x + y for x, y in zip(a, b)]
print("Suma de vectores:", resultado)
```

### 2. Producto escalar de dos vectores
```python
a = [1, 2, 3]
b = [4, 5, 6]
dot = sum(x * y for x, y in zip(a, b))
print("Producto escalar:", dot)
```

### 3. Multiplicación escalar de una matriz
```python
matriz = [[1, 2], [3, 4]]
escalar = 3
producto = [[x * escalar for x in fila] for fila in matriz]
print("Matriz escalada:", producto)
```

### 4. Multiplicación de matrices
```python
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print("Multiplicación de matrices:", resultado)
```

### 💡 Ejercicio Complejo: Recomendación basada en similitud de usuario
- Enunciado:
Tienes una pequeña base de datos de puntuaciones que distintos usuarios le han dado a diferentes películas. Representa estas puntuaciones como vectores y utiliza álgebra lineal para encontrar cuál usuario es más parecido a un nuevo usuario en base a sus puntuaciones, usando el producto punto y la norma de los vectores (cálculo de similitud de coseno).

🎬 Datos de ejemplo:

|Película	    |Usuario A	|Usuario B	|Usuario C	|Nuevo Usuario  |
|---------------|-----------|-----------|-----------|---------------|
|Matrix	        |5	        |3	        |4	        |4              |
|Inception	    |3	        |4	        |3	        |5              |
|Interstellar   |4	        |2	        |5	        |4              |
|Gladiator	    |4	        |1	        |2	        |5              |

#### 🧠 Objetivo:
- Representa las puntuaciones de cada usuario como un vector.
- Calcula la similitud del coseno entre el nuevo usuario y los demás.
- Determina con qué usuario es más similar y recomienda una película que ese usuario haya
puntuado alto y que el nuevo usuario no haya visto (puedes simular que el nuevo usuario no puntuó alguna).

#### 🔧 Sugerencias técnicas:
- Usa **numpy.dot()** para el producto punto.
- Usa **numpy.linalg.norm()** para obtener la magnitud del vector.
- Fórmula de la similitud del coseno:

             𝐴 ⋅ 𝐵
Sim(𝐴,𝐵) = ---------
           ∥𝐴∥ ⋅ ∥𝐵∥
​

#### resultado
```python
import numpy as np

# 🎬 Datos de puntuaciones
usuarios = {
    "A": [5, 3, 4, 4],
    "B": [3, 4, 2, 1],
    "C": [4, 3, 5, 2],
    "Nuevo": [4, 5, 4, 0]  # El 0 indica que no ha puntuado "Gladiator"
}

peliculas = ["Matrix", "Inception", "Interstellar", "Gladiator"]

# 🧠 Función para calcular similitud del coseno
def similitud_coseno(v1, v2):
    dot = np.dot(v1, v2)
    norma_v1 = np.linalg.norm(v1)
    norma_v2 = np.linalg.norm(v2)
    return dot / (norma_v1 * norma_v2)

# Convertir a vectores
nuevo_vector = np.array(usuarios["Nuevo"])
similitudes = {}

for nombre, vector in usuarios.items():
    if nombre != "Nuevo":
        sim = similitud_coseno(np.array(vector), nuevo_vector)
        similitudes[nombre] = sim

# 📊 Mostrar similitudes
print("Similitudes con el Nuevo Usuario:")
for usuario, valor in similitudes.items():
    print(f"{usuario}: {valor:.4f}")

# 👤 Usuario más similar
usuario_similar = max(similitudes, key=similitudes.get)
print(f"\n🔍 Usuario más similar: {usuario_similar}")

# 📽 Recomendación de película
vector_similar = usuarios[usuario_similar]
recomendacion = None
mayor_puntuacion = -1

for i in range(len(peliculas)):
    if usuarios["Nuevo"][i] == 0:  # No la ha visto
        if vector_similar[i] > mayor_puntuacion:
            mayor_puntuacion = vector_similar[i]
            recomendacion = peliculas[i]

if recomendacion:
    print(f"🎯 Recomendación: '{recomendacion}' (puntuada {mayor_puntuacion} por {usuario_similar})")
else:
    print("✅ El nuevo usuario ya ha visto todas las películas.")

```
---

## 🎓 Recurso complementario

📺 [Álgebra Lineal desde cero - YouTube](https://www.youtube.com/watch?v=ZfijE4A4bgk)
