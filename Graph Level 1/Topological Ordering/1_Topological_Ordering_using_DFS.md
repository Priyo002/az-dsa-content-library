<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Topological Ordering Using DFS

Suppose an edge `u -> v` means that `u` must come before `v`: for example, a prerequisite must be completed before a task that depends on it.

A **topological ordering** arranges every vertex in one sequence while respecting all such requirements. DFS gives us this ordering by recording **when vertices finish**, rather than when they are first visited.

## 1. What Is a Topological Ordering?

For every directed edge `u -> v`, vertex `u` must appear **before** vertex `v` in the ordering.

If `pos[u]` is the position of `u` in the sequence, then a valid ordering satisfies:

$$
\text{pos}[u] < \text{pos}[v]
\qquad\text{for every edge }u\to v
$$

Every vertex appears exactly once, including isolated vertices.

A topological ordering is not necessarily unique. Some graphs have only one valid ordering; others have several. Vertices that are not forced into a relative order by the dependencies may appear in different positions in valid answers.

### Why Must the Graph Be Acyclic?

Consider the directed cycle:

```text
1 -> 2 -> 3 -> 1
```

It requires 1 before 2, 2 before 3, and 3 before 1. No linear sequence can satisfy all three conditions.

Thus, a directed graph has a topological ordering **if and only if it is a Directed Acyclic Graph (DAG)**.

## 2. Understanding the Illustrated DAG

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/fcb10340-9259-4a3c-a2e7-7c66b8f5a3dc.png" alt="Six-vertex DAG with edges 1-to-2, 2-to-3, 3-to-6, 4-to-1, 4-to-5, 5-to-2, and 5-to-3, rearranged below in valid topological order 4,5,1,2,3,6 so every edge points forward" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The directed edges are:

```text
1 -> 2
2 -> 3
3 -> 6
4 -> 1
4 -> 5
5 -> 2
5 -> 3
```

The lower part of the diagram rearranges the same vertices and edges into the valid ordering:

```text
4, 5, 1, 2, 3, 6
```

Every arrow goes from an earlier vertex to a later vertex in this sequence. For example, 5 appears before both 2 and 3, and 4 appears before both 1 and 5.

Another valid ordering is:

```text
4, 1, 5, 2, 3, 6
```

Vertices 1 and 5 can exchange positions here. Both must follow 4 and precede 2, but neither must precede the other.

A topological ordering is **not necessarily a path**. In the first ordering, 5 is followed by 1, but there is no edge `5 -> 1`. The sequence expresses ordering constraints, not a route through consecutive vertices.

## 3. DFS Idea: Append on Return, Then Reverse

When DFS explores a vertex `u`, it recursively visits its unvisited outgoing neighbours. Only **after** those recursive calls return do we append `u` to a list.

```cpp
void dfs(int u) {
    vis[u] = 1;
    for (int v : g[u]) {
        if (!vis[v]) dfs(v);
    }
    topo.push_back(u); // Record completion, not discovery.
}
```

For now, this short version assumes the input is a DAG. The complete implementation below also checks for cycles.

After running DFS from every still-unvisited vertex, reverse the list:

```cpp
reverse(topo.begin(), topo.end());
```

### Why Append After the Recursive Calls?

In a DAG, when `u` finishes, every outgoing neighbour `v` has already finished. So the unreversed completion list places `v` before `u`.

Reversing the list puts `u` before `v`, exactly as the edge `u -> v` requires.

For a simple chain:

```text
Edges:                1 -> 2 -> 3
DFS completion list:  3, 2, 1
After reversal:       1, 2, 3
```

A **sink** has no outgoing edges; it can finish immediately when DFS enters it. Sinks therefore occur early in the relevant completion sequence, **not because they should come first in the final topological ordering**.

Under the interpretation “`u -> v` means `u` is required before `v`,” reversal puts prerequisites before their dependents. In any nonempty DAG, the first vertex of a valid topological order has no incoming edges, and the last has no outgoing edges.

## 4. Dry Run: Completion Order vs. Topological Order

Use an outer loop over vertices 1 through 6 and the neighbour order from the sample input below.

Starting at 1, DFS enters:

```text
1 -> 2 -> 3 -> 6
```

| Event | Completion list after appending |
| --- | --- |
| 6 has no outgoing edges; finish 6. | `[6]` |
| Return to 3; finish 3. | `[6, 3]` |
| Return to 2; finish 2. | `[6, 3, 2]` |
| Return to 1; finish 1. | `[6, 3, 2, 1]` |
| The outer loop reaches unvisited 4. Its neighbour 1 is already finished; enter 5. | No append yet. |
| At 5, both 2 and 3 are already finished; finish 5. | `[6, 3, 2, 1, 5]` |
| Return to 4; finish 4. | `[6, 3, 2, 1, 5, 4]` |

Reverse the completed list:

```text
Completion list:    6, 3, 2, 1, 5, 4
Topological order:  4, 5, 1, 2, 3, 6
```

DFS began at 1, but the final order begins at 4. The source of a DFS call does not have to be the first vertex of the resulting topological order.

Notice why the outer loop is necessary: starting only from 1 cannot reach 4 or 5, even though they belong to the same graph.

## 5. Reject Cycles Before Using the Ordering

A visited array prevents repeated recursion, but it does not establish that the graph is a DAG. DFS can produce a completion list even when a directed cycle exists; reversing such a list does not make it a valid topological ordering.

Reuse the three-color states from the directed-cycle lesson:

| Color | Meaning |
| --- | --- |
| `1` | Unvisited. |
| `2` | Active on the current recursion stack. |
| `3` | Finished. |

For an edge `u -> v`:

- If `v` is unvisited, recursively explore it.
- If `v` is active, a back edge proves a cycle: reject the graph.
- If `v` is finished, no recursive call is needed.

Mark `u` finished and append it only after processing its outgoing edges successfully. If any DFS finds a cycle, discard any partial completion list and do not run the DAG longest-path calculation.

As before, this is a directed graph: **do not skip an edge just because it goes back to the parent**.

## 6. Why Reverse Completion Order Is Correct

Consider any edge `u -> v` when DFS examines it:

1. **If `v` is unvisited**, DFS explores `v` before finishing `u`, so `v` is appended first.
2. **If `v` is already finished**, it has already been appended before `u`.
3. **If `v` is active**, there is a directed cycle, and the algorithm reports that no topological ordering exists.

For a DAG, only the first two cases occur. Every edge therefore has its destination before its source in the completion list. Reversal makes its source come first.

The outer loop includes every vertex, and each vertex is appended once. Hence, the reversed list is a valid topological ordering of the whole graph.

## 7. Application: Longest Path in a DAG

Topological ordering is useful when a value at one vertex depends on values at other vertices. Because there are no cycles, we can evaluate those dependencies in an order where the needed answers are already available.

Here, all edges are unweighted, and we measure path length in **edges**.

Define:

$$
\text{dp}[u] = \text{maximum number of edges in a directed path starting at }u
$$

### Base Case

If `u` has no outgoing edges, the longest path starting there stays at `u` and uses **0 edges**:

$$
\text{dp}[u] = 0
$$

### Transition

If we take an edge `u -> v`, we use one edge and may then continue along a longest path starting at `v`:

$$
\text{dp}[u] = \max\left(0,\ \max_{u\to v}(1+\text{dp}[v])\right)
$$

The answer for the entire DAG is:

$$
\max_{1\leq u\leq n}\text{dp}[u]
$$

It is not necessarily the answer for vertex 1; a longest path can begin elsewhere.

### Memoized Recursive Version

After verifying that the graph is a DAG, initialize `dp` to -1 and use:

```cpp
vector<int> dp;

int rec(int node) { // Longest path starting at node, measured in edges.
    if (dp[node] != -1) return dp[node];

    int ans = 0;
    for (int v : g[node]) {
        ans = max(ans, 1 + rec(v));
    }
    return dp[node] = ans;
}
```

To obtain the global answer:

```cpp
dp.assign(n + 1, -1);
int longest = 0;
for (int node = 1; node <= n; ++node) {
    longest = max(longest, rec(node));
}
```

Memoization computes each vertex's value once. Multiple paths can lead to the same vertex, but they reuse its stored answer rather than recomputing the entire suffix.

**Counting vertices instead:** initializing `ans = 1` would count vertices on the path. A sink would have value 1. Both conventions are possible, but a path with \(k\) vertices has \(k-1\) edges. This lesson consistently uses the edge-count version, with base value 0.

Memoization alone does not make recursion safe on a cyclic graph: a recursive dependency may revisit a vertex before its answer has been stored. Apply this recurrence only after the DAG check.

## 8. Evaluating the Same DP Iteratively

For an edge `u -> v`, `dp[u]` depends on `dp[v]`. We must compute `v` before `u`.

But a topological order puts `u` before `v`. Therefore, to calculate the longest path **starting at each vertex**, iterate in **reverse topological order**:

```cpp
vector<int> dp(n + 1, 0);
for (auto it = topo.rbegin(); it != topo.rend(); ++it) {
    int u = *it;
    for (int v : g[u]) {
        dp[u] = max(dp[u], 1 + dp[v]);
    }
}
```

Here, `topo` is already the final topological order, after reversing the DFS completion list. Its reverse iteration visits successors before predecessors.

### DP Dry Run on the Illustrated Graph

```text
Topological order:     4, 5, 1, 2, 3, 6
DP processing order:   6, 3, 2, 1, 5, 4
```

| Vertex processed | Calculation | Longest path starting here, in edges |
| --- | --- | --- |
| 6 | No outgoing edges. | 0 |
| 3 | `1 + dp[6]` | 1 |
| 2 | `1 + dp[3]` | 2 |
| 1 | `1 + dp[2]` | 3 |
| 5 | `max(1 + dp[2], 1 + dp[3])` | 3 |
| 4 | `max(1 + dp[1], 1 + dp[5])` | 4 |

The answer is **4 edges**. Two paths achieving it are:

```text
4 -> 1 -> 2 -> 3 -> 6
4 -> 5 -> 2 -> 3 -> 6
```

Each contains five vertices but four edges. The topological ordering itself contains six vertices and is not a six-vertex path.

### When Would Forward Topological Order Be Used?

Forward topological processing is also possible, but with a different state: the longest path **ending at** each vertex.

Initialize every value to 0 to allow a path to start anywhere. Then, for each edge `u -> v` while processing `u` in forward topological order, update:

```cpp
ending[v] = max(ending[v], ending[u] + 1);
```

Do not mix this forward-update rule with `dp[u] = 1 + dp[v]`. The direction of iteration must match what the state means and which values it depends on.

## 9. Complete C++17 Implementation

This program finds a topological ordering and then computes the longest path in edges using reverse topological DP. It rejects cyclic inputs before performing the DP.

### Input

- First line: `n m`, the numbers of vertices and directed edges.
- Next `m` lines: `u v`, representing `u -> v`.
- Assume `n >= 1` and valid vertex labels from 1 to `n`.

### Output for This Lesson

- If a cycle exists, print `No topological ordering: directed cycle found`.
- Otherwise, print one topological ordering and the longest path length in edges.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g;
vector<int> col, topo;

// Return true if a directed cycle is found.
bool dfs(int u) {
    col[u] = 2;

    for (int v : g[u]) {
        if (col[v] == 1) {
            if (dfs(v)) return true;
        } else if (col[v] == 2) {
            return true;
        }
    }

    col[u] = 3;
    topo.push_back(u); // Append only after successful completion.
    return false;
}

void solve() {
    int n, m;
    cin >> n >> m;
    g.assign(n + 1, {});
    col.assign(n + 1, 1);
    topo.clear();

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
    }

    for (int u = 1; u <= n; ++u) {
        if (col[u] == 1 && dfs(u)) {
            cout << "No topological ordering: directed cycle found\n";
            return;
        }
    }

    reverse(topo.begin(), topo.end());

    vector<int> dp(n + 1, 0);
    for (auto it = topo.rbegin(); it != topo.rend(); ++it) {
        int u = *it;
        for (int v : g[u]) {
            dp[u] = max(dp[u], 1 + dp[v]);
        }
    }

    int longest = 0;
    for (int u = 1; u <= n; ++u) {
        longest = max(longest, dp[u]);
    }

    cout << "Topological order:\n";
    for (size_t i = 0; i < topo.size(); ++i) {
        if (i > 0) cout << ' ';
        cout << topo[i];
    }
    cout << '\n';
    cout << "Longest path length (edges): " << longest << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
```

### Sample 1: The Illustrated DAG

Input:

```text
6 7
1 2
2 3
3 6
4 1
4 5
5 2
5 3
```

Output with this DFS order:

```text
Topological order:
4 5 1 2 3 6
Longest path length (edges): 4
```

A different DFS neighbour order may produce another valid topological order. The longest path length remains 4.

### Sample 2: A Directed Cycle

Input:

```text
3 3
1 2
2 3
3 1
```

Output:

```text
No topological ordering: directed cycle found
```

The edge `3 -> 1` reaches an active vertex. The program rejects the graph rather than printing the reversed completion list as an ordering.

### Sample 3: Isolated Vertices

Input:

```text
3 0
```

Output with this outer-loop order:

```text
Topological order:
3 2 1
Longest path length (edges): 0
```

With no edges, every permutation is a valid topological order, and every longest path has zero edges.

## 10. Complexity

- **Topological ordering with cycle detection:** \(O(n+m)\) time.
- **Longest path in a DAG:** \(O(n+m)\) time, using either memoization or topological DP.
- **Combined time:** \(O(n+m)\); a constant number of linear passes is still linear.
- **Auxiliary space:** \(O(n)\) for colors, the ordering, DP, and the DFS call stack.
- **Total space including adjacency lists:** \(O(n+m)\).

Recursive DFS can reach depth \(n\). Large graphs with long chains may require an iterative DFS because of the environment's call-stack limit. Memoized longest-path recursion has the same depth risk; iterative DP avoids that additional recursive pass.

## 11. Common Mistakes and Useful Checks

- **Appending on entry:** this records discovery order, not the completion order needed here.
- **Forgetting the reversal:** the completion list puts successors before predecessors.
- **Claiming sinks should come first:** a sink finishes early in DFS, but reversal places it after its prerequisites.
- **Assuming every graph has an ordering:** detect cycles unless the input guarantees a DAG.
- **Starting DFS from only one vertex:** other vertices may be unreachable from it.
- **Treating the order as a path:** consecutive vertices in a topological sequence need not share an edge.
- **Expecting a unique or lexicographically smallest answer:** this DFS returns one valid ordering determined by its traversal order, with no smallest-order guarantee.
- **Mixing path-length conventions:** base 0 counts edges; base 1 counts vertices.
- **Using forward iteration for a starting-at-vertex recurrence:** that recurrence needs successor values first, so process in reverse topological order.
- **Running the longest-path recurrence on a cyclic input:** its DAG dependency argument no longer applies.

To validate an ordering, check that it contains every vertex exactly once, build each vertex's position, and verify `pos[u] < pos[v]` for every directed edge.

## Quick Recap

- A topological order puts every edge's source before its destination.
- It exists exactly for DAGs and need not be unique.
- Append each vertex when DFS finishes, then reverse the completion list.
- Use active/finished states to reject directed cycles.
- Longest paths starting at each vertex use base 0 for edge counts and reverse topological processing.

</READING_WIDGET>
