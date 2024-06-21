import networkx as nx  # Librería para analizar grafos
import matplotlib.pyplot as plt  # Crea visualizaciones estáticas de los grafos

def knapsack_with_graph(values, weights, max_weight):
    n = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    G = nx.DiGraph()
    
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
            # Añadir nodo y arista al grafo
            node = (i, w, dp[i][w])
            if w - weights[i - 1] >= 0:
                prev_node1 = (i - 1, w, dp[i - 1][w])
                prev_node2 = (i - 1, w - weights[i - 1], dp[i - 1][w - weights[i - 1]])
                G.add_node(node)
                G.add_edge(prev_node1, node)
                G.add_edge(prev_node2, node)
            else:
                prev_node = (i - 1, w, dp[i - 1][w])
                G.add_node(node)
                G.add_edge(prev_node, node)
    
    max_value = dp[n][max_weight]
    w = max_weight
    items_taken = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append(i - 1)
            w -= weights[i - 1]
    
    return max_value, items_taken, G, dp, n, max_weight

# Ejemplo de uso
values = [60, 100, 120, 80]
weights = [10, 20, 30, 15]
max_weight = 50

max_value, items_taken, G, dp, n, max_weight = knapsack_with_graph(values, weights, max_weight)
print("El valor máximo que se puede obtener es:", max_value)
print("Los elementos a tomar son:", items_taken)

# Dibujar el grafo
pos = nx.spring_layout(G)
labels = {(i, w, v): f"{w},{v}" for i, w, v in G.nodes()}

nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)

# Función para resaltar la solución óptima
path = [(n, max_weight, dp[n][max_weight])]
current_weight = max_weight
for i in range(n, 0, -1):
    if dp[i][current_weight] != dp[i - 1][current_weight]:
        current_weight -= weights[i - 1]
        path.append((i - 1, current_weight, dp[i - 1][current_weight]))

path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="pink", width=2)

plt.title("Grafo de decisiones del problema de la mochila")
plt.show()
