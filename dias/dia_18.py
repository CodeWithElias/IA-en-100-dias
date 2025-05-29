# Importamos el dataset Iris
from sklearn.datasets import load_iris
# Importamos funciones de validación cruzada y particionamiento KFold
from sklearn.model_selection import cross_val_score, KFold
# Importamos el modelo de regresión logística
from sklearn.linear_model import LogisticRegression
# Importamos NumPy para operaciones matemáticas
import numpy as np

# Cargamos las características (X) y etiquetas (y) del dataset Iris
# Este dataset contiene 150 muestras de flores divididas en 3 clases
X, y = load_iris(return_X_y=True)

# Creamos el modelo: Regresión Logística
# max_iter=200 asegura que el modelo tenga suficiente iteraciones para converger
modelo = LogisticRegression(max_iter=200)

# Configuramos K-Fold Cross Validation con 5 particiones (folds)
# shuffle=True mezcla aleatoriamente los datos antes de dividirlos
# random_state=42 garantiza que los resultados sean reproducibles
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluamos el modelo usando validación cruzada
# cross_val_score entrena y evalúa el modelo en cada fold
# Retorna una lista con la precisión obtenida en cada fold
resultados = cross_val_score(modelo, X, y, cv=kfold)

# Imprimimos los resultados individuales por fold
print("Resultados por fold:", resultados)

# Imprimimos el promedio de precisión obtenida en los 5 folds
print("Precisión promedio:", np.mean(resultados))
