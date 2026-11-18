<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Maximum Path Sum in a Binary Tree

In the Diameter problem, we found the longest path between any two nodes by combining subtree heights. Now, each node contributes a value, and we want the path with the **largest sum**.

The structure of the solution remains the same: a node returns **one branch that its parent can extend**, while the answer may combine **both child branches through that node**. Negative values add one important decision: a branch that reduces the sum should be left out.

## 1. Problem Statement and Conventions

Given the root of a **nonempty binary tree**, return the maximum sum of node values along any nonempty simple path.

A valid path:

- Starts and ends at any nodes, including the same node.
- Follows edges between adjacent nodes without repeating a node.
- May travel upward to an ancestor and then downward into another branch.
- Does not have to include the root or end at a leaf.

Each node on the path contributes its value exactly once. We are maximizing the sum of **node values**, not counting nodes or edges.

Assume that:

- The input is a finite binary tree with no cycles or shared child nodes.
- Values may be positive, negative, zero, or repeated.
- Each value fits in a C++ `int`, and all path sums fit in a `long long`.
- The algorithm must leave the tree unchanged.

Let `n` be the number of nodes and `h` the height measured in nodes. We will use C++17.

### Can the Path Be Empty?

No. A path must contain at least one node.

For a tree containing only a node with value `-8`, the answer is **`-8`**, not `0`. This rule determines how we initialize the answer and how we interpret discarded negative branches.

An empty tree has no valid path under this definition. The implementation below explicitly rejects an empty input rather than assigning it a path sum.

## 2. Running Example

Consider this tree:

```text
         -10
         / \
        9   20
           /  \
          15   7
```

Some valid paths are:

| Path | Sum |
| --- | --- |
| `9` | `9` |
| `-10 -> 20 -> 15` | `25` |
| `9 -> -10 -> 20 -> 15` | `34` |
| `15 -> 20 -> 7` | `42` |

The maximum path sum is **`42`**, from `15 -> 20 -> 7`.

This path lies entirely inside the root's right subtree. A solution that checks only paths containing the root would miss it.

Also notice that the path with sum `34` contains more nodes than the path with sum `42`. **A longer path does not necessarily have a larger sum.**

## 3. The Key Observation: Every Path Has One Highest Node

As in the Diameter problem, every simple path has a unique highest node relative to the tree's root: the **lowest common ancestor of its endpoints**.

At a current node `cur`, a path contained in its subtree is either:

1. Entirely inside the left subtree.
2. Entirely inside the right subtree.
3. A path whose highest node is `cur`.

The recursive calls handle paths in the first two groups. To handle the third group, we combine:

- The current node.
- At most one downward branch from its left child.
- At most one downward branch from its right child.

Either branch may be omitted, allowing a path to end at `cur`. Both may be omitted, leaving the single-node path.

The left and right branches belong to disjoint subtrees. Joining them through `cur` therefore produces a valid simple path.

We do not need to find the LCA of every pair of endpoints. Instead, we visit every node as a possible highest node and compute the best path for that choice.

## 4. Define the Recursive State: One Extendable Branch

Define:

```text
gain(cur) = maximum sum of a nonempty downward path
            that starts at cur and stays in cur's subtree
```

This path must include `cur` and can continue into **at most one child**. It may stop at `cur`, even if `cur` is not a leaf.

For a null pointer, the helper returns `0` as a convenient base value. A null pointer is not itself a valid nonempty path.

### Why Can We Ignore a Negative Child Gain?

Suppose a child returns `-6`. Adding that branch would reduce the sum by `6`. Since the path is allowed to stop at the current node, omitting that branch is better.

After processing both children, define:

```text
left  = max(0, gain(cur->left))
right = max(0, gain(cur->right))
```

Here, `0` means **do not take a branch on this side**. It does not mean that the final path is allowed to be empty.

The best branch starting at `cur` is then:

```text
gain(cur) = cur->data + max(left, right)
```

It includes the current node and extends through whichever child offers the better positive contribution. If neither child helps, it stops at `cur`.

### The Best Complete Path at cur

A complete path whose highest node is `cur` can use both sides:

```text
candidate(cur) = cur->data + left + right
```

We maintain a shared answer across the traversal:

```text
answer = max(answer, candidate(cur))
```

The two calculations serve different purposes:

| Quantity | Formula | Meaning |
| --- | --- | --- |
| Gain returned to the parent | `cur->data + max(left, right)` | One downward branch beginning at `cur` |
| Candidate for the answer | `cur->data + left + right` | A complete path whose highest node is `cur` |

### Why Can't We Return Both Branches?

In the running example, node `20` can form:

```text
Complete path: 15 -> 20 -> 7
Sum:          15 + 20 + 7 = 42
```

But its parent cannot extend this path through `20`. That would require three incident edges at `20`: one to `15`, one to `7`, and one to the parent. A simple path cannot branch in three directions.

The branch returned upward must choose only one side:

```text
Returned branch: 20 -> 15
Returned gain:  20 + max(15, 7) = 35
```

The value `42` is retained in the answer, while `35` is returned to the parent. Keeping these two meanings separate is the central idea of the algorithm.

## 5. Handling Negative Values Correctly

### Discard a Negative Gain, Not Every Negative Node

Consider:

```text
       2
      /
    -5
    /
   10
```

The branch starting at `-5` has gain:

```text
-5 + 10 = 5
```

Its root is negative, but its overall contribution to node `2` is positive. We must compute the child's full gain before deciding whether to use it.

The best complete path in this tree is still the single node `10`. The example shows that **the sign of a node's value alone does not determine whether its branch helps its parent**.

A negative node can even belong to the optimal path:

```text
       -5
       / \
      10  10
```

The maximum path sum is `10 - 5 + 10 = 15`. The negative node connects two branches whose combined benefit outweighs its cost. We cannot skip that connecting node while retaining both branches because the resulting nodes would no longer form a connected path.

### All-Negative Trees

Consider:

```text
       -3
       / \
     -2  -5
```

Each child's negative gain is discarded by its parent. Every local candidate is therefore the current node's value, and the largest candidate is `-2`.

More generally, if all values are negative, any path containing multiple nodes has a smaller sum than at least one of its individual nodes. The answer is the **largest node value**.

Therefore:

- Initialize the answer to the lowest representable `long long`, or to a real node's value.
- Always include the current node in its candidate.
- Clamp child contributions to zero, not the final answer.

The returned gain may itself be negative. For example, a leaf with value `-8` returns `-8`; its parent decides whether to use that contribution.

## 6. From Repeated Computation to One Postorder DFS

A direct approach is to visit every possible highest node and separately compute the best downward gain from each of its children. Then form its two-branch candidate and keep the maximum.

This is correct, but recomputes gains for the same subtrees many times. On a chain of `n` nodes, those repeated scans examine approximately:

```text
(n - 1) + (n - 2) + ... + 1 = O(n^2) nodes in total
```

The improvement is to compute each child's gain once and return it during the same traversal that updates the answer.

At each node:

1. Recursively process the left subtree.
2. Recursively process the right subtree.
3. Replace negative child gains with zero.
4. Update the answer using both available branches.
5. Return the best single-branch gain.

Because the children are processed before their parent, this is **postorder DFS**.

```text
dfsGain(cur, answer):
    if cur is null:
        return 0

    left  = max(0, dfsGain(cur->left, answer))
    right = max(0, dfsGain(cur->right, answer))

    answer = max(answer, cur->data + left + right)
    return cur->data + max(left, right)
```

The answer tracks the best complete path found anywhere among processed nodes. It is not restricted to paths that can reach the current node's parent.

## 7. C++ Implementation

Combine the following definitions and functions with the later `main` to form a complete C++17 program.

### Headers and Node Definition

```cpp
#include <algorithm>
#include <iostream>
#include <limits>
#include <stdexcept>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    explicit Node(int value)
        : data(value), left(nullptr), right(nullptr) {}
};
```

### Return One Branch, Update the Best Complete Path

```cpp
long long dfsGain(const Node* cur, long long& answer) {
    if (cur == nullptr) return 0;

    long long left = max(0LL, dfsGain(cur->left, answer));
    long long right = max(0LL, dfsGain(cur->right, answer));
    long long value = cur->data;

    // Best complete path whose highest node is cur.
    long long throughCur = value + left + right;
    answer = max(answer, throughCur);

    // One branch that the parent can extend through cur.
    return value + max(left, right);
}

long long maxPathSum(const Node* root) {
    if (root == nullptr) {
        throw invalid_argument("Maximum path sum requires a nonempty tree");
    }

    long long answer = numeric_limits<long long>::lowest();
    dfsGain(root, answer);
    return answer;
}
```

`long long& answer` passes the same answer variable by reference to every recursive call. It acts as the global best for this traversal without requiring a global variable.

The wrapper initializes a fresh answer on every call, so results from earlier trees cannot carry over. It deliberately ignores the helper's return value: that value is the best **downward gain starting at the root**, not necessarily the best path anywhere in the tree.

The `0LL` literal makes both arguments to `max` have type `long long`. The addition also takes place in `long long` because `value`, `left`, and `right` all use that type. Assigning an already-overflowed `int` expression to a wider variable would not fix it.

The lowest-value sentinel is used only for comparison. We never add it to a path sum. Every non-null call constructs a candidate containing a real node, so a nonempty input always replaces the sentinel.

## 8. Dry Run on the Running Example

```text
         -10
         / \
        9   20
           /  \
          15   7
```

With left-child-first DFS, the non-null nodes finish in this order:

```text
9, 15, 7, 20, -10
```

Initially, `answer` is the lowest representable `long long`. Null calls return `0` and are omitted from the table. The `left` and `right` columns show gains **after clamping to zero**.

| Node value | `left` | `right` | Candidate `value + left + right` | Gain returned | `answer` after update |
| --- | --- | --- | --- | --- | --- |
| `9` | `0` | `0` | `9` | `9` | `9` |
| `15` | `0` | `0` | `15` | `15` | `15` |
| `7` | `0` | `0` | `7` | `7` | `15` |
| `20` | `15` | `7` | `42` | `35` | `42` |
| `-10` | `9` | `35` | `34` | `25` | `42` |

### At Node 20

```text
Left contribution  = 15
Right contribution = 7

Complete candidate = 20 + 15 + 7 = 42
Returned gain      = 20 + max(15, 7) = 35
```

The candidate represents `15 -> 20 -> 7`. The returned gain represents `20 -> 15`.

### At the Root -10

```text
Left contribution  = 9
Right contribution = 35

Complete candidate = -10 + 9 + 35 = 34
Returned gain      = -10 + max(9, 35) = 25
```

The root's candidate corresponds to `9 -> -10 -> 20 -> 15`. Its returned gain corresponds to `-10 -> 20 -> 15`.

Neither improves the complete path with sum `42` already found below the root. The wrapper returns **`42`** from `answer`, not the root's gain of `25`.

### A Short Negative-Value Dry Run

For the all-negative tree from Section 5:

| Node value | Raw left gain | Raw right gain | Contributions after clamping | Candidate | Gain returned | Best answer |
| --- | --- | --- | --- | --- | --- | --- |
| `-2` | `0` | `0` | `0, 0` | `-2` | `-2` | `-2` |
| `-5` | `0` | `0` | `0, 0` | `-5` | `-5` | `-2` |
| `-3` | `-2` | `-5` | `0, 0` | `-3` | `-3` | `-2` |

Clamping the contributions does not create a zero-sum answer. Each candidate still includes its current node, and the result is correctly **`-2`**.

## 9. Why Is the Algorithm Correct?

We need to justify both the gain returned to the parent and the complete paths considered for the answer.

### The Helper Returns the Correct Gain

For a non-null node `cur`, every downward path starting at `cur` must:

1. Stop at `cur`.
2. Continue into its left child.
3. Continue into its right child.

It cannot use both children because it must remain a single downward branch.

Assuming the child calls return their correct gains, the best choice is to add the larger child gain when it is positive, or add nothing when neither child helps. Therefore:

```text
gain(cur) = cur->data + max(0, gain(cur->left), gain(cur->right))
```

This is exactly the helper's return expression after clamping. At a leaf, it returns the leaf's value, so the same reasoning applies from the leaves upward.

### The Candidate Is Best for Its Highest Node

Any path whose highest node is `cur` contains `cur` and can use at most one downward branch from each child.

The best contribution from each side is its child's gain, or zero if that branch would reduce the sum. The choices are independent because the child subtrees are disjoint.

Thus, the best path with highest node `cur` has sum:

```text
cur->data + max(0, gain(cur->left)) + max(0, gain(cur->right))
```

This candidate is always a valid nonempty path, even if both branches are omitted.

### Taking the Maximum Finds the Global Optimum

Take an optimal path and let `x` be its highest node. DFS visits `x` and evaluates the best path with that highest node, so its candidate is at least as good as the chosen optimal path.

Every candidate is itself valid, so no candidate can exceed the true optimum. Taking the maximum candidate over all nodes therefore gives exactly the maximum path sum.

## 10. Connection to the Diameter Problem

Both algorithms distinguish between **a branch that can extend upward** and **a complete path formed locally**.

Using the earlier chapter's diameter-in-nodes convention:

| Detail | Diameter in nodes | Maximum path sum |
| --- | --- | --- |
| Contribution of the current node | `1` | `cur->data` |
| State returned by a child | Height in nodes | Best downward gain |
| Can a child contribution be harmful? | No | Yes, if negative |
| Usable child contributions | `leftHeight`, `rightHeight` | `max(0, leftGain)`, `max(0, rightGain)` |
| Complete candidate | `1 + leftHeight + rightHeight` | `value + left + right` |
| Return to the parent | `1 + max(leftHeight, rightHeight)` | `value + max(left, right)` |
| Answer initialization | `0` | Lowest value, or a real node value |
| Traversal | Postorder DFS | Postorder DFS |

If every node value is `1`, maximum path sum becomes exactly the **diameter in nodes**. For a nonempty tree, that result is one more than the diameter measured in edges.

With arbitrary values, the shape alone is insufficient. A short path with large positive values may beat a long path, and an unhelpful branch should be excluded even when it contains many nodes.

The transferable tree-DP pattern is:

> Return the best contribution the parent can extend. Separately evaluate the best complete solution formed at the current node.

## 11. Time and Space Complexity

Each node is visited once. After the two child calls finish, it performs constant work: clamp two gains, compute a candidate, update the answer, and compute its return value.

- **Time:** `O(n)`.
- **Auxiliary space:** `O(h)` for the recursion stack.

| Tree shape | Height | Auxiliary space |
| --- | --- | --- |
| Balanced tree | `O(log n)` | `O(log n)` |
| Skewed tree or chain | `O(n)` | `O(n)` |

The two child calls execute sequentially. The maximum number of active calls follows one root-to-leaf path, rather than including every node visited so far.

The input tree's storage is not counted as auxiliary space. A shared answer and a few variables per call do not make the recursive algorithm `O(1)` space; all active stack frames still count.

## 12. Building and Running the Example

Add this `main` after the implementation:

```cpp
int main() {
    Node root(-10), a(9), b(20), c(15), d(7);
    root.left = &a;
    root.right = &b;
    b.left = &c;
    b.right = &d;

    cout << "Maximum path sum: " << maxPathSum(&root) << '\n';

    Node negativeRoot(-3), left(-2), right(-5);
    negativeRoot.left = &left;
    negativeRoot.right = &right;

    cout << "All-negative tree: " << maxPathSum(&negativeRoot) << '\n';

    Node single(-8);
    cout << "Single negative node: " << maxPathSum(&single) << '\n';

    return 0;
}
```

Output:

```text
Maximum path sum: 42
All-negative tree: -2
Single negative node: -8
```

The nodes are local objects whose lifetimes cover the calls. They are destroyed automatically; do not call `delete` on them.

## 13. Edge Cases and Common Mistakes

### Edge Cases

| Case | Expected result | Reason |
| --- | --- | --- |
| Single node `8` | `8` | The single-node path is valid |
| Single node `-8` | `-8` | A nonempty path is required |
| Single node `0` | `0` | Zero is a valid node value |
| Root `5` with children `-2` and `-3` | `5` | Both child gains are discarded |
| Root `1` with children `2` and `3` | `6` | The best path uses both branches |
| Root `-3` with children `-2` and `-5` | `-2` | The largest node wins in an all-negative tree |
| Root `-5` with two children valued `10` | `15` | A negative connector can belong to the optimum |
| Chain `2 -> -1 -> 3` | `4` | A negative value can connect profitable portions |
| Chain `5 -> -100 -> 6` | `6` | A path cannot skip an internal node |
| All values are zero | `0` | Many nonempty paths tie for the optimum |
| Running example | `42` | The optimal path does not include the root |
| Three-node chain, each value `1000000000` | `3000000000` | Sums can exceed a 32-bit signed integer |
| Empty tree | Rejected by this implementation | No nonempty path exists |

Repeated values do not change the recurrence. If reconstructing a path, distinguish nodes by identity rather than by their stored values.

### Common Mistakes

- **Initializing the answer to zero.** This incorrectly returns `0` for an all-negative tree.
- **Returning `value + left + right` to the parent.** This can cause the parent to combine a branching structure that is not a simple path.
- **Returning the root's gain as the final answer.** A complete path may use both branches below the root; the running example would incorrectly return `25` instead of `42`.
- **Checking only the root's candidate.** The optimum may lie entirely in a child subtree.
- **Adding a negative child gain unconditionally.** The path can end at the current node, so a harmful branch is optional.
- **Skipping every negative node.** A negative node may connect positive portions of the optimal path.
- **Clamping the whole candidate to zero.** Each candidate must contain the current node; an empty path is not a valid fallback.
- **Requiring endpoints to be leaves.** This changes the problem. A single internal node may be the best path.
- **Overwriting the answer with the current candidate.** Use `max` to preserve better paths discovered earlier.
- **Passing the answer by value or retaining it across queries.** Use shared state within one traversal and reset it for each new tree.
- **Using a narrow type for intermediate arithmetic.** Make the additions themselves use a sufficiently wide type.

## 14. Interview and Competitive Programming Insights

**State the helper's contract before coding.** A precise explanation is: “My DFS returns the maximum sum of a downward path starting at this node. I ignore negative child contributions, use both sides to update the answer, and return only the better side to the parent.” This explains every part of the recurrence.

**Clarify which path problem is being asked.** Maximum root-to-leaf sum, maximum leaf-to-leaf sum, and maximum path sum with arbitrary endpoints have different constraints. In particular, a leaf-to-leaf problem cannot freely stop at an internal node or discard a required endpoint branch. The recurrence here relies on endpoints being unrestricted.

**Recognize the connection to Kadane's algorithm.** On a tree that is a single chain, valid paths are contiguous segments of the chain. The recurrence becomes `value + max(0, nextGain)`, with a separate maximum over all nodes. This is the maximum-subarray idea evaluated from one end of the chain. In a branching tree, the extra step is considering two contributions at a possible turning node.

**A shared answer is convenient, but not essential.** A helper can instead return a pair containing the best downward gain and the best complete path sum in its subtree. The parent computes its gain from the child gains, then takes the maximum of the two child answers and its own candidate. For an empty subtree, use gain `0` and a lowest-value sentinel for the complete-path answer; never add that sentinel into a sum.

**Returning the actual path needs additional information.** Along with each gain, retain the endpoint of the selected downward branch. When a complete candidate improves the answer, save its two endpoints and highest node, using the current node as an endpoint when a side is omitted. Parent links can then reconstruct the path. Store node identities because values may repeat. Avoid copying full path vectors at every recursive call, which can turn linear work into quadratic work on a chain.

**The pattern extends to a general rooted tree.** If a node has many children, return its value plus the largest positive child gain. For the complete candidate, add the two largest positive child gains, using zero for missing contributions. A simple path still uses at most two child branches at its highest node.

**Plan for recursion depth.** A sufficiently long chain may exhaust the call stack. The same recurrence can be evaluated with iterative postorder traversal. A straightforward implementation uses an explicit stack and a gain table keyed by node pointers, requiring `O(n)` auxiliary space.

## Quick Recap

- A path may start and end at any nodes, but must contain at least one node.
- Every path has a unique highest node, so evaluate a complete candidate at every node.
- A child contributes `max(0, childGain)` because a negative branch can be omitted.
- Update the answer with **`value + left + right`**.
- Return **`value + max(left, right)`** so the parent receives one extendable branch.
- Initialize the answer below all valid sums so all-negative trees are handled correctly.
- This is the same structural pattern as Diameter, with node values replacing unit contributions and negative gains discarded.
- One postorder DFS gives **`O(n)` time and `O(h)` auxiliary space**.

</READING_WIDGET>
