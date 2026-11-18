<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Nodes at Distance K from a Given Node in a Binary Tree

Finding nodes at a particular depth from the root is a level-order traversal problem. But what changes when the starting node can be **any node in the tree**?

The required nodes may lie below the target, above it, or in another branch reached through an ancestor. Child pointers alone cannot take us along all these paths.

The standard solution adds the missing direction: **use DFS to record every node's parent, then run BFS from the target**. Each BFS layer contains nodes one edge farther from the target. We stop at layer `K` and return that layer.

## 1. Problem Statement and Conventions

Given the root of a binary tree, a pointer to a target node, and an integer `K`, return the values of all nodes whose distance from the target is **exactly `K` edges**.

The distance between two nodes is the number of edges on their unique connecting path. In particular, the distance from a node to itself is `0`.

Assume that:

- The input is a finite binary tree with no cycles or shared child nodes.
- The tree is not necessarily a binary search tree.
- Nodes may contain repeated values. The target is identified by its **pointer**, not its value.
- Every edge contributes a distance of `1`.
- We must leave the tree unchanged.
- Results may be returned in any order unless the problem explicitly requires sorting.

The implementations in this lesson return an empty vector for an empty tree, a null target, a negative `K`, or a target that does not belong to the tree.

Let `n` be the number of nodes, `h` the height measured in nodes, and `m` the number of nodes in the answer. Auxiliary space excludes the input and returned answer, but includes recursion stacks and temporary containers. The code uses C++17 and assumes node counts and distances fit in an `int`.

### Single-Source or Multi-Source BFS?

For this problem, the queue initially contains **one target node**, so the traversal is **single-source BFS**. Exploring its left child, right child, and parent does not make it multi-source.

Multi-source BFS is the extension in which several starting nodes are placed in the queue at distance `0`. It computes each node's distance to the **nearest source**. We discuss that extension near the end of the lesson.

## 2. Running Example

Consider the following tree, with target node `5` and `K = 2`:

```text
            3
           / \
          5   1
         / \ / \
        6  2 0  8
          / \
         7   4
```

Group the nodes by their distance from `5`:

| Distance | Nodes | How they are reached |
| --- | --- | --- |
| `0` | `5` | The target itself |
| `1` | `6`, `2`, `3` | One move to a child or parent |
| `2` | `7`, `4`, `1` | `5 -> 2 -> 7`, `5 -> 2 -> 4`, `5 -> 3 -> 1` |
| `3` | `0`, `8` | Continue through node `1` |

The answer is **`[7, 4, 1]`**, in any order.

Node `1` is the important case: it is not in the target's subtree. A downward-only traversal starting at `5` would find `7` and `4` but miss `1`.

Also, node `5` is not part of the answer for `K = 2`. Walking `5 -> 6 -> 5` takes two steps, but it repeats a node. The distance from `5` to itself remains `0`; the problem asks for distance, not arbitrary walks of length `K`.

## 3. View the Tree as an Undirected Graph

Although the stored pointers point from parents to children, a tree edge can be traversed in either direction when measuring distance.

From a node `cur`, the possible neighbors are:

```text
cur->left
cur->right
parent[cur]
```

We already have the first two pointers. We only need a map that supplies the third:

```text
parent[child] = its parent node
parent[root] = nullptr
```

There is no need to construct a separate adjacency list. The two child pointers and the parent map together describe every neighbor.

### Why Use BFS?

All edges have the same cost, so BFS visits nodes in increasing order of distance from its starting node:

```text
Layer 0: distance 0 from target
Layer 1: distance 1 from target
Layer 2: distance 2 from target
...
Layer K: exactly the required nodes
```

The layers are measured from the **target**, not from the original root. Nodes at the same depth from the root do not necessarily have the same distance from the target.

## 4. Step 1: Build the Parent Map Using DFS

Pass both the current node and its parent into a recursive DFS:

1. If the current node is null, return.
2. Record its parent in the map.
3. Visit its left child, passing the current node as the parent.
4. Visit its right child in the same way.

For the running example, the completed map is:

| Node | Parent |
| --- | --- |
| `3` | `nullptr` |
| `5` | `3` |
| `1` | `3` |
| `6` | `5` |
| `2` | `5` |
| `0` | `1` |
| `8` | `1` |
| `7` | `2` |
| `4` | `2` |

These table entries use values as readable labels because the example has distinct values. The actual map uses **node pointers as keys**.

Recording the root with a null parent has another benefit: after DFS, every node belonging to the tree appears in the map. We can therefore check whether the supplied target is present before starting BFS.

## 5. Step 2: Run BFS from the Target

Initialize:

```text
queue = [target]
visited = {target}
distance = 0
```

To move from one layer to the next:

1. Save the current queue size.
2. Remove exactly that many nodes.
3. For each removed node, examine its left child, right child, and parent.
4. Enqueue each non-null neighbor that has not been visited, marking it visited immediately.
5. Increment the distance after the entire layer is processed.

Stop when the distance reaches `K` or the queue becomes empty.

### Why Save the Queue Size?

The queue grows as we add the next layer. If we keep processing until it is empty, we mix several distances into one iteration.

Saving `levelSize = q.size()` fixes the number of nodes in the current layer. Nodes added during that iteration belong to the next layer and must wait.

### Why Track Visited Nodes in a Tree?

The underlying undirected graph is still a tree, but adding access to parents allows us to immediately reverse an edge:

```text
5 -> 6 -> 5 -> 6 -> ...
```

Visited tracking prevents these repeated walks and ensures every node enters the queue at most once. It also prevents the target from appearing again at a positive distance.

Mark nodes visited **when enqueuing them**, so a queued node already counts as discovered.

### Stop Before Expanding Layer K

At the beginning of a BFS iteration, the queue contains exactly the nodes at the current distance.

Once `distance == K`, the queue is already the answer. Expanding it would move to distance `K + 1`, which we do not need.

For `K = 0`, no BFS expansion is required: the initial queue contains the target itself.

## 6. C++ Implementation: Parent Map and BFS

The following headers, node definition, and functions can be combined with the `main` below to form a complete C++17 program.

```cpp
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value)
        : data(value), left(nullptr), right(nullptr) {}
};

void buildParents(Node* cur, Node* par,
                  unordered_map<Node*, Node*>& parent) {
    if (cur == nullptr) return;

    parent[cur] = par;
    buildParents(cur->left, cur, parent);
    buildParents(cur->right, cur, parent);
}

vector<int> nodesAtDistanceK(Node* root, Node* target, int k) {
    vector<int> answer;
    if (root == nullptr || target == nullptr || k < 0) {
        return answer;
    }

    unordered_map<Node*, Node*> parent;
    buildParents(root, nullptr, parent);

    // Compare node identities and reject a target outside this tree.
    if (parent.find(target) == parent.end()) return answer;

    queue<Node*> q;
    unordered_set<Node*> visited;
    q.push(target);
    visited.insert(target);

    int distance = 0;

    while (!q.empty() && distance < k) {
        int levelSize = static_cast<int>(q.size());

        for (int i = 0; i < levelSize; ++i) {
            Node* cur = q.front();
            q.pop();

            Node* neighbors[] = {
                cur->left, cur->right, parent.at(cur)
            };

            for (Node* next : neighbors) {
                if (next != nullptr && visited.insert(next).second) {
                    q.push(next);
                }
            }
        }

        ++distance;
    }

    // If exploration ended too early, no node is at distance k.
    if (distance != k) return answer;

    while (!q.empty()) {
        answer.push_back(q.front()->data);
        q.pop();
    }

    return answer;
}
```

`visited.insert(next).second` is true only when `next` was newly inserted. This performs both the membership check and the visited update.

`parent.at(cur)` reads an existing map entry without inserting a new one. It is safe here because every queued node belongs to the tree and DFS recorded all such nodes, including the root.

The algorithm tracks pointers internally and returns values at the end. If two different answer nodes both contain `7`, the result correctly contains two copies of `7`. If a caller needs node identities, return a `vector<Node*>` instead.

### Building and Running the Example

```cpp
int main() {
    Node n3(3), n5(5), n1(1), n6(6), n2(2);
    Node n0(0), n8(8), n7(7), n4(4);

    n3.left = &n5;
    n3.right = &n1;
    n5.left = &n6;
    n5.right = &n2;
    n1.left = &n0;
    n1.right = &n8;
    n2.left = &n7;
    n2.right = &n4;

    vector<int> answer = nodesAtDistanceK(&n3, &n5, 2);
    for (int value : answer) cout << value << ' ';
    cout << '\n';

    return 0;
}
```

Output:

```text
7 4 1
```

This order follows the implementation's left-child, right-child, parent neighbor order. Other valid BFS neighbor orders may produce a different order of the same answer nodes.

The nodes are local objects that remain alive throughout the call. No dynamic allocation or manual deletion is needed for this example.

## 7. Dry Run: Target 5, K = 2

After the parent-map DFS:

```text
queue = [5]
visited = {5}
distance = 0
```

### Expand Distance 0

The saved layer size is `1`.

| Removed node | Neighbors considered | Newly enqueued |
| --- | --- | --- |
| `5` | Left `6`, right `2`, parent `3` | `6`, `2`, `3` |

After processing that layer:

```text
queue = [6, 2, 3]
visited = {5, 6, 2, 3}
distance = 1
```

### Expand Distance 1

The saved layer size is now `3`.

| Removed node | Neighbors considered | Newly enqueued | Queue afterward |
| --- | --- | --- | --- |
| `6` | Two null children; parent `5` already visited | None | `[2, 3]` |
| `2` | Children `7`, `4`; parent `5` already visited | `7`, `4` | `[3, 7, 4]` |
| `3` | Child `5` already visited; child `1`; null parent | `1` | `[7, 4, 1]` |

After processing that layer:

```text
queue = [7, 4, 1]
visited = {5, 6, 2, 3, 7, 4, 1}
distance = 2
```

Now `distance == K`. We collect the queue without expanding it, giving **`[7, 4, 1]`**.

Nodes `0` and `8` are not enqueued by this BFS because they are three edges from the target. The earlier parent-map DFS did visit them; BFS stopping early does not remove the cost of that preprocessing.

## 8. Why the Algorithm Is Correct

First, DFS records the correct parent of every node. Therefore, a node's left child, right child, and recorded parent describe all its adjacent nodes in the tree.

Now consider the BFS invariant:

> At the start of each layer, the queue contains exactly the nodes at the current distance from the target, each appearing once.

Initially, the queue contains only the target, whose distance is `0`.

Suppose the invariant holds at distance `d`. An unvisited neighbor of a node in this layer has distance at most `d + 1`. It cannot have a smaller distance: BFS would already have discovered it in an earlier layer or the current layer. Thus, it has distance exactly `d + 1`.

Conversely, every node at distance `d + 1` has a preceding node at distance `d` on its path from the target. Processing that preceding node discovers it. Marking on enqueue prevents duplicates.

The invariant therefore holds for the next layer. When the distance reaches `K`, the queue contains exactly the required nodes. If the queue becomes empty first, no farther reachable nodes remain, so the answer is empty.

## 9. Complexity Analysis

### Time Complexity

The parent-map DFS visits all `n` nodes. BFS enqueues each node at most once and checks at most three neighbors per processed node.

With expected constant-time operations in `unordered_map` and `unordered_set`:

```text
Parent-map construction: O(n)
BFS:                     O(n) in the worst case
Collecting the answer:   O(m)
Total expected time:     O(n)
```

Even when `K` is small, this implementation builds the entire parent map first. For a non-null target and nonnegative `K`, it therefore takes expected `O(n)` time, including when `K = 0`. That also lets it validate target membership.

Hash-container operations are expected constant time, not guaranteed constant time. Pathological collisions can make the total time `O(n^2)`. The usual interview bound of `O(n)` assumes expected hash performance. Ordered maps and sets give deterministic `O(n log n)` time; indexed arrays can give deterministic `O(n)` time when nodes already have suitable unique indices.

### Space Complexity

| Storage | Worst-case size |
| --- | --- |
| Parent map | `O(n)` |
| Visited set | `O(n)` |
| BFS queue | `O(n)` |
| Parent-map DFS call stack | `O(h)` |
| Returned answer | `O(m)` |

Total auxiliary space is **`O(n)`**, with another `O(m)` for the returned answer. Including the output, the overall extra space remains `O(n)` because `m <= n`.

The queue can contain a linear number of nodes in a broad tree; it is not bounded by the tree's height. In a skewed tree, `h` can be `n`, so the recursive parent-building step may exhaust the call stack. An explicit DFS stack is a practical replacement for that step when inputs are very deep.

## 10. Alternative: Recursive DFS Without a Parent Map

We can avoid the parent map, queue, and visited set by using recursive return values to carry the distance to the target upward.

Every answer node belongs to one of these groups:

1. A descendant of the target.
2. An ancestor of the target.
3. A node in the opposite subtree of some ancestor on the root-to-target path.

The recursive approach handles these groups directly.

### Helper 1: Collect Nodes at a Downward Distance

Define `collectDown(cur, remaining)` to collect nodes exactly `remaining` edges below `cur`:

- If `cur` is null or `remaining < 0`, stop.
- If `remaining == 0`, append `cur` and stop this branch.
- Otherwise, recurse into both children with `remaining - 1`.

### Helper 2: Return the Distance to the Target

Define `findDistance(cur)` to return:

```text
-1: target does not occur in cur's subtree
 0 or more: distance from cur to target
```

If `cur == target`, collect nodes `K` edges below it and return `0`.

Otherwise, search the left subtree. Suppose it returns `leftDistance >= 0`. Then:

```text
Distance from cur to target = leftDistance + 1
```

If this equals `K`, add `cur` itself. Otherwise, an answer in the right subtree must be reached by moving from the target up to `cur`, then down one edge to `cur->right`:

```text
target -> ... -> cur -> cur->right -> ... -> answer

Distance used before reaching cur->right = leftDistance + 2
Remaining downward distance             = K - leftDistance - 2
```

Collect nodes at that remaining distance in the right subtree. A negative remaining distance simply produces no nodes.

If the target is found in the right subtree instead, apply the symmetric logic to the left subtree.

### C++ Implementation

Use the same `Node` definition and headers from the BFS implementation:

```cpp
void collectDown(Node* cur, int remaining, vector<int>& answer) {
    if (cur == nullptr || remaining < 0) return;

    if (remaining == 0) {
        answer.push_back(cur->data);
        return;
    }

    collectDown(cur->left, remaining - 1, answer);
    collectDown(cur->right, remaining - 1, answer);
}

int findDistance(Node* cur, Node* target, int k,
                 vector<int>& answer) {
    if (cur == nullptr) return -1;

    if (cur == target) {
        collectDown(cur, k, answer);
        return 0;
    }

    int leftDistance = findDistance(cur->left, target, k, answer);
    if (leftDistance != -1) {
        int distance = leftDistance + 1;

        if (distance == k) {
            answer.push_back(cur->data);
        } else if (distance < k) {
            collectDown(cur->right, k - distance - 1, answer);
        }

        return distance;
    }

    int rightDistance = findDistance(cur->right, target, k, answer);
    if (rightDistance != -1) {
        int distance = rightDistance + 1;

        if (distance == k) {
            answer.push_back(cur->data);
        } else if (distance < k) {
            collectDown(cur->left, k - distance - 1, answer);
        }

        return distance;
    }

    return -1;
}

vector<int> nodesAtDistanceKDFS(Node* root, Node* target, int k) {
    vector<int> answer;
    if (root == nullptr || target == nullptr || k < 0) {
        return answer;
    }

    findDistance(root, target, k, answer);
    return answer;
}
```

The code uses `k - distance - 1`, where `distance` is already the distance from the current node to the target. This is the same as `k - leftDistance - 2` or its right-subtree equivalent.

If the target is absent, every search returns `-1`. No downward collection is triggered, so the answer remains empty. Each query also starts with a fresh answer vector; there is no persistent global state.

### Dry Run on the Same Example

For target `5` and `K = 2`:

| Current node | Action | Result |
| --- | --- | --- |
| `5` | Target found; collect nodes `2` edges below it | Add `7`, `4`; return distance `0` |
| `3` | Left child returned `0`, so target is `1` edge away | Current node is too close to be an answer |
| `3` | Enter the opposite subtree at node `1` with remaining distance `2 - 1 - 1 = 0` | Add `1`; return distance `1` |

The answer is again **`[7, 4, 1]`**.

For `K = 1`, node `5` collects its children `6` and `2`, and node `3` adds itself because its distance to the target is exactly `1`.

### Why Does This Stay O(n)?

It may appear that launching `collectDown` from several ancestors creates quadratic work. However, the target's subtree and the opposite subtrees along its ancestor path are **disjoint**.

The search helper visits each node at most once. The collection helpers together visit each node at most once more. Some nodes may first be searched unsuccessfully and later visited during collection, but that is only a constant number of visits per node.

Therefore:

- **Time:** `O(n)` in the worst case, without relying on hashing.
- **Auxiliary space:** `O(h)` for recursion, excluding the `O(m)` output.
- **Skewed-tree space:** `O(n)` because `h` may equal `n`.

The active search frames and a downward collection follow a root-to-descendant route, so their combined stack depth is still `O(h)`. Each answer is added once: descendants, qualifying ancestors, and opposite-subtree nodes belong to separate groups.

### Comparing the Approaches

| Approach | Time | Auxiliary space | Main idea |
| --- | --- | --- | --- |
| DFS parent map + BFS | Expected `O(n)` | `O(n)` | Explore neighbors in distance layers |
| Recursive DFS only | `O(n)` | `O(h)` | Return target distance and search opposite subtrees |

The BFS approach makes distance layers explicit and is straightforward to extend to multiple sources. The DFS-only approach reduces auxiliary storage in a balanced tree but requires careful distance arithmetic and recursion management.

## 11. Edge Cases and Common Mistakes

| Case | Expected behavior |
| --- | --- |
| Empty tree | Return an empty vector |
| Null target or target outside the tree | Return an empty vector |
| Negative `K` | Return an empty vector under this lesson's convention |
| `K = 0`, target exists | Return only the target's value |
| Single-node tree | Return its value for `K = 0`; otherwise return empty |
| Target is the root | Find nodes at depth `K` from the root |
| Target is a leaf | Allow upward moves and entry into other branches |
| `K` exceeds every distance from the target | Return an empty vector |
| Different nodes contain the same value | Track them separately by pointer; repeated output values are valid |
| Tree is a long chain | Count edges correctly and account for recursion depth |

In the running example, target `5` with `K = 4` gives an empty answer because its farthest nodes, `0` and `8`, are only three edges away. With target `7` and `K = 2`, the answer is `[4, 5]` in any order.

Common mistakes include:

- **Searching only the target's descendants.** Answers may require moving through a parent and into another branch.
- **Counting nodes instead of edges.** The target starts at distance `0`, not `1`.
- **Collecting every node within distance K.** Only the final layer belongs in an exact-distance answer.
- **Omitting visited tracking in BFS.** Parent access allows backtracking along the same edge.
- **Using values as visited keys.** Equal values can belong to different nodes.
- **Expanding the layer at distance K.** Its nodes already form the answer.
- **Using a changing queue size as the layer boundary.** Save the size before adding the next layer.
- **Subtracting only one edge for an opposite subtree.** If distance is measured from the child containing the target, reaching the opposite child uses two additional edges.
- **Claiming the DFS-only method uses constant space.** Its recursion stack uses `O(h)` space.

## 12. Interview and Competitive Programming Insights

### Explain the Missing Direction First

A useful interview explanation is: “Distance is measured along tree edges in either direction, but the input stores only child pointers. I will record parents, then run BFS from the target and return the nodes in layer `K`.”

This connects the data structure limitation directly to the algorithm. No BST ordering is needed, and node values do not influence traversal decisions.

### Clarify Node Identity and Output Order

If the input gives a target value instead of a pointer, determine whether values are unique. When duplicates are allowed, a value alone may not identify one node.

Do not sort the answer unless required. If sorted values are required, sorting `m` results adds `O(m log m)` time. The BFS order is not a sorted-value guarantee.

### Multi-Source BFS Is a Related Follow-Up

Suppose several existing target nodes are given and the task asks for nodes whose **minimum distance to any target** is exactly `K`.

After building the same parent map:

1. Insert all distinct source pointers into the visited set.
2. Enqueue those sources at distance `0`.
3. Run the same layer-by-layer BFS and collect layer `K`.

Sources spread simultaneously, and the first discovery of a node gives its distance to the nearest source. The expected time and auxiliary space remain `O(n)` for tree traversal, plus the time to read the source list.

This answers a different question from “distance `K` from at least one source.” A node can be `K` edges from one source but closer to another; multi-source BFS assigns it the smaller distance and excludes it from layer `K`. It also does not directly find nodes that are exactly `K` edges from **every** source.

### A Previous-Node Pointer Can Replace Visited in a Tree

Because a tree has a unique path between nodes, a single-source traversal can carry `(current, previous)` and skip the neighbor it just came from. There is no alternate route that can revisit a node.

This can remove the visited set for the single-source tree problem. The standard visited-set version remains a clear choice and extends naturally to general graphs and multiple sources. A previous-node check alone is not sufficient for those extensions.

### Reuse Preprocessing for Repeated Queries

For many queries on an unchanged tree, build the parent map once and reuse it. Each query still needs fresh BFS state, and one query can still explore `O(n)` nodes. For `Q` queries, the worst-case expected time remains `O(n + Qn)`.

Preprocessing does not remove the cost of reporting the answer: returning `m` nodes always takes at least `O(m)` time. Counting answers and listing all answer nodes are different tasks and may justify different techniques.

### Connect the Problem to LCA and Spreading Processes

From the LCA lesson, with depths measured in edges:

```text
distance(u, v) = depth(u) + depth(v) - 2 * depth(LCA(u, v))
```

This formula is useful for checking individual pair distances. Applying it separately to every candidate node is unnecessary for the single-target problem: BFS directly groups all nodes by distance.

The same layers also describe a process spreading one edge per time unit. Layer `K` contains nodes first reached at time `K`; continuing until all nodes are visited gives the time needed to reach the whole tree. The relevant value is the farthest distance from the chosen target, which need not equal the tree's diameter.

## Quick Recap

- Distance counts **edges**, so the target is at distance `0`.
- Build a parent-pointer map with DFS to enable upward traversal without modifying the tree.
- Run single-source BFS from the target, tracking visited node pointers and processing one complete layer at a time.
- Stop at distance `K` and collect that layer: expected `O(n)` time and `O(n)` auxiliary space, including preprocessing.
- A recursive DFS-only alternative returns the distance to the target and collects nodes from the appropriate subtrees: `O(n)` time and `O(h)` auxiliary space.
- Multiple starting targets lead to multi-source BFS, which measures distance to the **nearest** target.

</READING_WIDGET>
