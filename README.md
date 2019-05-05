# UMSL CS5130 Project 3

This program fulfills the requirements for CS5130 Project 3. It takes the adjacency matrix for an undirected graph as input. It outputs, for each connected component in the graph, the two bipartite vertex sets, or the first three-cycle it encounters.

## Program Outline

When processing an input file, the following steps are performed:

1. **Input** - The input file is read, and split into rows based on newlines. Each row is split into cells based on spaces. The result is a matrix.
2. **Validation** - The matrix is validated as follows. If any of these validations fail, the program will notify the user and exit.

   - **Square Matrix** - The matrix must have the same number of rows and columns.
   - **Bit Value Entries** - Each cell in the matrix must be `0` or `1`.
   - **No Self-Loops** - The diagonal cells (from top left to bottom right) must all be `0`.
   - **Undirected Graph** - The adjacency matrix must be symmetric over the diagonal (from top left to bottom right).

3. **Find all Connected Components** - The matrix is converted into a graph. Each connected component in this graph is identified.
4. **Bipartite Validation** - Each connected component is validated to ensure it is bipartite. If a component is found to have at least one cycle of length 3, it is not bipartite.
5. **Find Vertex Sets** - Each bipartite component is processed to split it vertices into two disjoint and independent sets.
6. **Output Results** - For each connected component, one of two things is output, depending on whether or not it is bipartite. If the component is bipartite, its two vertex sets are printed to the console. Otherwise, the first cycle of length 3 is printed.

## Requirements

To run this program, you must have Python 3.7 installed on your machine. Older and newer versions may work, but only 3.7 has been tested.

## Running

- You can use the included `run` script:
  ```
  ./run data/test11.matrix
  ```
- Alternatively, you can run the `main.py` script directly:
  ```
  python3.7 src/main.py data/test11.matrix
  ```

## Unit Tests

- You can use the included `test` script:
  ```
  ./test
  ```
- Alternatively, you can run the `test_*.py` files directly:
  ```
  python3.7 src/test_adjacency_matrix.py
  python3.7 src/test_graph.py
  python3.7 src/test_cycles.py
  python3.7 src/test_bipartite.py
  ```

## Output For `data/*.matrix` Files

```
$ ./run data/test1.matrix
Reading input file: data/test1.matrix

Using the following input data as Adjacency Matrix:
-----
0 1 0
1 0 1
0 1 0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 1 connected components.

Finding bipartite vertex sets in connected component 0...
Vertex Set 1: [1]
Vertex Set 2: [0, 2]

Done.
```

```
$ ./run data/test2.matrix
Reading input file: data/test2.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 x
0 1 0
1 0 1
-----

Parsing matrix...
Validating matrix cells are 0 or 1...

Found invalid matrix cell: "x"
Exiting.
```

```
$ ./run data/test3.matrix
Reading input file: data/test3.matrix

Using the following input data as Adjacency Matrix:
-------
1 0 1
0 1 0 0
1 0 1
-------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...

Matrix is not square.
Exiting.
```

```
$ ./run data/test4.matrix
Reading input file: data/test4.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 1
0 1 0
1 0 1
0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...

Matrix is not square.
Exiting.
```

```
$ ./run data/test5.matrix
Reading input file: data/test5.matrix

Using the following input data as Adjacency Matrix:
-----
1 0 1
0 1 0
1 0 1
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...

Found self loop on vertex 0
Exiting.
```

```
$ ./run data/test6.matrix
Reading input file: data/test6.matrix

Using the following input data as Adjacency Matrix:
-----
0 1 0
0 0 1
0 1 0
-----

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found nonsymmetric cell in matrix: row=0 col=1
Exiting.
```

```
$ ./run data/test7.matrix
Reading input file: data/test7.matrix

Using the following input data as Adjacency Matrix:
---------------
0 1 0 0 1 0 0 0
1 0 0 0 0 1 0 0
0 0 0 1 0 1 1 0
0 0 1 0 0 0 1 1
1 0 0 0 0 0 0 0
0 1 1 0 0 0 1 0
0 0 1 1 0 1 0 1
0 0 0 1 0 0 1 0
---------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 1 connected components.

Finding bipartite vertex sets in connected component 0...
Connected component 0 is not bipartite.
Found cycle with length 3:
  5 -> 6 -> 2 -> 5

Done.
```

```
$ ./run data/test8.matrix
Reading input file: data/test8.matrix

Using the following input data as Adjacency Matrix:
---------
0 1 0 1 0
1 0 1 1 1
0 1 0 0 1
1 1 0 0 0
0 1 1 0 0
---------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 1 connected components.

Finding bipartite vertex sets in connected component 0...
Connected component 0 is not bipartite.
Found cycle with length 3:
  0 -> 3 -> 1 -> 0

Done.
```

```
$ ./run data/test9.matrix
Reading input file: data/test9.matrix

Using the following input data as Adjacency Matrix:
-------------
0 1 0 0 0 0 1
1 0 1 1 1 0 0
0 1 0 1 0 0 1
0 1 1 0 1 1 1
0 1 0 1 0 0 0
0 0 0 1 0 0 0
1 0 1 1 0 0 0
-------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 1 connected components.

Finding bipartite vertex sets in connected component 0...
Connected component 0 is not bipartite.
Found cycle with length 3:
  1 -> 3 -> 2 -> 1

Done.
```

```
$ ./run data/test10.matrix
Reading input file: data/test10.matrix

Using the following input data as Adjacency Matrix:
-----------------
0 0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 1 0 0
0 0 0 0 0 1 0 0 1
1 1 0 0 1 0 0 0 0
0 1 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 0 1 0 1 0 0 0 0
-----------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 1 connected components.

Finding bipartite vertex sets in connected component 0...
Vertex Set 1: [1, 2, 0, 4, 3]
Vertex Set 2: [7, 5, 6, 8]

Done.
```

```
$ ./run data/test11.matrix
Reading input file: data/test11.matrix

Using the following input data as Adjacency Matrix:
-----------------
0 0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0
0 0 0 0 1 0 0 0 1
0 0 0 1 0 0 0 0 1
1 1 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
-----------------

Parsing matrix...
Validating matrix cells are 0 or 1...
Validating matrix is square...
Validating matrix contains no self loops...
Validating matrix is symmetric...

Found 2 connected components.

Finding bipartite vertex sets in connected component 0...
Vertex Set 1: [0, 2, 1]
Vertex Set 2: [7, 5, 6]

Finding bipartite vertex sets in connected component 1...
Connected component 1 is not bipartite.
Found cycle with length 3:
  3 -> 8 -> 4 -> 3

Done.
```
