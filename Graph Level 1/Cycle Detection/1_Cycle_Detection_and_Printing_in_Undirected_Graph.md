<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Cycle Detection and Printing in an Undirected Graph

DFS explores a graph by following unvisited neighbours and returning when a branch is finished. The edges used to discover new vertices form a tree within each connected component.

What happens if another edge connects a vertex back to an ancestor in that tree? It closes a loop—and gives us a way to **detect and print a cycle**.

## 1. Problem Statement

Given an **undirected graph**, determine whether it contains a cycle. If it does, print **one** cycle as a sequence of vertices, repeating the starting vertex at the end to show that the cycle closes.

For example:

```text
2 -> 3 -> 4 -> 2
```

This cycle has three edges. The four printed labels include vertex 2 twice only to indicate the closing edge.

For this lesson, assume:

- Vertices are numbered from 1 to \(n\).
- The graph is **simple**: there are no self-loops or parallel edges.
- The graph may be disconnected.

A cycle has at least three distinct vertices, with no repeated vertex except the closing copy of its start. We want any one cycle—not necessarily the shortest, and not every cycle.

## 2. DFS Tree: Tree Edges and Back Edges

Whenever DFS discovers a new vertex `v` from `u`, record:

```cpp
par[v] = u;
```

The root has no parent. The parent links form the **DFS tree** of that connected component. For a disconnected graph, starting DFS in each unvisited component produces a **DFS forest**.

### Tree Edges

An edge used to discover an unvisited vertex is a **tree edge**.

For example, if DFS at 2 discovers 3, then `(2,3)` is a tree edge and `par[3] = 2`.

### Back Edges

When DFS examines an edge from a vertex to an **active ancestor other than its parent**, it finds a **back edge**. The edge is not part of the DFS tree.

For example, if the current recursive path is `1 -> 2 -> 3 -> 4` and vertex 4 has an edge to 2, then `(4,2)` is a back edge to ancestor 2.

The underlying edge is undirected. We describe it as going “back” because of the direction in which DFS encounters it: **from the descendant toward the ancestor**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/b6bcbf3c-4062-4bcd-8ba7-d66c4542c533.png" alt="DFS rooted at 1 in an eight-vertex undirected graph. Green tree edges are 1-2, 2-3, 3-4, 1-5, 5-6, 6-7, and 7-8. Red back edges 4-2 and 8-5 close a triangle and a four-vertex cycle." style="max-width: 100%; height: auto;" identifier="az-img-upload">

In this illustration, DFS explores the branch through 2 before the branch through 5:

| Edge type | Edges |
| --- | --- |
| Tree edges, shown in green | `1-2`, `2-3`, `3-4`, `1-5`, `5-6`, `6-7`, `7-8` |
| Back edges, shown in red | `4-2`, `8-5` |

The two back edges reveal these cycles:

- `2 -> 3 -> 4 -> 2`
- `5 -> 6 -> 7 -> 8 -> 5`

The diagram shows a complete DFS tree. Our implementation will stop as soon as it finds one cycle, so it need not explore the second branch after finding the first cycle.

The DFS tree depends on the starting vertex and neighbour order. An edge's role as a tree edge or back edge depends on that traversal; it is not a permanent property of the original graph.

## 3. Why Must We Ignore the Parent Edge?

An undirected edge `(u,v)` is stored in both adjacency lists:

```cpp
g[u].push_back(v);
g[v].push_back(u);
```

After DFS moves from `u` to a new vertex `v`, the neighbour list of `v` contains `u`. That does **not** prove a cycle exists: it is simply the same tree edge being examined in reverse.

Therefore, while processing `node`, skip its parent:

```cpp
if (v == parent) continue;
```

For example, a graph containing only `1-2` has no cycle. Walking `1 -> 2 -> 1` uses the same undirected edge twice; it is not a cycle under our simple-graph definition.

## 4. Distinguish Active Vertices from Finished Vertices

A boolean visited array is sufficient for the usual yes/no cycle test in a simple undirected graph: a visited non-parent neighbour indicates a cycle.

For **printing through parent links**, we need a stronger guarantee: the neighbour we are tracing toward must be an ancestor of the current vertex.

Use three DFS states:

| State | Meaning |
| --- | --- |
| `0` | Unvisited: DFS has not entered this vertex. |
| `1` | Active: its recursive call is still on the call stack. |
| `2` | Finished: its neighbours have been processed and its call has returned normally. |

At the current vertex `node`:

1. Mark it active and record its parent.
2. Skip the edge back to its parent.
3. For an unvisited neighbour, recurse.
4. For an active non-parent neighbour, record a cycle and stop.
5. Ignore a finished neighbour for reconstruction.
6. If no cycle was found, mark `node` finished before returning.

### Why Is an Active Neighbour an Ancestor?

Recursive DFS completes one child's call before moving to another child. Thus, while a call is running, the other active vertices lie on the chain of callers leading to it.

With self-loops excluded, an active neighbour of the current vertex must be a proper ancestor. After skipping the parent, the remaining active-neighbour edge closes a genuine cycle.

### Why Not Trace Toward Every Visited Neighbour?

Imagine DFS continued after exploring `2 -> 3 -> 4`. Once those descendant calls return, vertex 2 may inspect its edge to the now-finished vertex 4.

Vertex 4 is visited, but it is **below** 2 in the DFS tree. Following parents from 2 cannot reach 4; it moves toward 1 and then the root's sentinel instead.

This is why we reconstruct only from an edge to an **active ancestor**, rather than blindly following parents toward any visited vertex. We also return immediately after finding a cycle, preventing repeated reporting of the same undirected cycle.

## 5. How a Back Edge Gives Us the Cycle

Suppose DFS at `node` finds an active non-parent neighbour `v`.

- The parent links give a tree path from ancestor `v` down to `node`.
- The back edge `(node,v)` returns to the beginning.

Together, they form a cycle.

Record:

```cpp
cycle_start = v;    // Ancestor.
cycle_end = node;   // Descendant with the back edge.
```

To reconstruct:

1. Put `cycle_start` in the result.
2. Begin at `cycle_end` and follow parents until reaching `cycle_start`, appending each vertex encountered.
3. Append `cycle_start` again to close the cycle.
4. Reverse the result to show the tree path from ancestor to descendant, followed by the back edge.

Because `cycle_start` is an ancestor, the parent walk is guaranteed to reach it.

## 6. Dry Run on the Illustrated Graph

Using the sample's edge order, DFS begins at vertex 1 and enters:

```text
1 -> 2 -> 3 -> 4
```

| Event | What DFS does |
| --- | --- |
| Enter 1 | Mark 1 active; set `par[1] = -1`. |
| Examine `1-2` | 2 is unvisited: recurse and set `par[2] = 1`. |
| At 2, examine `2-1` | Skip the parent edge. |
| Examine `2-3` | 3 is unvisited: recurse and set `par[3] = 2`. |
| At 3, examine `3-2` | Skip the parent edge. |
| Examine `3-4` | 4 is unvisited: recurse and set `par[4] = 3`. |
| At 4, examine `4-3` | Skip the parent edge. |
| Examine `4-2` | 2 is active and is not 4's parent: a cycle is found. |

At detection:

```text
Active call stack: [1, 2, 3, 4]
cycle_start = 2
cycle_end   = 4

Parent chain: 4 -> 3 -> 2 -> 1
```

Reconstruction proceeds as follows:

```text
Start with ancestor: [2]
Append 4:            [2, 4]
Append par[4] = 3:   [2, 4, 3]
Reach 2; close:      [2, 4, 3, 2]
Reverse:             [2, 3, 4, 2]
```

Vertex 1 is **not** included: the cycle closes at ancestor 2, not necessarily at the DFS root.

The successful return propagates through the calls for 4, 3, 2, and 1. The search stops without needing to discover vertices 5 through 8.

## 7. Complete C++17 Implementation

### Input

- First line: `n m`, the numbers of vertices and edges.
- Next `m` lines: endpoints `u v` of each undirected edge.
- Assume `n >= 1`, valid vertex labels, and a simple graph.

### Output for This Lesson

- If there is no cycle, print `No cycle`.
- Otherwise, print `Cycle found` and one closed sequence of cycle vertices.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g;
vector<int> state, par;
int cycle_start = -1;
int cycle_end = -1;

bool dfs(int node, int parent) {
    state[node] = 1; // Active on the recursion stack.
    par[node] = parent;

    for (int v : g[node]) {
        if (v == parent) continue;

        if (state[v] == 0) {
            if (dfs(v, node)) return true;
        } else if (state[v] == 1) {
            // v is an active ancestor other than the parent.
            cycle_start = v;
            cycle_end = node;
            return true;
        }
        // Finished neighbours (state 2) need no reconstruction.
    }

    state[node] = 2; // This call finishes without finding a cycle.
    return false;
}

void solve() {
    int n, m;
    cin >> n >> m;
    g.assign(n + 1, {});
    state.assign(n + 1, 0);
    par.assign(n + 1, -1);
    cycle_start = cycle_end = -1;

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    // A cycle might be in a component that does not contain vertex 1.
    for (int node = 1; node <= n; ++node) {
        if (state[node] == 0 && dfs(node, -1)) {
            break;
        }
    }

    if (cycle_start == -1) {
        cout << "No cycle\n";
        return;
    }

    vector<int> cycle;
    cycle.push_back(cycle_start);
    for (int cur = cycle_end; cur != cycle_start; cur = par[cur]) {
        cycle.push_back(cur);
    }
    cycle.push_back(cycle_start);
    reverse(cycle.begin(), cycle.end());

    cout << "Cycle found\n";
    for (size_t i = 0; i < cycle.size(); ++i) {
        if (i > 0) cout << ' ';
        cout << cycle[i];
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

The three states are not backtracking choices: a finished vertex becomes state 2, **not** unvisited again.

When a cycle is found, the function returns early and some states remain 1 even as calls unwind. This is intentional: the entire search stops, so those states are never used for another branch. A new call to `solve()` resets all search data.

### Sample 1: The Illustrated Graph

Input:

```text
8 9
1 2
2 3
3 4
2 4
1 5
5 6
6 7
7 8
5 8
```

Output with this neighbour order:

```text
Cycle found
2 3 4 2
```

A different neighbour order could find `5 6 7 8 5`, or print a valid cycle with a different start or orientation. The task accepts any one cycle.

### Sample 2: No Cycle

Input:

```text
4 2
1 2
2 3
```

Output:

```text
No cycle
```

The path `1-2-3` and the isolated vertex 4 are both acyclic. The outer loop checks both components.

### Sample 3: A Cycle in a Later Component

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
Cycle found
3 4 5 3
```

Calling DFS only from 1 would miss this cycle. The outer loop reaches vertex 3 after finishing the first component.

## 8. Why the Algorithm Is Correct

### Every Reported Cycle Is Valid

Detection occurs only on an edge from the current vertex to an active ancestor other than its parent. Following parent links between these endpoints visits distinct vertices on the DFS tree path. Adding the detected edge closes that path.

Skipping the parent edge and excluding self-loops ensures that the cycle contains at least three distinct vertices.

### If a Cycle Exists, DFS Finds One

The DFS tree edges alone cannot contain a cycle. Therefore, a cycle in the original graph contains an edge that is not a tree edge.

In recursive DFS of an undirected graph, such an edge connects an ancestor and a descendant: an edge to an unvisited vertex would have caused that vertex to be explored in the same branch. When its descendant endpoint examines the non-tree edge, the ancestor's call is still active.

That edge triggers detection. Since the outer loop starts DFS in every still-unvisited component, a cycle cannot be missed merely because the graph is disconnected.

## 9. Complexity

- **Time:** \(O(n+m)\). Each vertex is entered at most once, and every undirected edge is examined at most twice. Reconstructing one cycle takes at most \(O(n)\) additional time.
- **Auxiliary space:** \(O(n)\) for states, parents, the recursion stack, and the printed cycle.
- **Total space including adjacency lists:** \(O(n+m)\).

For a long chain, recursive depth can reach \(n\). Large inputs may exceed the environment's call-stack limit; an iterative DFS implementation is preferable when that is a risk.

## 10. Common Mistakes and Scope Checks

- **Treating the parent edge as a cycle:** in an undirected graph, it is the reverse view of the same tree edge.
- **Confusing ancestors and descendants:** the detected back edge goes from the current descendant to an active ancestor.
- **Following parents toward an arbitrary visited neighbour:** that neighbour may be a finished descendant and cannot be reached by walking upward.
- **Failing to propagate success:** returning only from the detecting call lets its callers continue searching. Return `true` through the recursive chain and stop the outer loop too.
- **Tracing all the way to the root:** stop at `cycle_start`; the root need not belong to the cycle.
- **Not closing the printed sequence:** repeat the first vertex at the end so the final edge is explicit.
- **Checking only one component:** a different component may contain the cycle.
- **Expecting all cycles or the shortest cycle:** this implementation returns one DFS-discovered cycle only.

**Parallel-edge caveat:** skipping every neighbour equal to the parent is correct under our simple-graph assumption. If parallel edges are allowed, skip the specific parent **edge ID**, not all edges to the parent vertex; a second parallel edge can form a two-edge cycle under multigraph conventions. That is outside the input model used here.

The parent-edge rule is specifically for **undirected graphs**. Do not apply it unchanged to directed-graph cycle detection.

## Quick Recap

- Tree edges discover new vertices and define parent links.
- A back edge to an active non-parent ancestor closes a cycle.
- Skip the parent edge and distinguish unvisited, active, and finished states.
- Record the back-edge endpoints, follow parents, and close the sequence.
- Stop after one cycle is found; otherwise, check every connected component.

</READING_WIDGET>
