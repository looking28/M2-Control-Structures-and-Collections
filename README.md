# M2-Control-Structures-and-Collections
# 🧮 Evaluador de Palabras y Coordenadas

Este programa en Python realiza dos funciones principales:

1. **Evalúa la longitud de una palabra ingresada por el usuario.**
2. **Determina en qué cuadrante del plano cartesiano se encuentra un punto dado por sus coordenadas (X, Y).**

---

## 📂 Estructura del Programa

El código está dividido en dos secciones principales:

---

### 1. ✅ Verificación de la longitud de una palabra

#### 🔧 Función utilizada:

```python
def word_length(word):
```

#### 🚦 Lógica:

* Si la palabra tiene entre **4 y 8 letras**, se considera **correcta**.
* Si tiene **menos de 4 letras**, se indica que **faltan letras**.
* Si tiene **más de 8 letras**, se informa que tiene **demasiadas letras**.
* Si el usuario no ingresa nada (una cadena vacía), se muestra un mensaje de error.

#### 📌 Entrada:

Solicita al usuario una palabra a través de `input()`.

---

### 2. 📍 Determinación de cuadrante cartesiano

#### 🔧 Función utilizada:

```python
def determine_quadrant(x, y):
```

#### 🚦 Lógica:

* Cuadrante I: x > 0 y y > 0
* Cuadrante II: x < 0 y y > 0
* Cuadrante III: x < 0 y y < 0
* Cuadrante IV: x > 0 y y < 0
* Si **x o y son cero**, el punto **no está en ningún cuadrante**.

#### 📌 Entrada:

Se piden dos valores numéricos (float) usando `input()`, uno para **X** y otro para **Y**.

#### ⚠️ Manejo de errores:

* Se incluye un bloque `try-except` para capturar errores si el usuario no introduce números válidos.

---

## 💡 Reflexiones del Desarrollo

* 💬 **Validaciones**: Fue fundamental validar las entradas del usuario para evitar errores de ejecución, como cadenas vacías o valores no numéricos.
* 🧠 **Lógica Condicional**: La práctica refuerza el uso de estructuras `if-elif-else`, esenciales para la toma de decisiones en programación.
* 🧪 **Pruebas**: Se probaron varios casos extremos (palabras vacías, números cero, entradas no numéricas) para garantizar la robustez del programa.
* 🛠️ **Mantenimiento**: El código está estructurado en funciones reutilizables, facilitando su mantenimiento o ampliación futura.

---

## 🚀 Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado (versión 3.x).
2. Copia el código en un archivo llamado `evaluador.py`.
3. Ejecuta el programa en la terminal o consola:

```bash
python evaluador.py
```

4. Sigue las instrucciones del programa.

---

## ✨ Posibles Mejoras Futuras

* Crear una interfaz gráfica simple usando `Tkinter`.
* Agregar soporte para evaluar múltiples palabras o puntos en un solo ciclo.
* Permitir guardar los resultados en un archivo `.txt` o `.csv`.

---

¿Te gustaría que genere este archivo `README.md` para descarga o que lo convierta en un documento PDF?
