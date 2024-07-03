def knapsack_dynamic(values, weights, max_weight):
    n = len(values)
    # Crear una tabla para almacenar los valores máximos posibles para diferentes pesos
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    
    # Llenar la tabla dp de forma iterativa
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # El valor máximo está en dp[n][max_weight]
    max_value = dp[n][max_weight]
    
    # Para encontrar los elementos seleccionados, rastreamos la tabla
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    return max_value, selected_items

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50

max_value, selected_items = knapsack_dynamic(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", selected_items)
