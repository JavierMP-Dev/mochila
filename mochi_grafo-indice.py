import networkx as nx
import matplotlib.pyplot as plt

def knapsack_backtracking(values, weights, max_weight):
    # Número de elementos
    n = len(values)
    
    # Función auxiliar de DFS y backtracking
    def dfs(index, current_weight, current_value, taken_items, G, parent=None):
        # Añadir nodo al grafo
        node = (index, current_weight)
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
labels = {(i, w): f"{i},{w}" for i, w in G.nodes()}

nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)

# Resaltar la solución óptima
path = [(0, 0)]
current_weight = 0
for i in best_items:
    current_weight += weights[i]
    path.append((i + 1, current_weight))

path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

plt.title("Grafo de decisiones del problema de la mochila")
plt.show()
