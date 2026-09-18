<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bipartite Graphs Using DFS

In the previous lesson, we used DFS to give every vertex in a connected component the **same component ID**. We can adapt that traversal to solve a different problem:

> **Can we assign one of two colours to every vertex so that the endpoints of every edge have different colours?**

This time, we pass the **opposite colour** when moving to an uncoloured neighbour. If an edge joins two vertices with the same colour, the colouring is invalid.

Throughout this lesson, the graph is **undirected**, and vertex labels run from 1 to \(n\).

## 1. What Is a Bipartite Graph?

A graph is **bipartite** if its vertices can be divided into two disjoint sets, \(A\) and \(B\), such that every edge has one endpoint in each set.

The two sets together contain all vertices, and no vertex belongs to both sets. There are no edges joining two vertices inside \(A\), and no edges joining two vertices inside \(B\).

Equivalently, we can think of the sets as two colours:

- Vertices in \(A\) receive colour 1.
- Vertices in \(B\) receive colour 2.
- Every edge must join colour 1 to colour 2.

The two sets do **not** need equal sizes. Also, being bipartite does not require every vertex in one set to be adjacent to every vertex in the other set.

An isolated vertex can receive either colour because it has no incident edge to constrain its choice. We allow a colour class to be empty when the graph permits it; we do not require both colours to appear.

## 2. The Connection with Odd Cycles

An undirected graph is bipartite **if and only if it contains no odd-length cycle**.

To understand why an odd cycle is impossible, start at one vertex and alternate colours along the cycle:

- After an even number of edges, the alternating pattern returns to the original colour.
- After an odd number of edges, the pattern demands the opposite colour.

But completing a cycle brings us back to the **same vertex**, which cannot have two different colours. Therefore, an odd cycle cannot be properly coloured with two colours.

For an even cycle, the alternation closes without a conflict. More generally, if an undirected graph contains no odd cycle, a valid two-colouring exists.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/dfd5ca26-d6a0-4c63-aec6-614b9367db2c.png" alt="An even four-edge cycle with alternating red and blue vertices, compared with an odd five-edge cycle whose remaining vertex cannot be assigned either colour without a conflict" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Reading the Illustration

- **Top graph:** the cycle has four edges. Red and blue alternate around it, and the two additional leaf vertices also have colours different from their neighbours.
- **Bottom graph:** the cycle has five edges. The vertex marked `??` is adjacent to one red vertex and one blue vertex. Giving it red conflicts with one neighbour; giving it blue conflicts with the other.

The `??` represents an impossible choice using the two available colours, not a third colour.

**An even cycle somewhere in a graph is not enough to make the whole graph bipartite.** There must be no odd cycle anywhere, including in a different connected component.

We do not need to enumerate cycles explicitly. DFS can test bipartiteness directly by trying to construct a valid two-colouring.

## 3. Store Colours in the Visited Array

Use an integer array `vis` with three possible values:

| Value | Meaning |
| --- | --- |
| `0` | Unvisited and uncoloured |
| `1` | Visited and assigned colour 1 |
| `2` | Visited and assigned colour 2 |

Here, `vis` stores **colours**, not the component IDs used in the previous lesson. Two disconnected vertices may have the same colour; that does not mean they belong to the same component.

For colours 1 and 2, the expression `3 - color` gives the opposite colour:

$$
3-1=2,\qquad 3-2=1
$$

Reserve 0 for uncoloured vertices so that `if (!vis[v])` correctly identifies a neighbour that has not been visited.

## 4. DFS Through the Recursion Framework

### State and Meaning

The call `dfs(node, color)` assigns `color` to `node` and explores its still-uncoloured neighbours, checking that every inspected edge joins opposite colours.

The caller invokes it only for an uncoloured vertex. A shared flag, `is_bipartite`, begins as `true` and becomes `false` if any conflict is found.

### Work at the Current State

Set `vis[node] = color` **before** exploring neighbours. This prevents a cycle from recursively rediscovering the same vertex.

### Recursive Transition

For each neighbour `v` of `node`, there are three cases:

1. **`v` is uncoloured:** recurse with `dfs(v, 3 - color)`.
2. **`v` already has the opposite colour:** this edge satisfies the condition; no recursive call is needed.
3. **`v` already has the same colour:** this edge is a conflict, so set `is_bipartite = false`.

Notice the difference from ordinary reachability DFS: an already-visited neighbour must still have its **colour checked**. Simply skipping all visited neighbours would miss conflicts.

### Returning from a Call

When there are no more neighbours to inspect, the call returns. Keep its colour assigned; do not reset it to 0 while backtracking.

We are constructing one consistent colouring, not undoing choices to enumerate candidate colourings.

```cpp
bool is_bipartite = true;

void dfs(int node, int color) {
    vis[node] = color;

    for (int v : g[node]) {
        if (!vis[v]) {
            dfs(v, 3 - color);
        } else if (vis[v] == vis[node]) {
            is_bipartite = false;
        }
    }
}
```

In an undirected graph, the edge back to the vertex that called us is also inspected. Its endpoints have opposite colours, so it does not cause a conflict. This implementation does not need a separate parent parameter.

## 5. Check Every Connected Component

A graph may be disconnected. Start DFS from every uncoloured vertex, just as in the connected-components lesson:

```cpp
int no_of_comp = 0;

for (int node = 1; node <= n; ++node) {
    if (!vis[node]) {
        ++no_of_comp;
        dfs(node, 1);
    }
}
```

Each new component can start with colour 1 because it has no edge to any other component. Starting it with colour 2 would simply swap the two colours throughout that component, if it is bipartite.

Keep `is_bipartite` shared across the entire graph. **Do not reset it to `true` when a new component starts.** A conflict in even one component makes the whole graph non-bipartite.

The code continues traversing after a conflict, so it still counts all connected components. However, the assigned colours must not be presented as a valid colouring if the flag is false.

## 6. Dry Run: A Valid Two-Colouring

Consider a graph with these undirected edges:

$$
(1,2),\quad (2,3),\quad (3,4),\quad (4,1),\quad (6,7)
$$

There are seven vertices. Vertices 1–4 form a four-edge cycle, vertex 5 is isolated, and vertices 6–7 form another component.

Starting from vertex 1 and following the input order above:

| Step | Action | Colour assigned or checked |
| --- | --- | --- |
| 1 | Start `dfs(1, 1)`. | `vis[1] = 1` |
| 2 | From 1, visit uncoloured neighbour 2. | `vis[2] = 2` |
| 3 | At 2, the edge back to 1 is valid. Visit 3. | `vis[3] = 1` |
| 4 | At 3, the edge back to 2 is valid. Visit 4. | `vis[4] = 2` |
| 5 | At 4, both neighbours 3 and 1 already have colour 1. | Both edges are valid. |
| 6 | Return through the calls. At 1, neighbour 4 already has colour 2. | No conflict; the first component is complete. |
| 7 | The outer loop reaches uncoloured vertex 5. | `vis[5] = 1`; return immediately. |
| 8 | Start at vertex 6 and visit 7. | `vis[6] = 1`, `vis[7] = 2` |

The final colours are:

```text
Vertex:  1  2  3  4  5  6  7
Colour:  1  2  1  2  1  1  2
```

One valid bipartition is therefore:

$$
A=\{1,3,5,6\},\qquad B=\{2,4,7\}
$$

Every edge crosses between these sets. The graph is bipartite and has three connected components.

## 7. Dry Run: Finding a Conflict

Now consider the triangle with edges \((3,4)\), \((4,5)\), and \((5,3)\).

Starting with colour 1 at vertex 3:

```text
dfs(3, 1): colour vertex 3 with 1
dfs(4, 2): colour vertex 4 with 2
dfs(5, 1): colour vertex 5 with 1
```

At vertex 5, the edge to already-coloured vertex 3 joins **colour 1 to colour 1**. This sets `is_bipartite = false`.

Giving vertex 5 colour 2 instead would conflict with vertex 4. Swapping both colours throughout the component would still leave a same-colour edge. The triangle is an odd cycle, so no valid two-colouring exists.

This is the same obstruction shown by the five-edge cycle in the illustration: the conflict is caused by odd length, not specifically by having three vertices.

## 8. Complete C++ Implementation

The program below checks the entire graph, counts its connected components, and prints one valid colouring when possible. The following section uses the component count to determine the number of valid colourings.

### Input

- First line: `n m`, the number of vertices and undirected edges.
- Next `m` lines: edge endpoints `u v`, with labels from 1 to \(n\).

### Output for This Example

- If the graph is not bipartite, print `Not Bipartite`.
- Otherwise, print `Bipartite`, the number of components, and the colours of vertices 1 through \(n\), on three separate lines.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g;
vector<int> vis;  // 0 = uncoloured; 1 and 2 are the two colours.
bool is_bipartite;

void dfs(int node, int color) {
    vis[node] = color;

    for (int v : g[node]) {
        if (!vis[v]) {
            dfs(v, 3 - color);
        } else if (vis[v] == vis[node]) {
            is_bipartite = false;
        }
    }
}

void solve() {
    int n, m;
    cin >> n >> m;

    g.assign(n + 1, vector<int>());
    vis.assign(n + 1, 0);
    is_bipartite = true;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    int no_of_comp = 0;
    for (int node = 1; node <= n; ++node) {
        if (!vis[node]) {
            ++no_of_comp;
            dfs(node, 1);
        }
    }

    if (!is_bipartite) {
        cout << "Not Bipartite\n";
        return;
    }

    cout << "Bipartite\n";
    cout << no_of_comp << '\n';

    for (int node = 1; node <= n; ++node) {
        if (node > 1) cout << ' ';
        cout << vis[node];
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

### Sample 1: Bipartite, with Multiple Components

Input:

```text
7 5
1 2
2 3
3 4
4 1
6 7
```

Output:

```text
Bipartite
3
1 2 1 2 1 1 2
```

This matches the valid-colouring dry run. Different valid colours may result from different starting choices; the existence of a valid colouring does not depend on those choices.

### Sample 2: A Conflict in a Later Component

Input:

```text
5 4
1 2
3 4
4 5
5 3
```

Output:

```text
Not Bipartite
```

The component \(\{1,2\}\) is bipartite, but the triangle \(\{3,4,5\}\) is not. Checking only the component containing vertex 1 would give the wrong answer.

## 9. Why Does This DFS Test Work?

Once a component's starting vertex has a colour, every recursive discovery forces its neighbour to have the opposite colour. The implementation never changes an assigned colour.

- **If no conflict occurs:** every vertex is coloured, and every adjacency entry has been inspected. Each edge joins opposite colours, so the two colour classes form a valid bipartition.
- **If a conflict occurs:** an edge requires two already-forced colours to be different, but they are equal. The only other possible starting colour would swap all colours in that component and preserve the conflict. No valid two-colouring exists.

Thus, the test accepts exactly the bipartite graphs. It does not need to list the odd cycle explicitly to establish that a conflict exists.

## 10. Number of Valid Two-Colourings

Here, the two colours are **distinct labels**, such as red and blue, or 1 and 2. Swapping them produces a different colouring. We count assignments to vertices; we do not require both colours to be used.

### One Connected Component

For a nonempty connected bipartite component:

1. Choose the colour of one starting vertex: there are two choices.
2. Every other vertex is connected to it by a path, along which the colours must alternate.
3. Because the component is bipartite, these constraints are consistent and fix every other vertex's colour.

Therefore, there are **exactly two** valid colourings of that component. They are obtained from each other by swapping colours 1 and 2 everywhere in the component.

This also holds for an isolated vertex: it can be assigned either of the two colours.

### Multiple Connected Components

Different components have no edges between them, so their colour choices are independent.

If the graph is bipartite and has \(c\) connected components:

$$
\text{Number of valid two-colourings}
= \underbrace{2\times2\times\cdots\times2}_{c\text{ components}}
= 2^c
$$

Including the non-bipartite case:

$$
\text{Number of valid two-colourings} =
\begin{cases}
2^c, & \text{if the graph is bipartite},\\
0, & \text{otherwise}.
\end{cases}
$$

For Sample 1, the four-cycle, isolated vertex 5, and edge \((6,7)\) give three components. Hence the number of valid colourings is:

$$
2^3=8
$$

For Sample 2, the triangle makes the answer **0**, even though the other component can be coloured.

For a graph with \(n\) vertices and no edges, every vertex is its own component, so all \(2^n\) assignments are valid.

> **CP counting caution:** \(2^c\) can quickly exceed built-in integer limits. Follow the problem's required output format: use exact large-integer arithmetic when needed, or modular arithmetic if a modulus is specified. In C++, `2 ^ c` means bitwise XOR, not exponentiation.

## 11. Complexity

For an adjacency-list representation with \(n\) vertices and \(m\) undirected edges:

- Each vertex is coloured once.
- Every adjacency-list entry is inspected once; there are \(2m\) such entries.
- The outer loop considers all \(n\) vertices, including isolated vertices.

Therefore, the **bipartiteness test and component count** take \(\Theta(n+m)\) time.

The graph uses \(O(n+m)\) space. The colour array and recursion stack use \(O(n)\) auxiliary space. Computing or printing a potentially large exact value of \(2^c\) is separate from this traversal cost and is not part of the example program.

A long chain can make the recursion depth \(O(n)\). As with ordinary DFS, an explicit-stack implementation may be needed if the environment cannot support that depth.

## 12. Common Mistakes and Quick Checks

- **Checking only one component:** another component may contain an odd cycle.
- **Giving a neighbour the same colour:** recurse with `3 - color`, not `color`.
- **Skipping every visited neighbour:** inspect its colour to detect a same-colour edge.
- **Resetting colours while returning:** keep each vertex's colour fixed throughout the traversal.
- **Resetting the flag between components:** one conflict makes the whole graph non-bipartite.
- **Treating every cycle as a conflict:** even cycles are allowed; odd cycles are not.
- **Returning \(2^c\) without checking bipartiteness:** a non-bipartite graph has zero valid two-colourings.
- **Ignoring isolated vertices:** each is a component and contributes two choices to the count.

A self-loop immediately makes a graph non-bipartite because its two endpoints are the same vertex and cannot have different colours. Repeated parallel edges between two distinct vertices do not add a new colouring constraint: each copy requires the same pair of endpoints to have opposite colours.

## Quick Recap

- A bipartite graph admits a two-colouring in which every edge joins opposite colours.
- Store 0 for uncoloured vertices and 1 or 2 for their assigned colours.
- Use DFS to give uncoloured neighbours the opposite colour and check already-coloured neighbours for conflicts.
- Process every connected component; one odd cycle anywhere is enough to reject the graph.
- A bipartite graph with \(c\) components has \(2^c\) valid assignments of two distinct colours. A non-bipartite graph has none.

</READING_WIDGET>
