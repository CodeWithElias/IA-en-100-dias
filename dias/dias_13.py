# Importamos las bibliotecas necesarias
import numpy as np  # Para trabajar con arreglos numéricos
from sklearn.tree import DecisionTreeClassifier, plot_tree  # Para usar el modelo de árbol de decisión y visualizarlo
import matplotlib.pyplot as plt  # Para crear gráficos

# Creamos los datos de entrenamiento:
# x representa las horas de estudio de distintos estudiantes
# y representa si aprobaron (1) o no (0)
# 20 datos de entrada: Horas de estudio (entre 0 y 10)
x = np.array([[0.5], [1], [1.5], [2], [2.5], [3], [3.5], [4], [4.5], [5],
              [5.5], [6], [6.5], [7], [7.5], [8], [8.5], [9], [9.5], [10]])

# Etiquetas correspondientes: 0 = No aprueba, 1 = Aprueba
# Supongamos que a partir de 4 horas, las probabilidades de aprobar aumentan
y = np.array([0, 0, 0, 0, 1, 0, 0, 1, 1, 1,
              1, 1, 1, 1, 1, 1, 1, 0, 1, 1])

# Creamos el modelo de árbol de decisión
# max_depth=6 limita la profundidad del árbol para evitar sobreajuste
# random_state=0 asegura que los resultados sean reproducibles
modelo = DecisionTreeClassifier(max_depth=6, random_state=0)

# Entrenamos el modelo con nuestros datos
modelo.fit(x, y)

# Visualizamos gráficamente el árbol de decisión entrenado
plt.figure(figsize=(8, 6))  # Tamaño de la figura
plot_tree(
    modelo, 
    filled=True,  # Colorea las hojas según la clase predicha
    feature_names=["Horas de estudio"],  # Nombre de la variable
    class_names=["No Aprueba", "Aprueba"]  # Etiquetas de salida
)
plt.title("Árbol de Decisión: Aprobación según horas de estudio")
plt.show()

# Ahora realizamos una predicción con un nuevo dato:
# Queremos saber si un estudiante que estudia 3.5 horas aprueba
nueva_hora = [[5]]  # Entrada nueva
prediccion = modelo.predict(nueva_hora)  # El modelo predice 0 (no aprueba) o 1 (aprueba)

# Mostramos el resultado de forma legible
print(f"¿Aprueba con 5h de estudio? {'Sí' if prediccion[0] == 1 else 'No'}")
