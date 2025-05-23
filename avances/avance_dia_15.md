# 🧠 Día 15: Máquinas de Soporte Vectorial (SVM)

## 📌 ¿Qué es una SVM?
Las **Máquinas de Soporte Vectorial (Support Vector Machines)** son algoritmos de aprendizaje supervisado muy poderosos usados para **clasificación** y **regresión**. El objetivo principal de una SVM es **encontrar un hiperplano óptimo** que separe los datos de diferentes clases con el **máximo margen posible**.

### 🔍 Conceptos Clave:
- **Margen máximo:** la distancia entre el hiperplano y los puntos más cercanos de cada clase.
- **Vectores de soporte:** los puntos de datos más cercanos al hiperplano, que definen su posición.
- **Kernel trick:** permite proyectar datos no linealmente separables a espacios de mayor dimensión donde sí puedan separarse.

## 🧪 Ejemplo en Python (Clasificación binaria)
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_blobs

# Generamos datos simulados de dos clases
x, y = make_blobs(n_samples=100, centers=2, random_state=42, cluster_std=1.5)

# Creamos el modelo SVM
modelo = SVC(kernel='linear')  # también puedes usar 'rbf', 'poly', etc.
modelo.fit(x, y)

# Visualizamos la clasificación
def plot_svm(x, y, model):
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm', s=30)
    
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Crear una malla para dibujar la decisión
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = model.decision_function(xy).reshape(XX.shape)

    # Dibujar el hiperplano y los márgenes
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], linestyles=['--', '-', '--'])
    plt.title("Clasificación con SVM")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.show()

plot_svm(x, y, modelo)
```

## ✅ ¿Qué aprendimos?
- Las SVM buscan el mejor límite de decisión posible entre dos clases.
- Pueden funcionar en problemas no lineales gracias a los *kernels*.
- Son ideales cuando el número de características es alto.

## 📘 Recurso recomendado:
- Video: [SVM explicado con visualización - YouTube](https://www.youtube.com/watch?v=efR1C6CvhmE)
