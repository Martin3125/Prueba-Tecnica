#Dado un horario en formato de 12 horas con AM o PM (ej: hh:mm:ssAM o hh:mm:ssPM), escribe una función que convierta ese horario al formato de 24 horas (militar).

def convertir_hora_12_a_24(s):
    # Se extran las partes de la hora
    hora = int(s[0:2])
    minutos = s[3:5]
    segundos = s[6:8]
    periodo = s[8:]  # AM o PM

    # Se ajusta la hora según el período que corresponda
    if periodo == "AM":
        if hora == 12:
            hora = 0
    else:  # PM
        if hora != 12:
            hora += 12

    # Se formatea la hora a dos dígitos
    if hora < 10:
        hora_str = "0" + str(hora)
    else:
        hora_str = str(hora)

    return hora_str + ":" + minutos + ":" + segundos

# Leer entrada
entrada = input()

# Procesar y mostrar resultado
print(convertir_hora_12_a_24(entrada))
