<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Graph Terminologies - 1

A graph describes **objects and the connections between them**. For example, in a road network, the objects can be intersections and the connections can be roads.

In this lesson, we will learn how to name the parts of a graph, describe its edges, and count the connections at each vertex.

## Level-1 Terms: The Building Blocks

### Vertex (Node)

A **vertex**, also called a **node**, represents one object in a graph.

For example:

- In a social network, a vertex can represent a person.
- In a road network, a vertex can represent an intersection.

In a diagram, vertices are usually drawn as circles. A number or name inside a circle identifies the vertex.

### Edge

An **edge** connects two vertices. It represents a relationship between the objects represented by those vertices.

For example, an edge can represent a friendship between two people or a road between two intersections.

An edge joining vertices 1 and 2 is written as \((1, 2)\). Whether the order matters depends on whether the graph is directed or undirected, which we will discuss below.

### Sets of Vertices and Edges: \(V\) and \(E\)

We use two sets to describe a graph:

- \(V\): the set of all vertices.
- \(E\): the set of all edges.

The **cardinality** of a set means the number of elements in it. Therefore:

- \(|V|\): the number of vertices.
- \(|E|\): the number of edges.

Keep the set and its size separate: \(V\) is a collection of vertices, while \(|V|\) is a number. The same distinction applies to \(E\) and \(|E|\).

### Graph Notation: \(G = (V, E)\)

We write a graph as \(G = (V, E)\), also commonly written as \(G(V, E)\). This tells us which vertices exist and which edges connect them.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/5f47ef55-547c-413b-b3dc-a27649e40177.png" alt="Graph with five vertices and five edges, showing the vertex set V and edge set E" style="max-width: 100%; height: auto;" identifier="az-img-upload">

For the graph above:

$$
V = \{1, 2, 3, 4, 5\}, \qquad |V| = 5
$$

$$
E = \{(1,2), (1,3), (2,3), (3,4), (3,5)\}, \qquad |E| = 5
$$

For example, vertex 3 has edges joining it to vertices 1, 2, 4, and 5.

> **CP notation:** Problem statements often use \(n\) for the number of vertices and \(m\) for the number of edges. In that notation, \(n = |V|\) and \(m = |E|\).

## Level-2 Terms: Describing a Graph

### Weighted and Unweighted Graphs

This distinction answers the question: **Does each edge carry a numerical value?**

#### Unweighted Graph

In an **unweighted graph**, edges indicate connections without an explicitly assigned weight.

For example, an edge may tell us that two people are friends. It does not specify a numerical cost or distance.

#### Weighted Graph

In a **weighted graph**, each edge has a numerical value called its **weight**. Depending on the problem, this value may represent distance, cost, time, or capacity.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/0e995a2b-0950-40bd-b908-313fafd42d9e.png" alt="The same four-vertex graph shown without weights and with edge weights 1, 4, 2, and 8" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Both graphs above have the same connections. The graph on the right additionally assigns a weight to each edge:

- The edge between vertices 1 and 2 has weight 1.
- The edge between vertices 1 and 3 has weight 4.
- The edge between vertices 2 and 3 has weight 2.
- The edge between vertices 3 and 4 has weight 8.

The numbers **inside the vertices** identify them. The numbers **beside the edges** are weights. Adding weights does not change the number of edges.

### Directed and Undirected Graphs

This distinction answers the question: **Does an edge have a direction?**

#### Undirected Graph

In an **undirected graph**, an edge has no direction. A connection between \(u\) and \(v\) works both ways.

For example, a two-way road allows travel from \(u\) to \(v\) and from \(v\) to \(u\).

The notations \((u, v)\) and \((v, u)\) refer to the **same undirected edge**. It is counted once in \(|E|\).

#### Directed Graph

In a **directed graph**, each edge points from one vertex to another. We write \(u \rightarrow v\) for an edge from \(u\) to \(v\).

For example, a one-way road from \(u\) to \(v\) does not automatically allow travel from \(v\) to \(u\).

The edges \(u \rightarrow v\) and \(v \rightarrow u\) are **different directed edges**. Either, both, or neither may exist.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/cbead11a-e2d4-4698-a5d6-f7cf73c6fd72.png" alt="Undirected edges compared with directed arrows, including separate arrows from 1 to 2 and from 2 to 1" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the directed graph above, there are two separate arrows between vertices 1 and 2: \(1 \rightarrow 2\) and \(2 \rightarrow 1\). The arrow \(4 \rightarrow 3\), however, does not imply an edge \(3 \rightarrow 4\).

**Direction and weight describe different properties.** A graph can be directed or undirected independently of whether it is weighted or unweighted.

### Labelled and Unlabelled Graphs

This distinction answers the question: **Are the vertices given specific identities?**

#### Labelled Graph

In a **labelled graph**, vertices have distinct labels, such as numbers or names. These labels let us refer to a particular vertex.

For example, “the edge between vertices 1 and 2” uses labels to identify its endpoints.

#### Unlabelled Graph

In an **unlabelled graph**, vertices are not assigned specific identities. We focus on how they are connected rather than on their names.

The vertices still exist as separate objects; the absence of labels does not remove them or their edges.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/19d9a0af-5356-4a24-8dd2-a6035c3b3f04.png" alt="Matching graph structures with numbered vertices on the left and unlabelled vertices on the right" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The two drawings above show the same pattern of connections. The left drawing identifies the vertices using 1, 2, 3, and 4; the right drawing omits those labels.

A vertex label is an identifier, not an edge weight.

### Sparse and Dense Graphs

This distinction answers the question: **How many edges are present relative to the number that could be present?**

- A **sparse graph** has relatively few edges.
- A **dense graph** has relatively many edges.

To compare them, let \(n = |V|\) and \(m = |E|\).

For an undirected graph in which edges join distinct vertices and each pair has at most one edge:

$$
0 \leq m \leq \frac{n(n-1)}{2}
$$

The maximum occurs when every pair of distinct vertices is joined by an edge. Such a graph is called a complete graph. The maximum grows quadratically with \(n\), or \(\Theta(n^2)\).

For a directed graph with no edges from a vertex to itself and at most one edge for each ordered pair, the maximum is \(n(n-1)\), which is also \(\Theta(n^2)\).

In common algorithmic usage, graphs with \(O(n)\) edges are typical sparse graphs, while graphs with \(\Theta(n^2)\) edges are typical dense graphs. **There is no universal numerical cutoff** separating the two terms.

<img src="images/sparse-dense-corrected.png" alt="Sparse and dense graphs compared by increasing edge count for the same number of vertices" style="max-width: 100%; height: auto;" identifier="az-img-upload">


### Degree in an Undirected Graph

The **degree** of a vertex is the number of edge ends attached to it. For the edges shown here, which join different vertices, this is simply the number of edges connected to that vertex.

We write the degree of vertex \(v\) as \(\deg(v)\).

<img src="https://d3pdqc0wehtytt.cloudfront.net/academy-media/27/65449667-e195-4e9d-adeb-4bbf88c4e50e.png" alt="Six-vertex undirected graph with degrees 1, 1, 2, 2, 2, and 0, summing to twice its four edges" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the graph above:

- Vertices 1 and 2 each have degree 1.
- Vertices 3, 4, and 5 each have degree 2.
- Vertex 6 has degree 0 because no edge is attached to it.

A vertex does not need an edge to be part of the graph. Vertex 6 still contributes to \(|V|\).

#### Sum of Degrees

Each undirected edge has two ends, so it contributes a total of 2 to the sum of all vertex degrees:

$$
\sum_{v \in V} \deg(v) = 2|E|
$$

For the illustrated graph, there are four edges:

$$
1 + 1 + 2 + 2 + 2 + 0 = 8 = 2 \times 4
$$

We count each edge once in \(|E|\), but its two ends contribute separately to the degree sum.

> **Quick check:** If the degrees of all vertices are given, their sum must equal twice the number of edges. This is a useful way to check an edge count or catch a counting mistake.

### Indegree and Outdegree in a Directed Graph

In a directed graph, distinguish between edges entering a vertex and edges leaving it:

- **Indegree**, written \(\operatorname{indeg}(v)\): the number of edges pointing **into** \(v\).
- **Outdegree**, written \(\operatorname{outdeg}(v)\): the number of edges pointing **out of** \(v\).

An edge \(u \rightarrow v\) contributes 1 to the outdegree of \(u\) and 1 to the indegree of \(v\).

<img src="https://d3pdqc0wehtytt.cloudfront.net/academy-media/27/b11b198b-442c-4500-bed2-3cf9914e0a5d.png" alt="Directed graph with edges 1 to 2, 2 to 3, 2 to 4, and 4 to 3, showing each vertex's indegree and outdegree" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The image contains four directed edges:

$$
1 \rightarrow 2,\qquad 2 \rightarrow 3,\qquad
2 \rightarrow 4,\qquad 4 \rightarrow 3
$$

| Vertex | Incoming edges | Indegree | Outgoing edges | Outdegree |
| --- | --- | --- | --- | --- |
| 1 | None | 0 | \(1 \rightarrow 2\) | 1 |
| 2 | \(1 \rightarrow 2\) | 1 | \(2 \rightarrow 3,\;2 \rightarrow 4\) | 2 |
| 3 | \(2 \rightarrow 3,\;4 \rightarrow 3\) | 2 | None | 0 |
| 4 | \(2 \rightarrow 4\) | 1 | \(4 \rightarrow 3\) | 1 |

#### Sum of Indegrees and Outdegrees

Every directed edge leaves one vertex and enters one vertex. Therefore, it is counted once in each sum:

$$
\sum_{v \in V} \operatorname{indeg}(v)
=
\sum_{v \in V} \operatorname{outdeg}(v)
=
|E|
$$

For the graph above:

$$
\text{Sum of indegrees} = 0 + 1 + 2 + 1 = 4
$$

$$
\text{Sum of outdegrees} = 1 + 2 + 0 + 1 = 4
$$

Adding the two sums gives:

$$
\sum_{v \in V}
\left(\operatorname{indeg}(v) + \operatorname{outdeg}(v)\right)
= 2|E| = 8
$$

**Each separate sum is \(|E|\); only the combined sum is \(2|E|\).** Individual vertices do not need equal indegree and outdegree.

## Quick Recap

- **Vertices** are the objects; **edges** are the connections.
- \(V\) and \(E\) are sets; \(|V|\) and \(|E|\) are their sizes.
- **Weights** attach numerical values to edges; **directions** specify which way edges point.
- **Labels** identify vertices; they are not weights.
- **Sparse and dense** describe relative edge counts, not a fixed universal threshold.
- In an **undirected graph**, the degree sum is \(2|E|\).
- In a **directed graph**, the indegree sum and outdegree sum are each \(|E|\).

</READING_WIDGET>
