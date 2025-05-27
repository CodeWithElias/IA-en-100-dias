## Día 17: K-means y clustering

- Introducción a los algoritmos de clustering.
- ¿Qué es K-means? Un algoritmo de aprendizaje no supervisado que agrupa datos en "k" clústeres basándose en la distancia a los centroides.
- Pasos del algoritmo K-means:
  1. Inicializar k centroides aleatoriamente.
  2. Asignar cada punto de datos al centroide más cercano.
  3. Recalcular los centroides como el promedio de los puntos asignados.
  4. Repetir hasta que los centroides no cambien significativamente.
- Casos de uso:
  - Segmentación de clientes.
  - Compresión de imágenes.
  - Análisis de patrones de comportamiento.
- Limitaciones:
  - Necesita definir el número de clústeres previamente (k).
  - Sensible a valores atípicos.

### Ejemplo en Python:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generamos datos simulados con 3 clústeres
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

# Creamos el modelo KMeans con k=3
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Obtenemos las etiquetas asignadas y los centroides
etiquetas = kmeans.predict(X)
centroides = kmeans.cluster_centers_

# Visualizamos los clústeres
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], s=300, c='red', marker='x')
plt.title("Clustering con K-means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()
```

- 📌 Recurso: [K-means explicado visualmente - StatQuest (YouTube)](https://youtu.be/mICySHB0fh4)
