import sys

from utils import pretty_format_cycle
from matrix import parse_adjacency_matrix
from graph import Graph
from cycles import find_all_cycles
from bipartite import find_connected_components, validate_is_bipartite


# # Visualization:
# #
# #    0---1  2
# #           |
# #       3---4
# #
# matrix = [
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1],
#     [0, 0, 1, 1, 0],
# ]

# # Visualization:
# #
# #    0---1---2
# #        |   |
# #        3---4
# #
# matrix = [
#     [0, 1, 0, 0, 0],
#     [1, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 0, 1, 0, 0],
# ]


# Visualization:
#
#   0---1   2---3
#   |   | / | / |
#   4   5---6---7
#
matrix = [
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0],
]

graph = Graph.from_adjacency_matrix(matrix)

connected_components = find_connected_components(graph)

for subgraph in connected_components:
    print('COMPONENTS:')
    print(subgraph.nodes)
    validate_is_bipartite(subgraph)
    print()

# if len(sys.argv) < 2:
#     print('No input file specified')
#     print('Exiting.')
#     exit(1)

# input_file_path = sys.argv[1]

# print('Reading input file:', input_file_path)
# with open(input_file_path, 'r') as input_file:
#     contents = input_file.read().strip()
#     lines = contents.splitlines()
# print()

# print('Using the following input data as Adjacency Matrix:')
# longest_line = max([len(line) for line in lines])
# print('-' * longest_line)
# print(contents)
# print('-' * longest_line)
# print()

# try:
#     matrix = parse_adjacency_matrix(contents, log=True)
# except Exception as e:
#     print()
#     print(e)
#     print('Exiting.')
#     exit(1)
# print()

# graph = Graph.from_adjacency_matrix(matrix)

# print('Finding all cycles in graph...')
# cycles = find_all_cycles(graph)
# if len(cycles) == 0:
#     print('Graph contains no cycles.')
#     print('Exiting.')
#     exit(0)
# for cycle in cycles:
#     print('• Found cycle:', pretty_format_cycle(cycle))
# print()

# print('Finding girth of graph...')
# girth = min(map(len, cycles))
# print('• Found girth:', girth)
# print()

# print('Finding all cycles whose length equals the girth...')
# girth_cycles = [cycle for cycle in cycles if len(cycle) == girth]
# for cycle in girth_cycles:
#     pretty_cycle = pretty_format_cycle(cycle)
#     print('• Found girth cycle:', pretty_cycle)
