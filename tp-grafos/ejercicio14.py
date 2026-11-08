from clases.graph import Graph

# a: cada vértice es un ambiente de la casa (grafo no dirigido)
casa = Graph(is_dir=False)

ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho", "Baño 1", "Baño 2",
    "Habitación 1", "Habitación 2", "Sala de estar", "Terraza", "Patio"
]

for ambiente in ambientes:
    casa.add_vertex(ambiente)



# b: aristas con la distancia en metros
# Todos los vértices tienen al menos 3 aristas; Quincho y Terraza tienen 5.
conexiones = [
    (4,  "Cocina", "Comedor"),
    (6,  "Cocina", "Patio"),
    (8,  "Cocina", "Quincho"),
    (5,  "Cocina", "Sala de estar"),
    (3,  "Comedor", "Sala de estar"),
    (5,  "Comedor", "Baño 1"),
    (9,  "Comedor", "Terraza"),
    (5,  "Cochera", "Patio"),
    (7,  "Cochera", "Quincho"),
    (12, "Cochera", "Baño 2"),
    (4,  "Quincho", "Patio"),
    (10, "Quincho", "Terraza"),
    (9,  "Quincho", "Baño 2"),
    (4,  "Baño 1", "Habitación 1"),
    (6,  "Baño 1", "Habitación 2"),
    (5,  "Baño 2", "Habitación 2"),
    (6,  "Habitación 1", "Sala de estar"),
    (3,  "Habitación 1", "Habitación 2"),
    (7,  "Habitación 2", "Terraza"),
    (5,  "Sala de estar", "Terraza"),
    (11, "Terraza", "Patio"),
]

for metros, origen, destino in conexiones:
    casa.add_edge(metros, origen, destino)



# c: árbol de expansión mínima y metros de cable necesarios
print("=== PUNTO c: ÁRBOL DE EXPANSIÓN MÍNIMA ===")
arbol = casa.kruskal("Cocina")   # devuelve un string 'origen-destino-peso;origen-destino-peso;...'

total_cable = 0
for arista in arbol.split(';'): #formateo del string para mostrarlo bonito
    origen, destino, peso = arista.split('-')
    print(f"{origen} <-> {destino}: {peso} m")
    total_cable += int(peso)

print(f"\nMetros de cable necesarios para conectar todos los ambientes: {total_cable} m")



# d: camino más corto de Habitación 1 a Sala de estar (router -> Smart TV)
print("\n=== PUNTO d: CAMINO MÁS CORTO HABITACIÓN 1 -> SALA DE ESTAR ===")
camino, metros = casa.shortest_path("Habitación 1", "Sala de estar")

if metros is None:
    print("No existe un camino entre los dos ambientes")
else:
    print(f"Camino: {' -> '.join(camino)}")
    print(f"Metros de cable de red necesarios: {metros} m")