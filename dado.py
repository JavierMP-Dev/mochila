import random
import pandas as pd

def tiradas(num_faces, num_veces=100000, seed_interval=10000):
    results = [0] * num_faces
    for i in range(num_veces):
        if i % seed_interval == 0:
            random.seed()  # Cambia la semilla del generador de números aleatorios
        roll = random.randint(1, num_faces)
        results[roll - 1] += 1
    return results

def guardar_en_excel(results, num_faces):
    # Crear un DataFrame con los resultados
    df = pd.DataFrame({
        "Cara": [f"Cara {i+1}" for i in range(num_faces)],
        "Frecuencia": results
    })
    
    # Guardar el DataFrame en un archivo Excel
    nombre_archivo = f"resultados_dado_{num_faces}_caras.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"Resultados guardados en {nombre_archivo}")

def main():
    try:
        num_faces = int(input("Introduce el número de caras del dado: "))
        
        if num_faces <= 1:
            print("El número de caras debe ser mayor a 1.")
            return

        results = tiradas(num_faces)
        
        print(f"\nResultados después de 100,000 tiradas de un dado de {num_faces} caras:")
        for i, count in enumerate(results, start=1):
            print(f"Cara {i}: {count} veces")
        
        # Guardar los resultados en un archivo Excel
        guardar_en_excel(results, num_faces)
    
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()
