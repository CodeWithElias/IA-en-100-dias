# 🧠 Día 4: Funciones y Módulos en Python

## 📌 ¿Qué es una función?
Una **función** es un bloque de código reutilizable que realiza una tarea específica. 
Sirve para **organizar mejor tu código**, **evitar repeticiones** y **facilitar el mantenimiento**.

---

## 🎯 Ventajas de usar funciones
- Reutilización del código
- Facilitan la depuración y el mantenimiento
- Aumentan la legibilidad
- Permiten dividir problemas complejos en partes más manejables

---

## 🧠 Parámetros y retorno
Las funciones pueden recibir **parámetros** (entradas) y devolver **valores** (salidas):
- **Parámetros**: valores que se le pasan a la función.
- **`return`**: permite devolver un valor.

---

### Tipos de parámetros
- **Obligatorios:** Se deben proporcionar sí o sí.
- **Opcionales (por defecto):** Tienen un valor por defecto.
- **Arbitrarios:** Se puede pasar cualquier cantidad.

### 🔧 Sintaxis básica:
```python
def nombre_funcion(parámetros):
    # bloque de código
    return resultado
```

```python
def saludar():
    print("Hola, bienvenido al reto de IA con Python.")
```

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)  # Imprime 7
```

### ✅ Ejemplo simple:
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Carlos"))
```

---

## 📦 Módulos en Python

Un **módulo** es un archivo `.py` con funciones, clases o variables que puedes importar en otros programas.

### Módulos estándar útiles:
- `math` – Funciones matemáticas
- `random` – Generación de números aleatorios
- `datetime` – Fechas y horas
- `os` – Interacción con el sistema operativo

### 🔹 Importar un módulo estándar:
```python
import math

print(math.sqrt(16))  # Raíz cuadrada: 4.0
```

### 🔹 Importar una función específica:
```python
from math import pi

print(pi)  # 3.141592...
```

### 🔹 Crear tu propio módulo:

1. Crea un archivo `mimodulo.py`:
```python
def saludar(nombre):
    return f"Hola, {nombre}!"
```

2. Luego lo importas en otro archivo:
```python
import mimodulo

print(mimodulo.saludar("Ana"))
```

---

## 🧪 Ejercicio sugerido:
Crea una función que reciba una lista de números y devuelva la suma de los pares.

```python
def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma

print(suma_pares([1, 2, 3, 4, 5, 6]))  # 12
```
## ✅ Buenas prácticas

- Usa nombres descriptivos para las funciones.
- Limita la función a una sola responsabilidad.
- Documenta cada función con docstrings.
- Evita usar variables globales dentro de funciones.

---

## 🎥 Recurso en video: