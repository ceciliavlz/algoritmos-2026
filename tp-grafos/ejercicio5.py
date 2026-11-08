from clases.graph import Graph

#a. cada vertice tiene el equipo y su tipo 
grafo = Graph(is_dir=False)

nodos_red = [
    # Routers
    ("Router 1", "router"),
    ("Router 2", "router"),
    ("Router 3", "router"),
    # Switches
    ("Switch 1", "switch"),
    ("Switch 2", "switch"),
    # Servidores
    ("Guaraní", "servidor"),
    ("MongoDB", "servidor"),
    # Impresora
    ("Impresora", "impresora"),
    # Notebooks
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch", "notebook"),
    # PCs
    ("Ubuntu", "pc"),
    ("Mint", "pc"),
    ("Manjaro", "pc"),
    ("Fedora", "pc"),
    ("Parrot", "pc")
]
# Carga de aristas (conexiones y pesos de la imagen)
conexiones = [
    (37, "Router 1", "Router 2"),
    (43, "Router 1", "Router 3"),
    (50, "Router 2", "Router 3"),
    (29, "Router 1", "Switch 1"),
    (25, "Router 2", "Red Hat"),
    (9, "Router 2", "Guaraní"),
    (61, "Router 3", "Switch 2"),
    (17, "Switch 1", "Debian"),
    (18, "Switch 1", "Ubuntu"),
    (22, "Switch 1", "Impresora"),
    (80, "Switch 1", "Mint"),
    (40, "Switch 2", "Manjaro"),
    (12, "Switch 2", "Parrot"),
    (5, "Switch 2", "MongoDB"),
    (56, "Switch 2", "Arch"),
    (3, "Switch 2", "Fedora")
]
for nombre, tipo in nodos_red:
    grafo.add_vertex(nombre, other_values=tipo)

for peso, origen, destino in conexiones:
    grafo.add_edge(peso, origen, destination=destino)


#b: Barrido en profundidad y amplitud desde las 3 notebooks
notebooks = ["Red Hat", "Debian", "Arch"]

print("=== PUNTO b: BARRIDOS DESDE LAS NOTEBOOKS ===")
for nb in notebooks:
    print(f"\n--- Barrido en Profundidad (Deep Show) desde {nb}: ---")
    grafo.deep_show(nb)
    
    print(f"\n--- Barrido en Amplitud (Amplitude Show) desde {nb}: ---")
    grafo.amplitude_show(nb)


#c: Camino más corto para imprimir desde Manjaro, Red Hat y Fedora
print("\n=== PUNTO c: CAMINO MÁS CORTO HACIA LA IMPRESORA ===")
mejor_impresora = None
for origen in ["Manjaro", "Red Hat", "Fedora"]:
    camino, costo = grafo.shortest_path(origen, "Impresora")
    print(f"{origen} -> Impresora: {' -> '.join(camino)} | costo: {costo}")
    if costo is not None and (mejor_impresora is None or costo < mejor_impresora[1]):
        mejor_impresora = (origen, costo, camino)

if mejor_impresora is not None:
    print(f"Mejor opción: {mejor_impresora[0]} con costo {mejor_impresora[1]}")



#d: Árbol de expansión mínima (Kruskal)
print("\n=== PUNTO d: ÁRBOL DE EXPANSIÓN MÍNIMA ===")
min_tree = grafo.kruskal('Router 1')
print(min_tree)



#e: PC (no notebook) con el camino más corto al servidor “Guaraní”
print("\n=== PUNTO e: PC CON CAMINO MÁS CORTO A 'GUARANÍ' ===")
# Como el grafo es no dirigido, Dijkstra desde 'Guaraní' nos da la distancia a todos
paths_guarani = grafo.dijkstra('Guaraní')

mejor_pc = None
min_costo = float('inf')
camino_mejor_pc = []

while paths_guarani.size() > 0:
    value = paths_guarani.pop()
    nodo_nombre = value[0]
    costo = value[1]
    
    # Buscar el nodo en el grafo para verificar si su tipo es 'pc'
    pos = grafo.search(nodo_nombre, 'value')
    if pos is not None:
        tipo_nodo = grafo[pos].other_values
        if tipo_nodo == 'pc' and costo < min_costo:
            min_costo = costo
            mejor_pc = nodo_nombre
            # Reconstruir camino
            dest = nodo_nombre
            temp_camino = []
            # Copiamos temporalmente para reconstruir (o podemos guardar el stack)

print(f"La PC con el camino más corto hacia 'Guaraní' es: {mejor_pc} con un costo de {min_costo}")



#f: Computadora del Switch 1 con el camino más corto a “MongoDB”
print("\n=== PUNTO f: COMPUTADORA DE SWITCH 1 MÁS CERCANA A 'MONGODB' ===")
# Dispositivos directamente conectados al Switch 1 (según imagen): Debian, Ubuntu, Impresora, Mint
dispositivos_switch1 = ["Debian", "Ubuntu", "Impresora", "Mint"]

paths_mongo = grafo.dijkstra('MongoDB')
# Guardamos los resultados de Dijkstra en un diccionario auxiliar para consultar fácil
costos_mongo = {}
while paths_mongo.size() > 0:
    val = paths_mongo.pop()
    costos_mongo[val[0]] = (val[1], val[2])

menor_costo_sw1 = float('inf')
mejor_dispositivo_sw1 = None

for disp in dispositivos_switch1:
    if disp in costos_mongo:
        costo = costos_mongo[disp][0]
        if costo < menor_costo_sw1:
            menor_costo_sw1 = costo
            mejor_dispositivo_sw1 = disp

print(f"La computadora/dispositivo del Switch 1 más cercano a 'MongoDB' es: {mejor_dispositivo_sw1} (Costo: {menor_costo_sw1})")



#g: Cambiar conexión de la impresora al Router 2 y re-resolver punto b
print("\n=== PUNTO g: CAMBIAR IMPRESORA A ROUTER 2 Y RE-RESOLVER PUNTO b ===")
# 1. Eliminar arista actual de la impresora con Switch 1
grafo.delete_edge('Switch 1', 'Impresora')

# 2. Agregar nueva arista entre Router 2 e Impresora (asumiendo peso 22 como el original)
grafo.add_edge(22, 'Router 2', 'Impresora')

# 3. Volver a realizar los barridos en profundidad y amplitud desde las notebooks
for nb in notebooks:
    print(f"\n--- [Post-cambio] Profundidad desde {nb}: ---")
    grafo.deep_show(nb)
    
    print(f"\n--- [Post-cambio] Amplitud desde {nb}: ---")
    grafo.amplitude_show(nb)