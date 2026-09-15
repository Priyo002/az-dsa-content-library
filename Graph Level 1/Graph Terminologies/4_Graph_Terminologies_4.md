<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Graph Terminologies - 4

The previous lessons described paths, cycles, and common graph structures. We now look at routes that cover **every vertex** or **every edge** of a graph.

The distinction to remember is:

- **Hamiltonian:** visit every **vertex** exactly once.
- **Eulerian:** use every **edge** exactly once.

Both ideas apply to undirected and directed graphs. In a directed graph, every step must follow the direction of its edge.

## Level-6 Terms: Covering Vertices and Edges

### Hamiltonian

#### Hamiltonian Path

A **Hamiltonian path** visits every vertex of the graph exactly once.

It must satisfy two conditions:

- Every consecutive pair of vertices is connected by a valid edge.
- Every vertex appears exactly once in the sequence.

It does **not** need to use every edge of the graph. Edges that are not part of the chosen path may remain unused.

For a graph with \(n\) vertices, a Hamiltonian path contains \(n\) vertices and traverses \(n-1\) edges.

#### Hamiltonian Cycle

A **Hamiltonian cycle** visits every vertex exactly once and then returns to the starting vertex.

Only the starting vertex appears twice in the written sequence: once at the beginning and once at the end to close the cycle. No other vertex repeats.

Equivalently, take a Hamiltonian path and add an unused edge from its final vertex back to its starting vertex, **provided that edge exists**. The closing step must not reuse an edge of the path. In a directed graph, the closing edge must point toward the starting vertex.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/d471cc3d-78a7-4dae-99b4-574b2ac52368.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

#### Reading the Hamiltonian Examples

The image contains five vertices and six edges:

$$
(1,2),\quad (1,5),\quad (2,5),\quad
(2,3),\quad (3,4),\quad (4,5)
$$

**Hamiltonian path:**

$$
1 \rightarrow 2 \rightarrow 5 \rightarrow 4 \rightarrow 3
$$

Each consecutive pair shares an edge, and all five vertices appear exactly once. The route uses four edges.

The edges \((1,5)\) and \((2,3)\) are unused, which is allowed: Hamiltonian paths must cover vertices, not edges.

**Hamiltonian cycle:**

$$
1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 1
$$

The first five entries visit all five vertices exactly once. The final step follows edge \((5,1)\) back to the start.

This cycle uses five edges. Edge \((2,5)\) is unused, but the cycle is still Hamiltonian.

The arrows in these sequences indicate traversal order; the illustrated graph is undirected.

#### Hamiltonian Graph

A graph is **Hamiltonian** if it contains a Hamiltonian cycle.

The graph above is Hamiltonian because the displayed cycle visits all its vertices and returns to the start.

Having a Hamiltonian path alone is **not enough** to call a graph Hamiltonian. For example, a graph consisting only of the edges \(1-2\) and \(2-3\) has the Hamiltonian path \(1,2,3\), but no edge closes it into a cycle.

### Eulerian

#### Eulerian Path

An **Eulerian path** uses every edge of the graph exactly once.

Unlike a Hamiltonian path, it **may revisit vertices**. The restriction is on repeating edges, not vertices.

In this terminology, “Eulerian path” is the conventional name for an edge-covering route, also called an Eulerian trail. It is not required to be a simple path as defined earlier.

An Eulerian path may:

- Start and end at different vertices, or
- Return to its starting vertex, in which case it is also an Eulerian cycle.

For a graph with \(m\) edges, an Eulerian path traverses exactly \(m\) edges. Its written vertex sequence has \(m+1\) entries, possibly with repetitions.

#### Eulerian Cycle

An **Eulerian cycle** uses every edge exactly once and returns to its starting vertex.

Vertices may repeat, including intermediate vertices. This differs from a Hamiltonian cycle, where only the starting vertex repeats at the end.

An Eulerian cycle is also an Eulerian path under the definition above; the word **cycle** adds the requirement that the route closes.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/da0d5b32-d498-42de-979a-c5cac58f082c.png" alt="Graph Course Image" style="max-width: 100%; height: auto;" identifier="az-img-upload">

#### Reading the Eulerian Examples

The graph contains five vertices and six edges:

$$
(1,2),\quad (2,3),\quad (3,4),\quad
(2,4),\quad (2,5),\quad (1,5)
$$

The first displayed route is:

$$
1 \rightarrow 2 \rightarrow 3 \rightarrow 4
\rightarrow 2 \rightarrow 5 \rightarrow 1
$$

Let us check its edges one by one:

| Step | Edge used |
| --- | --- |
| \(1 \rightarrow 2\) | \((1,2)\) |
| \(2 \rightarrow 3\) | \((2,3)\) |
| \(3 \rightarrow 4\) | \((3,4)\) |
| \(4 \rightarrow 2\) | \((2,4)\) |
| \(2 \rightarrow 5\) | \((2,5)\) |
| \(5 \rightarrow 1\) | \((1,5)\) |

All six edges are used exactly once. Vertex 2 appears more than once, which is permitted.

Because the route begins and ends at 1, it is **both an Eulerian path and an Eulerian cycle**.

The second displayed route is:

$$
5 \rightarrow 2 \rightarrow 3 \rightarrow 4
\rightarrow 2 \rightarrow 1 \rightarrow 5
$$

It also uses every edge exactly once and returns to its starting vertex. It is another Eulerian cycle of the same graph.

These examples show that a graph may have more than one valid route. The definition does not require the route to be unique.

#### Eulerian Graph

A graph is **Eulerian** if it contains an Eulerian cycle.

The illustrated graph is Eulerian because either displayed route uses all its edges exactly once and returns to its start.

An Eulerian path with different endpoints does not, by itself, make a graph Eulerian. For example, the graph with edges \(1-2\) and \(2-3\) has the Eulerian path \(1,2,3\), but no Eulerian cycle.

## Hamiltonian vs. Eulerian

| Question | Hamiltonian | Eulerian |
| --- | --- | --- |
| What must be covered exactly once? | Every vertex | Every edge |
| Can vertices repeat? | No, except the start at the end of a cycle | Yes |
| Can some edges remain unused? | Yes | No |
| Can an edge be reused? | No | No |
| What makes the route a cycle? | It returns to the start after visiting every vertex once | It returns to the start after using every edge once |
| What makes the graph Hamiltonian or Eulerian? | Existence of a Hamiltonian cycle | Existence of an Eulerian cycle |

> **CP / interview check:** Ask what must be covered: vertices or edges. Visiting all vertices does not prove that a route is Eulerian, and using all edges does not prove that it is Hamiltonian.

When checking a proposed route:

1. Verify that every step follows an existing edge, respecting direction where applicable.
2. For a Hamiltonian route, check that every vertex is covered without repetition, except the closing vertex of a cycle.
3. For an Eulerian route, check that every edge is used exactly once. In an undirected graph, using the same edge in reverse still counts as reusing it. If parallel edges exist, track each edge separately: two different edges may have the same endpoints.
4. If the route is claimed to be a cycle, verify that its endpoints match.

## Quick Recap

- A **Hamiltonian path** visits every vertex exactly once.
- A **Hamiltonian cycle** additionally returns to the start.
- A **Hamiltonian graph** contains a Hamiltonian cycle, not merely a Hamiltonian path.
- An **Eulerian path** uses every edge exactly once; vertices may repeat.
- An **Eulerian cycle** additionally returns to the start.
- An **Eulerian graph** contains an Eulerian cycle, not merely an open Eulerian path.

</READING_WIDGET>
