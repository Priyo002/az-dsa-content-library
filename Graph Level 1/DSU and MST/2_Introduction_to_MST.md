<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Minimum Spanning Tree: Kruskal's Algorithm

Suppose we need to connect every city in a network, and each available road has a construction cost. We want all cities connected while minimizing the **total cost of the roads selected**.

This is a minimum spanning tree problem. Unlike a shortest-path problem, it does not choose a starting city or minimize distances from a source.

## 1. What Is a Spanning Tree?

For a connected, undirected graph, a **spanning tree** is a subgraph that:

- Contains all the original vertices.
- Is connected.
- Has no cycle.

A spanning tree on `n` vertices has exactly **`n - 1` edges**. All selected edges must come from the original graph.

A **minimum spanning tree (MST)** is a spanning tree with the smallest possible sum of edge weights:

$$
\text{MST cost} = \min_{T\text{ is a spanning tree}}\sum_{e\in T}w(e).
$$

The graph may have positive, zero, or negative weights. The tree requirement still applies: we cannot add extra negative-weight edges if they create cycles. A disconnected graph has no spanning tree covering all its vertices. These conventions agree with the [Princeton Algorithms treatment of MSTs](https://algs4.cs.princeton.edu/43mst/).

For a single vertex, the empty edge set is a spanning tree of cost `0`.

## 2. Read the Example Graph

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/1d839e44-650e-40c5-9011-2132af4baac6.png" alt="AlgoZenith diagram showing a six-vertex weighted undirected graph above and an MST below with edges 1-2 of weight 3, 2-3 of weight 5, 3-6 of weight 3, 5-6 of weight 2, and 6-4 of weight 7, giving total cost 20" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The upper drawing is the original graph. The lower drawing selects:

| Selected edge | Weight |
| --- | --- |
| `5 — 6` | 2 |
| `1 — 2` | 3 |
| `3 — 6` | 3 |
| `2 — 3` | 5 |
| `4 — 6` | 7 |

These five edges connect all six vertices without a cycle. Their total weight is:

$$
2 + 3 + 3 + 5 + 7 = \boxed{20}.
$$

An alternative MST replaces `2 — 3` with `1 — 5`, which also has weight `5`. Both trees cost `20`; the drawing shows one valid choice.

## 3. Kruskal's Idea: Add the Cheapest Safe Edge

Initially, select no edges. Every vertex forms its own component.

Process all edges in **nondecreasing order of weight**. For each edge `(u, v)`:

- If `u` and `v` are in different components of the selected forest, accept the edge and merge those components.
- If they are already in the same component, reject the edge: there is already a selected path between them, so adding it would create a cycle.

Stop when `n - 1` edges have been accepted. If all edges have been considered but fewer than `n - 1` were accepted, the graph is disconnected and no MST exists.

The important word is **safe**. Simply selecting the cheapest `n - 1` edges is insufficient; those edges might contain a cycle and leave some vertices disconnected.

## 4. Use DSU to Check Components

DSU represents connectivity in the **edges selected so far**, not in all input edges.

Before considering `(u, v)`, compare `find_set(u)` and `find_set(v)`. Different representatives mean the edge joins two separate trees and can be accepted.

Using the boolean-returning union operation from the previous lesson, this becomes:

```cpp
if (dsu.union_sets(edge.u, edge.v)) {
    cost += edge.weight;
    chosen.push_back(edge);
}
```

The DSU performs a merge only when the roots differ. A successful union therefore corresponds to exactly one accepted MST edge.

Keep selected graph edges separately if you want the tree itself. **DSU parent pointers are not necessarily original graph edges** and cannot be used as the MST edge list.

## 5. Dry Run on the Diagram

For equal weights, use the order shown below. Equal-weight edges may be processed in any order without changing the minimum total cost, although the selected tree may differ.

| Edge | Weight | Decision | Reason | Accepted edges | Cost |
| --- | --- | --- | --- | --- | --- |
| `5 — 6` | 2 | Accept | Joins `{5}` and `{6}` | 1 | 2 |
| `1 — 2` | 3 | Accept | Joins `{1}` and `{2}` | 2 | 5 |
| `3 — 6` | 3 | Accept | Joins `{3}` and `{5, 6}` | 3 | 8 |
| `2 — 3` | 5 | Accept | Joins `{1, 2}` and `{3, 5, 6}` | 4 | 13 |
| `1 — 5` | 5 | Reject | Both endpoints are already connected | 4 | 13 |
| `2 — 5` | 6 | Reject | Both endpoints are already connected | 4 | 13 |
| `4 — 6` | 7 | Accept | Connects the remaining vertex `4` | 5 | 20 |

We now have `6 - 1 = 5` accepted edges, so we stop. The remaining edge `3 — 4` of weight `9` is not needed.

## 6. Why Does the Greedy Choice Work?

Maintain the statement: **the selected edges can be extended to some MST**.

Suppose the next accepted edge is `e = (u, v)`. Its endpoints lie in different selected components.

Consider an MST `T` containing all edges already selected:

1. If `T` already contains `e`, accepting it preserves the statement.
2. Otherwise, adding `e` to `T` creates a cycle. On the old path from `u` to `v`, some edge `f` must leave `u`'s selected component.
3. That edge `f` cannot already be selected, because it joins different selected components.
4. Since edges are processed in increasing weight order, `w(e) <= w(f)`. A strictly cheaper crossing edge would have been processed and accepted earlier, joining those components.
5. Remove `f` and keep `e`. The result is still a spanning tree, still contains all selected edges, and has no larger cost. It is therefore also an MST.

Each accepted edge preserves the statement. Once `n - 1` edges have been accepted, the selected forest is itself a spanning tree and hence an MST.

## 7. Complete C++17 Implementation

### Input and Output

Input:

```text
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

Assume `n >= 1`, vertices numbered `1 ... n`, and integer edge weights. Each input line describes **one undirected edge**; do not insert a second copy for its reverse direction.

Parallel edges and self-loops are allowed. A self-loop is always rejected because both endpoints have the same representative.

Print the total MST cost, or `No Solution` if the graph is disconnected. The function also retains the selected edges, though the program prints only the cost.

Use `long long` for edge weights and totals. Input bounds must ensure that every sum of at most `n - 1` edge weights fits in `long long`.

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

class DSU {
private:
    vector<int> parent;
    vector<int> size;

public:
    explicit DSU(int n) : parent(n + 1), size(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
        size[0] = 0;
    }

    int find_set(int v) {
        if (parent[v] == v) {
            return v;
        }
        return parent[v] = find_set(parent[v]);
    }

    bool union_sets(int a, int b) {
        a = find_set(a);
        b = find_set(b);
        if (a == b) {
            return false;
        }
        if (size[a] < size[b]) {
            swap(a, b);
        }
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

struct Edge {
    int u, v;
    long long weight;
    int id;  // Input order, used only to break ties deterministically.
};

struct MSTResult {
    bool exists;
    long long cost;
    vector<Edge> chosen;
};

MSTResult kruskal(int n, vector<Edge> edges) {
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        if (a.weight != b.weight) {
            return a.weight < b.weight;
        }
        return a.id < b.id;
    });

    DSU dsu(n);
    MSTResult result{false, 0, {}};

    for (const Edge& edge : edges) {
        if (static_cast<int>(result.chosen.size()) == n - 1) {
            break;
        }
        if (dsu.union_sets(edge.u, edge.v)) {
            result.cost += edge.weight;
            result.chosen.push_back(edge);
        }
    }

    result.exists = (static_cast<int>(result.chosen.size()) == n - 1);
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<Edge> edges;
    edges.reserve(m);
    for (int id = 0; id < m; ++id) {
        int u, v;
        long long weight;
        cin >> u >> v >> weight;
        edges.push_back({u, v, weight, id});
    }

    MSTResult result = kruskal(n, edges);
    if (!result.exists) {
        cout << "No Solution\n";
    } else {
        cout << result.cost << '\n';
    }
    return 0;
}
```

The function takes the edge vector by value, so sorting its local copy does not modify the caller's input order. The `id` field makes equal-weight choices reproducible; it is not required for correctness.

For a disconnected graph, the selected edges form a minimum spanning forest: one minimum spanning tree per connected component. However, `exists` is false, and its partial cost must not be reported as an MST covering all `n` vertices.

## 8. Examples

### Example 1: The Illustrated Graph

Input:

```text
6 8
1 2 3
2 3 5
3 4 9
4 6 7
5 6 2
1 5 5
2 5 6
3 6 3
```

Output:

```text
20
```

With input-order tie-breaking, the selected edges match the lower drawing exactly.

### Example 2: Disconnected Graph

Input:

```text
4 2
1 2 5
3 4 2
```

Output:

```text
No Solution
```

Only two edges can be accepted, fewer than the required `4 - 1 = 3`.

### Example 3: Negative Weights Are Valid

Input:

```text
3 3
1 2 -4
2 3 0
1 3 5
```

Output:

```text
-4
```

Unlike Dijkstra's algorithm, Kruskal's algorithm does not require nonnegative weights. It compares edge weights and prevents cycles; it does not compute shortest-path distances.

## 9. Important MST Properties

### Uniqueness

If all edge weights are distinct, the MST is unique. Equal weights **may** produce multiple MSTs, but do not guarantee that they will. For example, a graph that is already a tree has exactly one spanning tree even if its edge weights repeat.

The illustrated graph has two MSTs because either weight-5 edge `2 — 3` or `1 — 5` can join the same two selected components at that stage.

### Minimum Product for Positive Weights

For **strictly positive** edge weights, an MST also minimizes the product of its selected edge weights.

Replace each weight `w` with `log(w)`. Since the logarithm is strictly increasing, it preserves the ordering and equality of edge weights. Kruskal therefore selects the same edges with the same tie-breaking. Also:

$$
\sum_{e\in T}\log w(e) = \log\left(\prod_{e\in T}w(e)\right).
$$

Minimizing the sum of transformed weights minimizes the original product. There is no need to compute logarithms in the implementation.

Do not apply this logarithm argument to zero or negative weights. The ordinary minimum-sum MST algorithm still supports those weights, but this additional property is being stated only for positive weights.

### Smallest Possible Maximum Edge

Every MST also minimizes the weight of its largest edge among all spanning trees. This is called the **minimum-bottleneck** property.

To see why, remove a largest edge `e` from an MST. The tree splits into two groups. A spanning tree whose every edge is strictly lighter than `e` would have a lighter edge connecting these groups. Replacing `e` with that edge would reduce the MST's total cost, a contradiction.

The converse does not always hold. In a triangle with weights `1, 2, 2`, the tree using both weight-2 edges has the smallest possible maximum edge (`2`), but costs `4` instead of the MST cost `3`.

### Maximum Spanning Tree

To maximize the total tree weight, process edges in **nonincreasing** weight order and use the same DSU cycle check.

Negating weights and running a minimum spanning tree algorithm is mathematically equivalent, but sorting in descending order avoids overflow when negating the most negative representable integer. The tree must still connect every vertex, even when some edge weights are negative.

## 10. Complexity

For `n` vertices and `m` input edges:

- DSU initialization: `O(n)`.
- Sorting edges: `O(m log(m + 1))`.
- Processing edges with optimized DSU: `O(m * alpha(n))` amortized.

The total is:

$$
O\bigl(n + m\log(m + 1) + m\alpha(n)\bigr).
$$

This is commonly summarized as `O(m log m)` for a connected graph with at least two vertices. The expanded expression also accounts for initialization when the graph has many isolated vertices or no edges.

The implementation uses `O(n + m)` space for DSU arrays, stored edges, the sorting copy, and selected edges. Path-compressed, size-balanced DSU has at most `O(log n)` recursive find depth.

## 11. Common Mistakes

- **Confusing MST with shortest paths:** minimizing the total selected weight does not minimize the path from a source to every vertex. In the illustrated MST, the path `1 -> 2 -> 3 -> 6 -> 5` costs `13`, even though the original graph has a direct `1 — 5` edge of weight `5`.
- **Pre-merging every input edge:** DSU must track only edges accepted into the selected forest.
- **Taking the first `n - 1` sorted edges without checking cycles:** this can fail to connect the whole graph.
- **Ignoring disconnected graphs:** verify that exactly `n - 1` edges were accepted.
- **Counting examined edges rather than accepted edges:** only successful unions contribute to the tree and its cost.
- **Using `int` for the total:** a sum of individually valid edge weights may exceed 32-bit range.
- **Assuming tied weights make the answer invalid:** ties are allowed; they may change which MST is returned.

The complete pattern is: **sort edges by weight, accept only edges joining different DSU components, and require `n - 1` successful unions.**

</READING_WIDGET>
