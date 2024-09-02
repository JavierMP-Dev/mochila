<<<<<<< HEAD
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
=======
def knapsack_backtracking(values, weights, max_weight):
    # Número de elementos
    n = len(values)
    
    # Función auxiliar de DFS y backtracking
    def dfs(index, current_weight, current_value, taken_items):
        # Caso base: si hemos considerado todos los elementos
        if index == n:
            return current_value, taken_items
        
        # Opción 1: no tomar el elemento actual
        max_value, best_items = dfs(index + 1, current_weight, current_value, taken_items)
        
        # Opción 2: tomar el elemento actual (si cabe en la mochila)
        if current_weight + weights[index] <= max_weight:
            value_with_item, items_with_item = dfs(index + 1, current_weight + weights[index], current_value + values[index], taken_items + [index])
            # Comparamos si tomar el elemento actual da una mejor solución
            if value_with_item > max_value:
                max_value = value_with_item
                best_items = items_with_item
        
        return max_value, best_items
    
    # Llamamos a la función DFS desde el primer elemento
    max_value, best_items = dfs(0, 0, 0, [])
    
    # Regresamos el máximo valor y los elementos tomados
    return max_value, best_items
>>>>>>> master

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50

<<<<<<< HEAD
max_value, selected_items = knapsack_dynamic(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", selected_items)
=======
max_value, best_items = knapsack_backtracking(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", best_items)
>>>>>>> master
