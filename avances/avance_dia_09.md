# 📊 Día 9: Visualización de Datos con Python

## 🎯 Objetivo del Día
Aprender a representar visualmente los datos usando Python con las bibliotecas **Matplotlib** y **Seaborn**.

---

## 📈 ¿Por qué es importante la visualización de datos?

Visualizar datos permite:
- Detectar patrones, tendencias y anomalías.
- Comunicar hallazgos de forma comprensible.
- Ayudar en la toma de decisiones basada en datos.
- Validar resultados de modelos de IA.

---

## 🧰 Herramientas que usaremos

- **Matplotlib**: Biblioteca estándar de gráficos en Python.
- **Seaborn**: Librería basada en Matplotlib, especializada en visualizaciones estadísticas.

---

## 1️⃣ Matplotlib

### 📚 Instalación

```bash
pip install matplotlib
```

### 📌 Sintaxis Básica

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Ejemplo de gráfico")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```

### 📊 Tipos de gráficos comunes

- `plt.plot()` – línea.
- `plt.bar()` – barras.
- `plt.scatter()` – dispersión.
- `plt.hist()` – histograma.
- `plt.pie()` – pastel.

---

## 2️⃣ Seaborn

### 📚 Instalación

```bash
pip install seaborn
```

### 📌 Sintaxis Básica

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset incluido
tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Cuenta total por día")
plt.show()
```

### 📊 Tipos de gráficos útiles

- `sns.barplot()` – barra.
- `sns.histplot()` – histograma.
- `sns.scatterplot()` – dispersión.
- `sns.boxplot()` – caja.
- `sns.heatmap()` – mapa de calor.

---

## 🔍 Matplotlib vs Seaborn

| Característica       | Matplotlib     | Seaborn           |
|----------------------|----------------|-------------------|
| Nivel                | Bajo (personalizable) | Alto (abstracción) |
| Facilidad de uso     | Media          | Alta              |
| Estética por defecto | Básica         | Profesional       |

---

## 🧠 Ejercicio práctico

**Visualiza un dataset real de Seaborn:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Mapa de calor de correlaciones
correlation = tips.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlación entre variables")
plt.show()
```

---

## 🎥 Recurso recomendado

📘 [Visualización de Datos en Python (Píldoras Informáticas)]()

---

## 📌 Tarea

- Crear 3 visualizaciones diferentes con un dataset real.
- Publicar una imagen del resultado en LinkedIn y TikTok.
- Reflejar en el repositorio del reto tu progreso.

---
