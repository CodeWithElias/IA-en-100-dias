# 🧠 Día 8: Probabilidad para Inteligencia Artificial

## 📌 ¿Qué es la probabilidad?

La **probabilidad** es una rama de las matemáticas que mide la posibilidad de que ocurra un evento. En IA, la usamos para modelar incertidumbre y tomar decisiones informadas.

### 💡 Conceptos Clave:

- **Espacio muestral (S):** Conjunto de todos los resultados posibles.
- **Evento (E):** Subconjunto del espacio muestral.
- **Probabilidad de un evento:**  
  \[
  P(E) = \frac{\text{Número de casos favorables}}{\text{Número de casos posibles}}
  \]

### 🎲 Ejemplo simple:

> Lanzar una moneda → Espacio muestral: {cara, cruz}  
> Evento E: obtener "cara"  
> P(E) = 1/2

---

## 📊 Tipos de Probabilidad

- **Probabilidad clásica:** Supone que todos los resultados son igualmente probables.
- **Probabilidad frecuentista:** Basada en la frecuencia de ocurrencia.
- **Probabilidad bayesiana:** Usa conocimiento previo (a priori) para actualizar con nueva información.

---

## 📈 Distribuciones de Probabilidad

### 🔹 Distribución uniforme
Todos los resultados tienen la misma probabilidad.  
Ejemplo: lanzar un dado.

### 🔹 Distribución binomial
Modela el número de éxitos en una secuencia de experimentos de sí/no.

\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\]

### 🔹 Distribución normal
La famosa "campana de Gauss". Se usa cuando los datos se agrupan alrededor de una media.

\[
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{ - \frac{(x - \mu)^2}{2\sigma^2} }
\]

---

## 🧠 Teorema de Bayes
🧠 ¿Qué es el Teorema de Bayes?
El **Teorema de Bayes** es una fórmula matemática utilizada para calcular la probabilidad condicional: la probabilidad de que ocurra un evento A dado que ya ocurrió un evento B. Se basa en cómo se actualiza una creencia inicial (probabilidad a priori) con nueva evidencia (probabilidad condicional), y es clave para la inferencia bayesiana.

\[
P(E|+) = (P(+|E) * P(E)) / P(+) 
\]

- P(A|B): Probabilidad posterior.
- P(B|A): Verosimilitud.
- P(A): Probabilidad a priori.
- P(B): Evidencia.

### 🎯 Ejemplo:

Supón que:
- P(Enfermo) = 0.01
- P(Prueba positiva | Enfermo) = 0.99
- P(Prueba positiva | Sano) = 0.05

Entonces, ¿cuál es la probabilidad de estar enfermo si la prueba es positiva?

---

## 🧪 Ejercicio práctico

**Enunciado:**

Supón una urna con 3 bolas rojas y 2 bolas azules. Se extrae una bola al azar.

1. ¿Cuál es la probabilidad de que sea roja?
2. Si sacas una roja y **no la devuelves**, ¿cuál es la probabilidad de que la siguiente también sea roja?

---

## 📚 Recurso adicional

🎥 Video: [Probabilidad para IA - YouTube](https://youtu.be/VKxiZ5rPeP0?si=mp6XDQYN2mBZrcqT)

---

