import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Generar datos sintéticos: Horas de estudio (x) y si aprueba o no (y)
np.random.seed(42)
x = np.random.uniform(0, 10, 100).reshape(-1, 1)  # 100 valores entre 0 y 10
y = (x.ravel() > 2).astype(int)  # aprueba si estudia más de 3 horas

# Creamos y entrenamos el modelo
modelo = LogisticRegression()
modelo.fit(x, y)

# Predicción de probabilidades
x_test = np.linspace(0, 7, 100).reshape(-1, 1)
probabilidades = modelo.predict_proba(x_test)[:, 1]

# Gráfica de la curva sigmoide
plt.plot(x_test, probabilidades, color='green', label='Curva sigmoide')
plt.scatter(x, y, color='red', label='Datos reales')
plt.xlabel("Horas de estudio")
plt.ylabel("Probabilidad de aprobar")
plt.title("Regresión Logística")
plt.legend()
plt.grid(True)
plt.show()

# Predicción de un nuevo dato
nueva_hora = 3
prob = modelo.predict_proba([[nueva_hora]])[0][1]
print(f"Probabilidad de aprobar con {nueva_hora} horas de estudio: {prob:.2f}")  # prob devuelve los 2 valores aprobado y reprobado