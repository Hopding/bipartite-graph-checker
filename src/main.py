import sys

from utils import pretty_format_cycle
from matrix import parse_adjacency_matrix
from graph import Graph, node_ids
from bipartite import find_connected_components, find_bipartite_sets, NotBipartiteBecauseHasThreeCycleError


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

connected_components = find_connected_components(graph)
print(f'Found {len(connected_components)} connected components.')
print()

for (idx, subgraph) in enumerate(connected_components):
    print(f'Finding bipartite vertex sets in connected component {idx}...')
    try:
        (set1, set2) = find_bipartite_sets(subgraph)
        print('Vertex Set 1:', node_ids(set1))
        print('Vertex Set 2:', node_ids(set2))
    except NotBipartiteBecauseHasThreeCycleError as e:
        print(f'Connected component {idx} is not bipartite.')
        print(f'Found cycle with length 3:')
        print(' ', pretty_format_cycle(e.cycle))
    print()

print('Done.')
