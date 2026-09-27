<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Shortest Path Idea 3: Paying for Edges and Vertices

In ordinary weighted shortest-path problems, we pay for the edges we traverse. What if visiting a vertex also has a cost?

We can still use Dijkstra's algorithm. The important step is to define the cost of a transition so that **every edge and every visited vertex is counted correctly**.

## 1. Problem Statement and Cost Definition

You are given an undirected graph with `n` vertices and `m` edges:

- Every edge `(u, v)` has a weight `w(u, v)`.
- Every vertex `v` has a value `val[v]`, interpreted as a cost of visiting that vertex.
- A source vertex `s` is given.

Find the minimum total cost from `s` to every vertex, where a route pays for **all its edges and all its vertices, including the source and destination**.

For a path:

$$
P = (s = v_0, v_1, \ldots, v_r),
$$

its cost is:

$$
\operatorname{cost}(P)
= \sum_{i=0}^{r} \operatorname{val}[v_i]
+ \sum_{i=1}^{r} w(v_{i-1}, v_i).
$$

For this lesson and implementation, assume that **all edge weights and vertex values are nonnegative**. Zero costs, parallel edges, and disconnected vertices are allowed.

These assumptions allow a minimum-cost route to be chosen without repeated vertices: removing a loop cannot increase its cost. Thus, no state describing previously visited vertices or previously paid fees is needed.

### A Small Example

If `val[1] = 3`, `val[2] = 4`, and the edge `1 -- 2` has weight 1, then the route from `1` to `2` costs:

```text
Source value + edge weight + destination value
      3      +      1      +         4          = 8
```

The cost of staying at source `1` is `3`, not `0`, under this problem's definition.

## 2. Absorb the Destination's Value into the Move

Suppose `dist[u]` is the best total cost found for reaching vertex `u`. It already includes `val[u]`.

To extend that route across edge `u -- v`, the new costs are:

1. The edge weight `w(u, v)`.
2. The destination vertex's value `val[v]`.

Therefore, the candidate is:

$$
\text{candidate}
= \operatorname{dist}[u] + w(u, v) + \operatorname{val}[v].
$$

Relax only if this candidate improves the existing answer:

$$
\operatorname{dist}[v]
= \min\left(\operatorname{dist}[v],\;
\operatorname{dist}[u] + w(u, v) + \operatorname{val}[v]\right).
$$

Do not add `val[u]` again. That would charge the current vertex twice.

### Why This Models the Whole Path

Starting with `val[s]` and adding the edge weight plus destination value for every move gives:

```text
val[s]
+ (w(s, v1) + val[v1])
+ (w(v1, v2) + val[v2])
+ ...
+ (w(v[r-1], v[r]) + val[v[r]])
```

This is exactly the cost specified in the problem: every path edge and every path vertex appears once.

## 3. An Undirected Edge Gives Two Transition Costs

We can think of the original edge `u -- v` as two directed transitions:

$$
u \to v:\quad w(u,v) + \operatorname{val}[v],
$$

$$
v \to u:\quad w(u,v) + \operatorname{val}[u].
$$

Their costs may differ because their destinations differ. For the small example above:

- The move `1 -> 2` adds `1 + 4 = 5`.
- The move `2 -> 1` adds `1 + 3 = 4`.

In the code, store the original edge in both adjacency lists, then add the appropriate destination value during relaxation. We do not need to construct a separate transformed graph explicitly.

Both transition costs are nonnegative under the stated assumptions, so Dijkstra's usual greedy argument applies: the smallest unsettled tentative distance can be finalized safely.

More generally, Dijkstra requires the **effective transition costs** to be nonnegative. If negative values are allowed by a different problem, check `w(u,v) + val[v]` for each direction; nonnegative original edge weights alone are not enough.

## 4. Initialize the Source Correctly

Set:

```cpp
dist[source] = val[source];
```

All other distances initially equal `INF`. Put `(val[source], source)` into the min-heap.

Starting at zero would omit the source fee from every reachable answer. Do not compensate by repeatedly adding the source fee during relaxation—it is paid once at initialization.

If a different problem explicitly excludes the source's fee, initialization would change. Here, both endpoints are included, so `dist[source] = val[source]` is required.

## 5. Dry Run on the Illustrated Graph

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/6de252c3-7d06-4a32-908f-62f0168f116f.png" alt="Undirected graph with source 1, vertex values 3 4 8 7 9 13 11, and final node-inclusive shortest costs 3 8 12 18 32 29 41; cream background, rounded border, and AlgoZenith logo" style="max-width: 100%; height: auto;" identifier="az-img-upload">

In the left panel, the numbers **inside the circles are vertex labels**. The red numbers beside the vertices are their values; the teal numbers on the edges are edge weights.

The source is vertex `1`. The vertex values are:

| Vertex | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `val` | 3 | 4 | 8 | 7 | 9 | 13 | 11 |

The undirected edges are:

```text
1 -- 2: 1       1 -- 3: 1
2 -- 4: 3       3 -- 4: 2
4 -- 5: 5       3 -- 6: 4
6 -- 7: 1       5 -- 7: 8
```

### Heap Processing and Relaxations

Initialize `dist[1] = 3` and all other distances to `INF`.

| Vertex finalized | Final cost | Main updates or comparisons |
| --- | --- | --- |
| 1 | 3 | `dist[2] = 3 + 1 + 4 = 8`; `dist[3] = 3 + 1 + 8 = 12` |
| 2 | 8 | `dist[4] = 8 + 3 + 7 = 18` |
| 3 | 12 | Candidate for 4 is `12 + 2 + 7 = 21`, so keep 18; `dist[6] = 12 + 4 + 13 = 29` |
| 4 | 18 | `dist[5] = 18 + 5 + 9 = 32` |
| 6 | 29 | `dist[7] = 29 + 1 + 11 = 41` |
| 5 | 32 | Candidate for 7 is `32 + 8 + 11 = 51`, so keep 41 |
| 7 | 41 | No further improvement |

The final costs, in **vertex-label order**, are:

```text
Vertex:  1  2   3   4   5   6   7
Cost:    3  8  12  18  32  29  41
```

These match all seven annotations in the image's right panel. That panel retains the original graph edges; it is not a shortest-path tree.

### The Cheapest Edge-Only Route May Not Be the Answer

Compare two routes to vertex `4`:

| Route | Edge-weight sum | Vertex-value sum | Total cost |
| --- | --- | --- | --- |
| `1 -> 2 -> 4` | `1 + 3 = 4` | `3 + 4 + 7 = 14` | **18** |
| `1 -> 3 -> 4` | `1 + 2 = 3` | `3 + 8 + 7 = 18` | **21** |

The second route has smaller edge cost but a larger total cost. Node values must participate in the relaxation; they cannot simply be added to the destination after running an edge-only shortest-path algorithm.

## 6. Complete C++17 Implementation

### Input and Output Used Here

```text
n m source
val[1] val[2] ... val[n]
u1 v1 w1
u2 v2 w2
...
um vm wm
```

Vertices are labelled `1` through `n`. Every input edge is undirected. Print the minimum total cost to every vertex, in label order; use `INF` for an unreachable vertex.

Use `long long` for values, weights, heap distances, and answers. All costs must be nonnegative and every finite shortest answer must be strictly below `INF = LLONG_MAX`. The code checks both additions before performing them. A candidate too large to represent cannot improve any representable answer, so it is skipped; inputs whose true answer reaches or exceeds `INF` require a wider numeric representation and are outside these bounds.

```cpp
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

using ll = long long;
using State = pair<ll, int>; // (total cost, vertex)
const ll INF = numeric_limits<ll>::max();

vector<ll> dijkstraWithNodeCosts(
    const vector<vector<pair<int, ll>>>& g,
    const vector<ll>& val,
    int source
) {
    int n = static_cast<int>(g.size()) - 1;
    vector<ll> dist(n + 1, INF);
    vector<char> settled(n + 1, false);
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[source] = val[source];
    pq.push({dist[source], source});

    while (!pq.empty()) {
        auto [currentCost, u] = pq.top();
        pq.pop();

        if (settled[u]) continue;
        settled[u] = true;

        for (auto [v, weight] : g[u]) {
            if (settled[v]) continue;

            // Guard both additions; all operands are nonnegative.
            if (weight > INF - currentCost) continue;
            ll candidate = currentCost + weight;
            if (val[v] > INF - candidate) continue;
            candidate += val[v];

            if (candidate < dist[v]) {
                dist[v] = candidate;
                pq.push({candidate, v});
            }
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, source;
    cin >> n >> m >> source;

    vector<ll> val(n + 1);
    for (int v = 1; v <= n; ++v) cin >> val[v];

    vector<vector<pair<int, ll>>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        ll weight;
        cin >> u >> v >> weight;
        g[u].push_back({v, weight});
        g[v].push_back({u, weight});
    }

    vector<ll> dist = dijkstraWithNodeCosts(g, val, source);
    for (int v = 1; v <= n; ++v) {
        if (v > 1) cout << ' ';
        if (dist[v] == INF) cout << "INF";
        else cout << dist[v];
    }
    cout << '\n';
}
```

### What Does `settled` Mean?

It means the vertex has been **finalized on removal from the min-heap**, not merely discovered.

A better candidate may be found after a vertex was first inserted. Insert the improved pair without trying to delete the older entry. The first removal of an unsettled vertex has its minimum distance; later entries for that vertex are skipped before scanning its edges.

This is exactly standard Dijkstra. Only the source initialization and the relaxation cost have changed.

### Sample 1: The Illustrated Graph

Input:

```text
7 8 1
3 4 8 7 9 13 11
1 2 1
1 3 1
2 4 3
3 4 2
4 5 5
3 6 4
6 7 1
5 7 8
```

Output:

```text
3 8 12 18 32 29 41
```

### Sample 2: Improve an Earlier Candidate

Input:

```text
4 3 1
2 10 1 0
1 2 10
1 3 1
3 2 1
```

Output:

```text
2 15 4 INF
```

The first candidate for vertex `2` is `2 + 10 + 10 = 22`. After vertex `3` is finalized at cost 4, the route through it improves vertex `2` to `4 + 1 + 10 = 15`. The old heap entry `(22, 2)` is later skipped. Vertex `4` is disconnected.

### Sample 3: Only the Source Exists

Input:

```text
1 0 1
7
```

Output:

```text
7
```

Even with no edges, the starting vertex's value must be included.

## 7. Complexity

For `n` vertices and `m` undirected edges:

- Each vertex is settled at most once, and the adjacency lists contain `2m` entries in total.
- Each successful relaxation adds a heap entry. There are at most `O(m)` such entries, including obsolete candidates.
- **Time: `O(n + m log(m + 2))`** for this lazy-heap implementation. For a simple graph, the familiar bound is `O((n + m) log n)` for `n >= 2`.
- **Space: `O(n + m)`**, including adjacency lists, distances, settled flags, and heap entries.

Absorbing a destination value into a transition requires constant extra work per edge; it does not change Dijkstra's asymptotic complexity.

## 8. Common Mistakes

- **Starting with `dist[source] = 0`:** this omits the source value under the stated cost definition.
- **Adding `val[u]` again when leaving `u`:** `dist[u]` already includes it.
- **Forgetting `val[v]` on entry:** every destination vertex, including the final target, contributes its value.
- **Choosing an edge-only shortest path first:** it may pass through expensive vertices and fail to minimize the total cost.
- **Assigning both directions the same transformed weight:** each direction pays for its own destination.
- **Finalizing on insertion:** a later route may improve the tentative cost.
- **Allowing negative effective transition costs without reconsidering the algorithm:** Dijkstra's correctness depends on nonnegative increments.
- **Using `int` for accumulated costs:** multiple edge weights and node values can exceed its range.

The formulation to remember is: **pay the source once, then pay each edge and the vertex you enter.**

</READING_WIDGET>
