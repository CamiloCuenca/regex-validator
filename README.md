
# Validador de Expresiones Regulares

## Descripción del Proyecto
Esta aplicación permite validar un conjunto de cadenas de texto frente a una expresión regular proporcionada por el usuario. A través de una interfaz gráfica, los usuarios pueden ingresar tanto la expresión regular como las cadenas a evaluar. Los resultados de la validación se muestran claramente en la misma ventana, indicando si cada cadena es aceptada o rechazada por la expresión regular.

## Características
- **Validación de Expresiones Regulares**: La aplicación evalúa si cada cadena coincide completamente con la expresión regular ingresada.
- **Manejo de Errores**: Los errores en la expresión regular son manejados y se muestran mensajes de error claros.
- **Interfaz Gráfica de Usuario**: La interfaz es intuitiva y fácil de usar. Permite ingresar expresiones regulares y cadenas de manera sencilla.
- **Resultados Visuales**: Las cadenas aceptadas se muestran en color verde, mientras que las rechazadas en rojo, mejorando la claridad del resultado.

## Requisitos del Sistema
- Python 3.x
- Biblioteca **Tkinter** (incluida en la mayoría de las instalaciones de Python)
- Biblioteca **re** para manejo de expresiones regulares (incluida en Python)

## Instalación
1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/CamiloCuenca/regex-validator.git
    ```
2. Asegúrate de tener Python 3.x instalado. Puedes verificar esto ejecutando:
    ```bash
    python --version
    ```

3. No necesitas instalar librerías adicionales, ya que **Tkinter** y **re** están incluidas en Python. Sin embargo, asegúrate de ejecutar el programa desde un entorno compatible con Tkinter (generalmente es compatible en sistemas Windows, macOS y Linux).

## Uso
1. Ejecuta el programa en tu terminal o desde un entorno de desarrollo:
    ```bash
    python validador.py
    ```

2. **Interfaz de Usuario**:
   - **Expresión Regular**: Ingresa la expresión regular en el campo correspondiente.
   - **Cadenas**: Ingresa una o más cadenas para validar, cada una en una línea separada.
   - Haz clic en el botón **Validar** para ejecutar la validación.

3. **Resultados**:
   - La aplicación mostrará si cada cadena es **Aceptada** (en verde) o **Rechazada** (en rojo) según la expresión regular ingresada.

## Expresión Regular de Prueba


Esta es una expresion regular para el formata de un correo electronico

    ```regex
    ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
    
### Ejemplos de correos electrónicos

A continuación, se muestran algunos ejemplos de correos electrónicos válidos e inválidos que puedes utilizar para probar la expresión regular:

#### Ejemplos válidos

1. `usuario@example.com`
2. `nombre.apellido@dominio.edu`
3. `user+tag@sub.dominio.org`

#### Ejemplos inválidos

1. `usuario@.com` - No se permite comenzar con un punto (`.`) en el dominio.
2. `usuario@dominio` - Falta la extensión de dominio (como `.com` o `.edu`).
3. `usuario@dominio_com` - No se permiten guiones bajos (`_`) en la extensión del dominio.


## Autores
- Juan Camilo Cuenca Sepúlveda
- Brandon Montealegre
