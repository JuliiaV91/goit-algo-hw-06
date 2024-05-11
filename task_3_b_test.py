
graph = {
    "Ravensburg": {"München": 3, "Stuttgart": 2},
    "München": {"Ravensburg": 3, "Berlin": 11, "Dresden": 5, "Frankfurt": 6, "Düsseldorf": 9, "Stuttgart": 4},
    "Frankfurt": {"Düsseldorf": 2, "München": 6, "Stuttgart": 4, "Berlin": 8, "Wiesbaden": 1},
    "Düsseldorf": {"München": 9, "Berlin": 4, "Stuttgart": 5, "Frankfurt": 2, "Dresden": 3},
    "Dresden": {"Düsseldorf": 3, "Berlin": 5},
    "Berlin": {"Stuttgart": 6, "Frankfurt": 8, "Düsseldorf": 4, "Dresden": 5},
    "Stuttgart": {"München": 4, "Frankfurt": 4, "Düsseldorf": 5, "Berlin": 6, "Ravensburg": 2}, 
    "Wiesbaden": {"Frankfurt": 1}
}

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

print(dijkstra(graph, "Ravensburg"))
