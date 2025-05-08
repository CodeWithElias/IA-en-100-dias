## 🧠 Día 5: Listas, tuplas y diccionarios en Python

### 📌 1. ¿Qué son?

Las **estructuras de datos** te permiten almacenar y organizar colecciones de valores. Son fundamentales para construir algoritmos, manipular datos y desarrollar soluciones en Inteligencia Artificial.

---

### 📌 Listas (`list`)


* **Mutables**: se pueden modificar (agregar, eliminar, cambiar).
* Ordenadas.
* Se representan con `[]`.

```python
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])         # manzana
frutas.append("uva")     # agrega un elemento
```

#### Métodos comunes de listas:

| Método               | Descripción |
|----------------------|-------------|
| `append(x)`          | Agrega un ítem al final de la lista. |
| `extend(iterable)`   | Extiende la lista agregando todos los elementos de un iterable. |
| `insert(i, x)`       | Inserta un ítem en una posición dada. |
| `remove(x)`          | Elimina el primer ítem con el valor x. |
| `pop([i])`           | Elimina y devuelve el ítem en la posición dada. |
| `clear()`            | Elimina todos los ítems de la lista. |
| `index(x[, start[, end]])` | Devuelve el índice del primer ítem con valor x. |
| `count(x)`           | Cuenta cuántas veces aparece x en la lista. |
| `sort()`             | Ordena la lista en su lugar. |
| `reverse()`          | Invierte los elementos de la lista en su lugar. |
| `copy()`             | Devuelve una copia superficial de la lista. |


📎 **Consejo**: Puedes usar `type()` y `dir()` para explorar más sobre estas estructuras en tiempo real:

```python
my_list = [1, 2, 3]
print(type(my_list))    # <class 'list'>
print(dir(my_list))     # Muestra todos los métodos y atributos

#### 📚 Métodos comunes:

```python
len(frutas)             # longitud de la lista
frutas.remove("uva")    # elimina un elemento
frutas.sort()           # ordena la lista
frutas.pop()            # elimina el último elemento
```

#### 🧪 Ejercicio 1
Crea una lista con 5 números enteros. Luego:
1. Agrega un número al final.
2. Inserta un número en la posición 2.
3. Elimina el primer número de la lista.
4. Ordena la lista de mayor a menor.

```python
numeros = [10, 5, 7, 3, 8]
numeros.append(12)
numeros.insert(2, 15)
numeros.remove(10)
numeros.sort(reverse=True)
print(numeros)
```
---

### 🔹 Tuplas

* **Inmutables**: no se pueden modificar una vez creadas.
* Más eficientes y seguras que las listas.
* Se representan con `()`.

```python
coordenadas = (10.5, 20.3)
print(coordenadas[0])  # 10.5
```

### Métodos comunes de tuplas:

| Método       | Descripción |
|--------------|-------------|
| `count(x)`   | Devuelve cuántas veces aparece el valor x. |
| `index(x)`   | Devuelve el índice de la primera aparición de x. |

> ✅ Las tuplas no tienen métodos como `append`, `remove` o `pop` porque son **inmutables**.

#### 🧪 Ejercicio 2
Define una tupla con los nombres de 5 países. Luego:
1. Cuenta cuántas veces aparece un país específico.
2. Muestra la posición (índice) de un país dado.

```python
paises = ('México', 'Argentina', 'Colombia', 'Perú', 'Chile')
print(paises.count('Chile'))
print(paises.index('Colombia'))
```

---

### 🔹 Diccionarios

* Almacenan pares **clave**\*\*:valor\*\*.
* Muy usados para representar estructuras tipo JSON o configuraciones.
* Se representan con `{}`.

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana
```

### Métodos comunes de diccionarios:

| Método                 | Descripción |
|------------------------|-------------|
| `get(key[, default])`  | Devuelve el valor para la clave. Si no existe, devuelve `default`. |
| `keys()`               | Devuelve una vista con todas las claves. |
| `values()`             | Devuelve una vista con todos los valores. |
| `items()`              | Devuelve una vista con todos los pares (clave, valor). |
| `update([other])`      | Actualiza el diccionario con pares clave-valor de otro diccionario. |
| `pop(key[, default])`  | Elimina la clave y devuelve su valor. |
| `popitem()`            | Elimina y devuelve un par clave-valor aleatorio (último desde Python 3.7). |
| `setdefault(key[, default])` | Devuelve el valor de la clave. Si no existe, la crea con `default`. |
| `clear()`              | Elimina todos los ítems del diccionario. |
| `copy()`               | Devuelve una copia superficial del diccionario. |

```python
persona["ciudad"] = "Madrid"  # agregar una clave nueva
persona.get("email", "No disponible")  # acceso seguro
persona.keys()     # obtener las claves
persona.values()   # obtener los valores
```

#### 🧪 Ejercicio 3
Crea un diccionario con nombres de estudiantes y sus calificaciones. Luego:
1. Agrega un nuevo estudiante.
2. Cambia la calificación de uno existente.
3. Elimina a un estudiante.
4. Muestra todas las claves, valores y pares.

```python
calificaciones = {
    'Ana': 90,
    'Luis': 85,
    'Carlos': 78
}

calificaciones['Marta'] = 95
calificaciones['Luis'] = 88
del calificaciones['Carlos']

print(calificaciones.keys())
print(calificaciones.values())
print(calificaciones.items())
```

---

### 🔍 Aplicación en IA

Estas estructuras son esenciales en proyectos de IA para:

* Manipular datos de entrenamiento y prueba.
* Almacenar resultados y predicciones.
* Representar vectores, matrices y configuraciones.

---

### 🧪 Ejercicios prácticos

```python
# Lista de números
numeros = [5, 3, 9, 1]
numeros.sort()
print(numeros)  # [1, 3, 5, 9]

# Tupla de colores
colores = ("rojo", "verde", "azul")
print("Color favorito:", colores[1])

# Diccionario de producto
producto = {"nombre": "Laptop", "precio": 1200}
print(f"{producto['nombre']} cuesta ${producto['precio']}")
```

---

### 🖊️ Desafío del día

1. Crea una lista con tus 5 libros favoritos.
2. Crea una tupla con 3 coordenadas GPS.
3. Crea un diccionario que represente un estudiante con las claves: nombre, edad, curso y promedio.

### 🧩 Ejercicio desafío mixto
🧪 Crea una función que reciba una lista de nombres y devuelva un diccionario donde las claves sean las iniciales y los valores,
listas de nombres que empiezan por esa letra.

```python
def agrupar_por_inicial(lista_nombres):
    resultado = {}
    for nombre in lista_nombres:
        inicial = nombre[0].upper()
        if inicial not in resultado:
            resultado[inicial] = []
        resultado[inicial].append(nombre)
    return resultado

nombres = ['Ana', 'Andrés', 'Carlos', 'Camila', 'Luis', 'Laura']
print(agrupar_por_inicial(nombres))
```

---

### 🎥 Recurso recomendado:
