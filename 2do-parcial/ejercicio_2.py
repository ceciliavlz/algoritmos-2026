"""
Ejercicio 2 - Grafo no dirigido de personajes de Star Wars.
"""

from graph import Graph
from star_wars_data import STAR_WARS_CHARACTERS, STAR_WARS_EDGES


def title(text):
    print()
    print("=" * 70)
    print(text)
    print("=" * 70)


def episodes_text(amount):
    return f"{amount} episodio" if amount == 1 else f"{amount} episodios"


def load_graph():
    """Carga personajes como vértices y relaciones como aristas."""
    graph = Graph(is_dir=False)  # Grafo no dirigido.

    for character in STAR_WARS_CHARACTERS:
        graph.add_vertex(character["name"], character)

    for origin, destination, weight in STAR_WARS_EDGES:
        graph.add_edge(weight, origin, destination)

    return graph


def show_graph(graph):
    title("Grafo de personajes de Star Wars")

    for vertex in graph:
        episodes = vertex.other_values["episodes_count"]
        print(f"{vertex.value} (episodios: {episodes})")
        for edge in vertex.edges:
            print(f"  -> {edge.destination}: {episodes_text(edge.weight)} juntos")


def parse_tree(tree):
    """Convierte el string devuelto por Graph.kruskal en una lista de aristas."""
    edges = []

    for part in tree.split(";"):
        if part:
            origin, destination, weight = part.split("-")
            edges.append((origin, destination, int(weight)))

    return edges


def show_mst(graph, origin):
    title(f"Árbol de expansión mínimo desde {origin}")

    tree = graph.kruskal(origin)
    edges = parse_tree(tree)
    edges.sort(key=lambda edge: (edge[2], edge[0], edge[1]))

    total = 0
    for origin_name, destination_name, weight in edges:
        print(f"  {origin_name} - {destination_name}: {episodes_text(weight)}")
        total += weight

    print(f"\nCantidad de aristas: {len(edges)}")
    print(f"Peso total del árbol: {total}")

    return edges


def normalized_pair(first, second):
    """Devuelve el par sin importar el orden (para no repetir aristas)."""
    return (first, second) if first <= second else (second, first)


def show_max_shared_episodes(graph):
    title("Máximo número de episodios compartidos entre dos personajes")

    seen = set()
    max_weight = -1
    pairs = []

    for vertex in graph:
        for edge in vertex.edges:
            pair = normalized_pair(vertex.value, edge.destination)
            if pair in seen:
                continue

            seen.add(pair)

            if edge.weight > max_weight:
                max_weight = edge.weight
                pairs = [pair]
            elif edge.weight == max_weight:
                pairs.append(pair)

    print(f"Máximo número de episodios compartidos: {max_weight}")
    print("Pares de personajes:")
    for first, second in pairs:
        print(f"  {first} - {second}")


def shortest_path(graph, origin, destination):
    """Calcula camino y costo usando Graph.dijkstra."""
    if not graph.exist_path(origin, destination):
        return None, None

    path_stack = graph.dijkstra(origin)

    # Cada elemento tiene la forma [personaje, distancia, predecesor].
    distances = {}
    predecessors = {}

    while path_stack.size() > 0:
        value, distance, predecessor = path_stack.pop()
        distances[value] = distance
        predecessors[value] = predecessor

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = predecessors[current]

    path.reverse()

    return path, distances[destination]


def show_shortest_path(graph, origin, destination):
    title(f"Camino más corto de {origin} a {destination}")

    path, cost = shortest_path(graph, origin, destination)

    if path is None:
        print("No existe un camino entre ambos personajes.")
        return

    print(" -> ".join(path))
    print(f"Costo total (episodios juntos): {cost}")


def show_nine_episodes():
    title("Personajes que aparecieron en los nueve episodios")

    characters = [
        character["name"]
        for character in STAR_WARS_CHARACTERS
        if character["episodes_count"] == 9
    ]

    for name in characters:
        print(f"  {name}")



graph = load_graph()
show_graph(graph)

# Árbol de expansión mínimo desde cada vértice pedido.
for origin in ("C_3PO", "Yoda", "Leia"):
    show_mst(graph, origin)

print(
    "\nComo el grafo es conexo, los tres árboles de expansión mínima "
    "coinciden:\ncontienen las mismas aristas y el mismo peso total."
)

# Máximo número de episodios compartidos y todos los pares que lo cumplen.
show_max_shared_episodes(graph)

# Caminos más cortos pedidos.
show_shortest_path(graph, "C_3PO", "R2_D2")
show_shortest_path(graph, "Yoda", "Darth_Vader")

# Personajes presentes en los nueve episodios.
show_nine_episodes()