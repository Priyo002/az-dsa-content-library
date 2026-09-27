<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bellman–Ford: Shortest Paths with Negative Edges

Dijkstra's algorithm relies on nonnegative edge weights to finalize distances greedily. What if an edge can have a negative weight?

**Bellman–Ford repeatedly relaxes every edge**, allowing improvements to propagate through the graph. It finds single-source shortest distances when no negative-weight cycle is reachable from the source, and can detect when such a cycle exists.

## 1. Problem and Assumptions

Given a **directed, weighted graph** with `n` vertices, `m` edges, and source `s`:

- Find the minimum total edge weight from `s` to every vertex.
- Recover one shortest path from `s` to a target `t`.
- Allow positive, zero, and negative edge weights.
- Report if a negative-weight cycle is reachable from `s`.

A **negative-weight cycle** is a directed cycle whose edge weights sum to a negative number. Going around it repeatedly keeps reducing the cost. Any vertex reachable from that cycle has no finite shortest distance from `s`, provided the cycle itself is reachable from `s`.

A negative cycle in an unreachable component does **not** affect this single-source problem. Even a reachable negative cycle does not necessarily affect every vertex; only vertices reachable from it have unbounded-below distances. The implementation below reports the presence of any reachable negative cycle and stops, rather than classifying affected vertices individually.

For an undirected graph, represent each edge by two directed edges. However, a negative undirected edge permits repeatedly travelling across it and back for a negative total cost. If it is reachable, ordinary shortest-walk distances are therefore not finite in that component.

## 2. What Do We Store?

| Structure | Meaning |
| --- | --- |
| `edges` | All directed edges `(u, v, weight)` |
| `dist[v]` | Best cost from `s` to `v` found so far |
| `parent[v]` | Previous vertex on the currently recorded route to `v` |
| `changed` | Whether any relaxation improved a distance in the current pass |

An edge list is convenient because every pass scans **all edges**. No priority queue or permanently visited array is needed.

Initially:

$$
\operatorname{dist}[s] = 0, \qquad
\operatorname{dist}[v] = \infty \quad (v \ne s).
$$

Set every parent to `-1`. Here, infinity means that no route from the source has been found yet.

## 3. Relaxation: Can This Edge Improve the Route?

Consider an edge `u -> v` with weight `w`. If `u` is reachable, taking this edge gives a candidate cost:

$$
\text{candidate} = \operatorname{dist}[u] + w.
$$

If this is smaller than `dist[v]`, update both the distance and parent:

```cpp
if (dist[u] != INF && dist[u] + w < dist[v]) {
    dist[v] = dist[u] + w;
    parent[v] = u;
}
```

For example, if `dist[u] = 7`, `w = -1`, and `dist[v] = 7`, the candidate is `6`. The route through `u` is better, so `dist[v]` becomes `6`.

The `dist[u] != INF` guard is essential. An unreachable vertex must not produce a route just because `INF + a_negative_weight` happens to be smaller than the numeric value used for `INF`.

## 4. Why Are `n - 1` Passes Enough?

One **pass** means scanning every edge once and attempting relaxation.

If no negative cycle is reachable from `s`, a shortest route can be chosen without repeated vertices: removing a cycle of nonnegative total weight cannot increase its cost. Such a simple path has at most `n - 1` edges.

Relaxation propagates shortest distances along these paths:

1. Before any pass, the zero-edge path to `s` is known.
2. After one pass, every shortest path needing at most one edge is accounted for.
3. After two passes, every shortest path needing at most two edges is accounted for.
4. After `n - 1` passes, all finite shortest distances are correct.

More precisely, if a shortest path to a vertex uses at most `k` edges, that vertex has its correct distance after `k` complete passes. When the last edge of such a path is scanned, its predecessor already has its correct distance from the previous pass, or acquired it even earlier.

**The code updates distances in place.** An improvement may be used by a later edge in the same pass, so one pass can propagate through several edges. Do not interpret pass `k` as finding paths of *exactly* `k` edges, or only paths of at most `k` edges. Edge order affects the number of passes needed, but not the final answer when shortest distances are finite.

### Stop Early When Nothing Changes

If a complete pass makes no update, another pass over the same edges cannot improve anything either. The distances have stabilized, so we can stop early.

The `n - 1` bound is a correctness guarantee, not just a limit added to prevent an infinite loop.

## 5. Dry Run on the Illustrated Graph

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/2687259a-e08b-4dc9-980c-c87d81708911.png" alt="Directed graph with weights 1 to 2: 5, 2 to 3: 2, 2 to 4: 1, 4 to 5: 1, and 5 to 3: minus 1; shortest distances from 1 are 0, 5, 6, 6, 7" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The left panel gives the directed edges and weights. The right panel shows the final distances from source `1`; it retains all graph edges and is **not** a shortest-path tree.

For this dry run, store the edges in the following order:

```text
5 -> 3, weight -1
4 -> 5, weight  1
2 -> 4, weight  1
2 -> 3, weight  2
1 -> 2, weight  5
```

This deliberately places several edges before the edges that make their starting vertices reachable, showing why multiple passes may be necessary.

| After pass | `dist[1]` | `dist[2]` | `dist[3]` | `dist[4]` | `dist[5]` | Improvements |
| --- | --- | --- | --- | --- | --- | --- |
| Initialization | 0 | ∞ | ∞ | ∞ | ∞ | Only the source is reachable |
| 1 | 0 | 5 | ∞ | ∞ | ∞ | `1 -> 2` |
| 2 | 0 | 5 | 7 | 6 | ∞ | `2 -> 4`, then `2 -> 3` |
| 3 | 0 | 5 | 7 | 6 | 7 | `4 -> 5` |
| 4 | 0 | 5 | 6 | 6 | 7 | `5 -> 3` improves 7 to 6 |

The final route to vertex `3` is:

```text
1 -> 2 -> 4 -> 5 -> 3
Cost = 5 + 1 + 1 - 1 = 6
```

The shorter-in-edges route `1 -> 2 -> 3` costs `7`. We minimize **total weight**, not the number of edges.

With a different edge order, the same distances could be found sooner. The worst-case bound remains `n - 1` passes.

## 6. Detecting a Reachable Negative Cycle

After the `n - 1` passes, scan the edges once more. If any edge can still improve a distance from a **reachable** starting vertex, a negative cycle is reachable from `s`.

```cpp
if (dist[u] != INF && dist[u] + w < dist[v]) {
    // A negative-weight cycle is reachable from the source.
}
```

Why does this work?

- Without a reachable negative cycle, the `n - 1` passes have already found all finite shortest distances, so no further improvement is possible.
- On a reachable negative cycle, not all inequalities `dist[v] <= dist[u] + w` can hold. Adding them around the cycle would imply `0 <= sum_of_cycle_weights`, contradicting its negative total. Therefore, some edge is still relaxable.

For example:

```text
1 -> 2, weight  1
2 -> 3, weight -2
3 -> 2, weight  1
```

The cycle `2 -> 3 -> 2` costs `-1`. Repeating it keeps improving the costs of reaching vertices `2` and `3`.

Do not reconstruct paths from the resulting parent array: it may contain a cycle. The program checks for this condition **before** following parents.

## 7. Reconstructing One Shortest Path

When no reachable negative cycle exists:

1. If `dist[t] == INF`, there is no path from `s` to `t`.
2. Otherwise, start at `t` and repeatedly follow `parent[cur]` until reaching the source, whose parent remains `-1`.
3. Reverse the collected vertices to obtain the path from `s` to `t`.

Update parents only on a **strict improvement**. Equal-cost alternatives do not need to replace the current parent. The algorithm returns one shortest path, not necessarily the lexicographically smallest one.

If `s == t` and no reachable negative cycle exists, the recovered path contains only `s` and has cost `0`.

## 8. Complete C++17 Implementation

### Input and Output Used Here

This teaching program uses 1-based vertex labels:

```text
n m s t
u1 v1 w1
u2 v2 w2
...
um vm wm
```

Each edge is directed from `u` to `v`. If a reachable negative cycle exists, print a diagnostic and stop. Otherwise, print every distance (`INF` for unreachable vertices), then the path to `t` or `No path`.

Use `long long`, not `int`, for weights and distances. The implementation assumes that **all intermediate additions** `dist[u] + weight` fit in signed 64-bit arithmetic and every finite distance is smaller than `INF`. This includes values encountered while testing graphs with negative cycles, not just final answers. Check the problem's bounds; a conservative sufficient bound for this implementation is `n * max(1, m) * W < LLONG_MAX`, evaluated mathematically, where `W` is the maximum absolute edge weight. Do not clamp negative distances to a fixed floor, since that can hide further improvements and break cycle detection.

```cpp
#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

using ll = long long;
const ll INF = numeric_limits<ll>::max();

struct Edge {
    int u, v;
    ll weight;
};

struct Result {
    vector<ll> dist;
    vector<int> parent;
    bool hasNegativeCycle;
};

Result bellmanFord(int n, const vector<Edge>& edges, int source) {
    vector<ll> dist(n + 1, INF);
    vector<int> parent(n + 1, -1);
    dist[source] = 0;

    for (int pass = 1; pass <= n - 1; ++pass) {
        bool changed = false;

        for (const Edge& e : edges) {
            if (dist[e.u] == INF) continue;

            ll candidate = dist[e.u] + e.weight;
            if (candidate < dist[e.v]) {
                dist[e.v] = candidate;
                parent[e.v] = e.u;
                changed = true;
            }
        }

        if (!changed) break;
    }

    // Only edges reachable from source can reveal a relevant cycle.
    for (const Edge& e : edges) {
        if (dist[e.u] != INF && dist[e.u] + e.weight < dist[e.v]) {
            return {dist, parent, true};
        }
    }

    return {dist, parent, false};
}

vector<int> restorePath(int target, const vector<int>& parent) {
    // Call only after ruling out reachable negative cycles
    // and confirming that target is reachable.
    vector<int> path;
    for (int cur = target; cur != -1; cur = parent[cur]) {
        path.push_back(cur);
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, source, target;
    cin >> n >> m >> source >> target;

    vector<Edge> edges(m);
    for (Edge& e : edges) cin >> e.u >> e.v >> e.weight;

    Result result = bellmanFord(n, edges, source);
    if (result.hasNegativeCycle) {
        cout << "Reachable negative cycle\n";
        return 0;
    }

    cout << "Distances:";
    for (int v = 1; v <= n; ++v) {
        if (result.dist[v] == INF) cout << " INF";
        else cout << ' ' << result.dist[v];
    }
    cout << '\n';

    if (result.dist[target] == INF) {
        cout << "No path\n";
        return 0;
    }

    vector<int> path = restorePath(target, result.parent);
    cout << "Path:";
    for (int v : path) cout << ' ' << v;
    cout << '\n';
}
```

### Sample 1: The Illustrated Graph

Input:

```text
5 5 1 3
5 3 -1
4 5 1
2 4 1
2 3 2
1 2 5
```

Output:

```text
Distances: 0 5 6 6 7
Path: 1 2 4 5 3
```

### Sample 2: A Reachable Negative Cycle

Input:

```text
3 3 1 3
1 2 1
2 3 -2
3 2 1
```

Output:

```text
Reachable negative cycle
```

### Sample 3: An Unreachable Negative Cycle

Input:

```text
4 3 1 3
1 2 4
3 4 -2
4 3 1
```

Output:

```text
Distances: 0 4 INF INF
No path
```

The negative cycle between `3` and `4` cannot be reached from source `1`, so it does not trigger the single-source cycle check.

## 9. Complexity

- At most `n - 1` relaxation passes, each scanning `m` edges, plus one `O(m)` cycle-check scan.
- Worst-case time: **`O(nm)`** for the edge scans. Including initialization and printing, write `O(n + nm)` to also cover an edgeless graph.
- Auxiliary space: **`O(n)`** for distances, parents, and the recovered path; **`O(n + m)`** including the edge list.
- Early stopping can save passes, but does not change the worst-case bound.

## 10. Common Mistakes

- **Using a visited/finalized flag like Dijkstra:** Bellman–Ford must allow a vertex's distance to improve in later passes.
- **Relaxing from infinity:** skip edges whose starting vertex is unreachable.
- **Assuming a negative edge is a negative cycle:** a directed graph can contain negative edges and still have perfectly valid shortest paths, as the diagram shows.
- **Assuming every negative cycle matters to this source:** only reachable cycles are detected by this initialization.
- **Following parents before checking for a negative cycle:** this can loop indefinitely or produce a meaningless route.
- **Using `int` or ignoring intermediate overflow:** distance bounds must cover repeated relaxations, including the detection scan.

The central idea is simple: **keep giving every edge a chance to improve a route; if improvement is still possible after `n - 1` passes, a reachable negative cycle explains it.**

</READING_WIDGET>
