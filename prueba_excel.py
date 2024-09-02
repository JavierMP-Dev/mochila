import pandas as pd

# Supongamos que tienes estos resultados en una lista de diccionarios
resultados = [
    {"Nombre": "Juan", "Edad": 25, "Calificación": 85},
    {"Nombre": "Ana", "Edad": 22, "Calificación": 90},
    {"Nombre": "Luis", "Edad": 24, "Calificación": 88},
    {"Nombre": "Fransisco", "Edad": 35, "Calificación": 88}
]

# Convertir los resultados a un DataFrame
df = pd.DataFrame(resultados)

# Escribir el DataFrame en un archivo Excel
df.to_excel("resultados.xlsx", index=False)

print("Archivo Excel creado con éxito.")
