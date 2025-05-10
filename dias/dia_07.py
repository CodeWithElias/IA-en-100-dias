# MEDIA
datos = [4,5,6,7,8,8,8,8,9,10,11,12]
media = 0
for i in datos:
    media +=i
media = media/len(datos)
print(f"Media: {media}")

import statistics
media1 = statistics.mean(datos)
print(f"Media: {media1}")

# MEDIANA
mediana = statistics.median(datos)
print(f"Mediana: {mediana}")

# MODA
moda = statistics.mode(datos)
print(f"Moda: {moda}")

# VARIANZA
varianza = statistics.variance(datos)
print(f"Varianza: {varianza}")

# DESVIACION ESTANDAR
desviacion = statistics.stdev(datos)
print(f"Desviacion estander: {desviacion}")

# RANGO
rango = max(datos) - min(datos)
print(f"rango: {rango}")

# EJERCICIO
# Contexto:
#Una profesora de Inteligencia Artificial aplicó un examen
# a sus estudiantes y obtuvo las siguientes calificaciones (de 0 a 10):
#calificaciones = [7, 8, 9, 6, 7, 10, 6, 8, 9, 5, 6, 7, 8, 9, 7]
# Objetivos:
#Calcula lo siguiente con Python:
#Media de las calificaciones.
#Mediana.
#Moda.
#Varianza.
#Desviación estándar.
#Rango.

# solucion
calificaciones = [7,8,9,6,7,10,6,8,9,5,6,7,8,9,7]
# media de calificaiones
media = statistics.mean(calificaciones)
# mediana de calificaciones
mediana = statistics.median(calificaciones)
# moda de calificaciones
moda = statistics.mode(calificaciones)
# varianza de calificaciones
varianza = statistics.variance(calificaciones)
# desviacion de calificaciones
desviacion = statistics.stdev(calificaciones)

# imprimir las mediadas resultantes
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Desviacion: {desviacion}")