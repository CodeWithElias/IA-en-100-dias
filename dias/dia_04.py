#💡 Enunciado
#Crea un programa en Python que simule un sistema de gestión de estudiantes para una clase. 
# El programa debe cumplir con los siguientes requisitos:
#Solicitar al usuario ingresar los datos de varios estudiantes (nombre, edad, nota).
#Almacenar los datos en una estructura de lista de diccionarios.
#Utilizar estructuras de control para:
#Validar que la edad sea mayor que 0.
#Validar que la nota esté entre 0 y 10.
#Crear funciones para:
#Agregar un estudiante.
#Mostrar todos los estudiantes.
#Calcular el promedio de notas.
#Filtrar y mostrar los estudiantes que aprobaron (nota >= 6).
#Utilizar al menos un módulo estándar, por ejemplo statistics para calcular el promedio o os para limpiar la pantalla entre acciones.


import os
import statistics

# Lista para almacenar estudiantes
estudiantes = []

# Función para limpiar pantalla (Windows/Linux/Mac)
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para agregar un estudiante
def agregar_estudiante():
    nombre = input("Nombre del estudiante: ")
    
    while True:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido para la edad.")
    
    while True:
        try:
            nota = float(input("Nota final (0-10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Introduce un valor numérico para la nota.")
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }
    estudiantes.append(estudiante)
    print(f"✅ Estudiante '{nombre}' agregado correctamente.\n")

# Función para mostrar todos los estudiantes
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\n📋 Lista de Estudiantes:")
    for est in estudiantes:
        print(f"- {est['nombre']} | Edad: {est['edad']} | Nota: {est['nota']}")

# Función para calcular promedio de notas
def promedio_notas():
    if not estudiantes:
        print("No hay estudiantes para calcular el promedio.")
        return
    notas = [est['nota'] for est in estudiantes]
    promedio = statistics.mean(notas)
    print(f"\n📊 Promedio de notas: {promedio:.2f}")

# Función para mostrar estudiantes aprobados
def mostrar_aprobados():
    aprobados = [est for est in estudiantes if est['nota'] >= 6]
    if not aprobados:
        print("❌ Ningún estudiante aprobado.")
        return
    print("\n✅ Estudiantes aprobados:")
    for est in aprobados:
        print(f"- {est['nombre']} | Nota: {est['nota']}")

# Menú principal
def menu():
    while True:
        print("\n=== Sistema de Gestión de Estudiantes ===")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Calcular promedio de notas")
        print("4. Mostrar estudiantes aprobados")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        limpiar_pantalla()
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            promedio_notas()
        elif opcion == '4':
            mostrar_aprobados()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# Ejecutar programa
menu()
