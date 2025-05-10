# 🧠 Día 7: Estadística básica para Inteligencia Artificial

La estadística es un pilar fundamental de la inteligencia artificial y el aprendizaje automático. Nos permite **entender, describir, interpretar y modelar los datos**. En este módulo aprenderás los conceptos básicos que necesitas dominar antes de profundizar en modelos predictivos más avanzados.

---

## 📊 ¿Por qué es importante la estadística en IA?

En la IA:
- Los algoritmos **aprenden de datos**.
- La **distribución, tendencia central y dispersión** de esos datos afecta directamente el rendimiento de los modelos.
- Los conceptos estadísticos ayudan a **evaluar la calidad y confiabilidad de los modelos**.

---

## 📐 Conceptos clave

### 1. Media (Promedio)

**Definición:**
> Suma de todos los valores dividida por la cantidad de elementos.
La media aritmética es el valor promedio de un conjunto de datos. Se obtiene sumando todos los valores y dividiéndolos entre la cantidad total de elementos.

**Fórmula:**
    sumatoria(x_i)
x = ---------------
          n

Donde:

* x es la media.
* x_i son los valores del conjunto.
* n es el número total de valores.

**Ejemplo en Python:**
```python
import statistics

datos = [4, 5, 8, 6, 7]
media = statistics.mean(datos)
print(f"Media: {media}")
```

---

### 2. Mediana
> Valor central cuando los datos están ordenados.
**Definición:**
La mediana es el valor que se encuentra en el centro de un conjunto de datos ordenados. Si hay un número impar de datos, es el valor central. Si es par, es el promedio de los dos valores centrales.

**Fórmula:**
Para una lista ordenada $x_1, x_2, ..., x_n$:

* Si n es impar:
           n + 1
mediana = -------
             2

* Si n es par:
           n/2 + (n/2)+1
mediana = ---------------
                2

**Ejemplo en Python:**
```python
mediana = statistics.median(datos)
print(f"Mediana: {mediana}")
```

---

### 3. Moda

> Valor que más se repite en el conjunto de datos.
**Definición:**
La moda es el valor que ocurre con mayor frecuencia en un conjunto de datos. Puede no existir, ser única, o haber múltiples modas (distribución multimodal).


**Ejemplo:**
```python
moda = statistics.mode(datos)
print(f"Moda: {moda}")
```

---

### 4. Varianza

> Mide la dispersión de los datos con respecto a la media.
**Definición:**
La varianza mide la dispersión de los datos con respecto a la media. Cuanto mayor sea la varianza, más alejados están los valores de la media.

**Fórmula (muestral):**
      sumatoria(x_i - x)^2
s^2 = ---------------------
                n - 1

Donde:

* s^2 es la varianza muestral.
* x es la media.
* n es el número total de datos.
* x_i son los valores del conjunto

**Ejemplo:**
```python
varianza = statistics.variance(datos)
print(f"Varianza: {varianza}")
```

---

### 5. Desviación estándar

> Raíz cuadrada de la varianza. Indica cuánto se alejan los datos del promedio.
**Definición:**
Es la raíz cuadrada de la varianza. Representa la dispersión típica de los datos respecto a la media.

**Fórmula:**

s = raiz(s^2)

Donde: 
 * s^2 es la varianza muestral

```python
import math
desviacion = statistics.stdev(datos)
print(f"Desviación estándar: {desviacion}")
```

---

### 6. Rango

**Definición:**
Es la diferencia entre el valor máximo y el valor mínimo del conjunto de datos.

**Fórmula:**

rango = x_i(maximo) - x_i(minimo)

---

## 📌 Extras útiles

### Percentiles y cuartiles
- Permiten dividir el conjunto de datos en partes iguales.
- Se usan en análisis de dispersión y detección de outliers.

```python
import numpy as np

percentil_25 = np.percentile(datos, 25)
percentil_75 = np.percentile(datos, 75)
print(f"Q1 (25%): {percentil_25}")
print(f"Q3 (75%): {percentil_75}")
```

---

## 🧪 Ejercicio práctico

Dado un conjunto de datos de calificaciones:

```python
calificaciones = [6, 7, 8, 9, 6, 7, 9, 10, 5, 7]
```

1. Calcula la media, mediana, moda, varianza y desviación estándar.
2. Determina si hay algún valor atípico (outlier).
3. Representa los datos en un histograma usando `matplotlib`.

---

## 🎓 Aplicación en IA

- **Normalización de datos**: se hace con media y desviación estándar.
- **Modelos estadísticos**: regresión lineal, bayesianos, etc.
- **Validación de resultados**: distribución de errores, métricas de evaluación.

---

## ✅ Conclusión

Dominar estas herramientas estadísticas te permitirá analizar datos con criterio, detectar sesgos y preparar información de calidad para modelos de machine learning.

---