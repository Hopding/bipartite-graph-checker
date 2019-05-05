import sys

from utils import pretty_format_cycle
from matrix import parse_adjacency_matrix
from graph import Graph, node_ids
from bipartite import find_connected_components, find_bipartite_sets


if len(sys.argv) < 2:
    print('No input file specified')
    print('Exiting.')
    exit(1)

input_file_path = sys.argv[1]

print('Reading input file:', input_file_path)
with open(input_file_path, 'r') as input_file:
    contents = input_file.read().strip()
    lines = contents.splitlines()
print()

print('Using the following input data as Adjacency Matrix:')
longest_line = max([len(line) for line in lines])
print('-' * longest_line)
print(contents)
print('-' * longest_line)
print()

try:
    matrix = parse_adjacency_matrix(contents, log=True)
except Exception as e:
    print()
    print(e)
    print('Exiting.')
    exit(1)
print()

graph = Graph.from_adjacency_matrix(matrix)

for subgraph in find_connected_components(graph):
    (set1, set2) = find_bipartite_sets(subgraph)
    print('SET1:', node_ids(set1))
    print('SET2:', node_ids(set2))
    print()
