<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Graph Terminologies - 3

So far, we have described the parts of a graph, paths, and connectivity. This lesson introduces graph types based on **which edges are allowed**, **whether cycles exist**, and **how vertices can be colored**.

## Level-4 Terms: Loops and Repeated Edges

### Self Loop

A **self loop** is an edge that connects a vertex to itself. Its two endpoints are the same vertex.

For a vertex \(u\), we write this edge as \((u,u)\), or \(u \rightarrow u\) in a directed graph.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/e980e0a0-0bd9-405b-b742-51b5c3ae0b71.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the illustration, the curved edge returns to the left-hand vertex. That edge is the self loop.

A self loop is still **one edge**. It does not introduce a new vertex.

Connecting this to degree:

- In an undirected graph, a self loop contributes **2** to the vertex's degree, because both ends are attached to that vertex.
- In a directed graph, it contributes **1 to indegree** and **1 to outdegree**.

### Multiple Edges

**Multiple edges**, also called **parallel edges**, are distinct edges connecting the same pair of vertices.

In a directed graph, they must have the **same starting vertex and the same ending vertex**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/e7fd71b9-2902-43dc-b7d2-79130780b1bf.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The illustration shows two separate edges from vertex 1 to vertex 2:

- One has weight 3.
- The other has weight 5.

These are two edges, not one edge with two weights. Parallel edges can also have equal weights; what matters is that they are separate edges with the same endpoints and direction.

The edges \(1 \rightarrow 2\) and \(2 \rightarrow 1\) are **not** parallel edges: their directions differ.

### Multigraph

A **multigraph** allows multiple edges between the same pair of vertices.

For example, two separate roads connecting the same two intersections can be represented as two edges.

In this course, we allow a multigraph to contain self loops as well. Some references use a narrower definition, so the explicit conditions in a problem statement take priority.

### Simple Graph

A **simple graph** has:

- No self loops.
- No multiple edges.

For an undirected simple graph, each pair of distinct vertices has **at most one edge** between them.

“At most one” does not mean an edge must exist. A simple graph may have very few edges or even no edges.

For directed graphs under the same restrictions, each ordered pair of distinct vertices has at most one edge. Both \(u \rightarrow v\) and \(v \rightarrow u\) may exist without being parallel edges.

> **CP / interview check:** Check whether self loops and multiple edges are allowed before making assumptions about edge counts. The bound \(n(n-1)/2\) applies to simple undirected graphs, not to unrestricted multigraphs.

## Level-5 Terms: Common Graph Structures

### Directed Acyclic Graph (DAG)

A **Directed Acyclic Graph**, or **DAG**, is a directed graph with **no directed cycles**.

Both words matter:

- **Directed:** every edge has a direction.
- **Acyclic:** following the arrows can never take us around a cycle back to the starting vertex.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/f69ed07f-591c-49a2-87d9-d0893e6e69b6.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the illustration, there are seven vertices. The arrows allow movement along the displayed routes, but there is no directed route that returns to its starting vertex after traversing edges.

Notice the triangular arrangement near the right. Its edges do not form a directed cycle: the arrow directions do not permit a trip around the triangle.

A DAG can represent dependencies. For example, \(A \rightarrow B\) may mean “task A must finish before task B can begin.” A directed cycle would create a circular dependency.

#### Connection to SCCs

A DAG with \(n\) vertices has **exactly \(n\) strongly connected components**, each containing one vertex.

If two distinct vertices could reach each other, the routes between them would create a directed cycle. A DAG cannot contain such a cycle.

Therefore, the illustrated DAG has seven SCCs.

A DAG does not have to be a tree, and its number of edges is not necessarily \(n-1\).

### Tree

A **tree** is a **connected, acyclic, undirected graph**.

That means:

- **Connected:** every vertex can reach every other vertex.
- **Acyclic:** there are no cycles.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/b239bf2d-e1f6-40bd-8994-477784bb0a92.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The illustrated tree has six vertices and five edges:

$$
(1,2),\quad (1,3),\quad (2,4),\quad (2,5),\quad (3,6)
$$

#### Number of Edges

A tree with \(n\) vertices has exactly:

$$
|E| = n-1
$$

For the image:

$$
|E| = 6-1 = 5
$$

A single vertex with no edges is also a tree: \(n=1\) and \(|E|=0\).

#### Unique Simple Path

There is **exactly one simple path** between any two vertices in a tree.

For example, the only simple path from vertex 4 to vertex 6 is:

$$
4 \rightarrow 2 \rightarrow 1 \rightarrow 3 \rightarrow 6
$$

The arrows here show the order of traversal; the tree's edges are undirected.

Connectivity guarantees that a path exists. If two different simple paths existed between the same pair of vertices, they would create a cycle.

> **Common pitfall:** Having \(n-1\) edges alone does not prove that a graph is a tree. Connectivity matters too. For example, a triangle and a separate single vertex have four vertices and three edges, but do not form a tree.

### Forest

A **forest** is an undirected graph with no cycles. Each of its connected components is a tree.

A tree is one connected acyclic graph; a forest may contain several separate trees.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/d1d29986-9cd7-401a-a0c7-2dfc41caf44f.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The forest above has three components:

- Vertices \(\{1,2,3,4,5\}\) form one tree with five vertices and four edges.
- Vertices \(\{6,7,8\}\) form another tree with three vertices and two edges.
- Vertices \(\{9,10\}\) form a tree with two vertices and one edge.

The entire graph is not connected, but each component is connected and has no cycle.

A single vertex may also be a component of a forest. A forest with exactly one non-empty component is a tree.

### Bipartite Graph

An undirected graph is **bipartite** if its vertices can be divided into two groups so that **every edge joins vertices from different groups**.

Equivalently, we can color its vertices using at most two colors such that no two vertices joined by an edge have the same color.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/2f2aea18-2bf6-4c6f-8371-a3f3f3b10577.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the illustration:

- The red vertices form one group.
- The blue vertices form the other group.
- Every edge joins a red vertex to a blue vertex.

The two groups do not need to contain equal numbers of vertices. Also, not every possible edge between the groups must exist.

#### Connection to Odd-Length Cycles

An undirected graph is bipartite **if and only if it contains no odd-length cycle**.

Why does an odd cycle cause a problem? As we move around a cycle, the colors must alternate. With an odd number of edges, the final edge forces two vertices of the same color to be joined.

For example, a triangle cannot be colored with just two colors while keeping the endpoints of every edge different.

The four-edge cycle in the illustration alternates red, blue, red, blue and closes without a conflict.

**A bipartite graph can contain cycles; it cannot contain odd-length cycles.**

### Chromatic Number

The **chromatic number** of a graph is the **minimum number of colors** needed to color its vertices so that the endpoints of every edge have different colors.

For this discussion, consider undirected graphs without self loops. A self loop would require a vertex to have a different color from itself, which is impossible.

The important word is **minimum**. Finding a valid coloring using four colors does not prove that four colors are necessary.

Examples:

- A non-empty graph with no edges needs only **one color**.
- The bipartite graph above needs **two colors**: two are sufficient, and its edges prevent a one-color solution.
- A triangle needs **three colors**, because each of its vertices is connected to the other two.

Thus, a bipartite graph with at least one edge has chromatic number 2. A non-empty graph with no edges is also bipartite, but its chromatic number is 1.

### Complete Graph

A **complete graph** is a simple undirected graph in which **every pair of distinct vertices is joined by an edge**.

A complete graph with \(n\) vertices is denoted by \(K_n\).

Do not confuse **connected** with **complete**:

- **Connected:** a path exists between every pair of vertices.
- **Complete:** a direct edge exists between every pair of distinct vertices.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/8c226dae-7cdb-4594-ab31-2d9e8c15481c.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The illustration shows \(K_5\):

- There are five vertices.
- Each vertex is connected directly to the other four.
- There are ten edges.

Crossings of lines in the drawing do not create additional vertices. Only the five marked circles are vertices.

#### Number of Edges

Each of the \(n\) vertices is connected to \(n-1\) others. This counts each undirected edge twice, once from each endpoint, so:

$$
|E| = \frac{n(n-1)}{2}
$$

For \(K_5\):

$$
|E| = \frac{5 \times 4}{2} = 10
$$

Every vertex has degree \(n-1\). A complete graph also needs \(n\) different colors, since every pair of vertices is joined by an edge.

## Quick Recap

- A **self loop** joins a vertex to itself.
- **Multiple edges** are distinct edges with the same endpoints; direction also matters in directed graphs.
- A **multigraph** permits multiple edges; a **simple graph** excludes multiple edges and self loops.
- A **DAG** has directed edges and no directed cycles.
- A **tree** is connected, undirected, and acyclic, with \(n-1\) edges and a unique simple path between every pair of vertices.
- A **forest** consists of tree components.
- A **bipartite graph** can be colored with at most two colors and has no odd-length cycle.
- The **chromatic number** is the minimum number of colors needed.
- A **complete graph** \(K_n\) has every possible edge between distinct vertices, totaling \(n(n-1)/2\).


</READING_WIDGET>