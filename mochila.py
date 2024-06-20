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

# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50

max_value, best_items = knapsack_backtracking(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", best_items)
