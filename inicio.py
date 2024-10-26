import tkinter as tk
import re

"""
    Valida un conjunto de cadenas contra una expresión regular dada.

    Parámetros:
    expresion (str): La expresión regular a validar.
    cadenas (list): Una lista de cadenas a validar.

    Retorna:
    dict: Un diccionario donde las claves son las cadenas y los valores son 
    booleanos que indican si la cadena es válida (True) o no (False).
    str: Un mensaje de error si la expresión regular es inválida.
"""
def validar_expresion_regular(expresion, cadenas):

    resultados = {}
    try:
        # Compila la expresión regular
        expresion_compilada = re.compile(expresion)
        for cadena in cadenas:
            # Verifica si cada cadena coincide con la expresión regular
            resultados[cadena] = bool(expresion_compilada.fullmatch(cadena))
    except re.error:
        return "Error en la expresión regular."
    return resultados

"""
    Función que se ejecuta al presionar el botón de validar. 
    Toma la expresión regular y las cadenas de entrada, 
    y muestra si cada cadena es aceptada o rechazada.
"""
def validar():

    expresion = entrada_expresion.get()  # Obtiene la expresión regular
    cadenas = entrada_cadenas.get("1.0", tk.END).strip().splitlines()  # Obtiene las cadenas
    resultados.delete("1.0", tk.END)  # Limpia el área de resultados

    resultados_validacion = validar_expresion_regular(expresion, cadenas)  # Llama a la función de validación

    if isinstance(resultados_validacion, str):  # Comprueba si hay un error en la regex
        resultados.insert(tk.END, resultados_validacion, 'rechazada')
    else:
        for cadena, es_valida in resultados_validacion.items():
            if es_valida:
                resultados.insert(tk.END, f"{cadena}: Aceptada\n", 'aceptada')
            else:
                resultados.insert(tk.END, f"{cadena}: Rechazada\n", 'rechazada')

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Expresiones Regulares")
ventana.geometry("400x400")
ventana.configure(bg="#f0f0f0")  # Color de fondo

# Estilos para etiquetas y botones
estilo_etiqueta = {
    'bg': '#f0f0f0',
    'font': ('Arial', 12)
}

estilo_boton = {
    'bg': '#4CAF50',
    'fg': 'white',
    'font': ('Arial', 12, 'bold')
}

# Etiqueta y entrada para la expresión regular
tk.Label(ventana, text="Expresión Regular:", **estilo_etiqueta).pack(pady=5)
entrada_expresion = tk.Entry(ventana, width=50)
entrada_expresion.pack(pady=5)

# Etiqueta y área de texto para las cadenas
tk.Label(ventana, text="Cadenas (una por línea):", **estilo_etiqueta).pack(pady=5)
entrada_cadenas = tk.Text(ventana, height=10, width=50)
entrada_cadenas.pack(pady=5)

# Botón para validar
boton_validar = tk.Button(ventana, text="Validar", command=validar, **estilo_boton)
boton_validar.pack(pady=10)

# Etiqueta y área de texto para los resultados
tk.Label(ventana, text="Resultados:", **estilo_etiqueta).pack(pady=5)
resultados = tk.Text(ventana, height=10, width=50)
resultados.pack(pady=5)

# Configuración de colores para los resultados
resultados.tag_config('aceptada', foreground='green')  # Resultado aceptado
resultados.tag_config('rechazada', foreground='red')   # Resultado rechazado

# Inicia el bucle principal de la interfaz
ventana.mainloop()
