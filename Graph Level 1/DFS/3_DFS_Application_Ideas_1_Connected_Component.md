<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Connected Components

In the previous lesson, we used DFS to visit every vertex of a graph. Whenever the outer loop found an unvisited vertex, it started a new DFS.

For an **undirected graph**, each such starting call explores exactly one connected component. We can use this observation to answer four questions:

- How many connected components are there?
- How many vertices belong to each component?
- Which vertices belong to each component?
- Are two given vertices in the same component?

Throughout this lesson, the graph is **undirected and unweighted**, with vertices numbered from 1 to \(n\). We store each edge in both directions in an adjacency list.

## 1. What Is a Connected Component?

A **connected component** is a maximal group of vertices in which every pair of vertices is connected by a path.

Here, **maximal** means that we cannot add another vertex from the graph to the group while keeping it connected. If a vertex outside the group had a path to a vertex inside it, it would belong to the same component.

Remember:

- Two vertices in the same component do not need a direct edge between them. A path is enough.
- There is no path between vertices in different components.
- Every vertex belongs to exactly one component.
- An isolated vertex forms a component of size 1.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/d3041d27-0547-4103-b25a-e085d58be710.png" alt="Undirected graph with four connected components: vertices 1, 3, 4, 5, 8; vertices 2, 6, 9; vertices 7, 10; and isolated vertex 11" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The illustrated graph has \(n = 11\) vertices and \(m = 8\) edges. Its components are:

| Component | Vertices | Size |
| --- | --- | --- |
| CC1 | \(\{1,3,4,5,8\}\) | 5 |
| CC2 | \(\{2,6,9\}\) | 3 |
| CC3 | \(\{7,10\}\) | 2 |
| CC4 | \(\{11\}\) | 1 |

For example, vertices 1 and 8 are in the same component because the path \(1-3-4-8\) connects them. Vertices 1 and 2 are in different components because no path connects them.

> **Scope check:** This lesson counts connected components of an undirected graph. Following outgoing edges with ordinary DFS in a directed graph does not, by itself, identify strongly connected components.

## 2. Counting the Components

### Key Observation

Starting DFS from an unvisited vertex visits every vertex in its component and cannot leave that component.

After this DFS finishes, any vertex that remains unvisited must belong to a different component. Therefore:

> **Increment the component count only when the outer loop starts DFS from an unvisited vertex.**

Using the single-argument `dfs(node)` and visited array from the previous lesson:

```cpp
int no_of_comp = 0;

for (int node = 1; node <= n; ++node) {
    if (!vis[node]) {
        ++no_of_comp;
        dfs(node);
    }
}

cout << no_of_comp << '\n';
```

Initialize every entry of `vis` to 0 before the loop, and keep the same visited array throughout it.

Do **not** increment the count inside every recursive call. Recursive calls explore more vertices of the current component; they do not necessarily discover a new component.

### Dry Run on the Illustrated Graph

Suppose the outer loop scans labels from 1 to 11:

| Vertex considered by the outer loop | Action | Component count |
| --- | --- | --- |
| 1 | Unvisited: start DFS and visit \(\{1,3,4,5,8\}\). | 1 |
| 2 | Unvisited: start DFS and visit \(\{2,6,9\}\). | 2 |
| 3, 4, 5, 6 | Already visited: skip. | 2 |
| 7 | Unvisited: start DFS and visit \(\{7,10\}\). | 3 |
| 8, 9, 10 | Already visited: skip. | 3 |
| 11 | Unvisited: visit this isolated vertex and return. | 4 |

There are four **starting calls from the outer loop**, so the answer is 4. The sets in the table show membership, not the order of recursive visits.

## 3. Assigning a Component ID to Each Vertex

A Boolean visited marker tells us whether a vertex has been visited, but not **which component it belongs to**.

We can use the same array to store more information:

- `vis[node] = 0`: the vertex is unvisited.
- `vis[node] = c`, where `c > 0`: the vertex belongs to component `c`.

In this version, `vis` acts as both a visited array and a **component-ID array**. Component IDs start at 1 because 0 is reserved for unvisited vertices.

### DFS State and Transition

The function becomes `dfs(node, comp_no)`:

1. Assign `comp_no` to the current vertex.
2. For each unvisited neighbour, recurse with the **same** `comp_no`.
3. Return when there are no more neighbours to explore. Do not clear the assigned ID when returning.

```cpp
void dfs(int node, int comp_no) {
    vis[node] = comp_no;

    for (int v : g[node]) {
        if (!vis[v]) {
            dfs(v, comp_no);
        }
    }
}
```

The outer loop creates a new ID only when it finds an unvisited vertex:

```cpp
int no_of_comp = 0;

for (int node = 1; node <= n; ++node) {
    if (!vis[node]) {
        ++no_of_comp;
        dfs(node, no_of_comp);
    }
}
```

The recursive calls keep the ID fixed. For example, `dfs(1, 1)` assigns ID 1 to every vertex it discovers, not a different ID to each vertex.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/812357ef-9898-40fa-8814-61b2be15a80f.png" alt="Component IDs stored in vis: vertices 1, 3, 4, 5, 8 have ID 1; 2, 6, 9 have ID 2; 7, 10 have ID 3; and 11 has ID 4" style="max-width: 100%; height: auto;" identifier="az-img-upload">

After processing the illustrated graph, the array is:

```text
Vertex:  1  2  3  4  5  6  7  8  9 10 11
vis:     1  2  1  1  1  2  3  1  2  3  4
```

Component IDs are labels assigned by our traversal, not vertex numbers. For example, vertex 2 belongs to component 2, while vertex 3 belongs to component 1.

Changing the order in which the outer loop chooses starting vertices may change the IDs, but it does not change the actual groups of connected vertices.

## 4. Finding the Size of Each Component

Once every vertex has an ID, count how many vertices have each ID:

```cpp
vector<int> comp_size(no_of_comp + 1, 0);

for (int node = 1; node <= n; ++node) {
    ++comp_size[vis[node]];
}
```

For each vertex, `vis[node]` tells us which counter to increment. For example:

- Vertex 1 has ID 1, so it contributes to `comp_size[1]`.
- Vertex 2 has ID 2, so it contributes to `comp_size[2]`.
- Vertex 3 also has ID 1, so it contributes to `comp_size[1]`.

For our graph:

```text
comp_size[1] = 5
comp_size[2] = 3
comp_size[3] = 2
comp_size[4] = 1
```

Index 0 is unused because all vertices have received positive IDs before this counting pass.

We use `vector<int>` because the number of components is known at runtime. A declaration such as `int comp_size[no_of_comp + 1]` is a variable-length array and is **not standard C++**.

**Sanity check:** Every vertex belongs to exactly one component, so the sizes must sum to \(n\):

$$
\sum_{c=1}^{\text{no\_of\_comp}} \text{comp\_size}[c]
= 5+3+2+1 = 11
$$

## 5. Collecting the Vertices of Each Component

To keep the actual members, create one vector for each component and put every vertex into the vector indicated by its ID:

```cpp
vector<vector<int>> comp_set(no_of_comp + 1);

for (int node = 1; node <= n; ++node) {
    comp_set[vis[node]].push_back(node);
}
```

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/2ad76dc3-782a-4cc3-9c03-cbf0cca986f5.png" alt="Component member lists: comp_set[1] is [1,3,4,5,8], comp_set[2] is [2,6,9], comp_set[3] is [7,10], and comp_set[4] is [11]" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Despite the name `comp_set`, this is a **vector of vectors**, not a C++ `set`. Every vertex is inserted exactly once because the loop processes each label once.

The lists are in increasing vertex-label order because this grouping loop scans from 1 to \(n\). They are **not necessarily in DFS discovery order**.

For each component `c`, `comp_set[c].size()` equals `comp_size[c]`. If a problem needs only one of these representations, there is no need to store the other.

## 6. Are Two Vertices in the Same Component?

After labelling the entire graph, vertices `x` and `y` are connected if and only if their component IDs match:

```cpp
int x, y;
cin >> x >> y;

if (vis[x] == vis[y]) {
    cout << "Same Component\n";
} else {
    cout << "Different Component\n";
}
```

For the example:

| Query | IDs compared | Result |
| --- | --- | --- |
| \(x=1,\ y=8\) | \(1=1\) | Same component |
| \(x=2,\ y=7\) | \(2\ne3\) | Different components |
| \(x=7,\ y=10\) | \(3=3\) | Same component |
| \(x=11,\ y=11\) | \(4=4\) | Same component |

An isolated vertex is connected to itself by a path of length zero.

> **Important:** Perform this comparison only after component labelling is complete. Before traversal, two unvisited vertices both have ID 0; equal zeros do not prove that they are connected.

Each query now takes \(O(1)\) time. We do not run a new DFS for every pair of vertices. These IDs describe the graph that was processed; if its edges change, the stored component information may no longer be valid.

## 7. Complete C++ Implementation

This program combines counting, labelling, sizes, member lists, and connectivity queries. It assumes valid vertex labels from 1 to \(n\).

### Input Format for This Example

- The first line contains `n m`.
- The next `m` lines contain undirected edges `u v`.
- The next line contains the number of queries `q`.
- Each of the next `q` lines contains vertices `x y`.

### Output Format for This Example

- First line: the number of components.
- Second line: component sizes in ID order.
- Next `no_of_comp` lines: the vertices in each component, in ID order.
- Remaining lines: `Same Component` or `Different Component` for each query.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g;
vector<int> vis;  // 0 = unvisited; positive value = component ID.

void dfs(int node, int comp_no) {
    vis[node] = comp_no;

    for (int v : g[node]) {
        if (!vis[v]) {
            dfs(v, comp_no);
        }
    }
}

void solve() {
    int n, m;
    cin >> n >> m;

    g.assign(n + 1, vector<int>());
    vis.assign(n + 1, 0);

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
            dfs(node, no_of_comp);
        }
    }

    vector<int> comp_size(no_of_comp + 1, 0);
    vector<vector<int>> comp_set(no_of_comp + 1);

    for (int node = 1; node <= n; ++node) {
        int id = vis[node];
        ++comp_size[id];
        comp_set[id].push_back(node);
    }

    cout << no_of_comp << '\n';

    for (int id = 1; id <= no_of_comp; ++id) {
        if (id > 1) cout << ' ';
        cout << comp_size[id];
    }
    cout << '\n';

    for (int id = 1; id <= no_of_comp; ++id) {
        for (int j = 0; j < static_cast<int>(comp_set[id].size()); ++j) {
            if (j > 0) cout << ' ';
            cout << comp_set[id][j];
        }
        cout << '\n';
    }

    int q;
    cin >> q;
    while (q--) {
        int x, y;
        cin >> x >> y;
        cout << (vis[x] == vis[y] ? "Same Component" : "Different Component")
             << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

### Sample Input

The edges below reproduce the graph shown in all three images.

```text
11 8
1 3
1 5
3 4
4 8
5 8
2 6
6 9
7 10
4
1 8
2 7
7 10
11 11
```

### Sample Output

```text
4
5 3 2 1
1 3 4 5 8
2 6 9
7 10
11
Same Component
Different Component
Same Component
Same Component
```

For this input order, `dfs(1, 1)` discovers vertices in the order `1, 3, 4, 8, 5`. The later grouping loop produces `[1, 3, 4, 5, 8]` because it scans vertex labels in increasing order. Both describe the same component.

## 8. Why Does the Method Work?

Consider a DFS started by the outer loop at an unvisited vertex `s`:

1. **It cannot label a vertex outside `s`'s component.** Every recursive step follows an edge, so every vertex it reaches has a path from `s`.
2. **It labels every vertex in that component.** DFS checks all neighbours of each discovered vertex. If a reachable vertex remained unvisited, a path to it would contain an edge from a visited vertex to an unvisited vertex, which DFS would have explored.
3. **The component is counted once.** After that DFS finishes, all vertices in the component are marked. The outer loop skips them and starts another DFS only in a different component.

Thus, each component gets exactly one ID. Counting or collecting vertices with that ID gives its size and members, and comparing IDs correctly answers connectivity queries.

## 9. Complexity

Let \(n\) be the number of vertices, \(m\) the number of undirected edges, and \(q\) the number of queries.

- **Component labelling:** \(\Theta(n+m)\). Each vertex is visited once and the adjacency lists contain \(2m\) entries in total.
- **Counting sizes and collecting members:** \(\Theta(n)\). Each vertex contributes to exactly one component.
- **Each connectivity query:** \(O(1)\).
- **Total time for the complete program:** \(O(n+m+q)\), including printing all component members and query answers.

The graph uses \(O(n+m)\) space. Component IDs, sizes, member lists, and the recursion stack together use \(O(n)\) additional space.

Although `comp_set` is a vector of vectors, it stores **\(n\) vertices in total**, not \(n\) vertices for every component.

> **CP / interview caution:** A large component may contain a long DFS chain, so recursive DFS can exhaust the call stack. The same component-labelling idea can be implemented with an explicit stack when recursion depth is a concern.

## 10. Common Mistakes and Quick Checks

- **Counting every recursive call as a component:** increase the count only for a new DFS started by the outer loop.
- **Using ID 0 for a component:** reserve 0 for unvisited vertices and start real IDs at 1.
- **Changing the ID during recursion:** pass the same `comp_no` to every recursive call in that traversal.
- **Clearing IDs on return:** component membership must remain recorded after DFS finishes.
- **Ignoring isolated vertices:** scan all labels, not just vertices appearing in the edge input.
- **Using a Boolean array for component IDs:** IDs may exceed 1, so use an integer array or vector.
- **Comparing IDs before labelling is complete:** two zeros mean unvisited, not connected.

Useful checks for a nonempty graph:

- \(1 \leq \text{no\_of\_comp} \leq n\).
- A connected graph has one component of size \(n\).
- A graph with no edges has \(n\) components, each of size 1.
- All component sizes sum to \(n\), and every vertex appears in exactly one member list.

## Quick Recap

- One DFS from an unvisited vertex explores one connected component of an undirected graph.
- Count the new starting calls to find the number of components.
- Store the component ID in `vis` to record both visitation and membership.
- Count or group vertices by ID to obtain component sizes and member lists.
- After preprocessing, equal IDs mean that two vertices are connected.

</READING_WIDGET>
