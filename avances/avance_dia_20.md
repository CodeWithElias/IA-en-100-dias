# Día 20: Overfitting y Underfitting

## ¿Qué son Overfitting y Underfitting?

Cuando entrenamos un modelo de Machine Learning, queremos que **generalice bien**, es decir, que funcione correctamente con datos nuevos (no vistos durante el entrenamiento). Pero a veces puede pasar lo siguiente:

### 🔴 Overfitting (Sobreajuste)
- El modelo **aprende demasiado bien** los datos de entrenamiento, incluso el **ruido** o las **excepciones**.
- Tiene **muy bajo error en entrenamiento** pero **alto error en prueba**.
- Es como un estudiante que memoriza las respuestas de un examen anterior pero no entiende el tema.

**Ejemplo:**
Un árbol de decisión muy profundo que memoriza todos los puntos de los datos de entrenamiento.

### 🟡 Underfitting (Subajuste)
- El modelo es **demasiado simple** para aprender los patrones de los datos.
- Tiene **alto error tanto en entrenamiento como en prueba**.
- Es como un estudiante que apenas estudia: no memoriza ni comprende.

**Ejemplo:**
Una regresión lineal usada para clasificar datos no lineales.

---

## 🎯 Objetivo ideal: **Buen ajuste**
Queremos que el modelo:
- Aprenda los patrones generales de los datos.
- Tenga **bajo error de entrenamiento y bajo error de prueba**.
- Generalice bien a nuevos datos.

---

## 📊 Gráfico comparativo

| Tipo           | Error Entrenamiento | Error Test | Complejidad del Modelo |
|----------------|---------------------|------------|-------------------------|
| Underfitting   | Alto                | Alto       | Baja                    |
| Buen Ajuste    | Bajo                | Bajo       | Media                   |
| Overfitting    | Muy Bajo            | Alto       | Alta                    |

---

## 🧠 ¿Cómo detectar Overfitting?

- Altísima precisión en entrenamiento (>95%) y mucha menor en test (<80%).
- Métricas como la curva de aprendizaje o validación cruzada lo revelan.

---

## 🛠️ ¿Cómo evitar Overfitting?

1. **Más datos:** ayuda al modelo a generalizar mejor.
2. **Regularización:** agrega penalizaciones al modelo (ej. L1, L2).
3. **Validación cruzada:** para asegurar que el modelo generaliza.
4. **Reducir la complejidad del modelo:** limitar profundidad o número de parámetros.
5. **Early stopping:** detener el entrenamiento antes de sobreajustar.
6. **Dropout (en redes neuronales):** apaga aleatoriamente algunas neuronas.

---

## 📌 Ejemplo en Python

```python
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generamos un dataset sintético
X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)

# Dividimos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo con overfitting: árbol muy profundo
modelo_overfit = DecisionTreeClassifier(max_depth=None)
modelo_overfit.fit(X_train, y_train)

# Modelo regularizado: profundidad limitada
modelo_regularizado = DecisionTreeClassifier(max_depth=3)
modelo_regularizado.fit(X_train, y_train)

# Evaluamos
print("Overfitting:")
print("Entrenamiento:", accuracy_score(y_train, modelo_overfit.predict(X_train)))
print("Prueba:", accuracy_score(y_test, modelo_overfit.predict(X_test)))

print("\nRegularizado:")
print("Entrenamiento:", accuracy_score(y_train, modelo_regularizado.predict(X_train)))
print("Prueba:", accuracy_score(y_test, modelo_regularizado.predict(X_test)))
