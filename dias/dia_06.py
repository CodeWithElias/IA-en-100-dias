# VECTORES  (LISTA)
#vector_a = [1,2,3]
#vector_b = [3,5,7]

#resultado = []
#for x,y in zip(vector_a,vector_b):
#    resultado.append(x*y)

#print(resultado)

# MATRICES (lista de listas)
#matriz = [[1,2,4],  #filas = i
#          [2,4,7],   # columnas = j
#          [6,4,3]]

#for fila in matriz:
#    for i in fila:
#        print(i)


import numpy as np

# 🎬 Datos de puntuaciones
usuarios = {
    "A": [5, 3, 4, 4],
    "B": [3, 4, 2, 1],
    "C": [4, 3, 5, 2],
    "Nuevo": [4, 5, 4, 0]  # El 0 indica que no ha puntuado "Gladiator"
}

peliculas = ["Matrix", "Inception", "Interstellar", "Gladiator"]

# 🧠 Función para calcular similitud del coseno
def similitud_coseno(v1, v2):
    dot = np.dot(v1, v2)
    norma_v1 = np.linalg.norm(v1)
    norma_v2 = np.linalg.norm(v2)
    return dot / (norma_v1 * norma_v2)

# Convertir a vectores
nuevo_vector = np.array(usuarios["Nuevo"])
similitudes = {}

for nombre, vector in usuarios.items():
    if nombre != "Nuevo":
        sim = similitud_coseno(np.array(vector), nuevo_vector)
        similitudes[nombre] = sim

# 📊 Mostrar similitudes
print("Similitudes con el Nuevo Usuario:")
for usuario, valor in similitudes.items():
    print(f"{usuario}: {valor:.4f}")

# 👤 Usuario más similar
usuario_similar = max(similitudes, key=similitudes.get)
print(f"\n🔍 Usuario más similar: {usuario_similar}")

# 📽 Recomendación de película
vector_similar = usuarios[usuario_similar]
recomendacion = None
mayor_puntuacion = -1

for i in range(len(peliculas)):
    if usuarios["Nuevo"][i] == 0:  # No la ha visto
        if vector_similar[i] > mayor_puntuacion:
            mayor_puntuacion = vector_similar[i]
            recomendacion = peliculas[i]

if recomendacion:
    print(f"🎯 Recomendación: '{recomendacion}' (puntuada {mayor_puntuacion} por {usuario_similar})")
else:
    print("✅ El nuevo usuario ya ha visto todas las películas.")
