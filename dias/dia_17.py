# Importamos matplotlib para visualización de datos en gráficos
import matplotlib.pyplot as plt
# Importamos el modelo KMeans desde sklearn para aplicar clustering
from sklearn.cluster import KMeans
# Importamos make_blobs para generar datos artificiales agrupables
from sklearn.datasets import make_blobs

# Generamos un conjunto de datos simulado con 300 muestras, distribuidas en 3 clústeres.
# cluster_std indica la dispersión de los datos y random_state asegura reproducibilidad.
X, y = make_blobs(n_samples=1000, centers=3, cluster_std=0.60, random_state=0)

# Creamos el modelo KMeans especificando que queremos encontrar 3 clústeres (k=3)
kmeans = KMeans(n_clusters=3, random_state=0)

# Entrenamos el modelo KMeans con los datos simulados
kmeans.fit(X)

# Obtenemos las etiquetas asignadas por el modelo a cada punto (a qué clúster pertenece)
etiquetas = kmeans.predict(X)

# Obtenemos las coordenadas de los centroides de cada clúster encontrado
centroides = kmeans.cluster_centers_

# Visualizamos los datos agrupados por color según su clúster
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis')  # Puntos coloreados según clúster

# Dibujamos los centroides en color rojo y con una 'x'
plt.scatter(centroides[:, 0], centroides[:, 1], s=300, c='red', marker='x')  # Centroides

# Título del gráfico
plt.title("Clustering con K-means")

# Etiquetas de los ejes
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")

# Mostrar el gráfico completo
plt.show()
