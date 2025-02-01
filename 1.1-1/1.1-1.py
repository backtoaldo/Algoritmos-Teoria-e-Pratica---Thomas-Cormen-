import heapq

def dijkstra(graph, start, end):
    # Inicializa as distâncias e os predecessores
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}

    # Define a distancia do nó inicial como 0
    distances[start] = 0

    # Cria uma fila de prioridade com os nós a serem processados
    queue = [(0, start)]

    while queue:
        # Extrai o nó com a menor distância da fila
        current_distance, current_node = heapq.heappop(queue)

        # Se o nó atual for o destino, podemos parar
        if current_node == end:
            break

        # Processa os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Se a distância para o vizinho for menor que a distância atual, atualiza a distância e o predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstrói a rota mais curta
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()

    return path, distances[end]

# Exemplo de uso
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1, 'E': 4},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

start_node = 'A'
end_node = 'F'

path, distance = dijkstra(graph, start_node, end_node)
print(f"Rota mais curta de {start_node} para {end_node}: {path}")
print(f"Distância: {distance}")
