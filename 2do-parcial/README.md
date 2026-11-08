# Segundo parcial - Ejercicios 1 y 2

Este trabajo suma dos ejercicios aplicados a estructuras de datos y algoritmos para el parcial.

## Ejercicio 1: Pokémon y árboles binarios de búsqueda

Se trabaja con una base de datos de Pokémon (archivo `pok_mon_list_generator.py`) y se construyen tres índices para acceder a la información de forma eficiente:

- árbol por nombre
- árbol por número
- árbol por tipo

Además, se agregan las siguientes funcionalidades:

- mostrar todos los datos de un Pokémon por su número
- buscar Pokémon por nombre con coincidencia parcial (por ejemplo: "bul")
- listar Pokémon por tipo: Fantasma, Fuego, Acero y Eléctrico
- mostrar listados ordenados ascendentemente por número y por nombre
- recorrer el árbol por niveles
- identificar qué Pokémon son débiles frente a Jolteon, Lycanroc y Tyrantrum
- contar cuántos Pokémon hay por tipo
- contar cuántos Pokémon tienen megaevolución
- contar cuántos Pokémon tienen forma Gigamax

## Ejercicio 2: Grafos de Star Wars

Se trabaja con un grafo no dirigido donde cada vértice es un personaje y cada arista representa la cantidad de episodios en los que ambos personajes aparecieron juntos.

Se agregan estas tareas:

- cargar personajes y relaciones entre ellos
- obtener el árbol de expansión mínimo desde C-3PO, Yoda y Leia
- determinar el máximo número de episodios compartidos entre dos personajes
- mostrar todos los pares que cumplen ese máximo
- calcular caminos mínimos entre C-3PO y R2-D2, y entre Yoda y Darth Vader
- identificar qué personajes aparecieron en los nueve episodios de la saga


## Cómo ejecutarlos

```bash
python ejercicio_1.py
python ejercicio_2.py
```
