<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Identical Trees and Symmetric Tree

When comparing binary trees, matching node values is only part of the problem. We must also check **where those values occur**, including the positions of missing children.

Two closely related questions arise:

- **Identical trees:** Do two trees have the same structure and the same value at every corresponding position?
- **Symmetric tree:** Does one tree look the same when reflected across a vertical line through its root?

Both problems can be solved by comparing **pairs of nodes**. The base cases stay the same; only the child pairs change. We will build recursive and iterative solutions for both, then trace how they detect value and structure mismatches.

## 1. Problem Statements and Conventions

### Problem 1: Check Whether Two Trees Are Identical

Given roots `a` and `b`, return `true` if the trees have:

1. The same structure, including left and right child positions.
2. The same value at every corresponding position.

The nodes do not need to occupy the same memory addresses. Two separately allocated trees can be identical.

```text
Tree A:              Tree B:

       1                    1
      / \                  / \
     2   3                2   3
      \                    \
       4                    4

Result: true
```

Changing `4` in Tree B to `9` makes the answer `false`. Moving it from the right child of `2` to the left child also makes the answer `false`, even though all values remain the same.

### Problem 2: Check Whether a Tree Is Symmetric

Given `root`, return `true` if its left and right subtrees are **mirror images of each other**, considering both structure and values.

```text
          1
        /   \
       2     2
      / \   / \
     3   4 4   3

Result: true
```

The outer nodes containing `3` match, and the inner nodes containing `4` match. The left and right subtrees are mirrors, even though they are not identical in their original orientation.

Assume throughout that:

- Inputs are finite binary trees with no cycles or shared child nodes within a tree.
- Values may repeat or be negative; there is no BST ordering assumption.
- Neither problem allows us to change values or child pointers.
- Two empty trees are identical, and an empty tree is symmetric.

For identical trees, let the node counts be `n1` and `n2`, heights be `h1` and `h2`, and maximum level widths be `w1` and `w2`. For symmetry, use `n`, `h`, and `w` for the single tree. Height is measured in nodes: an empty tree has height `0`, and a leaf has height `1`.

## 2. One Comparison Pattern, Two Pairing Rules

Before deciding which children to compare, consider a pair of pointers `(a, b)`:

| State of the pair | Result | Reason |
| --- | --- | --- |
| Both are null | `true` | Both positions are empty |
| Exactly one is null | `false` | The structures differ |
| Both exist, but values differ | `false` | Corresponding values do not match |
| Both exist and values match | Check their children | A match at this position does not prove a match below it |

**Check for null pointers before reading node values or children.**

Once the current pair matches, the problem determines which children correspond:

| Check | First child pair | Second child pair |
| --- | --- | --- |
| Identical | `(a->left, b->left)` | `(a->right, b->right)` |
| Mirror | `(a->left, b->right)` | `(a->right, b->left)` |

For identity, the directions are the same. For a mirror, the directions are opposite **at every depth**, not just at the root.

This also explains why comparing a tree with itself using an identical-tree function cannot test symmetry. Every valid tree is identical to itself, including an asymmetric one.

## 3. Shared C++ Setup

All implementations use C++17. Combine this setup with the functions and the demonstration `main` later in the lesson to form a complete program.

```cpp
#include <iostream>
#include <queue>
#include <utility>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value)
        : data(value), left(nullptr), right(nullptr) {}
};
```

The checking functions accept `const Node*` because they only inspect the trees. They return a Boolean result rather than printing during traversal.

## 4. Identical Trees: Recursive Approach

### Recursive Contract

```text
areIdentical(a, b): return whether the entire subtrees rooted at a and b
have the same structure and values.
```

After handling null pointers and unequal values, both of these conditions must hold:

1. The left subtree of `a` is identical to the left subtree of `b`.
2. The right subtree of `a` is identical to the right subtree of `b`.

We combine them with logical **AND**, because a mismatch on either side is enough to reject the trees.

### C++ Implementation

```cpp
bool areIdentical(const Node* a, const Node* b) {
    if (a == nullptr && b == nullptr) return true;
    if (a == nullptr || b == nullptr) return false;
    if (a->data != b->data) return false;

    return areIdentical(a->left, b->left) &&
           areIdentical(a->right, b->right);
}
```

C++ evaluates `&&` from left to right and short-circuits: if the left comparison returns `false`, the right comparison is skipped. We do not need to count nodes or calculate heights first.

### Recursive Dry Run

Use the identical trees from Section 1. In the table, a pair such as `(2, 2)` represents two corresponding nodes, one from each tree. `#` represents `nullptr`.

| Call | What happens? |
| --- | --- |
| `(1, 1)` | Values match; compare the left subtrees |
| `(2, 2)` | Values match; compare their left children |
| `(#, #)` | Both positions are empty; return `true` |
| `(4, 4)` | Values match; both child comparisons are `(#, #)`, so return `true` |
| Return to `(2, 2)` | Both child comparisons succeeded; return `true` |
| `(3, 3)` | Values match; both child comparisons are `(#, #)`, so return `true` |
| Return to `(1, 1)` | Both subtree comparisons succeeded; return `true` |

Now move `4` in Tree B to the **left** of `2`:

```text
Tree A:              Tree B:

       1                    1
      / \                  / \
     2   3                2   3
      \                  /
       4                4
```

The comparisons reach `(2, 2)`, then compare their left children: `(#, 4)`. Exactly one pointer is null, so the result is `false`. Short-circuiting carries this failure back to the root.

If Tree B instead keeps the original structure but replaces `4` with `9`, the comparison reaches `(4, 9)` and fails at the value check.

### Why Is It Correct?

For empty positions, the base cases accept precisely when both are empty. For two existing nodes, identity requires equal root values and identical subtrees on each corresponding side. The function checks exactly these three conditions. Applying the same reasoning recursively proves that it accepts precisely the identical trees.

## 5. Identical Trees: Iterative Approach

Recursion stores unfinished comparisons on the call stack. We can instead store pairs explicitly in a queue and process them in breadth-first order.

The queue holds **positions that must match**. A position may be null, so do not discard missing children independently from the two trees.

### C++ Implementation

```cpp
bool areIdenticalIterative(const Node* a, const Node* b) {
    queue<pair<const Node*, const Node*>> pending;
    pending.push({a, b});

    while (!pending.empty()) {
        auto [first, second] = pending.front();
        pending.pop();

        if (first == nullptr && second == nullptr) continue;
        if (first == nullptr || second == nullptr) return false;
        if (first->data != second->data) return false;

        pending.push({first->left, second->left});
        pending.push({first->right, second->right});
    }

    return true;
}
```

For a pair of null pointers, use `continue`, not `return true`. That pair is valid, but other pending pairs might still contain a mismatch. Return `true` only when the queue is empty.

### Iterative Dry Run

For the original identical trees, the queue evolves as follows. Its front is shown on the left.

| Pair removed | Queue after processing the pair |
| --- | --- |
| Initial state | `[(1, 1)]` |
| `(1, 1)` | `[(2, 2), (3, 3)]` |
| `(2, 2)` | `[(3, 3), (#, #), (4, 4)]` |
| `(3, 3)` | `[(#, #), (4, 4), (#, #), (#, #)]` |
| `(#, #)` | `[(4, 4), (#, #), (#, #)]` |
| `(4, 4)` | `[(#, #), (#, #), (#, #), (#, #)]` |
| Remaining four null pairs | Each is skipped; the queue becomes empty |

The result is `true`. If the node values were `(4, 9)`, the algorithm would return `false` when that pair was removed.

### Why Is It Correct?

Initially, the queue contains the two roots that must match. Every matching non-null pair is replaced by its two required child comparisons. A mismatch rejects the trees immediately; two null pointers need no further work. If the queue becomes empty, every required comparison has succeeded, so the trees are identical.

## 6. Symmetric Tree: Recursive Approach

### Why an Identical-Tree Check Is Not Enough

In the symmetric example, the left subtree has children `3, 4`, while the right subtree has children `4, 3`.

```text
Left subtree:        Right subtree:

      2                    2
     / \                  / \
    3   4                4   3
```

Comparing left-to-left would compare `3` with `4` and reject the tree. Symmetry requires **cross comparisons**:

- The left child of the first node matches the right child of the second.
- The right child of the first node matches the left child of the second.

Define a helper with this contract:

```text
areMirrors(a, b): return whether the subtrees rooted at a and b
are mirror images, including both structure and values.
```

### C++ Implementation

```cpp
bool areMirrors(const Node* a, const Node* b) {
    if (a == nullptr && b == nullptr) return true;
    if (a == nullptr || b == nullptr) return false;
    if (a->data != b->data) return false;

    return areMirrors(a->left, b->right) &&
           areMirrors(a->right, b->left);
}

bool isSymmetric(const Node* root) {
    if (root == nullptr) return true;
    return areMirrors(root->left, root->right);
}
```

The root lies on the axis of symmetry, so its value requires no separate comparison. We check whether its two subtrees mirror each other.

### Recursive Dry Run

Return to the symmetric tree:

```text
          1
        /   \
       2     2
      / \   / \
     3   4 4   3
```

To distinguish repeated values, use paths from the root: `L` means left, `R` means right, and `LR` means left then right.

| Call | Values | Result |
| --- | --- | --- |
| `areMirrors(L, R)` | `(2, 2)` | Values match; check the outer pair first |
| `areMirrors(LL, RR)` | `(3, 3)` | Both cross-child comparisons are null pairs; return `true` |
| `areMirrors(LR, RL)` | `(4, 4)` | Both cross-child comparisons are null pairs; return `true` |
| Return to `areMirrors(L, R)` | `(2, 2)` | Both pairs succeeded; return `true` |

Therefore, `isSymmetric(root)` returns `true`.

Now consider a tree whose two children both have only a **right** child:

```text
          1
        /   \
       2     2
        \     \
         3     3
```

The pair `(L, R)` has matching values. But its first cross comparison is `(LL, RR)`, whose values are `(#, 3)`. The function returns `false` because the missing positions do not mirror each other.

Notice that the two subtrees in this failing example are **identical**. Identical subtrees do not necessarily make the whole tree symmetric.

### Why Is It Correct?

Two empty subtrees are mirrors, while exactly one empty subtree cannot match an existing one. For existing roots, the mirror relation requires equal values, a left-to-right mirror match, and a right-to-left mirror match. The helper checks precisely these conditions recursively. The wrapper applies this relation to the two sides of the root, which is exactly the definition of symmetry.

## 7. Symmetric Tree: Iterative Approach

Use a queue of pairs again. This time, every queued pair represents two positions that must **mirror** each other.

### C++ Implementation

```cpp
bool isSymmetricIterative(const Node* root) {
    if (root == nullptr) return true;

    queue<pair<const Node*, const Node*>> pending;
    pending.push({root->left, root->right});

    while (!pending.empty()) {
        auto [first, second] = pending.front();
        pending.pop();

        if (first == nullptr && second == nullptr) continue;
        if (first == nullptr || second == nullptr) return false;
        if (first->data != second->data) return false;

        pending.push({first->left, second->right});
        pending.push({first->right, second->left});
    }

    return true;
}
```

The base cases are unchanged from the identical-tree algorithm. The initial pair is the root's two children, and every later pair uses opposite child directions.

### Iterative Dry Run

For the symmetric seven-node tree:

| Pair removed | Queue after processing the pair |
| --- | --- |
| Initial state | `[(L, R)]`, with values `(2, 2)` |
| `(L, R)` | `[(LL, RR), (LR, RL)]`, with values `(3, 3), (4, 4)` |
| `(LL, RR)` | `[(LR, RL), (#, #), (#, #)]` |
| `(LR, RL)` | `[(#, #), (#, #), (#, #), (#, #)]` |
| Remaining four null pairs | Each is skipped; the queue becomes empty |

All required pairs match, so the result is `true`.

For the asymmetric example where both `2` nodes have only a right child, processing `(L, R)` instead produces:

```text
[(#, 3), (3, #)]
```

The first pair immediately fails the structure check. If the symmetric example's rightmost `3` were changed to `5`, the outer pair `(3, 5)` would instead fail the value check.

The correctness argument follows the queue invariant: every pending pair must satisfy the mirror relation. Expanding a matching pair adds exactly its two required cross comparisons. An empty queue means that all of them succeeded.

## 8. Time and Space Complexity

All bounds below describe auxiliary space; the input trees are not counted. Empty inputs take `O(1)` time and space.

### Identical Trees

**Time:** `O(n1 + n2)` is a safe upper bound. Each expanded pair performs constant work and creates two child pairs. No node position is repeatedly expanded.

For these implementations, a tighter bound is **`O(min(n1, n2) + 1)`**. Expansion occurs only when both nodes exist and have equal values; the algorithm stops at the first mismatch. The `+1` accounts for comparing roots when one or both trees are empty. For identical trees with `n` nodes each, the running time is `O(n)`.

**Recursive space:** `O(min(h1, h2) + 1)`. Active calls follow corresponding downward paths. For two matching trees, this is conventionally written as `O(h)`: `O(log n)` for balanced trees and `O(n)` for skewed trees.

**Queue space:** `O(w1 + w2 + 1)` is a safe upper bound. The queue holds pairs from a level and the next level as BFS progresses. Null pairs are generated only from matching existing nodes and are never expanded, so they do not change the asymptotic bound. For matching trees of maximum width `w`, the bound is `O(w)` for nonempty trees.

### Symmetric Tree

**Time:** `O(n)`. On a symmetric tree, every non-root node participates in one non-null pair. Null positions also contribute only linear total work. A mismatch can stop the traversal early.

**Recursive space:** `O(h)` for a nonempty tree. The recursion follows mirrored paths, reaching `O(log n)` depth on a balanced tree and up to `O(n)` depth on a tall symmetric tree made of two mirrored chains.

**Queue space:** `O(w)` for a nonempty tree. The queue contains pending mirror pairs across at most two adjacent levels, including a constant number of null pairs per expanded pair. A broad tree can require `O(n)` queue space.

| Problem | Recursive auxiliary space | Iterative BFS auxiliary space |
| --- | --- | --- |
| Identical trees | `O(min(h1, h2) + 1)` | `O(w1 + w2 + 1)` |
| Symmetric tree | `O(h)` for nonempty trees | `O(w)` for nonempty trees |

These are upper bounds, not a claim that every input reaches them. A nontrivial one-sided chain is rejected by the symmetry check immediately because one root child is missing. In contrast, two matching chains require the identical-tree recursion to descend through their full height.

### Can We Use an Explicit Stack Instead?

Yes. Replace the queue with `stack<pair<const Node*, const Node*>>`, read with `top()`, and include `<stack>`. Keep the same pair checks and pairing rules. To reproduce the recursive order, push the second recursive pair first and the first recursive pair second.

This gives iterative DFS with the same time bounds and height-based auxiliary-space upper bounds. Actual stack occupancy can be smaller than recursion depth because the explicit stack stores pending pairs rather than all active function calls.

> **CP insight:** Choose based on the possible shape. Deep trees can overflow the recursive call stack, while wide trees can make BFS memory-heavy. An explicit DFS stack avoids recursion depth limits and keeps a height-based space bound.

## 9. Building and Running the Examples

Combine the shared setup, all four checking functions and the `areMirrors` helper with this `main`:

```cpp
int main() {
    Node a1(1), a2(2), a3(3), a4(4);
    a1.left = &a2;
    a1.right = &a3;
    a2.right = &a4;

    Node b1(1), b2(2), b3(3), b4(4);
    b1.left = &b2;
    b1.right = &b3;
    b2.right = &b4;

    cout << boolalpha;
    cout << "Identical (recursive): " << areIdentical(&a1, &b1) << '\n';
    cout << "Identical (iterative): "
         << areIdenticalIterative(&a1, &b1) << '\n';

    // Change only the position of b4 to demonstrate a structure mismatch.
    b2.right = nullptr;
    b2.left = &b4;
    cout << "After moving a child: " << areIdentical(&a1, &b1) << '\n';

    Node root(1), l(2), r(2), ll(3), lr(4), rl(4), rr(3);
    root.left = &l;
    root.right = &r;
    l.left = &ll;
    l.right = &lr;
    r.left = &rl;
    r.right = &rr;

    cout << "Symmetric (recursive): " << isSymmetric(&root) << '\n';
    cout << "Symmetric (iterative): " << isSymmetricIterative(&root) << '\n';

    rr.data = 5;
    cout << "After changing a value: " << isSymmetric(&root) << '\n';
}
```

Output:

```text
Identical (recursive): true
Identical (iterative): true
After moving a child: false
Symmetric (recursive): true
Symmetric (iterative): true
After changing a value: false
```

Only the demonstration code changes links or values to create new inputs. The checking functions leave the trees unchanged. All nodes here are local objects that remain alive until `main` finishes; do not call `delete` on them.

## 10. Edge Cases and Common Mistakes

### Identical Trees

| Input | Expected result |
| --- | --- |
| Both roots are null | `true` |
| Exactly one root is null | `false` |
| Single nodes with equal values | `true` |
| Single nodes with unequal values | `false` |
| Same values, but a child is on different sides | `false` |
| Same structure, but one corresponding value differs | `false` |
| Matching trees with repeated or negative values | `true` |
| Same node count and height, but different structures | `false` |

### Symmetric Tree

| Input | Expected result |
| --- | --- |
| Empty tree | `true` |
| Single node | `true` |
| Root has exactly one child | `false` |
| Equal-valued leaf children | `true` |
| Mirrored structure, but one mirrored pair has unequal values | `false` |
| Root has equal-valued children, each with only an equal-valued right child | `false` |
| Root has equal-valued children; the left has only a left leaf, and the right has only an equal-valued right leaf | `true` |
| All values are equal, but the structure is asymmetric | `false` |

Watch for these mistakes:

- **Checking only values.** Null child positions are part of the structure and must match under the chosen pairing rule.
- **Using pointer equality as tree equality.** Different addresses do not imply different structures or values.
- **Using `||` between the recursive comparisons.** Both child pairs must match, so use `&&`.
- **Using identical-tree child pairs for symmetry.** Symmetry requires cross comparisons at every recursive step.
- **Returning `true` after one successful queue pair.** Other pending pairs still need checking.
- **Skipping null children independently.** This loses the positional information needed to detect structure mismatches.
- **Reading `data` before the null checks.** A structure mismatch may otherwise cause an invalid pointer dereference.
- **Claiming recursion uses constant space.** Count the active call stack.

## 11. Interview Insights

### Explain the Pairing Rule Before the Code

A concise explanation is: “I compare two positions at a time. Both empty is a match; one empty or unequal values is a mismatch. Then I compare either corresponding children for identity or opposite children for a mirror.”

This explains the entire solution and makes the difference between the two problems explicit.

### Traversal Values Alone Can Lose Structure

Consider these trees:

```text
     1              1
    /                \
   2                  2
```

Both have preorder values `[1, 2]`, but they are not identical. A preorder serialization that includes null markers distinguishes them:

```text
Left-child tree:  1 2 # # #
Right-child tree: 1 # 2 # #
```

Comparing unambiguous serializations with null markers is a valid alternative, but it stores extra output and generally builds it before comparing. Direct node-pair comparison avoids those strings and can stop at the first mismatch.

Similarly, checking whether each level's **non-null values** forms a palindrome is not sufficient for symmetry. The asymmetric tree where both `2` nodes have only a right child has levels `[1]`, `[2, 2]`, and `[3, 3]`. All are palindromes, yet their positions do not mirror each other.

### Checking Symmetry Does Not Require Flipping the Tree

The conceptual relation is:

```text
root's left subtree == mirror(root's right subtree)
```

However, physically flipping a subtree modifies the input and would require restoration. Creating a mirrored copy requires additional nodes. Cross comparison checks this relation directly without either operation.

### Identity, Symmetry, and Flip Equivalence Are Different

- **Identity** preserves every left/right position.
- **Symmetry** requires a fixed reflection across the root.
- **Flip equivalence** allows selected nodes to exchange their children to make two trees match.

If an interviewer permits arbitrary child swaps, clarify the specification: the identical-tree algorithm here intentionally rejects trees whose child positions differ.

## Quick Recap

- Compare pairs of positions, including missing children.
- Two null pointers match; exactly one null pointer does not.
- Existing paired nodes must have equal values.
- Identical trees compare **left-to-left and right-to-right**.
- Mirror trees compare **left-to-right and right-to-left**.
- A tree is symmetric when its left and right subtrees are mirrors.
- Recursion uses height-based space; iterative BFS uses width-based space.
- Both problems support early rejection and require no changes to the input trees.

</READING_WIDGET>
