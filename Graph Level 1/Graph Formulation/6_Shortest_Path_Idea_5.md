<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Shortest Path Idea 5: Compress Same-Value Jumps with Super Nodes

Sometimes the natural graph model is correct but contains too many edges. Instead of changing the shortest-path algorithm, we can change the graph representation while preserving the cost of every useful move.

Here, a shared **super node** replaces all pairwise jumps between indices having the same array value.

## 1. Problem Statement

You are given an array `arr[1 ... n]`. From index `i`, you may:

1. Move to `i - 1` or `i + 1`, if that index exists, at cost **`a`**.
2. Jump to another index `j` with `arr[i] == arr[j]`, at cost **`b`**.

Find the minimum total cost to travel from a source index `s` to a target index `t`.

The supplied move rules do not fix the endpoints, so the teaching program below takes `s` and `t` as input. For the version asking to travel from the first index to the last, use `s = 1` and `t = n`. The same Dijkstra run also computes costs to all other indices.

Assume `n >= 1`, valid 1-based endpoints, and **nonnegative** move costs `a` and `b`. Array values are labels used only to test equality; they may be negative, zero, or large and are not added to the path cost.

All indices are reachable through adjacent moves. If `s == t`, the minimum cost is `0`.

## 2. The Natural Graph—and Its Size Problem

Create one vertex for each array index.

### Adjacent Moves

For each `i` from `1` to `n - 1`, add:

```text
i     -> i + 1    cost a
i + 1 -> i        cost a
```

This uses `2(n - 1)` directed edges, which is `O(n)`.

### Same-Value Jumps

If a value appears at `f` indices, every one can jump to each of the other `f - 1` indices. Explicitly representing those jumps requires `f(f - 1)` directed edges.

In the worst case, every array value is the same. Then there are `n(n - 1)` jump edges: **`O(n^2)`** memory and graph-building work.

Generating the full same-value group every time an index is processed can also take quadratic work. We need to represent the shared connections more compactly.

## 3. Create One Super Node per Distinct Value

A super node is an auxiliary graph vertex representing a group. It is **not an actual array position**.

For each distinct value `x`, create a super node `H_x`. For every index `i` with `arr[i] == x`, add exactly two directed edges:

$$
i \to H_x \quad \text{with cost }0,
$$

$$
H_x \to i \quad \text{with cost }b.
$$

Now a jump between any two indices in that group is represented as:

$$
i \xrightarrow{0} H_x \xrightarrow{b} j.
$$

The total cost is **`0 + b = b`**, exactly the original jump cost.

Keep the adjacent edges of cost `a` unchanged. They connect neighbouring positions regardless of whether their values match.

### The Directions Matter

These two super-node connections must be stored as directed edges with their respective weights.

- Giving both directions weight `b` would charge `2b` for a jump.
- Giving both directions weight `0` would make all same-value jumps free.
- Treating a zero-cost entry edge as undirected would incorrectly allow free exits.

The original jumps work both ways, but each direction is represented by its own two-edge route through the shared node.

## 4. Read the Illustrated Construction

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/6b3f40d1-8173-4e6f-bd46-9ef42b0dc307.png" alt="Array values 1 2 3 1 2 1 with adjacent edges of cost a and one AlgoZenith-styled super node per distinct value; index-to-super edges cost zero and super-to-index edges cost b" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The numbers in the six array boxes are **array values**, not vertex IDs. Reading from left to right:

```text
Index:  1  2  3  4  5  6
Value:  1  2  3  1  2  1
```

The groups are:

| Value | Member indices | Auxiliary node |
| --- | --- | --- |
| 1 | `{1, 4, 6}` | `H_1` |
| 2 | `{2, 5}` | `H_2` |
| 3 | `{3}` | `H_3` |

For example, the jump from index `2` to index `5` becomes `2 -> H_2 -> 5` at cost `b`. It cannot lead directly to index `4`, whose value is different.

The singleton group for value `3` does not enable a useful jump. Keeping its super node makes construction uniform and is harmless: going `3 -> H_3 -> 3` costs `b >= 0` and cannot improve the distance to index `3`.

## 5. Why Are Shortest Costs Preserved?

We must check both directions of the transformation.

### Every Original Route Can Be Represented

- An adjacent move keeps the same edge and cost `a`.
- A same-value jump `i -> j` becomes `i -> H_x -> j`, costing `b`.

Thus every original route has a transformed route with the same total cost. The transformed optimum cannot be larger.

### The New Graph Does Not Create a Cheaper Invalid Route

Consider a transformed route whose endpoints are original indices. Whenever it enters `H_x`, its next exit goes to an index whose value is also `x`. The two edges together cost `b` and correspond to a permitted same-value jump.

If it exits back to the very same index, that excursion costs a nonnegative amount and can be removed without increasing the cost. Compressing all other super-node passages produces a valid original route of no greater cost. The original optimum therefore cannot be larger either.

Together, the two arguments show that **shortest costs between original array indices are unchanged**.

This preserves monetary or weighted cost, not the number of graph edges. One original jump is now represented by two edges, so ordinary unweighted BFS on the transformed graph would solve the wrong objective in general.

## 6. Apply Dijkstra to the Smaller Graph

The transformed edge weights are `a`, `0`, and `b`. Since they are nonnegative, Dijkstra applies directly.

1. Group indices by array value.
2. Give original indices IDs `1 ... n`.
3. Give the distinct values auxiliary IDs starting at `n + 1`.
4. Add adjacent edges and the two directed edges for every index's group membership.
5. Set `dist[s] = 0` and run Dijkstra from the original source index.
6. Read `dist[t]` for the original target index.

Use the map's keys to identify groups, not as vertex IDs. For example, the array value `-1000000000` still needs only one ordinary auxiliary node ID.

The super nodes are just normal vertices during Dijkstra. Processing a finalized `H_x` scans its group's members once; it does not rebuild all pairwise jump edges.

## 7. Dry Run on the Illustrated Array

Choose:

```text
arr = [1, 2, 3, 1, 2, 1]
a = 4, b = 3
s = 2, t = 6
```

The implementation uses a sorted map, so the auxiliary IDs are:

```text
H_1 = 7, H_2 = 8, H_3 = 9
```

Initialize `dist[2] = 0`. With heap ties broken by vertex ID, the important processing steps are:

| Vertex finalized | Cost | Updates or comparisons |
| --- | --- | --- |
| Index `2` | 0 | Indices `1` and `3` get 4; `H_2` gets 0 |
| `H_2` | 0 | Index `5` gets 3; returning to `2` cannot improve 0 |
| Index `5` | 3 | Indices `4` and `6` get `3 + 4 = 7` |
| Index `1` | 4 | `H_1` gets 4 |
| Index `3` | 4 | `H_3` gets 4; candidate 8 for index `4` does not improve 7 |
| `H_1` | 4 | Candidates for indices `4` and `6` are 7, equal to their current distances |
| `H_3` | 4 | Returning to index `3` cannot improve its distance |
| Index `4` | 7 | No improvement |
| Index `6` | 7 | No improvement |

The final distances for the original indices are:

```text
Index:     1  2  3  4  5  6
Distance:  4  0  4  7  3  7
```

One optimal route is:

```text
Original moves:  2 --jump, cost 3--> 5 --adjacent, cost 4--> 6
Graph route:    2 --0--> H_2 --3--> 5 --4--> 6
Total cost:     7
```

An adjacent-only route would take four moves from index 2 to index 6 and cost `4 * 4 = 16`.

Why is 7 optimal? Jumps alone keep the array value unchanged, but the source has value 2 and the target has value 1, so at least one adjacent move is needed. No single legal move reaches index 6 from index 2. With positive costs 4 and 3, every feasible route therefore costs at least `4 + 3 = 7`, which the displayed route achieves.

## 8. Complete C++17 Implementation

### Input and Output Used Here

```text
n a b s t
arr[1] arr[2] ... arr[n]
```

Print the minimum total cost from index `s` to index `t`. This teaching format explicitly supplies the endpoints rather than assuming a particular pair.

Array labels and costs use `long long`. Require `a, b >= 0`, representable graph IDs, and every finite shortest distance strictly below `INF = LLONG_MAX`. The relaxation guards against overflow before adding an edge cost. Adjacent moves ensure reachability under the problem's rules, so no unreachable-output case is needed within these bounds.

```cpp
#include <functional>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

using ll = long long;
using Graph = vector<vector<pair<int, ll>>>;
using State = pair<ll, int>; // (total cost, vertex ID)
const ll INF = numeric_limits<ll>::max();

Graph buildGraph(const vector<ll>& arr, ll a, ll b) {
    int n = static_cast<int>(arr.size()) - 1;
    map<ll, vector<int>> groups;
    for (int i = 1; i <= n; ++i) groups[arr[i]].push_back(i);

    int groupCount = static_cast<int>(groups.size());
    Graph g(n + groupCount + 1);

    for (int i = 1; i < n; ++i) {
        g[i].push_back({i + 1, a});
        g[i + 1].push_back({i, a});
    }

    int hub = n + 1;
    for (const auto& entry : groups) {
        const vector<int>& members = entry.second;
        for (int i : members) {
            g[i].push_back({hub, 0}); // Enter the value group for free.
            g[hub].push_back({i, b}); // Pay b to exit at a member index.
        }
        ++hub;
    }

    return g;
}

vector<ll> dijkstra(const Graph& g, int source) {
    vector<ll> dist(g.size(), INF);
    vector<char> settled(g.size(), false);
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        auto [cost, u] = pq.top();
        pq.pop();

        if (settled[u]) continue;
        settled[u] = true;

        for (auto [v, weight] : g[u]) {
            if (settled[v]) continue;
            if (weight > INF - cost) continue;
            ll candidate = cost + weight;

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

    int n, source, target;
    ll a, b;
    cin >> n >> a >> b >> source >> target;

    vector<ll> arr(n + 1);
    for (int i = 1; i <= n; ++i) cin >> arr[i];

    Graph g = buildGraph(arr, a, b);
    vector<ll> dist = dijkstra(g, source);
    cout << dist[target] << '\n';
}
```

The min-heap can contain old candidates after a better distance is inserted. Finalize a vertex only on its first removal and skip subsequent entries. Use strict improvement, especially when `a` or `b` is zero, to avoid repeatedly inserting equal-cost routes.

### Sample 1: The Illustrated Array

Input:

```text
6 4 3 2 6
1 2 3 1 2 1
```

Output:

```text
7
```

### Sample 2: A Jump Is Not Always Cheaper

Input:

```text
3 2 10 1 3
5 5 5
```

Output:

```text
4
```

Two adjacent moves cost 4, while a direct same-value jump costs 10. Keep both move types and let Dijkstra choose.

### Sample 3: Free Same-Value Jumps

Input:

```text
4 5 0 1 4
-7 100 8 -7
```

Output:

```text
0
```

The equal values at indices 1 and 4 permit a zero-cost jump. The negative array label is not a negative edge weight.

## 9. Complexity

Let `k` be the number of distinct array values, so `k <= n`.

- **Vertices:** `n + k <= 2n`.
- **Adjacent edges:** `2(n - 1)` directed edges.
- **Group edges:** exactly `2n`, two for every original index.
- **Total directed edges:** `4n - 2 = O(n)`.

Using `map` to group indices takes `O(n log(n + 1))` time. Graph construction after grouping is linear, and Dijkstra on `O(n)` vertices and edges takes `O(n log(n + 1))` time.

Therefore:

- **Overall time: `O(n log(n + 1))`**, conventionally written `O(n log n)` for `n >= 2`.
- **Overall space: `O(n)`**, including groups, graph, distance arrays, and the heap's potentially duplicate entries.

The improvement is in the **number of represented edges**: a group of `f` indices needs `2f` connections instead of `f(f - 1)` pairwise jump edges. For large groups, this removes the quadratic bottleneck.

## 10. Common Mistakes

- **Building the full same-value clique first:** that has already incurred the quadratic cost the super nodes are meant to avoid.
- **Confusing array values with index IDs:** multiple indices can have the same label while remaining different vertices.
- **Connecting a hub to every index:** each hub must connect only to its own value group.
- **Making the hub edges undirected:** entry and exit have different costs.
- **Charging `b` on both entry and exit:** one jump should cost `b`, not `2b`.
- **Using BFS just because the graph is smaller:** its edge costs are still weighted and include zero-cost edges.
- **Reading the target's group distance instead of `dist[t]`:** arriving at a hub has not yet paid its exit cost.
- **Using negative `a` or `b` with Dijkstra:** the nonnegative-cost assumption is essential.

The pattern to remember is: **replace all-to-all connections within a group by a shared auxiliary node, and split the transition cost so that travelling through the node costs exactly one original move.**

</READING_WIDGET>
