# Día 2: Principios básicos de Python para IA

## 📌 Índice

- [📦 Instalación](#-instalación)
- [🐍 Principios básicos de Python para IA](#-principios_básicos_de_Python_para_IA)

## Instalacion

### 🪟 Windows
Ve al sitio oficial: https://www.python.org/downloads
Descarga el instalador recomendado para Windows.
MUY IMPORTANTE: marca la opción “Add Python to PATH” antes de hacer clic en “Install Now”.
Finaliza la instalación.

#### instalar jupyter Notebook
```bash
pip install notebook
```

#### ✅ Verifica que se instaló:
Abre CMD y escribe:
```bash
python --version
```

### 🍎 macOS
Descarga el instalador desde https://www.python.org/downloads
Ejecuta el archivo .pkg y sigue las instrucciones.
Tip: también puedes usar Homebrew (si lo tienes instalado):

```bash
brew install python
```

### 🐧 Linux (Ubuntu/Debian)
Python normalmente ya viene preinstalado. Si no, puedes instalarlo así:
```bash
sudo apt update
sudo apt install python3
```

#### ✅ Verifica que se instaló:
```bash
python3 --version
```

⚠️ Si usas Visual Studio Code
Te recomiendo instalar la extensión oficial de Python y asegurarte de que VS Code detecta tu instalación correctamente.

## 🐍 Principios básicos de Python para IA

🐍 ¿Por qué Python?
Python es el lenguaje más usado en Inteligencia Artificial gracias a su:
- Sintaxis simple.
- Amplia comunidad.
- Bibliotecas poderosas (NumPy, pandas, scikit-learn, TensorFlow, etc.).

### 🧱 Sintaxis básica: variables y tipos de datos

🔸 Variables
```bash
nombre = "IA"
edad = 2025
```

🔸 Tipos de datos comunes
```bash
# Texto (string)
mensaje = "Hola mundo"

# Enteros (int)
numero = 42

# Decimales (float)
pi = 3.1416

# Booleanos (bool)
activo = True

# Listas
colores = ["rojo", "verde", "azul"]
```

#### 🖋 Entrada y salida
🔹 Imprimir en pantalla (salida)
```bash
print("Hola desde Python")
```

🔹 Leer datos del usuario (entrada)
```bash
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)
```

#### ➕ Operaciones básicas
🔹 Aritméticas
```bash
suma = 5 + 3
resta = 10 - 4
producto = 2 * 6
division = 10 / 2
```

🔹 Comparación
```bash
a = 5
b = 7
print(a == b)   # False
print(a < b)    # True
```