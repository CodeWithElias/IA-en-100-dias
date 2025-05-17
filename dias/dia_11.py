import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Creamos los datos de ejemplo
x = np.array([1, 1.5, 2, 2.4, 3, 3.5, 4, 4.5, 5, 5.5]).reshape(-1, 1)  # Horas de estudio
y = np.array([40, 40, 50, 55, 60, 65, 65, 70, 75, 80])           # Calificaciones obtenidas

# Creamos el modelo de regresión
modelo = LinearRegression()
modelo.fit(x, y)  # Entrenamos el modelo con nuestros datos

# Realizamos predicciones con el modelo entrenado
predicciones = modelo.predict(x)

# Visualización de los resultados
plt.scatter(x, y, color='blue', label='datos reales')   # Puntos originales
plt.plot(x, predicciones, color='red', label='modelo lineal')  # Línea de regresión
plt.title("Regresión lineal: horas vs calificaciones")
plt.xlabel("horas de estudio")
plt.ylabel("calificacion")
plt.legend()
plt.grid(True)
plt.show()

# Imprimimos los parámetros aprendidos por el modelo
print("Pendiente (m):", modelo.coef_[0])
print("Intercepto (b):", modelo.intercept_)
print("Score R2:", modelo.score(x, y))  # Evaluación del modelo

# ----------------------------------------
# 🔮 Predicción con nueva hora de estudio
nueva_hora = 0.1  # Cambia este valor para predecir otra hora
nueva_prediccion = modelo.predict(np.array([[nueva_hora]]))
print(f"\nSi estudias {nueva_hora} horas, se predice que obtendrás una nota de: {nueva_prediccion[0]:.2f}")
