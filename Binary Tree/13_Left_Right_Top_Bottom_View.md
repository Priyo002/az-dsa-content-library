<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Left View, Right View, Top View and Bottom View of a Binary Tree

A level-order traversal visits every node of a binary tree. But if we look at the tree from one direction, some nodes hide others. Which nodes remain visible?

The answer depends on the direction. From the left or right, we select one node from each **level**. From the top or bottom, we select one node from each **vertical column**.

We will turn these visibility rules into precise selection rules, then implement all four views using breadth-first search (BFS).

## 1. Problem Statement and Conventions

Given the root of a binary tree, return its four views as separate sequences of node values:

| View | Which node do we select? | Output order |
| --- | --- | --- |
| Left view | Leftmost node at each depth | Top to bottom |
| Right view | Rightmost node at each depth | Top to bottom |
| Top view | Shallowest node at each horizontal distance | Leftmost column to rightmost column |
| Bottom view | Deepest node at each horizontal distance | Leftmost column to rightmost column |

Assume that:

- The input is a finite binary tree with no cycles or shared child nodes.
- An empty tree produces an empty sequence for every view.
- Node values may repeat. Visibility depends on positions, not values.
- The tree must remain unchanged.
- BFS enqueues the **left child before the right child**.

For top and bottom views, two nodes can have the same horizontal distance and depth. We use these tie rules:

- **Top view:** keep the node encountered first in left-to-right level order.
- **Bottom view:** keep the node encountered last in left-to-right level order.

Check the problem statement for its required tie rule. In particular, a bottom-view problem may specify which node wins when two nodes occupy the same coordinates.

Let `n` be the number of nodes, `h` the number of levels, `w` the maximum number of nodes on any level, and `k` the number of distinct horizontal distances. For an empty tree, all four quantities are zero.

## 2. A Running Example

Consider this tree:

```text
                 1
          /             \
         2               3
      /     \         /     \
     4       5       6       7
              \     /
               8   9
```

Here, **`8` is the right child of `5`, and `9` is the left child of `6`**. The drawing separates branches for readability; we will assign horizontal distances explicitly for the top and bottom views.

For clarity, the complete child relationships are:

| Node | Left child | Right child |
| --- | --- | --- |
| `1` | `2` | `3` |
| `2` | `4` | `5` |
| `3` | `6` | `7` |
| `5` | None | `8` |
| `6` | `9` | None |
| `4`, `7`, `8`, `9` | None | None |

Its levels, in left-to-right order, are:

```text
Depth 0: 1
Depth 1: 2, 3
Depth 2: 4, 5, 6, 7
Depth 3: 8, 9
```

The four answers are:

```text
Left view:   1, 2, 4, 8
Right view:  1, 3, 7, 9
Top view:    4, 2, 1, 3, 7
Bottom view: 4, 9, 6, 8, 7
```

We will derive each answer separately. Notice that the left view continues with `8` even though `4` has no children. A view is not simply a path obtained by following left or right child pointers.

## 3. Shared C++ Setup

All implementations use C++17. Combine the following setup, the four view functions, and the later demonstration `main` to form a complete program.

```cpp
#include <cstddef>
#include <iostream>
#include <map>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value)
        : data(value), left(nullptr), right(nullptr) {}
};
```

The functions return values rather than printing during traversal. This keeps the algorithms usable in an online judge or another part of a program.

## 4. Left View: The First Node of Every Level

### Key Observation

When BFS processes each level from left to right, the **first node at that level** belongs to the left view.

The queue already gives us level order. We only need to identify where each level starts and ends.

### Approach

1. Return an empty vector if the root is null.
2. Push the root into a queue.
3. At the start of a level, save the current queue size as `levelSize`.
4. Pop exactly `levelSize` nodes. Add the first one to the answer.
5. For each popped node, enqueue its left child and then its right child, if present.
6. Repeat until the queue is empty.

**Save the queue size before processing the level.** Its size changes as we remove current-level nodes and add next-level nodes. Rechecking `q.size()` as the loop bound would mix the level boundaries.

### C++ Implementation

```cpp
vector<int> leftView(Node* root) {
    vector<int> answer;
    if (root == nullptr) return answer;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        size_t levelSize = q.size();

        for (size_t i = 0; i < levelSize; ++i) {
            Node* current = q.front();
            q.pop();

            if (i == 0) {
                answer.push_back(current->data);
            }

            if (current->left != nullptr) q.push(current->left);
            if (current->right != nullptr) q.push(current->right);
        }
    }

    return answer;
}
```

### Dry Run

At the start of each outer-loop iteration, the queue contains exactly the next level in left-to-right order.

| Depth | Queue at level start | `levelSize` | First node selected | Answer after this level |
| --- | --- | --- | --- | --- |
| `0` | `[1]` | `1` | `1` | `[1]` |
| `1` | `[2, 3]` | `2` | `2` | `[1, 2]` |
| `2` | `[4, 5, 6, 7]` | `4` | `4` | `[1, 2, 4]` |
| `3` | `[8, 9]` | `2` | `8` | `[1, 2, 4, 8]` |

At depth `2`, node `4` contributes no children, node `5` contributes `8`, node `6` contributes `9`, and node `7` contributes none. The next level is therefore `[8, 9]`, and its first node is `8`.

### Why Is It Correct?

The root is the only node at depth zero, so the initial queue has the correct order.

If a level is processed from left to right, appending each node's left child before its right child produces the next level in left-to-right order. Saving `levelSize` ensures that we finish the current level before processing any of those children.

Therefore, the first popped node of every level is exactly its leftmost node. Selecting it gives the left view in top-to-bottom order.

### Complexity

- **Time:** `O(n)`, since every node is enqueued and dequeued once.
- **Auxiliary space, excluding the answer:** `O(w)` for the queue.
- **Output space:** `O(h)`, because the view contains one value per level.
- **Space including the answer:** `O(w + h)`.

During a level, the queue can contain parts of two adjacent levels. Their combined size is at most `2w`, so the queue bound remains `O(w)`.

### Edge Cases

- **Empty tree:** returns `[]`.
- **Single node `x`:** returns `[x]`.
- **A chain, even one that alternates left and right:** every level has one node, so all nodes appear from root to leaf.
- **The left subtree ends before the right subtree:** deeper nodes from the right subtree may enter the left view. Do not restrict traversal to the root's left subtree.

## 5. Right View: The Last Node of Every Level

### Key Observation

With the same left-to-right BFS, the **last node at each level** belongs to the right view.

There is no need to reverse the final left-view sequence. Reversal changes the order of the selected nodes; it does not select the other end of each level.

### Approach

Use the same level boundaries as before. For a level containing `levelSize` nodes, select the node whose index is `levelSize - 1`.

Continue enqueuing left children before right children so that the last processed node really is the rightmost one.

### C++ Implementation

```cpp
vector<int> rightView(Node* root) {
    vector<int> answer;
    if (root == nullptr) return answer;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        size_t levelSize = q.size();

        for (size_t i = 0; i < levelSize; ++i) {
            Node* current = q.front();
            q.pop();

            if (i == levelSize - 1) {
                answer.push_back(current->data);
            }

            if (current->left != nullptr) q.push(current->left);
            if (current->right != nullptr) q.push(current->right);
        }
    }

    return answer;
}
```

### Dry Run

| Depth | Nodes processed | Last node selected | Answer after this level |
| --- | --- | --- | --- |
| `0` | `[1]` | `1` | `[1]` |
| `1` | `[2, 3]` | `3` | `[1, 3]` |
| `2` | `[4, 5, 6, 7]` | `7` | `[1, 3, 7]` |
| `3` | `[8, 9]` | `9` | `[1, 3, 7, 9]` |

Although `7` is the rightmost node at depth `2`, it has no children. The rightmost node at depth `3` is `9`, reached through `1 -> 3 -> 6 -> 9`.

### Why Is It Correct?

The queue processes each level in left-to-right order, using the same invariant as the left-view algorithm. The final node in that order is the rightmost node at that depth.

Selecting exactly that node at every level gives the right view in top-to-bottom order.

### Complexity

- **Time:** `O(n)`.
- **Auxiliary space, excluding the answer:** `O(w)`.
- **Output space:** `O(h)`.
- **Space including the answer:** `O(w + h)`.

### Edge Cases

- **Empty tree:** returns `[]`.
- **Single node `x`:** returns `[x]`.
- **Any chain:** contains every node from root to leaf, just like the left view.
- **The right subtree ends before the left subtree:** deeper nodes from the left subtree can enter the right view. Following only right child pointers misses them.

## 6. Coordinates for Top and Bottom Views

Left and right views group nodes by **depth**. Top and bottom views group them by **horizontal distance**, abbreviated as `hd`.

Assign coordinates as follows:

```text
Root:        hd = 0, depth = 0
Left child:  hd = parent's hd - 1, depth = parent's depth + 1
Right child: hd = parent's hd + 1, depth = parent's depth + 1
```

Nodes with the same `hd` belong to the same vertical column, even when they are in different subtrees. These are logical coordinates; the spacing used to draw a tree does not change them.

For the running example:

| Node | Depth | Horizontal distance |
| --- | --- | --- |
| `1` | `0` | `0` |
| `2` | `1` | `-1` |
| `3` | `1` | `+1` |
| `4` | `2` | `-2` |
| `5` | `2` | `0` |
| `6` | `2` | `0` |
| `7` | `2` | `+2` |
| `8` | `3` | `+1` |
| `9` | `3` | `-1` |

Group those nodes by horizontal distance, keeping BFS order within each group:

```text
hd = -2: 4
hd = -1: 2, 9
hd =  0: 1, 5, 6
hd = +1: 3, 8
hd = +2: 7
```

Now the selection rules become:

- **Top view:** take the first node in each group.
- **Bottom view:** take the last node in each group.

This works because **BFS visits nodes in nondecreasing depth**. Within a depth, our left-child-first enqueue order resolves ties.

We will store one selected value per column in `map<int, int>`. A C++ `map` iterates through keys in ascending order, so the final output naturally runs from the leftmost column to the rightmost column.

## 7. Top View: Keep the First Node in Each Column

### Key Observation

The first node BFS reaches at a horizontal distance has the smallest depth in that column. Any later node in the same column is equally deep or deeper.

Therefore, **insert a column only when it has not been seen before**. Once its top-view value is stored, leave it unchanged.

### Approach

1. Return an empty vector for a null root.
2. Push `(root, 0)` into a queue of node-coordinate pairs.
3. Pop `(current, hd)`.
4. If `hd` is absent from the map, store `current->data` at that key.
5. Enqueue the left child with `hd - 1`, then the right child with `hd + 1`.
6. After BFS finishes, append the map's values in ascending key order.

### C++ Implementation

```cpp
vector<int> topView(Node* root) {
    vector<int> answer;
    if (root == nullptr) return answer;

    map<int, int> firstAtColumn;
    queue<pair<Node*, int>> q;
    q.push({root, 0});

    while (!q.empty()) {
        auto [current, hd] = q.front();
        q.pop();

        if (firstAtColumn.find(hd) == firstAtColumn.end()) {
            firstAtColumn[hd] = current->data;
        }

        if (current->left != nullptr) {
            q.push({current->left, hd - 1});
        }
        if (current->right != nullptr) {
            q.push({current->right, hd + 1});
        }
    }

    for (const auto& entry : firstAtColumn) {
        answer.push_back(entry.second);
    }

    return answer;
}
```

No explicit depth is needed in the queue because BFS already supplies the required depth order.

Use `find` to test whether a column exists. A condition such as `if (firstAtColumn[hd] == 0)` is incorrect: zero may be a valid node value, and `operator[]` inserts a missing key.

### Dry Run

BFS processes nodes in this order:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9
```

| Node | `hd` | Action | Map after processing, in key order |
| --- | --- | --- | --- |
| `1` | `0` | New column: store `1` | `{0: 1}` |
| `2` | `-1` | New column: store `2` | `{-1: 2, 0: 1}` |
| `3` | `+1` | New column: store `3` | `{-1: 2, 0: 1, 1: 3}` |
| `4` | `-2` | New column: store `4` | `{-2: 4, -1: 2, 0: 1, 1: 3}` |
| `5` | `0` | Already occupied: keep `1` | Unchanged |
| `6` | `0` | Already occupied: keep `1` | Unchanged |
| `7` | `+2` | New column: store `7` | `{-2: 4, -1: 2, 0: 1, 1: 3, 2: 7}` |
| `8` | `+1` | Already occupied: keep `3` | Unchanged |
| `9` | `-1` | Already occupied: keep `2` | Unchanged |

Reading map values in key order gives:

```text
Top view = [4, 2, 1, 3, 7]
```

The order in which columns were first discovered was `0, -1, +1, -2, +2`. Printing immediately upon discovery would produce `[1, 2, 3, 4, 7]`, which is not the required left-to-right output.

### Why Is It Correct?

Fix any horizontal distance `x`. Since BFS visits nodes by nondecreasing depth, the first node encountered at `x` has minimum depth among all nodes in that column.

If multiple nodes share that minimum depth, the first encountered wins under our stated convention. The map stores that node's value and never replaces it.

Every node is visited, so every occupied column receives a value. Iterating through the ordered map then returns exactly the top view from left to right.

### Complexity

For a nonempty tree, the map contains at most `k` entries.

- **Time:** `O(n log(k + 1))`, including map lookups and insertions; the final map traversal takes `O(k)`. In the worst case this is `O(n log n)`.
- **Auxiliary space, excluding the answer:** `O(w + k)` for the queue and map.
- **Output space:** `O(k)`.
- **Space including the answer:** still `O(w + k)`, and at most `O(n)`.

Writing `log(k + 1)` keeps the bound meaningful when there is only one column.

### Edge Cases

- **Empty tree:** returns `[]`.
- **Single node `x`:** returns `[x]`.
- **A chain containing only left children:** every node has a distinct column; output runs from the deepest node back to the root.
- **A chain containing only right children:** every node has a distinct column; output runs from root to deepest node.
- **A chain that changes direction:** columns may repeat, so not every node necessarily appears. For `1 -> left 2 -> right 3`, the top view is `[2, 1]`; node `3` lies below `1` at `hd = 0`.
- **A deeper node enters a new column:** it must be included. A top view is not limited to shallow levels or to paths that repeatedly follow only left or only right children.

## 8. Bottom View: Keep the Last Node in Each Column

### Key Observation

For the bottom view, a deeper node replaces a shallower node at the same horizontal distance.

Because BFS processes depths in increasing order, we can **overwrite the map entry every time we visit a column**. The last value written is from a deepest node in that column.

If two candidates share both horizontal distance and depth, this overwriting selects the later one in left-to-right level order, exactly matching our tie rule.

### Approach

Use the same `(node, hd)` BFS as for the top view. The only change in the selection step is:

```text
Top view:    write only when the column is absent
Bottom view: write on every visit to the column
```

After traversal, read values from the ordered map from smallest to largest `hd`.

### C++ Implementation

```cpp
vector<int> bottomView(Node* root) {
    vector<int> answer;
    if (root == nullptr) return answer;

    map<int, int> lastAtColumn;
    queue<pair<Node*, int>> q;
    q.push({root, 0});

    while (!q.empty()) {
        auto [current, hd] = q.front();
        q.pop();

        // Later BFS nodes are deeper, or win an equal-depth tie.
        lastAtColumn[hd] = current->data;

        if (current->left != nullptr) {
            q.push({current->left, hd - 1});
        }
        if (current->right != nullptr) {
            q.push({current->right, hd + 1});
        }
    }

    for (const auto& entry : lastAtColumn) {
        answer.push_back(entry.second);
    }

    return answer;
}
```

### Dry Run

| Node | Depth | `hd` | Update | Map after processing, in key order |
| --- | --- | --- | --- | --- |
| `1` | `0` | `0` | Store `1` | `{0: 1}` |
| `2` | `1` | `-1` | Store `2` | `{-1: 2, 0: 1}` |
| `3` | `1` | `+1` | Store `3` | `{-1: 2, 0: 1, 1: 3}` |
| `4` | `2` | `-2` | Store `4` | `{-2: 4, -1: 2, 0: 1, 1: 3}` |
| `5` | `2` | `0` | Replace `1` with deeper `5` | `{-2: 4, -1: 2, 0: 5, 1: 3}` |
| `6` | `2` | `0` | Replace `5` with later equal-depth `6` | `{-2: 4, -1: 2, 0: 6, 1: 3}` |
| `7` | `2` | `+2` | Store `7` | `{-2: 4, -1: 2, 0: 6, 1: 3, 2: 7}` |
| `8` | `3` | `+1` | Replace `3` with deeper `8` | `{-2: 4, -1: 2, 0: 6, 1: 8, 2: 7}` |
| `9` | `3` | `-1` | Replace `2` with deeper `9` | `{-2: 4, -1: 9, 0: 6, 1: 8, 2: 7}` |

Reading map values in key order gives:

```text
Bottom view = [4, 9, 6, 8, 7]
```

The tie at `hd = 0`, depth `2` is important. Both `5` and `6` are deepest in that column, but `6` is visited later and is therefore selected. We do not compare their values.

### Why Is It Correct?

Fix any horizontal distance `x`. After each visit to `x`, the map contains the most recently processed value from that column.

BFS never processes a shallower node after a deeper one. Consequently, when traversal finishes, the stored node has maximum depth at `x`. Among nodes at that maximum depth, overwriting keeps the last one in left-to-right level order.

This is precisely the bottom-view rule. Iterating through map keys in ascending order gives the required left-to-right output.

### Complexity

- **Time:** `O(n log(k + 1))` with the ordered map, or `O(n log n)` in the worst case.
- **Auxiliary space, excluding the answer:** `O(w + k)`.
- **Output space:** `O(k)`.
- **Space including the answer:** `O(w + k)`, and at most `O(n)`.

The traversal visits each node once, but each map assignment can take logarithmic time. A single traversal does not by itself imply `O(n)` total time.

### Edge Cases

- **Empty tree:** returns `[]`.
- **Single node `x`:** returns `[x]`.
- **A chain containing only left or only right children:** all nodes occupy distinct columns, so top and bottom views are identical, in horizontal-distance order.
- **A chain that revisits a column:** retain its deepest node. For `1 -> left 2 -> right 3`, the bottom view is `[2, 3]`.
- **Equal-depth candidates in one column:** retain the later BFS node. The running example selects `6` over `5`.
- **A column containing an internal node but no deeper node:** that internal node belongs to the bottom view. Bottom view is not simply the list of leaves.

For example, if root `1` has only a left child `2`, the bottom view is `[2, 1]`. The root is visible in its own column even though it is not a leaf.

## 9. Building and Running the Example

Add this helper and `main` after the four functions:

```cpp
void printView(const char* label, const vector<int>& values) {
    cout << label << ':';
    for (int value : values) {
        cout << ' ' << value;
    }
    cout << '\n';
}

int main() {
    Node n1(1), n2(2), n3(3), n4(4), n5(5);
    Node n6(6), n7(7), n8(8), n9(9);

    n1.left = &n2;
    n1.right = &n3;
    n2.left = &n4;
    n2.right = &n5;
    n3.left = &n6;
    n3.right = &n7;
    n5.right = &n8;
    n6.left = &n9;

    printView("Left view", leftView(&n1));
    printView("Right view", rightView(&n1));
    printView("Top view", topView(&n1));
    printView("Bottom view", bottomView(&n1));

    return 0;
}
```

Output:

```text
Left view: 1 2 4 8
Right view: 1 3 7 9
Top view: 4 2 1 3 7
Bottom view: 4 9 6 8 7
```

The nodes are local objects that remain alive for all four calls. They are destroyed automatically when `main` finishes; do not call `delete` on them.

Each function creates its own queue, map when needed, and answer vector. Repeated calls cannot retain results from an earlier tree. The coordinate implementations assume that horizontal distances fit in an `int`.

## 10. Comparing the Four Views

| Property | Left view | Right view | Top view | Bottom view |
| --- | --- | --- | --- | --- |
| Group nodes by | Depth | Depth | Horizontal distance | Horizontal distance |
| Selection under left-to-right BFS | First per level | Last per level | First per column | Last per column |
| Main storage | Queue | Queue | Queue and ordered map | Queue and ordered map |
| Output order | Increasing depth | Increasing depth | Increasing `hd` | Increasing `hd` |
| Number of output values | `h` | `h` | `k` | `k` |
| Time | `O(n)` | `O(n)` | `O(n log(k + 1))` | `O(n log(k + 1))` |
| Auxiliary space, excluding output | `O(w)` | `O(w)` | `O(w + k)` | `O(w + k)` |

For the running example, `h = 4` and `k = 5`. The side views each contain four values, while the top and bottom views each contain five.

**Views are also different from boundary traversal.** Boundary traversal follows a specified outer-boundary order, usually combining the root, left boundary, leaves, and reversed right boundary. A view selects one node per level or column. Concatenating the left and right views does not implement boundary traversal.

## 11. Common Mistakes

- **Following only left pointers or only right pointers.** A side view can continue through another branch after the current outer branch ends.
- **Using a changing queue size as the level-loop bound.** Store `levelSize` before processing any node in that level.
- **Changing child order without changing the selection rule.** With right-child-first BFS, the first node per level gives the right view instead of the left view. Equal-depth ties for the bottom view also change.
- **Grouping the top or bottom view by depth.** Their grouping key is horizontal distance.
- **Overwriting top-view entries.** Under BFS, this replaces shallower candidates with deeper ones and computes the bottom-view selection instead.
- **Keeping only the first entry for the bottom view.** A deeper node in the same column must replace it.
- **Using plain DFS with the same first-write or last-write map rules.** DFS does not visit nodes by increasing depth. A deep node in one subtree may be visited before a shallow node in another.
- **Printing top or bottom values in BFS discovery order.** Gather them by column and output columns in ascending horizontal distance.
- **Sorting by node value.** Values do not determine visibility or tie-breaking in this lesson.
- **Removing duplicate values from the answer.** Distinct visible nodes may store the same value, and both occurrences must remain.
- **Calling ordered-map solutions `O(n)` time.** Include the logarithmic lookup or update cost.
- **Assuming the BFS queue uses `O(h)` space.** Its size depends on width. A balanced tree can have `O(n)` nodes on its widest level even though its height is `O(log n)`.

## 12. Interview and Competitive Programming Insights

### Explain the Group and the Selection Rule First

A concise explanation before coding is:

> For left and right views, I group nodes by level and take the first or last node. For top and bottom views, I group nodes by horizontal distance and take the shallowest or deepest node. BFS turns those depth comparisons into first-visit or last-visit rules.

This establishes why the traversal order is useful, rather than presenting four unrelated algorithms.

### Clarify Tie-Breaking and Output Order

For top and bottom views, state both the coordinate rule and the equal-depth tie rule. Our bottom-view code keeps the later node in left-to-right level order. If a problem wants the earlier node among equally deep candidates, store depth with each value and replace only when a **strictly deeper** node arrives.

Also clarify that top and bottom answers run from smallest to largest `hd`; side-view answers run from root level downward.

### Compute Multiple Views in One BFS When Needed

The four separate functions keep each idea easy to study. If an application needs all four views together, use one level-order queue of `(node, hd)` pairs:

1. Save the level size and record its first and last nodes for the side views.
2. Insert a top-view value only if the column is absent.
3. Overwrite the bottom-view value on every visit.
4. Read both column maps in sorted order after traversal.

This reduces repeated traversal work, although ordered-map operations keep the combined time bound at `O(n log(k + 1))`.

### DFS Is an Alternative, with Different State Requirements

For the left view, a root-left-right DFS can record the first node it reaches at each depth. For the right view, use root-right-left DFS. In either case, append when `depth == answer.size()`.

These side-view DFS approaches take `O(n)` time and `O(h)` recursion space, excluding output. On a long chain, recursion depth becomes `n` and may exhaust the call stack; BFS avoids that recursion depth and has a constant-size queue for a chain.

For top or bottom views, DFS must explicitly track depths when updating column entries. Traversal order alone is not enough to compare a deep node in one subtree with a shallower node in another. Equal-depth ties also need a consistent rule.

### A Hash Map Can Reduce Expected Time

An `unordered_map` provides expected constant-time lookup and update, but its iteration order is not sorted. Sorting its `k` keys after BFS gives expected `O(n + k log k)` time.

There is another option: track the smallest and largest `hd` during traversal, then read the hash map from the minimum to the maximum distance. Occupied horizontal distances form a contiguous integer interval: any path from the root at `0` to a column changes `hd` by exactly one per edge and must pass through every intermediate distance.

Thus, scanning that interval takes `O(k)` time, giving **expected `O(n)` total time** and `O(w + k)` auxiliary space. Hash operations do not provide a general worst-case constant-time guarantee. The ordered map is a straightforward choice when deterministic logarithmic operations and automatic output ordering are preferred.

### Distinguish Views from Vertical Traversal

Vertical traversal may retain **all nodes** in each column and may impose additional ordering by depth or value. Top and bottom views retain only one node per column.

Do not transfer a vertical-traversal rule such as sorting equal-coordinate nodes by value into a view problem unless its statement explicitly requires that rule.

</READING_WIDGET>
