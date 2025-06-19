#Debe ser realizada solo con algoritmia, sin librerías asociadas más que las propiedades del lenguaje.
#Dado un horario en formato de 12 horas con AM o PM (ej: hh:mm:ssAM o hh:mm:ssPM), escribe una función que convierta ese horario al formato de 24 horas (militar).
def convertir_hora_12_a_24(s):
    # Validar longitud mínima
    if len(s) != 10:
        return "Formato incorrecto. Usa hh:mm:ssAM o hh:mm:ssPM"

    # Validar que termine en AM o PM
    periodo = s[-2:]
    if periodo not in ["AM", "PM"]:
        return "Falta el indicador AM o PM al final."

    # Validar separadores de tiempo
    if s[2] != ':' or s[5] != ':':
        return "Formato incorrecto. Usa dos puntos como separadores de hora, minutos y segundos."

    # Extraer y validar partes numéricas
    try:
        hora = int(s[0:2])
        minutos = int(s[3:5])
        segundos = int(s[6:8])
    except ValueError:
        return "Los valores de hora, minutos o segundos no son números válidos."

    if not (1 <= hora <= 12):
        return "La hora debe estar entre 01 y 12."
    if not (0 <= minutos < 60):
        return "Los minutos deben estar entre 00 y 59."
    if not (0 <= segundos < 60):
        return "Los segundos deben estar entre 00 y 59."

    # Convertir según AM/PM
    if periodo == "AM":
        if hora == 12:
            hora = 0
    else:  # PM
        if hora != 12:
            hora += 12

    hora_str = f"{hora:02}"

    return f"{hora_str}:{s[3:5]}:{s[6:8]}"


# Leer entrada del usuario
entrada = input("Ingresa la hora en formato 12h (ej: 07:05:45PM): ")
resultado = convertir_hora_12_a_24(entrada)

# Mostrar el resultado o mensaje de error
print("Resultado:", resultado)
