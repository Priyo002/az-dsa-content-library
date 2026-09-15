<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Graph Terminologies - 2

In the previous lesson, we described vertices, edges, and the different types of graphs. Now we will describe **how we move through a graph** and **which vertices can reach one another**.

## Level-3 Terms: Paths and Connectivity

### Path

A path describes a sequence of vertices visited by following edges:

$$
x_1, x_2, x_3, \ldots, x_r
$$

Every consecutive pair must be connected by an edge. In a directed graph, each edge must point in the direction we want to move: \(x_i \rightarrow x_{i+1}\).

In this lesson, a **path** has no repeated vertices. The term **simple path** makes this condition explicit.


The **length** of a path is the number of edges traversed, not the number of vertices written down. A path containing \(r\) vertices uses \(r-1\) edges.

### Cycle

A **cycle** follows edges back to its starting vertex, without repeating any other vertex or reusing an edge:

$$
x_1 = x_r
$$

The route must follow valid edges throughout. In a directed graph, it must also follow the arrows, including the edge that returns to the starting vertex.

The repeated starting vertex closes the loop. For example, \(2,3,6,5,2\) starts and ends at 2, with no other vertex repetition.

### Simple Path

A **simple path** is a path in which **no vertex appears more than once**.

This also prevents edges from repeating. However, checking only for repeated edges is not enough: a route can revisit a vertex using different edges.

For example, following a loop back to an already visited vertex breaks the simple-path condition even if every edge used so far is different.

### Simple Cycle

A **simple cycle** returns to its starting vertex without repeating any other vertex or reusing an edge.

The starting vertex is written again at the end to show that the loop closes. This is the only permitted vertex repetition.

In an undirected graph like the one below, going along an edge and immediately coming back along that same edge does **not** form a simple cycle.

<img src="images/paths-corrected.png" alt="Six-vertex graph with valid path, cycle, simple path, and simple cycle examples" style="max-width: 100%; height: auto;" identifier="az-img-upload">

#### Reading the Examples

The graph above contains the edges \((1,2)\), \((2,3)\), \((3,4)\), \((2,5)\), \((5,6)\), and \((3,6)\).

| Label in the image | Vertex sequence | What to notice |
| --- | --- | --- |
| Path | \(1,2,3,4\) | All vertices are distinct and consecutive vertices share an edge. Its length is 3. |
| Cycle | \(2,3,6,5,2\) | It returns to 2 without repeating any other vertex or reusing an edge. Its length is 4. |
| Simple Path | \(1,2,3,6,5\) | All five vertices are distinct. Its length is 4. |
| Simple Cycle | \(2,5,6,3,2\) | It follows the same loop in the opposite direction. Only vertex 2 repeats at the end. Its length is 4. |

Under these definitions, a path is a simple path and a cycle is a simple cycle. The word **simple** emphasizes the restriction on repetitions; avoiding repeated edges alone is not enough.

### Reachable

A vertex \(x\) is **reachable from** a vertex \(y\) if there is a valid path starting at \(y\) and ending at \(x\).

Read the phrase carefully:

$$
\text{“}x\text{ is reachable from }y\text{” means start at }y\text{ and reach }x.
$$

A direct edge is not required. We may pass through other vertices along the way.

A vertex is also considered reachable from itself without traversing any edges. This matters when discussing components containing just one vertex.

#### Reachability in an Undirected Graph

In an undirected graph, a path can be followed in reverse. Therefore, if \(x\) is reachable from \(y\), then \(y\) is reachable from \(x\).

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/8b7082be-a067-424f-b9b0-ce3995eb8b08.png" alt="Undirected graph in which vertices 1 through 5 can reach one another but cannot reach vertices 6 through 8" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In this graph:

- **1 is reachable from 4:** follow \(4,3,2,1\).
- **4 is reachable from 1:** reverse that path and follow \(1,2,3,4\).
- **1 is not reachable from 7:** there is no sequence of edges joining the right-hand group to the left-hand group.

#### Reachability in a Directed Graph

In a directed graph, we must follow the arrows. Reachability in one direction does not guarantee reachability in the other direction.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/e366f490-974a-4c46-93bc-b1dbcea4037f.png" alt="Directed graph where 1 can reach 4 through 2, but 4 has no outgoing edges and cannot reach 1" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In this graph:

- **4 is reachable from 1:** follow \(1 \rightarrow 2 \rightarrow 4\).
- **1 is not reachable from 4:** vertex 4 has no outgoing edges.
- Vertices **1, 2, and 3 can all reach one another** by following \(1 \rightarrow 2 \rightarrow 3 \rightarrow 1\).

> **CP / interview check:** Before answering a reachability question, identify the starting vertex and check whether the edges are directed. Do not assume that a directed edge can be followed backwards.

### Connected Components

In an **undirected graph**, a **connected component** is a maximal group of vertices in which every vertex can reach every other vertex.

Here, **maximal** means that we cannot add another vertex from the graph while keeping this property. A component includes the whole reachable group, not an arbitrarily chosen part of it.

Consequently:

- Every vertex belongs to exactly one connected component.
- Vertices in the same component can reach one another, possibly through several edges.
- Vertices in different components cannot reach one another.
- A vertex with no attached edges forms a component by itself.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/18e3042b-d9bd-4814-b608-2fae92cd1501.png" alt="Undirected graph divided into three connected components containing four vertices, one vertex, and two vertices" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The image shows **three connected components**:

- \(C_1\) contains the four vertices on the left.
- \(C_2\) contains the single vertex near the bottom.
- \(C_3\) contains the two vertices on the right.

Although \(C_1\) contains several edges, it is still only **one** component. We count separate reachable groups, not vertices or edges.

### Connected Graph

An **undirected graph** is **connected** if every vertex is reachable from every other vertex.

For a graph with at least one vertex, this is equivalent to having **exactly one connected component**.

The graph in the preceding image is not connected because it has three components. Each component is connected internally, but the entire graph is not.

Being connected does **not** mean that every pair of vertices must have a direct edge. A path through other vertices is enough.

### Strongly Connected Component

In a **directed graph**, a **strongly connected component**, or **SCC**, is a maximal group of vertices in which every vertex can reach every other vertex **while following the edge directions**.

For any two vertices \(u\) and \(v\) in the same SCC, both of these must be possible:

$$
u \text{ can reach } v
\qquad\text{and}\qquad
v \text{ can reach } u
$$

The paths in the two directions do not need to use the same edges.

As with connected components, maximal means that we cannot enlarge the group while preserving the required reachability. Every vertex belongs to exactly one SCC, and an SCC may contain only one vertex.

#### Example from the Directed Reachability Image

In the earlier directed graph, the SCCs are:

- \(\{1,2,3\}\): following the directed loop lets each vertex reach the other two.
- \(\{4\}\): the other vertices can reach 4, but 4 cannot reach them.

Vertex 4 is therefore not part of the same SCC as vertices 1, 2, and 3.

This shows an important difference: **directed edges can exist between different SCCs**. A one-way connection does not merge two SCCs; mutual reachability is required.

<img src="images/scc-corrected.png" alt="Three strongly connected components: a four-vertex directed loop, a singleton, and a three-vertex directed loop, with one-way links between groups" style="max-width: 100%; height: auto;" identifier="az-img-upload">

#### Reading the Three SCCs

The graph above has **three strongly connected components**:

- **SCC1:** The four vertices on the left form a directed loop: left \(\rightarrow\) top \(\rightarrow\) right \(\rightarrow\) bottom \(\rightarrow\) left. Every vertex can reach every other vertex in this group.
- **SCC2:** The middle vertex forms a component by itself.
- **SCC3:** The three vertices on the right form a directed loop: top \(\rightarrow\) right \(\rightarrow\) bottom \(\rightarrow\) top.

The edges between these groups lead from SCC1 to SCC2 and from SCC2 to SCC3. There are no return paths from SCC3 to SCC2 or from SCC2 to SCC1, so the groups cannot be combined into a larger SCC.

A single vertex can form an SCC even when it has incoming or outgoing edges. What matters is whether it is **mutually reachable** with another vertex.

## Quick Recap

- A valid route follows an edge between every consecutive pair of vertices and respects arrow directions.
- A **simple path** does not repeat vertices.
- A **simple cycle** repeats only its starting vertex at the end and does not reuse edges.
- **Reachability** asks whether we can get from one vertex to another; a direct edge is not necessary.
- A **connected component** is a maximal reachable group in an undirected graph.
- A non-empty undirected graph is **connected** when it has exactly one connected component.
- An **SCC** requires mutual directed reachability, not merely a one-way connection.

<READING_WIDGET>
