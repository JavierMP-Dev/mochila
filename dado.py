import random

def simulate_dice_rolls(num_faces, num_rolls=100000, seed_interval=10000):
    results = [0] * num_faces
    
    for i in range(num_rolls):
        if i % seed_interval == 0:
            random.seed()  # Cambia la semilla del generador de números aleatorios
            
        roll = random.randint(1, num_faces)
        results[roll - 1] += 1
        
    return results

def main():
    try:
        num_faces = int(input("Introduce el número de caras del dado: "))
        
        if num_faces <= 1:
            print("El número de caras debe ser mayor a 1.")
            return6

        results = simulate_dice_rolls(num_faces)
        
        print(f"\nResultados después de 100,000 tiradas de un dado de {num_faces} caras:")
       
        for i, count in enumerate(results, start=1):
            print(f"Cara {i}: {count} veces")
            
            f = write("myfile.xlsx", "x")
    
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()