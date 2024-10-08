<<<<<<< HEAD
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
=======
import networkx as nx
import matplotlib.pyplot as plt

def knapsack_backtracking(values, weights, max_weight):
    # Número de elementos
    n = len(values)
    
    # Función auxiliar de DFS y backtracking
    def dfs(index, current_weight, current_value, taken_items, G, parent=None):
        # Añadir nodo al grafo
        node = (index, current_weight, current_value)
        G.add_node(node)
        if parent:
            G.add_edge(parent, node)
        
        # Caso base: si hemos considerado todos los elementos
        if index == n:
            return current_value, taken_items
        
        # Opción 1: no tomar el elemento actual
        max_value, best_items = dfs(index + 1, current_weight, current_value, taken_items, G, node)
        
        # Opción 2: tomar el elemento actual (si cabe en la mochila)
        if current_weight + weights[index] <= max_weight:
            value_with_item, items_with_item = dfs(index + 1, current_weight + weights[index], current_value + values[index], taken_items + [index], G, node)
            # Comparamos si tomar el elemento actual da una mejor solución
            if value_with_item > max_value:
                max_value = value_with_item
                best_items = items_with_item
        
        return max_value, best_items
    
    # Crear grafo vacío
    G = nx.DiGraph()
    
    # Llamamos a la función DFS desde el primer elemento
    max_value, best_items = dfs(0, 0, 0, [], G)
    
    # Regresamos el máximo valor, los elementos tomados y el grafo
    return max_value, best_items, G

# Ejemplo de uso
values = [60, 100, 120, 80]
weights = [10, 20, 30, 15]
max_weight = 50

max_value, best_items, G = knapsack_backtracking(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", best_items)

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = {(i, w, v): f"{i},{w},{v}" for i, w, v in G.nodes()}

nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)

# funcion para Resaltar la solución óptima
path = [(0, 0, 0)]
current_weight = 0
current_value = 0
for i in best_items:
    current_weight += weights[i]
    current_value += values[i]
    path.append((i + 1, current_weight, current_value))

path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="yellow", width=2)

plt.title("Grafo de decisiones del problema de la mochila")
plt.show()
>>>>>>> master
