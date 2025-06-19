# Prueba-Tecnica

## Conversión de Hora 12h a 24h ⏰

Este repositorio contiene la solución a la prueba técnica solicitada por **Copec EMOAC**, la cual consiste en desarrollar un programa que convierta una hora en formato de **12 horas con AM/PM** (ej. `07:05:45PM`) a formato de **24 horas (militar)** (ej. `19:05:45`).

## Contenido

- `prueba_tecnica1_Martín_Soto_Contreras.py`: implementación en **Python**
- `prueba_tecnica1_Martín_Soto_Contreras.js`: implementación en **JavaScript**
- `Casos_de_prueba_Martín_Soto_Contreras.pdf`: documento con los resultados de los casos de prueba aplicados

---

## Funcionalidad

Ambas versiones del código (Python y JavaScript):

- Validan que el formato ingresado sea correcto (`hh:mm:ssAM` o `hh:mm:ssPM`)
- Verifican que los valores de hora, minutos y segundos estén dentro del rango permitido
- Realizan la conversión correcta a formato 24 horas

---

## Casos de prueba incluidos

| Entrada (12h)   | Salida esperada (24h) |
|----------------|------------------------|
| 07:05:45PM     | 19:05:45               |
| 12:01:00PM     | 12:01:00               |
| 12:01:00AM     | 00:01:00               |
| 01:00:00AM     | 01:00:00               |
| 11:59:59PM     | 23:59:59               |
| 04:30:00AM     | 04:30:00               |
| 08:15:45PM     | 20:15:45               |

---

## Cómo ejecutar

### Python

```bash
python prueba_tecnica1_Martín_Soto_Contreras.py

---

```bash
node prueba_tecnica1_Martín_Soto_Contreras.js

