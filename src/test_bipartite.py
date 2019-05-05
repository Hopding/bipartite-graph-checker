import unittest

from inspect import isclass

from graph import Graph, node_ids
from bipartite import find_bipartite_sets, NotBipartiteBecauseHasThreeCycleError, NotBipartiteBecauseNotConnectedError

# Tool to help create ASCII graphs: http://asciiflow.com/
test_cases = [
    # Visualization:
    #
    #    0---1---2
    #
    [[
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ], (
        {2, 0},
        {1},
    )],

    # Visualization:
    #
    #    0---1---2
    #        |   |
    #        3---4
    #
    [[
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
    ], (
        {3, 0, 2},
        {4, 1},
    )],

    # Visualization:
    #
    #    0---1  2
    #           |
    #       3---4
    #
    [[
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
    ], NotBipartiteBecauseNotConnectedError],

    # Visualization:
    #
    #   0---1   2---3
    #   |   | / | / |
    #   4   5---6---7
    #
    [[
        [0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
    ], NotBipartiteBecauseHasThreeCycleError],

    # Visualization:
    #
    #   --3--
    #   |   |
    #   0---1---2
    #       |   |
    #       --4--
    #
    [[
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
    ], NotBipartiteBecauseHasThreeCycleError],

    # Visualization:
    #
    #   -------------
    #   |           |
    #   |   ----4   |
    #   |   |   |   |
    #   0---1-\ |   |
    #       |  -3---6
    #       2-/ |   |
    #       |   |   |
    #       |   5   |
    #       |       |
    #       ---------
    #
    [[
        [0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
    ], NotBipartiteBecauseHasThreeCycleError],

    # Visualization:
    #
    #      0+-----+
    #             |
    #         +---+5
    #         |   |
    #      1+-----+
    #       | |
    #       +---+-+6
    #         | |
    #    ++2+-----+
    #    |    | | |
    #    |    | | +7
    #    |    | |
    #    | 3+---+
    #    |    |
    #    |  +-----+8
    #    |  | |    +
    #    | 4+-+    |
    #    |         |
    #    +---------+
    #
    [[
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0],
    ], (
        {0, 1, 2, 3, 4},
        {5, 6, 7, 8},
    )]
]


class TestFindBipartiteSets(unittest.TestCase):
    pass


def create_success_test(matrix, result):
    def test(self):
        graph = Graph.from_adjacency_matrix(matrix)
        (set1, set2) = find_bipartite_sets(graph)
        actual = (set(node_ids(set1)), set(node_ids(set2)))
        expected = result
        self.assertEqual(actual, expected)
    return test


def create_error_test(matrix, result):
    def test(self):
        graph = Graph.from_adjacency_matrix(matrix)
        self.assertRaises(result, find_bipartite_sets, graph)
    return test


if __name__ == '__main__':
    for (idx, test_case) in enumerate(test_cases):
        matrix = test_case[0]
        result = test_case[1]
        is_error_test = isclass(result) and issubclass(result, Exception)

        if is_error_test:
            test_name = f'test_{result.__name__}_{idx}'
            test = create_error_test(matrix, result)
        else:
            test_name = f'test_{idx}'
            test = create_success_test(matrix, result)

        setattr(TestFindBipartiteSets, test_name, test)

    unittest.main()
