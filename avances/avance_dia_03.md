
# 🚀 Día 3: Estructuras de control en Python

Hoy aprenderemos a controlar el flujo de ejecución de nuestros programas con **condicionales** y **bucles**, herramientas clave para construir lógica en IA y cualquier otro campo de la programación.

---

## 🔹 Condicionales

Las condicionales permiten ejecutar bloques de código si se cumplen ciertas condiciones.

### ✅ Sintaxis básica

```python
if condicion:
    # bloque si se cumple
elif otra_condicion:
    # bloque si se cumple la otra condición
else:
    # bloque si no se cumple ninguna
```

### 📌 Ejemplo

```python
x = 10
if x > 0:
    print("Número positivo")
elif x == 0:
    print("Es cero")
else:
    print("Número negativo")
```

---

## 🔁 Bucles

Los bucles permiten ejecutar código repetidamente.

### 🔸 `for` loop

Itera sobre elementos de una secuencia (listas, rangos, strings, etc.)

```python
for i in range(5):
    print(i)
```

### 🔸 `while` loop

Repite mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

---

## 📚 Ejercicios prácticos

### 🧩 Ejercicio 1: Números primos del 1 al 100

```python
for num in range(2, 101):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
```

### 🧩 Ejercicio 2: Adivina el número

```python
import random

numero_secreto = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (1-100): "))
    if intento == numero_secreto:
        print("¡Correcto!")
        adivinado = True
    elif intento < numero_secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
```

### 🧩 Ejercicio 3: Contador de vocales

```python
frase = input("Escribe una frase: ").lower()
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"La frase contiene {contador} vocales.")
```

---

## 🎥 Recurso adicional

- 📺 [Playlist de Python Básico para IA - YouTube (Programación Fácil)](https://www.youtube.com/playlist?list=PLZVftxMqRfKE5hFwgo6jlYqIhQuTrgE5A)

---

## ✅ Conclusión

Dominar las estructuras de control es esencial para tomar decisiones, repetir acciones y crear lógica dentro de tus programas. Son el núcleo de la programación condicional y repetitiva.

---

¿Listo para el Día 4? 🔥
