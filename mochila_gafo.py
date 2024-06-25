import time

def knapsack(values, weights, max_weight):
    n = len(values)
    # Crear una tabla para almacenar los valores máximos para cada subproblema
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla de manera bottom-up
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Imprimir la tabla
    for row in dp:
        print(row)
    
    # Encontrar los elementos que se tomaron para obtener el resultado óptimo
    taken_items = []
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken_items.append(i - 1)
            w -= weights[i - 1]
    
    # El valor máximo está en dp[n][max_weight]
    return dp[n][max_weight], taken_items

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50

start_time = time.time()
max_value, taken_items = knapsack(values, weights, max_weight)
end_time = time.time()

print("El valor máximo que se puede obtener es:", max_value)
print("Los índices de los elementos a tomar son:", taken_items)
print("Tiempo de ejecución:", end_time - start_time, "segundos")
