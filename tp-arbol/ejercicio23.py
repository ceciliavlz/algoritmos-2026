"""
Ejercicio 23 - Arbol de criaturas de la mitologia griega.

Se utilizan las clases BinaryTree y Node de clases/tree.py y HeapMax de
clases/heap.py.
"""

from clases.tree import BinaryTree
from clases.heap import HeapMax


datos_criaturas = [
    {"criatura": "Ceto", "derrotado_por": None},
    {"criatura": "Tifón", "derrotado_por": "Zeus"},
    {"criatura": "Equidna", "derrotado_por": "Argos Panoptes"},
    {"criatura": "Dino", "derrotado_por": None},
    {"criatura": "Pefredo", "derrotado_por": None},
    {"criatura": "Enio", "derrotado_por": None},
    {"criatura": "Escila", "derrotado_por": None},
    {"criatura": "Caribdis", "derrotado_por": None},
    {"criatura": "Euríale", "derrotado_por": None},
    {"criatura": "Esteno", "derrotado_por": None},
    {"criatura": "Medusa", "derrotado_por": "Perseo"},
    {"criatura": "Ladón", "derrotado_por": "Heracles"},
    {"criatura": "Águila del Cáucaso", "derrotado_por": None},
    {"criatura": "Quimera", "derrotado_por": "Belerofonte"},
    {"criatura": "Hidra de Lerna", "derrotado_por": "Heracles"},
    {"criatura": "León de Nemea", "derrotado_por": "Heracles"},
    {"criatura": "Esfinge", "derrotado_por": "Edipo"},
    {"criatura": "Dragón de la Cólquida", "derrotado_por": None},
    {"criatura": "Cerbero", "derrotado_por": None},
    {"criatura": "Cerda de Cromión", "derrotado_por": "Teseo"},
    {"criatura": "Ortro", "derrotado_por": "Heracles"},
    {"criatura": "Toro de Creta", "derrotado_por": "Teseo"},
    {"criatura": "Jabalí de Calidón", "derrotado_por": "Atalanta"},
    {"criatura": "Carcinos", "derrotado_por": None},
    {"criatura": "Gerión", "derrotado_por": "Heracles"},
    {"criatura": "Cloto", "derrotado_por": None},
    {"criatura": "Láquesis", "derrotado_por": None},
    {"criatura": "Átropos", "derrotado_por": None},
    {"criatura": "Minotauro de Creta", "derrotado_por": "Teseo"},
    {"criatura": "Harpías", "derrotado_por": None},
    {"criatura": "Argos Panoptes", "derrotado_por": "Hermes"},
    {"criatura": "Aves del Estínfalo", "derrotado_por": None},
    {"criatura": "Talos", "derrotado_por": "Medea"},
    {"criatura": "Sirenas", "derrotado_por": None},
    {"criatura": "Pitón", "derrotado_por": "Apolo"},
    {"criatura": "Cierva de Cerinea", "derrotado_por": None},
    {"criatura": "Basilisco", "derrotado_por": None},
    {"criatura": "Jabalí de Erimanto", "derrotado_por": None},
]

DESCRIPCIONES = {
    "Ceto": "Diosa marina, madre de las Grayas y las Gorgonas.",
    "Tifón": "Monstruo de cien cabezas, hijo de Gea y Tártaro.",
    "Equidna": "Mitad mujer y mitad serpiente, madre de monstruos.",
    "Dino": "Graya anciana, hermana de Enio y Pefredo.",
    "Pefredo": "Graya de cabellos grises, guardiana del camino a las Gorgonas.",
    "Enio": "Graya, hermana de Dino y Pefredo.",
    "Escila": "Monstruo marino con seis cabezas y doce patas.",
    "Caribdis": "Remolino marino que devora los barcos.",
    "Euríale": "Una de las Gorgonas, hermana de Medusa.",
    "Esteno": "Gorgona inmortal, hermana de Medusa.",
    "Medusa": "Gorgona cuyo cabello son serpientes; petrifica con la mirada.",
    "Ladón": "Dragón de cien cabezas que custodiaba las manzanas de las Hespérides.",
    "Águila del Cáucaso": "Ave que devoraba el hígado de Prometeo.",
    "Quimera": "Monstruo hibrido con cabeza de leon, cabra y serpiente.",
    "Hidra de Lerna": "Serpiente de muchas cabezas que regeneraban al cortarlas.",
    "León de Nemea": "Leon de piel invulnerable, estrangulado por Heracles.",
    "Esfinge": "Ser con cuerpo de leon y rostro de mujer que proponia acertijos.",
    "Dragón de la Cólquida": "Dragon que custodiaba el vellocino de oro.",
    "Cerbero": "Perro de tres cabezas, guardian del Hades.",
    "Cerda de Cromión": "Jabali gigante que asolaba Cromion.",
    "Ortro": "Perro de dos cabezas, hermano de Cerbero.",
    "Toro de Creta": "Toro monstruoso, padre del Minotauro.",
    "Jabalí de Calidón": "Jabali gigante cazado por Atalanta y Meleagro.",
    "Carcinos": "Cangrejo gigante aliado de la Hidra.",
    "Gerión": "Gigante de tres cuerpos, dueno de un rebano de bueyes.",
    "Cloto": "Moira que hila el hilo de la vida.",
    "Láquesis": "Moira que mide el hilo de la vida.",
    "Átropos": "Moira que corta el hilo de la vida.",
    "Minotauro de Creta": "Hombre con cabeza de toro encerrado en el laberinto.",
    "Harpías": "Aves con rostro de mujer que atormentaban a Fineo.",
    "Argos Panoptes": "Gigante de cien ojos, guardian infatigable.",
    "Aves del Estínfalo": "Aves de pico y plumas metalicas.",
    "Talos": "Automata de bronce que protegia Creta.",
    "Sirenas": "Seres con voz hipnotica que atraian a los navegantes.",
    "Pitón": "Serpiente gigante que custodiaba el oraculo de Delfos.",
    "Cierva de Cerinea": "Cierva de pezunas de bronce y astas de oro.",
    "Basilisco": "Serpiente cuyo aliento y mirada petrificaban.",
    "Jabalí de Erimanto": "Jabali gigante que asolaba el monte Erimanto.",
}


def titulo(texto):
    print()
    print("=" * 70)
    print(texto)
    print("=" * 70)


def cargar_arbol():
    """Genera el arbol. Cada nodo guarda derrotado_por, descripcion y capturada."""
    arbol = BinaryTree()
    for dato in datos_criaturas:
        arbol.insert_node(
            dato["criatura"],
            {
                "derrotado_por": dato["derrotado_por"],
                "descripcion": "",
                "capturada": None,
            },
        )
    return arbol


def cargar_descripcion(arbol, criatura, descripcion):
    """b. Carga una breve descripcion en el nodo de una criatura."""
    nodo = arbol.search(criatura)
    if nodo is not None:
        nodo.other_values["descripcion"] = descripcion
        return True
    return False


def mostrar_info(nodo):
    print(f"Criatura: {nodo.value}")
    print(f"  Derrotada por: {nodo.other_values['derrotado_por']}")
    print(f"  Descripcion: {nodo.other_values['descripcion']}")
    print(f"  Capturada por: {nodo.other_values['capturada']}")


def mostrar_top_3(arbol):
    """d. Usa un HeapMax para obtener los 3 que derrotaron mas criaturas."""
    cantidades = {}
    for nodo in arbol.inorden_nodes():
        heroe = nodo.other_values["derrotado_por"]
        if heroe is not None:
            cantidades[heroe] = cantidades.get(heroe, 0) + 1

    heap = HeapMax()
    for heroe, cantidad in cantidades.items():
        heap.arrive(heroe, cantidad)

    for _ in range(3):
        if heap.size() > 0:
            cantidad, heroe = heap.attention()
            print(f"  {heroe}: {cantidad} criatura(s)")


arbol = cargar_arbol()

titulo("a. Listado inorden de criaturas y quien las derroto")
for nodo in arbol.inorden_nodes():
    derrotado_por = nodo.other_values["derrotado_por"] or "No derrotada"
    print(f"{nodo.value}: {derrotado_por}")

titulo("b. Cargar una breve descripcion de cada criatura")
for criatura, descripcion in DESCRIPCIONES.items():
    cargar_descripcion(arbol, criatura, descripcion)
print("Descripciones cargadas en todas las criaturas.")

titulo("c. Toda la informacion de Talos")
nodo = arbol.search("Talos")
if nodo is not None:
    mostrar_info(nodo)
else:
    print("No se encontro a Talos.")

titulo("d. Los 3 heroes o dioses que derrotaron mas criaturas")
mostrar_top_3(arbol)

titulo("e. Criaturas derrotadas por Heracles")
for nodo in arbol.inorden_nodes():
    if nodo.other_values["derrotado_por"] == "Heracles":
        print(nodo.value)

titulo("f. Criaturas que no han sido derrotadas")
for nodo in arbol.inorden_nodes():
    if nodo.other_values["derrotado_por"] is None:
        print(nodo.value)

titulo("g. Campo 'capturada'")
print("Cada nodo tiene el campo 'capturada' (None = no fue capturada).")

titulo("h. Marcar como capturadas por Heracles")
for criatura in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    nodo = arbol.search(criatura)
    if nodo is not None:
        nodo.other_values["capturada"] = "Heracles"
        print(f"{criatura}: capturada por Heracles")

titulo("i. Busquedas por coincidencia")
print("Coincidencias con 'dra':")
arbol.proxy_search("dra", show_other_values=True)
print("\nCoincidencias con 'jabal':")
arbol.proxy_search("jabal", show_other_values=True)

titulo("j. Eliminar al Basilisco y a las Sirenas")
for criatura in ["Basilisco", "Sirenas"]:
    eliminada, datos = arbol.delete_node(criatura)
    if eliminada is not None:
        print(f"Eliminada: {eliminada}")
    else:
        print(f"No se encontro: {criatura}")

titulo("k. Agregar que Heracles derroto a varias Aves del Estinfalo")
nodo = arbol.search("Aves del Estínfalo")
if nodo is not None:
    nodo.other_values["derrotado_por"] = "Heracles (varias)"
    print("Aves del Estínfalo: derrotadas por Heracles (varias)")

titulo("l. Cambiar el nombre de Ladon por Dragon Ladon")
cambiado = arbol.modify_value("Ladón", "Dragón Ladón")
if cambiado is not None:
    print(f"{cambiado} ahora se llama Dragón Ladón")
else:
    print("No se encontro a Ladón.")

titulo("m. Listado por nivel del arbol")
arbol.by_level(show_level=True)

titulo("n. Criaturas capturadas por Heracles")
for nodo in arbol.inorden_nodes():
    if nodo.other_values["capturada"] == "Heracles":
        print(nodo.value)
