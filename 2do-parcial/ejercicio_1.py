"""
Ejercicio 1 - Pokémons y árboles binarios de búsqueda.

Se utilizan las clases BinaryTree y Node de tree.py y los datos de
pok_mon_list_generator.py.
"""

import random

from tree import BinaryTree
from pok_mon_list_generator import POKEMON_LIST


class Pokemon:

    def __init__(self, number, name, types, weaknesses, has_mega, has_gigantamax):
        self.number = number
        self.name = name
        self.types = types
        self.weaknesses = weaknesses
        self.has_mega = has_mega
        self.has_gigantamax = has_gigantamax

    def __str__(self):
        return (
            f"N.º {self.number:04d} - {self.name}\n"
            f"  Tipos: {', '.join(self.types)}\n"
            f"  Débil contra: {', '.join(self.weaknesses)}\n"
            f"  Megaevolución: {'Sí' if self.has_mega else 'No'}\n"
            f"  Gigamax: {'Sí' if self.has_gigantamax else 'No'}"
        )


def title(text):
    print()
    print("=" * 70)
    print(text)
    print("=" * 70)


def load_pokemons():
    pokemons = [Pokemon(**data) for data in POKEMON_LIST]
    random.shuffle(pokemons)
    return pokemons


def build_trees(pokemons):
    """Construye los árboles indexados por nombre, número y tipo."""
    name_tree = BinaryTree()
    number_tree = BinaryTree()
    type_tree = BinaryTree()

    for pokemon in pokemons:
        # Índice por nombre (se guarda el nombre original como clave).
        name_tree.insert_node(pokemon.name, pokemon)

        # Índice por número.
        number_tree.insert_node(pokemon.number, pokemon)

        # Índice por tipo. Varios Pokémons comparten el mismo tipo, por eso
        # el nodo del tipo guarda una lista con todos ellos.
        for type_name in pokemon.types:
            node = type_tree.search(type_name)
            if node is None:
                type_tree.insert_node(type_name, [pokemon])
            else:
                node.other_values.append(pokemon)

    return name_tree, number_tree, type_tree


def show_by_number(number_tree, number):
    title(f"Pokémon con número {number}")
    node = number_tree.search(number)
    if node is None:
        print(f"No se encontró un Pokémon con el número {number}.")
    else:
        print(node.other_values)


def show_by_name(name_tree, fragment):
    """fragment es el fragmento de nombre a buscar."""
    fragment = fragment.lower().strip()
    title(f'Pokémon cuyo nombre contiene "{fragment}"')
    name_tree.proxy_search(fragment, show_other_values=True)


def show_names_by_type(type_tree, type_name):
    node = type_tree.search(type_name)
    if node is None:
        print(f"No hay Pokémons de tipo {type_name}.")
        return

    pokemons = sorted(node.other_values, key=lambda pokemon: pokemon.name)
    print(f"Tipo {type_name} ({len(pokemons)} Pokémons):")
    for pokemon in pokemons:
        print(f"  {pokemon.name}")


def show_names_of_required_types(type_tree):
    title("Nombres de Pokémons de tipo Fantasma, Fuego, Acero y Eléctrico")
    for type_name in ("Fantasma", "Fuego", "Acero", "Eléctrico"):
        show_names_by_type(type_tree, type_name)
        print()


def show_ascending_by_number(number_tree):
    title("Listado ascendente por número")
    for pokemon in number_tree.inorden_list():
        print(f"  {pokemon.number:04d} - {pokemon.name}")


def show_ascending_by_name(name_tree):
    title("Listado ascendente por nombre")
    for pokemon in name_tree.inorden_list():
        print(f"  {pokemon.name}")


def show_by_level(name_tree):
    title("Listado por nivel (recorrido por niveles) usando el árbol de nombres")
    name_tree.by_level(show_level=True)


def show_weak_against(name_tree, target_names):
    title("Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum")

    for target_name in target_names:
        node = name_tree.search(target_name)
        if node is None:
            print(f"No se encontró {target_name}.")
            continue

        target = node.other_values
        target_types = set(target.types)
        weak_pokemons = [
            pokemon
            for pokemon in name_tree.inorden_list()
            if set(pokemon.weaknesses) & target_types
        ]

        print(
            f"\nFrente a {target.name} "
            f"(tipo/s: {', '.join(target.types)}):"
        )
        if not weak_pokemons:
            print("  Ninguno.")
            continue

        for pokemon in sorted(weak_pokemons, key=lambda item: item.name):
            coincidences = sorted(set(pokemon.weaknesses) & target_types)
            print(f"  {pokemon.name} (débil contra: {', '.join(coincidences)})")


def show_type_counts(type_tree):
    title("Tipos de Pokémons y cantidad de Pokémons de cada tipo")

    nodes = type_tree.inorden_nodes()
    total_assignments = 0

    for node in nodes:
        amount = len(node.other_values)
        total_assignments += amount
        print(f"  {node.value}: {amount}")

    print(f"\nTipos distintos registrados: {len(nodes)}")
    print(f"Total de asignaciones tipo-Pokémon: {total_assignments}")


def show_special_forms(name_tree):
    title("Pokémons con megavolución y con forma Gigamax")

    mega_count = name_tree.count_by(
        lambda pokemon: pokemon is not None and pokemon.has_mega
    )
    gigantamax_count = name_tree.count_by(
        lambda pokemon: pokemon is not None and pokemon.has_gigantamax
    )

    print(f"Pokémons con megavolución: {mega_count}")
    print(f"Pokémons con forma Gigamax: {gigantamax_count}")


pokemons = load_pokemons()
name_tree, number_tree, type_tree = build_trees(pokemons)

title("Ejercicio 1 - Pokémons")
print(f"Cantidad de Pokémons cargados: {len(pokemons)}")
print("Se construyeron tres árboles: por nombre, por número y por tipo.")

# Mostrar todos los datos a partir del número.
show_by_number(number_tree, 25)

# Mostrar todos los datos a partir del nombre (búsqueda por proximidad).
show_by_name(name_tree, "char")

# Nombres de Pokémons de los tipos pedidos.
show_names_of_required_types(type_tree)

# Listados ascendentes.
show_ascending_by_number(number_tree)
show_ascending_by_name(name_tree)

# Listado por nivel usando el índice de nombres.
show_by_level(name_tree)

# Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum.
show_weak_against(name_tree, ["Jolteon", "Lycanroc", "Tyrantrum"])

# Cantidad de Pokémons por tipo.
show_type_counts(type_tree)

# Megaevolución y Gigamax.
show_special_forms(name_tree)
