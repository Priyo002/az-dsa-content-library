<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Graph Representation

A graph drawing helps us see connections. To work with the graph in a program, we need to **store those connections in a data structure**.

The same graph can be stored in different ways. The right representation depends on what we need to do: check whether an edge exists, visit a vertex's neighbours, or process all edges.

In this lesson, we will use:

- \(n = |V|\): the number of vertices.
- \(m = |E|\): the number of edges.
- Vertex labels from **1 to \(n\)**.

The C++ snippets below are meant to run inside `main()` or `solve()`, with `<iostream>`, `<vector>`, `<utility>`, and `using namespace std;` declared above them.

## One Graph, Three Representations

We will represent the following **directed, unweighted graph** in three ways.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/590f290a-4cfe-4642-9402-a9122944bdd6.png" alt="Directed graph with vertices 1 to 5 and edges 1 to 2, 1 to 3, 3 to 1, 2 to 4, 3 to 5, and 4 to 5" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The graph has \(n = 5\) vertices and \(m = 6\) edges:

$$
1 \rightarrow 2,\quad 1 \rightarrow 3,\quad
3 \rightarrow 1,\quad 2 \rightarrow 4,\quad
3 \rightarrow 5,\quad 4 \rightarrow 5
$$

Notice that \(1 \rightarrow 3\) and \(3 \rightarrow 1\) are **two separate directed edges**. Also, vertex 5 exists even though it has no outgoing edges.

## 1. Adjacency Matrix

An **adjacency matrix** stores an entry for every ordered pair of vertices. It is an \(n \times n\) table in which:

- Row \(u\) represents the starting vertex.
- Column \(v\) represents the destination vertex.
- `adj[u][v] = 1` if the edge \(u \rightarrow v\) exists; otherwise, `adj[u][v] = 0`.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/f1fa2473-4d9a-4f7c-a6f3-b6de4343f519.png" alt="Five-by-five adjacency matrix with ones at row-column pairs (1,2), (1,3), (2,4), (3,1), (3,5), and (4,5)" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Reading the Matrix

For example:

- `adj[1][2] = 1` because \(1 \rightarrow 2\) exists.
- `adj[2][1] = 0` because \(2 \rightarrow 1\) does not exist.
- Row 3 contains ones in columns 1 and 5 because vertex 3 has outgoing edges to vertices 1 and 5.
- Row 5 contains only zeros because vertex 5 has no outgoing edges. This does **not** mean that it has no incoming edges.

For this graph, the number of ones in a row equals the corresponding vertex's **outdegree**, and the number of ones in a column equals its **indegree**.

### Building It in C++

The following snippet reads a directed graph. Each input pair `u v` means \(u \rightarrow v\).

```cpp
int n, m;
cin >> n >> m;

vector<vector<int>> adj(n + 1, vector<int>(n + 1, 0));

for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    adj[u][v] = 1;
}
```

Because the labels start at 1, the code allocates an extra row and column and leaves index 0 unused. The representation still uses \(\Theta(n^2)\) space.

For an **undirected graph**, set both `adj[u][v] = 1` and `adj[v][u] = 1`. Its adjacency matrix is symmetric because the same edge allows movement in both directions.

### Cost and Trade-off

- **Storage:** \(\Theta(n^2)\), even if the graph has very few edges.
- **Check whether \(u \rightarrow v\) exists:** \(O(1)\), by reading `adj[u][v]`.
- **Find all outgoing neighbours of \(u\):** \(\Theta(n)\), because we scan the entire row.
- **Build from \(m\) input edges:** \(\Theta(n^2 + m)\), including initialization of the matrix.

A matrix is useful when constant-time edge checks are important and the matrix fits in memory. For a sparse graph with many vertices, most entries would be zeros.

> **Representation limit:** A 0/1 matrix records whether an edge exists, not how many parallel edges exist. Setting the same entry to 1 again does not preserve an additional edge.

## 2. Adjacency List

An **adjacency list** stores a separate list of neighbours for each vertex.

For a directed graph, `g[u]` contains the vertices that can be reached from \(u\) using **one outgoing edge**. It does not list every vertex reachable through a longer path.

In C++, we commonly use `vector<vector<int>>`:

- The outer vector identifies a vertex.
- The inner vector contains that vertex's outgoing neighbours.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/c047cdb6-88ad-49ef-bb8e-eb7c67231205.png" alt="Adjacency lists: 1 has neighbours 2 and 3; 2 has 4; 3 has 1 and 5; 4 has 5; 5 has an empty list" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Reading the Lists

For example:

- `g[1] = {2, 3}` stores the edges \(1 \rightarrow 2\) and \(1 \rightarrow 3\).
- `g[3] = {1, 5}` stores the edges \(3 \rightarrow 1\) and \(3 \rightarrow 5\).
- `g[5]` is empty because vertex 5 has no outgoing edges.

Unlike a matrix, an adjacency list does not store a zero for every missing edge.

### Building It in C++

```cpp
int n, m;
cin >> n >> m;

vector<vector<int>> g(n + 1);

for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
}
```

For an **undirected graph**, also execute `g[v].push_back(u)` inside the loop. One undirected input edge then produces **two adjacency entries**, but it still counts as only one edge in \(m\).

### Why Is the Space Complexity \(\Theta(n + m)\)?

There are two contributions:

1. We keep a list for each of the \(n\) vertices, including vertices whose lists are empty.
2. We store the endpoints of outgoing edges in those lists.

For a directed graph, the lists contain \(m\) entries in total. For an undirected graph stored in both directions, they contain \(2m\) entries.

Therefore:

$$
\text{Directed: } \Theta(n+m),
\qquad
\text{Undirected: } \Theta(n+2m) = \Theta(n+m)
$$

### Cost and Trade-off

- **Storage:** \(\Theta(n+m)\).
- **Visit all neighbours of \(u\):** proportional to the length of `g[u]`.
- **Check whether a specific edge \(u \rightarrow v\) exists:** requires a search through `g[u]` in this unsorted-vector representation; it is not generally \(O(1)\).
- **Build from input:** \(\Theta(n+m)\) overall, using amortized constant-time `push_back` operations.

An adjacency list is particularly useful for graph traversal: we can directly iterate over the edges available from the current vertex. This is the representation we will use for DFS.

## 3. Edge List

An **edge list** stores the edges directly as pairs of endpoints.

For a directed graph, the ordered pair \((u,v)\) means \(u \rightarrow v\). For an undirected graph, the pair records one edge joining \(u\) and \(v\); there is no need to store the reverse pair separately.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/9ef73344-8193-4107-9908-b62b1184eb8e.png" alt="Edge list containing the six directed pairs (1,3), (1,2), (2,4), (4,5), (3,5), and (3,1)" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Every pair in the image corresponds to one arrow in the original graph. Both \((1,3)\) and \((3,1)\) appear because both directed edges exist.

### Building It in C++

```cpp
int n, m;
cin >> n >> m;

vector<pair<int, int>> edges;
edges.reserve(m);

for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    edges.push_back({u, v});
}
```

This stores \(m\) pairs, or \(2m\) endpoint values. Dropping the constant factor 2, the asymptotic space complexity of the edge list is **\(\Theta(m)\)**.

Keep \(n\) separately: the edge list alone does not reveal isolated vertices. For example, a graph with five vertices and no edges still has five vertices, even though its edge list is empty.

### Cost and Trade-off

- **Storage for the edge list:** \(\Theta(m)\).
- **Build it or process every edge:** \(\Theta(m)\).
- **Find the neighbours of one vertex:** requires scanning the edge list, taking \(O(m)\) time.
- **Check whether a specific edge exists:** \(O(m)\) in the worst case for an unsorted list.

An edge list is convenient when the operation is naturally “process each edge.” It stores sparse graphs compactly, but an adjacency list is usually more convenient when repeatedly exploring neighbours.

## Comparing the Representations

For the unweighted implementations above, let \(d(u)\) be the number of entries in `g[u]`: outdegree for a directed graph, or degree for an undirected graph stored in both directions.

| Operation | Adjacency matrix | Adjacency list | Edge list |
| --- | --- | --- | --- |
| Storage | \(\Theta(n^2)\) | \(\Theta(n+m)\) | \(\Theta(m)\) for edges; keep \(n\) separately |
| Check whether \(u \rightarrow v\) exists | \(O(1)\) | \(O(1+d(u))\) | \(O(1+m)\) |
| List all neighbours of \(u\) | \(\Theta(n)\) | \(\Theta(1+d(u))\) | \(\Theta(1+m)\) |
| Main convenience | Direct edge lookup | Direct neighbour traversal | Direct iteration over edges |

The added 1 accounts for constant work even when a list is empty. These lookup costs assume ordinary unsorted vectors, as used in the snippets.

For sparse graphs, an adjacency list avoids allocating a large matrix of mostly zeros. For dense graphs, an adjacency list also takes \(\Theta(n^2)\) space because \(m = \Theta(n^2)\); the operations needed by the problem still determine the choice.

> **CP / interview check:** Read the direction and indexing conventions before building the graph. Add both adjacency entries for an undirected edge, but only the forward entry for a directed edge. With 1-based labels, allocate `n + 1` positions.

The order of stored edges or neighbours does not change which graph is represented. For example, `{2, 3}` and `{3, 2}` describe the same outgoing neighbours of vertex 1. However, this order can affect the order in which a traversal visits vertices.

## Quick Recap

- An **adjacency matrix** answers “Is there an edge between this pair?” directly.
- An **adjacency list** answers “Where can I go next from this vertex?” directly.
- An **edge list** stores the edges as endpoint pairs for processing one by one.
- Directed edges are stored in their given direction; undirected adjacency representations store both directions.
- Count vertices even when they have no incident edges.

Next, we will use an adjacency list to explore a graph with **Depth-First Search**.

</READING_WIDGET>
