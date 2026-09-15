# Graph Terminologies - 3

## Level 4

### Self Loop
A self loop is an edge in a graph that connects a vertex to itself.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/e980e0a0-0bd9-405b-b742-51b5c3ae0b71.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Multiple Edge
Multiple edges are two or more edges that connect the same pair of vertices in a graph.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/e7fd71b9-2902-43dc-b7d2-79130780b1bf.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Multigraph
A multigraph is a type of graph in which multiple edges between the same pair of vertices are allowed. Additionally, a multigraph may also include self loops.

### Simple Graph
A simple graph is a type of graph that has no self loops or multiple edges. Each pair of vertices is connected by at most one edge.


## Level 5

### Directed Acyclic Graph (DAG)

A Directed Acyclic Graph (DAG) is a directed graph with no cycles. In a DAG:
- Each edge is directed.
- There are no closed loops or cycles.
- It is commonly used in tasks like task scheduling, data flow diagrams, and representing dependencies.
- A DAG with `n` nodes has `n` Strongly Connected Components (SCCs), where each node forms its own SCC.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/f69ed07f-591c-49a2-87d9-d0893e6e69b6.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Tree
A tree is a connected acyclic graph. It has the following properties:
- A tree with `n` nodes has exactly `n-1` edges.
- There is a unique simple path between any two nodes in a tree.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/b239bf2d-e1f6-40bd-8994-477784bb0a92.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Forest
A forest is a disjoint union of trees. Each connected component of a forest is a tree.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/d1d29986-9cd7-401a-a0c7-2dfc41caf44f.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Bipartite Graph
A bipartite graph is a graph that can be colored using two colors, such that:
- Each vertex is assigned one of two colors.
- No two adjacent vertices share the same color.
- A bipartite graph does not contain odd-length cycles.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/2f2aea18-2bf6-4c6f-8371-a3f3f3b10577.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Chromatic Number
The chromatic number of a graph is the minimum number of colors required to color the vertices of the graph such that:
- No two adjacent vertices share the same color.
The chromatic number depends on the structure of the graph, and determining it is a fundamental problem in graph theory.

### Complete Graph
A complete graph is a graph in which every pair of distinct vertices is connected by a unique edge.
- A complete graph with `n` vertices is denoted as `K_n`.
- It contains exactly `(n * (n-1)) / 2` edges.
- Every vertex in a complete graph is adjacent to every other vertex.
  
<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/8c226dae-7cdb-4594-ab31-2d9e8c15481c.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">