from graph import Graph
from cycles import find_all_cycles


class NotBipartiteBecauseNotConnectedError(Exception):
    pass


class NotBipartiteBecauseHasThreeCycleError(Exception):
    pass


def find_connected_components(graph):
    components = []

    def visitor(node, parents):
        if len(parents) == 0:
            components.append(set())
        components[-1].add(node)

    graph.breadth_first_search(visitor)

    return map(Graph.from_nodes, components)


def validate_is_bipartite(graph):
    num_roots = 0

    def visitor(node, parents):
        if len(parents) == 0:
            nonlocal num_roots
            num_roots += 1

    graph.breadth_first_search(visitor)

    if num_roots != 1:
        raise NotBipartiteBecauseNotConnectedError()

    all_cycles = find_all_cycles(graph)

    for cycle in all_cycles:
        if len(cycle) == 3:
            raise NotBipartiteBecauseHasThreeCycleError()


def find_bipartite_sets(graph):
    validate_is_bipartite(graph)
    set1 = set()
    set2 = set()

    def visitor(node, parents):
        is_even_distance_from_root = len(parents) % 2 == 0
        target_set = set1 if is_even_distance_from_root else set2
        target_set.add(node)

    graph.breadth_first_search(visitor)

    assert len(set1) + \
        len(set2) == len(graph.nodes), 'Incomplete bipartite sets!'
    return (set1, set2)
