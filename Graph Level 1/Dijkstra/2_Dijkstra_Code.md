<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Dijkstra's Algorithm: Min-Heap Implementation

The [concept lesson](1_Dijkstra_Concept.md) established the greedy rule: finalize the unsettled vertex with the smallest tentative distance, then relax its outgoing edges.

This lesson implements that rule efficiently using a **min-priority queue**, handles duplicate candidates, and reconstructs one shortest path.

## 1. Problem and Assumptions

Given a weighted graph and a source `s`, find the minimum total weight from `s` to every vertex.

- Edge weights may be any **nonnegative** values supported by the numeric type; they are not restricted to a fixed set of `k` values.
- Zero-weight edges, cycles, parallel edges, and unreachable vertices are allowed.
- Negative edge weights are **not** supported by Dijkstra's algorithm.
- The same algorithm works for directed and undirected graphs; only adjacency-list construction differs.

The complete program below uses an **undirected** graph to match the supplied diagram. It also accepts a target `t` so we can print one shortest path after computing all distances.

## 2. What Do We Store?

| Structure | Meaning |
| --- | --- |
| `g[u]` | Outgoing edges stored as `(neighbour, weight)` |
| `dist[u]` | Best distance from the source found so far |
| `settled[u]` | Whether `u` has been finalized and its edges processed |
| `parent[u]` | Previous vertex on the currently recorded shortest path |
| Min-heap | Candidate entries stored as `(distance, vertex)` |

Notice that the pair order is different in the adjacency list and the heap. The heap must compare **distance first**, not the vertex label.

Initialize the distances to `INF`, all settled flags to false, and all parents to `-1`. Then set `dist[s] = 0` and insert `(0, s)` into the heap.

Only finite candidates enter the heap. Unreachable vertices remain at `INF` and are never processed.

## 3. Building the Min-Heap in C++

By default, a C++ `priority_queue` is a max-heap. Use `greater` to select the smallest pair:

```cpp
using State = pair<long long, int>; // (distance, vertex)
priority_queue<State, vector<State>, greater<State>> pq;
```

For example, `(3, 8)` is removed before `(7, 2)` because 3 is the smaller distance.

Pairs compare by the first value, then by the second on a tie. Thus, equal-distance vertices are processed by increasing label in this implementation. This tie-breaking does **not** guarantee the lexicographically smallest shortest path; it just makes the heap's selection deterministic.

Use `pq.top()` to inspect the minimum and `pq.pop()` to remove it. A priority queue has no `front()` method.

## 4. Why Can a Vertex Appear More Than Once?

C++'s `priority_queue` does not directly update the priority of an existing entry. Whenever a relaxation improves `dist[v]`, push a **new** pair `(dist[v], v)`.

An old entry can remain in the heap. It is a snapshot of an earlier candidate distance, not a reference that changes when `dist[v]` changes.

For example:

```text
First candidate:     (7, 2)
Improved candidate:  (3, 2)
```

Both may be present, but `(3, 2)` is removed first. Vertex 2 is finalized at distance 3; the later `(7, 2)` entry must not expand it again.

### Settle on Removal, Not on Insertion

The implementation uses:

```cpp
auto [du, u] = pq.top();
pq.pop();

if (settled[u]) continue;
settled[u] = true;
```

This is the role of `vis` in the original snippet: it means **finalized**, not merely discovered. The name `settled` makes that distinction explicit.

For the first removal of an unsettled vertex, `du` equals its current best distance. If a smaller candidate had been inserted, the min-heap would have removed that entry first. By the nonnegative-weight argument from the concept lesson, this distance is final.

Skip later entries **before scanning the adjacency list**. That ensures every vertex's outgoing edges are examined only once.

### Another Common Guard

An alternative implementation omits the settled array and skips stale distance snapshots instead:

```cpp
if (du != dist[u]) continue;
```

With strict-improvement insertions and nonnegative weights, this is also a standard valid approach. The complete program below uses the settled-array version throughout; both guards are not required together.

## 5. Dry Run on the Illustrated Graph

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/84f3e817-5537-4be8-b725-b32785fde8bd.png" alt="Undirected weighted graph on seven vertices with source 1; weights 1–2:1, 2–3:4, 1–4:7, 3–4:10, 4–5:3, 4–6:8, 6–7:4; the right panel labels shortest distances 0,1,5,7,10,15,19" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The left panel gives edge weights. The right panel shows the same graph with **shortest distances from vertex 1** written beside the vertices; it is not a shortest-path tree with all unused edges removed.

The undirected edges are:

```text
1 -- 2 : 1
2 -- 3 : 4
1 -- 4 : 7
3 -- 4 : 10
4 -- 5 : 3
4 -- 6 : 8
6 -- 7 : 4
```

| Vertex finalized | Distance | Successful updates |
| --- | --- | --- |
| 1 | 0 | Reach 2 at 1 and 4 at 7 |
| 2 | 1 | Reach 3 at `1 + 4 = 5` |
| 3 | 5 | None; candidate `5 + 10 = 15` does not improve `dist[4] = 7` |
| 4 | 7 | Reach 5 at 10 and 6 at 15 |
| 5 | 10 | None |
| 6 | 15 | Reach 7 at 19 |
| 7 | 19 | None |

Final distances in vertex order:

```text
Vertex:    1  2  3  4   5   6   7
Distance:  0  1  5  7  10  15  19
```

One shortest path to vertex 7 is `1 -> 4 -> 6 -> 7`, with cost `7 + 8 + 4 = 19`.

## 6. Heap Dry Run with Duplicate Entries

The supplied graph does not need duplicate candidates. To see why the guard matters, return to the **directed** example from the concept lesson:

```text
1 -> 2 : 7
1 -> 3 : 2
3 -> 2 : 1
2 -> 4 : 2
3 -> 4 : 8
```

Vertex 5 is isolated. Start with heap `[(0, 1)]`.

The table lists heap entries in **future removal order** for readability. A heap's internal array is not necessarily sorted this way.

| Entry removed | Action | Remaining entries after updates |
| --- | --- | --- |
| `(0, 1)` | Finalize 1; insert candidates for 2 and 3 | `[(2,3), (7,2)]` |
| `(2, 3)` | Finalize 3; improve 2 to 3; reach 4 at 10 | `[(3,2), (7,2), (10,4)]` |
| `(3, 2)` | Finalize 2; improve 4 to 5 | `[(5,4), (7,2), (10,4)]` |
| `(5, 4)` | Finalize 4; no outgoing edges | `[(7,2), (10,4)]` |
| `(7, 2)` | Skip: vertex 2 is already settled | `[(10,4)]` |
| `(10, 4)` | Skip: vertex 4 is already settled | `[]` |

Final distances are `[0, 3, 2, 5, INF]`. There are six heap removals but only four finalizations. Vertex 5 never enters the heap.

## 7. Complete C++17 Implementation

The function returns all distances and parent pointers. `restorePath` then reconstructs a path to a requested target.

### Input

- First line: `n m s t`, the numbers of vertices and undirected edges, source, and target.
- Next `m` lines: `u v w`, an undirected edge with nonnegative integer weight `w`.
- Assume `n >= 1` and valid vertex labels from 1 to `n`.
- Weights fit in `long long`. Every finite shortest distance must be strictly smaller than `INF`, which is `LLONG_MAX` in this implementation.

### Output for This Lesson

- Distances to vertices 1 through `n`, using `-1` for unreachable vertices.
- One shortest path from `s` to `t`, or `No path` if `t` is unreachable.

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

using ll = long long;
using State = pair<ll, int>; // (distance, vertex)
const ll INF = numeric_limits<ll>::max();

struct ShortestPaths {
    vector<ll> dist;
    vector<int> parent;
};

ShortestPaths dijkstra(const vector<vector<pair<int, ll>>>& g, int source) {
    int n = static_cast<int>(g.size()) - 1;
    vector<ll> dist(n + 1, INF);
    vector<int> parent(n + 1, -1);
    vector<char> settled(n + 1, false);
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();

        if (settled[u]) continue;
        settled[u] = true;

        for (auto [v, w] : g[u]) {
            if (settled[v]) continue;

            // du is finite. All weights are nonnegative.
            if (w > INF - du) continue; // Prevent overflow in du + w.
            ll candidate = du + w;

            if (candidate < dist[v]) {
                dist[v] = candidate;
                parent[v] = u;
                pq.push({candidate, v});
            }
        }
    }

    return {dist, parent};
}

vector<int> restorePath(int target, const ShortestPaths& result) {
    if (result.dist[target] == INF) return {};

    vector<int> path;
    for (int v = target; v != -1; v = result.parent[v]) {
        path.push_back(v);
    }
    reverse(path.begin(), path.end());
    return path;
}

void solve() {
    int n, m, source, target;
    cin >> n >> m >> source >> target;
    vector<vector<pair<int, ll>>> g(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w}); // Omit this line for directed input.
    }

    ShortestPaths result = dijkstra(g, source);
    cout << "Distances:\n";
    for (int v = 1; v <= n; ++v) {
        if (v > 1) cout << ' ';
        cout << (result.dist[v] == INF ? -1 : result.dist[v]);
    }
    cout << '\n';

    vector<int> path = restorePath(target, result);
    if (path.empty()) {
        cout << "No path\n";
    } else {
        cout << "Shortest path to " << target << ":\n";
        for (size_t i = 0; i < path.size(); ++i) {
            if (i > 0) cout << ' ';
            cout << path[i];
        }
        cout << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
```

For directed input, add only `u -> v`. Nothing inside `dijkstra` or `restorePath` needs to change.

### Why `long long` and an Overflow Guard?

Even when individual weights fit in `int`, their sum may not. Distances, edge weights, and the first field of the heap pair therefore all use `long long`.

Only finite distances are enqueued. Before addition, `w > INF - du` checks whether `du + w` would exceed the representable limit. A candidate equal to `INF` also does not improve a distance, because `INF` is reserved for unreachable vertices.

The guard prevents overflow; it does not make answers at or above `INF` representable. Choose the numeric type and sentinel to accommodate the problem's actual bounds.

### Parent Pointers and Zero-Weight Edges

Update a parent only when the distance strictly improves. The main implementation assigns a parent from a settled vertex to an unsettled vertex, so following parents goes backwards through finalizations and cannot create a cycle.

An unreachable target returns an empty path. For `source == target`, reconstruction returns just the source, with cost 0. If several shortest paths exist, the code returns one, not all of them.

## 8. Sample Runs

### Sample 1: The Illustrated Undirected Graph

Input:

```text
7 7 1 7
1 2 1
2 3 4
1 4 7
3 4 10
4 5 3
4 6 8
6 7 4
```

Output:

```text
Distances:
0 1 5 7 10 15 19
Shortest path to 7:
1 4 6 7
```

### Sample 2: An Improved Distance and an Unreachable Vertex

Input:

```text
4 3 1 2
1 2 7
1 3 2
3 2 1
```

Output:

```text
Distances:
0 3 2 -1
Shortest path to 2:
1 3 2
```

The heap contains both `(7, 2)` and `(3, 2)` at one point. Only the removal of `(3, 2)` expands vertex 2. If target 4 were requested instead, the distances would stay the same and the program would print `No path`.

### Sample 3: Zero-Weight Cycle

Input:

```text
4 4 1 4
1 2 0
2 3 0
3 1 0
3 4 5
```

Output:

```text
Distances:
0 0 0 5
Shortest path to 4:
1 3 4
```

The source directly reaches 3 at cost 0. The equal-cost route through 2 does not replace `parent[3]`, so the recorded path is `1 -> 3 -> 4`.

### Sample 4: Source Equals Target

Input:

```text
1 0 1 1
```

Output:

```text
Distances:
0
Shortest path to 1:
1
```

## 9. Time and Space Complexity

Let `n` be the number of vertices and `m` the number of input edges.

- Initializing distances, parents, and settled flags costs `O(n)`.
- Each vertex is expanded at most once, so at most `O(m)` adjacency entries are examined, including the constant factor of two for undirected input.
- Each successful relaxation adds one heap entry. There are at most `O(m + 1)` total insertions and removals, including the source and stale entries.
- The heap can contain `O(m + 1)` candidates. An insertion or removal costs `O(log(m + 2))`.

A bound that also handles edgeless graphs is:

$$
O\bigl(n + m\log(m+2)\bigr)
$$

For simple graphs, where `m = O(n²)`, this is commonly written as **`O((n + m) log n)`**. The heap-size accounting matters when parallel edges are allowed: this lazy implementation stores candidate entries, not exactly one entry per vertex.

The arrays use `O(n)` space, adjacency lists use `O(n + m)`, and the heap uses up to `O(m + 1)`. Total space is **`O(n + m)`**.

Reconstructing one path takes time and space proportional to its length, at most `O(n)`. Printing a separate explicit path to every vertex may require `O(n²)` output even though the shared parent array is linear-sized.

## 10. Implementation Pitfalls

- **Using the default max-heap:** use `greater<State>` so the smallest distance comes first.
- **Storing `(vertex, distance)` in the heap:** that prioritizes labels instead of costs.
- **Using `int` in the heap while distances are `long long`:** keep the distance types consistent.
- **Marking a vertex on insertion:** its first candidate may not be optimal.
- **Rescanning settled vertices:** skip duplicate entries before iterating over outgoing edges.
- **Pushing without a strict improvement:** equal-cost routes do not need a new entry for this distances-and-one-path task.
- **Expecting an old heap pair to update itself:** push a new candidate after each improvement.
- **Adding a reverse edge for a directed input:** build adjacency lists according to the actual graph.
- **Treating negative weights as supported:** this implementation relies on nonnegative weights; it does not validate or repair negative-weight input.
- **Reusing state between test cases:** this version creates fresh arrays and a fresh heap inside each call.

For a single-target problem, an early return is safe when the target is removed as an unsettled vertex and finalized. Do not stop merely because an edge first reaches the target. To compute all distances, continue until the heap is empty.

## Quick Recap

- Store heap entries as `(distance, vertex)` and use a min-heap.
- On a strict relaxation, update the distance and parent, then push a new pair.
- Finalize a vertex on its first useful removal; ignore later entries for it.
- Unreachable vertices never enter the heap.
- Use wide distance types and reconstruct a path only after checking reachability.

</READING_WIDGET>
