<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Floyd–Warshall: All-Pairs Shortest Paths

Dijkstra and Bellman–Ford start from one source. What if we need the shortest distance **from every vertex to every other vertex**?

Floyd–Warshall solves this **all-pairs shortest paths** problem using a distance matrix. Its central question is:

> Can travelling from `i` to `j` through vertex `k` improve the best route we currently know?

## 1. Problem and Assumptions

Given a weighted graph with `n` vertices, compute `dist[i][j]`, the minimum total edge weight from `i` to `j`, for every ordered pair of vertices.

- The graph may be directed or undirected.
- Positive, zero, and negative edge weights are allowed.
- Unreachable pairs remain at infinity.
- If there are no negative-weight cycles, all reachable pairs have finite shortest distances.
- The algorithm can also detect a negative-weight cycle anywhere in the graph.

The examples and complete program below use a **directed graph**. In a directed graph, `dist[i][j]` need not equal `dist[j][i]`.

A negative cycle allows us to keep lowering a route's cost by travelling around the cycle repeatedly. For any pair that can reach such a cycle and then reach its destination, no finite shortest distance exists. Our program reports a negative cycle and stops; it does not attempt to label affected pairs individually.

## 2. Initialize the Distance Matrix Correctly

Before considering any intermediate vertices, the available routes are empty paths and direct edges.

### Step 1: Start with Infinity

Set every entry to `INF`, meaning that no route is known yet.

### Step 2: Set the Diagonal to Zero

Set `dist[i][i] = 0` for every vertex. Staying at the same vertex without traversing an edge costs zero.

### Step 3: Add the Edges

For each directed edge `u -> v` of weight `w`, set:

```cpp
dist[u][v] = min(dist[u][v], w);
```

Using `min` handles **parallel edges**: initially, we only need the cheapest direct connection between the same ordered pair.

The order matters: initialize the diagonal first, then read the edges. A negative self-loop must replace the diagonal's zero so it can be detected as a negative cycle. A positive self-loop must not replace the zero-cost empty path.

For an undirected edge, perform the update in both directions. A reachable negative undirected edge permits a negative-cost closed walk by going across it and back, so ordinary shortest-walk distances are not finite in that component.

Do not use `0` to mean “no edge”: zero-weight edges are valid. If input is supplied as a matrix instead, its format must explicitly specify how missing edges are represented.

## 3. What Does Phase `k` Mean?

Number the vertices `1` through `n`. Define:

$$
D^{(k)}[i][j]
$$

as the minimum cost of a route from `i` to `j` whose **intermediate vertices** are chosen only from `{1, 2, ..., k}`.

Intermediate vertices are the vertices between the endpoints. In `i -> a -> b -> j`, they are `a` and `b`; the source `i` and destination `j` are not restricted by this set.

- `D^(0)` is the initialized matrix: no intermediate vertices are allowed.
- Phase `1` allows vertex `1` as an intermediate.
- Phase `2` allows vertices `1` and `2`.
- After phase `n`, every vertex is allowed as an intermediate.

This invariant explains both the recurrence and the order of the loops.

## 4. The Transition: Use `k`, or Do Not Use It

Assume no negative cycle exists. When vertex `k` becomes available, a shortest path from `i` to `j` has two possibilities:

1. **It does not use `k` as an intermediate.** Keep the previous answer.
2. **It uses `k` as an intermediate.** Split the path into `i -> k` and `k -> j`. Their internal vertices can be chosen from `{1, ..., k - 1}`.

Therefore:

$$
D^{(k)}[i][j] = \min\left(
D^{(k-1)}[i][j],\;
D^{(k-1)}[i][k] + D^{(k-1)}[k][j]
\right).
$$

The second option is available only when **both subpaths exist**.

In code:

```cpp
if (dist[i][k] != INF && dist[k][j] != INF) {
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
}
```

### Why Can We Update One Matrix in Place?

Without negative cycles, `dist[k][k]` remains zero. During phase `k`, routing `i -> k` through `k` cannot improve it, and neither can routing `k -> j` through `k`.

Thus, the row and column used to construct candidates remain unchanged during that phase. We can update `dist[i][j]` directly without keeping separate old and new matrices.

### Why Must `k` Be the Outermost Loop?

Finish considering one allowed intermediate vertex for **all pairs** before introducing the next one:

```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            // Try the route i -> k -> j.
        }
    }
}
```

The `i` and `j` loops may be swapped. Moving `k` inside them does not generally implement the same recurrence correctly in one sweep.

Also, do **not** stop merely because one phase makes no changes. A later intermediate vertex may still improve routes. This differs from Bellman–Ford's early-stopping rule: each Floyd–Warshall phase considers a different intermediate vertex.

## 5. Dry Run on the Illustrated Graph

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/c81f1a5f-83a1-4725-aefe-7e085b54c7eb.png" alt="Four-vertex directed weighted graph and its all-pairs shortest-distance matrix: rows 0 3 5 6; 5 0 2 3; 3 6 0 1; 2 5 7 0" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The graph contains these directed edges:

```text
1 -> 2: 3       2 -> 1: 8
1 -> 4: 7       4 -> 1: 2
2 -> 3: 2       3 -> 1: 5
3 -> 4: 1
```

Rows represent sources; columns represent destinations. The matrix in the image is the **final shortest-distance matrix**, not the initial direct-edge matrix.

### Initial Matrix: No Intermediate Vertices

```text
       1   2   3   4
1      0   3   ∞   7
2      8   0   2   ∞
3      5   ∞   0   1
4      2   ∞   ∞   0
```

### Improvements in Each Phase

Only entries that change are listed below; every other entry stays the same.

| Intermediate `k` | Allowed intermediate vertices after the phase | Improvements |
| --- | --- | --- |
| 1 | `{1}` | `dist[2][4]: ∞ -> 15`; `dist[3][2]: ∞ -> 8`; `dist[4][2]: ∞ -> 5` |
| 2 | `{1, 2}` | `dist[1][3]: ∞ -> 5`; `dist[4][3]: ∞ -> 7` |
| 3 | `{1, 2, 3}` | `dist[1][4]: 7 -> 6`; `dist[2][1]: 8 -> 7`; `dist[2][4]: 15 -> 3` |
| 4 | `{1, 2, 3, 4}` | `dist[2][1]: 7 -> 5`; `dist[3][1]: 5 -> 3`; `dist[3][2]: 8 -> 6` |

For example, in phase `3`:

$$
\operatorname{dist}[1][4]
= \min(7,\; \operatorname{dist}[1][3] + \operatorname{dist}[3][4])
= \min(7,\; 5 + 1) = 6.
$$

The first subpath is already `1 -> 2 -> 3`, so the complete route is `1 -> 2 -> 3 -> 4`. A transition combines **paths**, not necessarily two direct edges.

In phase `4`, the route `2 -> 3 -> 4 -> 1` improves `dist[2][1]` to `2 + 1 + 2 = 5`.

### Final Matrix

```text
       1   2   3   4
1      0   3   5   6
2      5   0   2   3
3      3   6   0   1
4      2   5   7   0
```

This matches all 16 entries in the diagram. Notice the directionality: `dist[1][2] = 3`, but `dist[2][1] = 5`.

## 6. Detecting Negative Cycles

An empty route from a vertex to itself costs zero. If the algorithm finds:

$$
\operatorname{dist}[v][v] < 0,
$$

then there is a negative-cost closed walk from `v` back to itself, which implies a negative cycle. Conversely, a negative cycle causes at least one diagonal entry to become negative by the end of the algorithm.

For example:

```text
1 -> 2, weight  1
2 -> 3, weight -3
3 -> 1, weight  1
```

The cycle has total weight `-1`. Repeating it keeps lowering the cost, so finite shortest distances cannot describe the affected pairs.

Unlike a Bellman–Ford run from one source, Floyd–Warshall considers **all** sources. A negative cycle in any component can therefore be detected.

The program below checks the diagonal before the phases, to catch negative self-loops, and after every phase. It immediately reports a negative cycle instead of printing an invalid shortest-distance matrix. This early exit also avoids continuing to propagate ever-decreasing values after a cycle has already been detected.

Some pairs may still have valid finite distances despite a negative cycle elsewhere. Reporting those pairs separately is outside this implementation's scope.

## 7. Complete C++17 Implementation

### Input and Output Used Here

To make missing edges and zero-weight edges unambiguous, this teaching program reads an **edge list**:

```text
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

Input labels are 1-based; the matrix uses 0-based indices internally. Each edge is directed.

- If a negative cycle exists, print `Negative cycle`.
- Otherwise, print the shortest-distance matrix, using `INF` for unreachable pairs.

We do not use `-1` as the unreachable marker because a valid shortest distance can itself be `-1`.

Weights and distances use `long long`. The code assumes every finite input weight and distance is below `INF`, and every finite addition considered by the algorithm fits in signed 64-bit arithmetic. Check these bounds against the problem constraints, including intermediate values before negative-cycle detection. The infinity guards prevent adding the sentinel; they do not by themselves prevent overflow when adding two very large finite numbers.

```cpp
#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

using ll = long long;
const ll INF = numeric_limits<ll>::max();

bool hasNegativeDiagonal(const vector<vector<ll>>& dist) {
    int n = static_cast<int>(dist.size());
    for (int v = 0; v < n; ++v) {
        if (dist[v][v] < 0) return true;
    }
    return false;
}

// Returns false if a negative cycle is detected.
// On true, dist contains all-pairs shortest distances.
bool floydWarshall(vector<vector<ll>>& dist) {
    int n = static_cast<int>(dist.size());
    if (hasNegativeDiagonal(dist)) return false;

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            if (dist[i][k] == INF) continue;

            for (int j = 0; j < n; ++j) {
                if (dist[k][j] == INF) continue;

                ll candidate = dist[i][k] + dist[k][j];
                dist[i][j] = min(dist[i][j], candidate);
            }
        }

        if (hasNegativeDiagonal(dist)) return false;
    }

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<ll>> dist(n, vector<ll>(n, INF));
    for (int i = 0; i < n; ++i) dist[i][i] = 0;

    for (int e = 0; e < m; ++e) {
        int u, v;
        ll weight;
        cin >> u >> v >> weight;
        --u;
        --v;
        dist[u][v] = min(dist[u][v], weight);
    }

    if (!floydWarshall(dist)) {
        cout << "Negative cycle\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j > 0) cout << ' ';
            if (dist[i][j] == INF) cout << "INF";
            else cout << dist[i][j];
        }
        cout << '\n';
    }
}
```

### Sample 1: The Illustrated Graph

Input:

```text
4 7
1 2 3
2 1 8
1 4 7
4 1 2
2 3 2
3 1 5
3 4 1
```

Output:

```text
0 3 5 6
5 0 2 3
3 6 0 1
2 5 7 0
```

### Sample 2: Negative Edges, but No Negative Cycle

Input:

```text
4 4
1 2 4
1 2 2
2 3 -3
1 3 5
```

Output:

```text
0 2 -1 INF
INF 0 -3 INF
INF INF 0 INF
INF INF INF 0
```

The cheaper parallel edge gives `dist[1][2] = 2`. The route `1 -> 2 -> 3` costs `-1`, while vertex `4` is isolated. The diagonal entries remain zero.

### Sample 3: A Negative Cycle

Input:

```text
3 3
1 2 1
2 3 -3
3 1 1
```

Output:

```text
Negative cycle
```

## 8. Complexity and When to Use It

- **Time: `O(n^3)`** in the worst case: `n` intermediate vertices, `n` sources, and `n` destinations. Reading the edge list adds `O(m)`.
- **Space: `O(n^2)`** for the matrix. Input edges are processed directly, so an additional edge list is not stored.
- Each distance query after successful preprocessing takes **`O(1)`**.

Floyd–Warshall is useful when `n` is small enough for cubic work and we need many or all source–destination distances. It is not automatically the best choice for a large sparse graph just because the task involves shortest paths. Always compare the time and matrix-memory requirements with the constraints.

## 9. Common Mistakes

- **Leaving the diagonal at infinity:** the empty route has cost zero.
- **Overwriting a negative self-loop with zero:** initialize the diagonal before incorporating edges.
- **Keeping the last parallel edge rather than the cheapest one:** use `min` when reading edges.
- **Adding infinity to another distance:** check that both subpaths exist first.
- **Putting `k` inside the endpoint loops:** this breaks the phase invariant of the standard one-sweep algorithm.
- **Stopping after an unchanged phase:** later intermediate vertices can still improve answers.
- **Treating the matrix as symmetric for a directed graph:** edge directions must be respected.
- **Printing ordinary distances after detecting a negative cycle:** affected pairs do not have finite shortest distances.

The key idea is: **expand the set of allowed intermediate vertices one at a time, and update every source–destination pair before moving to the next phase.**

</READING_WIDGET>
