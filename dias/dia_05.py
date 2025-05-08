# LISTAS
frutas = ["manzana", "banana"]
print(frutas)
frutas.sort()
print(frutas)

# TUPLAS
coordenadas = (10.5, 15,8)
print(coordenadas[2])

# DICCIONARIOS
persona = {"nombre": "ana", "edad": 23}
print(persona)
print(persona["nombre"])
persona["ciudad"] = "madrid"
print(persona)

# APLICACION EN LA IA
persona = {
    "nombre": "ana",
    "edad": 24,
    "cuidad": "madrid"
}
print(persona)

# EJERCICIOS PRACTICOS
#🧪 Crea una función que reciba una lista de nombres y devuelva un 
# diccionario donde las claves sean las iniciales y los valores,
#listas de nombres que empiezan por esa letra.
def agrupar_por_inicial (lista):
    resultado = {}
    for nombre in lista:
        inicial = nombre[0].upper()
        if inicial not in resultado:
            resultado[inicial] = []
        resultado[inicial].append(nombre)
    return resultado

nombre = ["Ana", "Andres", "Carlos", "Camila", "Luis", "Laura", "Diego"]
diccionario = agrupar_por_inicial(nombre)

print(diccionario)

# resultado
#{
#    'A': ['Ana', 'Andres'],
#    'C': ['Carlos', 'Camila'], 
#    'L': ['Luis', 'Laura'], 
#    'D': ['Diego']
# }