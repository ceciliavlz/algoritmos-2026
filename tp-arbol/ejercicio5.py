"""
Ejercicio 5 - Arbol de superheroes y villanos.

Se utilizan las clases BinaryTree y Node de clases/tree.py y los datos de
super_heroes_data.py.
"""

from clases.tree import BinaryTree
from super_heroes_data import superheroes

def cargar_arbol():
    """a. Carga cada personaje con un booleano que indica si es villano."""
    arbol = BinaryTree()
    for personaje in superheroes:
        arbol.insert_node(
            personaje["name"],
            {"is_villain": personaje["is_villain"]},
        )
    return arbol


def generar_bosque(arbol):
    #g. Separa el arbol original en un arbol de heroes y otro de villanos.
    heroes = BinaryTree()
    villanos = BinaryTree()

    for nodo in arbol.inorden_nodes():
        if nodo.other_values["is_villain"]:
            villanos.insert_node(nodo.value, nodo.other_values)
        else:
            heroes.insert_node(nodo.value, nodo.other_values)

    return heroes, villanos


arbol = cargar_arbol()

print("\n=== b. Villanos ordenados alfabeticamente ===")
arbol.inorden_villain()

print("\n=== c. Superheroes que empiezan con C ===")
arbol.inorden_hero_star_with("C")

print("\n=== d. Cantidad de superheroes ===")
print(f"Hay {arbol.count_heroes()} superheroes en el arbol.")

print("\n=== e. Buscar a Doctor Strange por proximidad y corregir su nombre ====")
nodo = arbol.search_proxy("strann")
if nodo is not None:
    print(f"Encontrado: {nodo.value}")
    arbol.modify_value(nodo.value, "Dr Strange")
    print("Nombre corregido a: Dr Strange")
else:
    print("No se encontro el personaje.")

print("\n=== f. Superheroes ordenados de forma descendente ===")
arbol.postorden_hero()

print(" \n=== g. Bosque: arbol de superheroes y arbol de villanos ===")
heroes, villanos = generar_bosque(arbol)

print(f"Cantidad de nodos del arbol de superheroes: {heroes.count_nodes()}")
print(f"Cantidad de nodos del arbol de villanos: {villanos.count_nodes()}")

print("\nArbol de superheroes (orden alfabetico):")
heroes.inorden(show_height=False)

print("\nArbol de villanos (orden alfabetico):")
villanos.inorden(show_height=False)
