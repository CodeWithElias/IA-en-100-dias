# Importamos la biblioteca NumPy para operaciones numéricas
import numpy as np
# Importamos matplotlib para generar gráficos
import matplotlib.pyplot as plt
# Importamos la clase SVC (Support Vector Classifier) del módulo SVM de scikit-learn
from sklearn.svm import SVC
# Importamos make_blobs para generar datos artificiales de clasificación
from sklearn.datasets import make_blobs

# Generamos un conjunto de datos sintético con 100 muestras agrupadas en 2 centros (clases)
x, y = make_blobs(n_samples=100, centers=2, random_state=42, cluster_std=1.5)
# x → array de coordenadas (features) de cada muestra
# y → array de etiquetas de clase (0 o 1)

# Creamos un modelo SVM con un kernel lineal
modelo = SVC(kernel='linear')  # El kernel lineal permite encontrar un hiperplano recto entre clases

# Entrenamos (ajustamos) el modelo SVM con los datos generados
modelo.fit(x, y)

# Definimos una función para visualizar los datos y el modelo SVM entrenado
def plot_svm(x, y, model):
    # Dibujamos los puntos de datos con colores según su clase
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm', s=30)
    
    # Obtenemos el eje actual para usar sus límites en el gráfico
    ax = plt.gca()
    xlim = ax.get_xlim()  # Límite horizontal del gráfico
    ylim = ax.get_ylim()  # Límite vertical del gráfico

    # Creamos una cuadrícula de puntos en todo el espacio del gráfico
    xx = np.linspace(xlim[0], xlim[1], 30)  # 30 puntos en el eje x
    yy = np.linspace(ylim[0], ylim[1], 30)  # 30 puntos en el eje y
    YY, XX = np.meshgrid(yy, xx)  # Creamos una malla 2D con las coordenadas
    xy = np.vstack([XX.ravel(), YY.ravel()]).T  # Convertimos la malla en una lista de coordenadas (N x 2)

    # Calculamos la función de decisión del modelo SVM para cada punto de la malla
    Z = model.decision_function(xy).reshape(XX.shape)
    # Esta función devuelve la distancia de cada punto al hiperplano de decisión

    # Dibujamos las líneas del hiperplano (nivel 0) y los márgenes (niveles -1 y 1)
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], linestyles=['--', '-', '--'])

    # Añadimos título y etiquetas a los ejes
    plt.title("Clasificación con SVM")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")

    # Mostramos el gráfico completo
    plt.show()

# Llamamos a la función para visualizar el modelo SVM con los datos generados
plot_svm(x, y, modelo)
