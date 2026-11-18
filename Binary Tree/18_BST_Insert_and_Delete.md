<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# BST Insert and Delete Operations

A binary search tree is useful not only because we can search for a key, but also because we can **insert and delete keys while preserving its ordering**.

In [Binary Search Trees and Balanced BSTs](5_BST_and_Balanced_BST.md), we checked whether a tree satisfied BST ordering and height balance. Those checks did not modify the tree. This lesson complements that discussion by implementing the operations that change its values and links.

Insertion follows a search path until it finds an empty position. Deletion follows a search path too, but removing the node requires different actions depending on how many children it has.

## 1. Conventions and the Subtree-Root Contract

We use a **strict BST** throughout this lesson:

- Every key in a node's left subtree is smaller than its key.
- Every key in its right subtree is larger than its key.
- Both subtrees satisfy the same rule.

Keys are distinct. **Inserting an existing key leaves the tree unchanged**, and deleting a missing key also leaves it unchanged. Each operation assumes that its input is already a valid BST; it does not first validate or repair an arbitrary binary tree.

### Shared C++ Node Definition

All implementations use C++17 and this definition:

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    explicit Node(int value)
        : data(value), left(nullptr), right(nullptr) {}
};
```

Nodes in this lesson are created using `new` and released using `delete`. Each node belongs to exactly one tree, with no cycles or shared child nodes. The struct has no destructor that recursively deletes children, so deleting one node does not delete the subtree we reconnect in its place.

**Do not pass the stack-allocated example nodes from the validation lesson to these deletion functions.** Calling `delete` on a node that was not allocated with `new` is invalid.

Throughout the lesson, `n` is the number of nodes and `h` is the height measured in nodes: an empty tree has height `0`, and a leaf has height `1`.

### Why Return a Pointer?

An update can change the root of the subtree it receives:

- Inserting into an empty subtree creates its first root.
- Deleting a leaf makes that subtree empty.
- Deleting a node with one child promotes that child.

Our functions therefore follow one contract:

> **Return the root of the updated subtree.**

The caller must save that pointer, either in a child link or in the overall root:

```text
root->left = update(root->left, ...)
root->right = update(root->right, ...)
root = update(root, ...)
```

These assignments reconnect the updated subtree. Returning the right pointer is not enough if the caller ignores it.

## 2. BST Insertion: Find the Empty Position

To insert a key `x`, start at the root:

1. If the current subtree is empty, create a node containing `x`.
2. If `x` is smaller than the current key, insert into the left subtree.
3. If `x` is larger, insert into the right subtree.
4. If the keys are equal, return without inserting a duplicate.

For an absent key, the new node is attached as a **leaf**. Every comparison along the path contributes an ancestor constraint, so the final position satisfies the ordering of the entire tree.

### Recursive C++ Implementation

```cpp
Node* insertRecursive(Node* root, int x) {
    if (root == nullptr) {
        return new Node(x);
    }

    if (x < root->data) {
        root->left = insertRecursive(root->left, x);
    } else if (x > root->data) {
        root->right = insertRecursive(root->right, x);
    }
    // Equality: the key already exists, so nothing changes.

    return root;
}
```

Use it as `root = insertRecursive(root, x);`. In particular, the returned pointer becomes the overall root when the original tree is empty.

Notice the child assignments. If the left child was null, `insertRecursive(root->left, x)` returns a newly allocated node; assigning it to `root->left` makes that node reachable from its parent.

### Dry Run: Insert `65`

Start with this tree:

```text
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
```

| Current subtree root | Comparison | Action |
| --- | --- | --- |
| `50` | `65 > 50` | Insert into the right subtree |
| `70` | `65 < 70` | Insert into the left subtree |
| `60` | `65 > 60` | Insert into the right subtree |
| `nullptr` | Empty position | Create and return node `65` |

As recursion returns, `60->right` receives the new node. The calls at `70` and `50` return their existing subtree roots.

```text
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
           \
            65
```

The new key satisfies every relevant constraint: it is greater than `50`, smaller than `70`, and greater than `60`.

Trying to insert `65` again follows the same path, finds equality, and returns without allocating another node.

## 3. Iterative BST Insertion

The recursive version uses the call stack to remember where to reconnect the result. An iterative version can walk down the tree and attach the new node directly when it finds a missing child.

### C++ Implementation

```cpp
Node* insertIterative(Node* root, int x) {
    if (root == nullptr) {
        return new Node(x);
    }

    Node* cur = root;

    while (true) {
        if (x == cur->data) {
            return root;
        }

        if (x < cur->data) {
            if (cur->left == nullptr) {
                cur->left = new Node(x);
                return root;
            }
            cur = cur->left;
        } else {
            if (cur->right == nullptr) {
                cur->right = new Node(x);
                return root;
            }
            cur = cur->right;
        }
    }
}
```

Use it as `root = insertIterative(root, x);`.

The pointer `cur` moves along the search path, while `root` continues to identify the overall tree. At each iteration, we either return or move to an existing child, so `cur` is never null when its fields are accessed.

For the earlier insertion of `65`, `cur` follows `50 -> 70 -> 60`, then attaches `65` to `60->right`. Both insertion versions produce the same result for the same input tree and insertion sequence.

Allocation happens only after an empty position is found. Allocating a node before searching would require freeing that unused node when a duplicate is discovered.

## 4. BST Deletion: Search First, Then Reconnect

To delete `x`, first locate it using the usual BST comparisons:

- If `x < root->data`, delete from the left subtree.
- If `x > root->data`, delete from the right subtree.
- If the subtree is empty, the key is absent; return `nullptr`.
- On equality, handle the node according to its number of children.

| Children of the matched node | Replacement for that subtree root |
| --- | --- |
| Zero: a leaf | `nullptr` |
| One | Its only child |
| Two | Keep the node, copy a suitable replacement key, then remove the replacement's original node |

The following deletion dry runs are **independent**. Each starts from this same eight-node tree:

```text
        50
       /  \
     30    70
    / \   / \
   20 40 60 80
           \
            65
```

Its inorder sequence is:

```text
20 30 40 50 60 65 70 80
```

### Case A: Delete a Leaf

A leaf has no descendants to preserve. Release the node and return `nullptr` so its parent disconnects it.

**Dry run: delete `20`.**

| Step | Current node | Action |
| --- | --- | --- |
| 1 | `50` | `20 < 50`: recurse left |
| 2 | `30` | `20 < 30`: recurse left |
| 3 | `20` | Match; both children are null; delete the node and return `nullptr` |
| 4 | `30` | Assign the returned pointer to `30->left` |
| 5 | `50` | Retain the updated left subtree and return `50` |

Result:

```text
        50
       /  \
     30    70
       \  / \
       40 60 80
           \
            65
```

Inorder: `30 40 50 60 65 70 80`.

If the deleted leaf were the only node in the tree, the returned `nullptr` would become the overall root.

### Case B: Delete a Node with One Child

Replace the matched node with its only child. That child brings along its **entire subtree**, not just its own key.

**Dry run: delete `60`.**

| Step | Current node | Action |
| --- | --- | --- |
| 1 | `50` | `60 > 50`: recurse right |
| 2 | `70` | `60 < 70`: recurse left |
| 3 | `60` | Match; save its only child, node `65` |
| 4 | `60` | Delete node `60` and return the saved pointer to `65` |
| 5 | `70` | Set `70->left` to `65` |
| 6 | `50` | Retain the updated right subtree and return `50` |

Result:

```text
        50
       /  \
     30    70
    / \   / \
   20 40 65 80
```

Inorder: `20 30 40 50 65 70 80`.

Why is promotion valid? Every node below `60` already obeyed all constraints imposed by `60`'s ancestors. In particular, `65` is greater than `50` and smaller than `70`. Removing `60` does not change those relationships.

The same rule works when the only child is on the left. Save the child pointer **before** deleting the node; reading `root->left` or `root->right` afterward would access freed memory.

### Case C: Delete a Node with Two Children

Simply returning one child would lose the other subtree. Instead, choose a key that can replace the current key without violating ordering:

- **Inorder successor:** the smallest key in the right subtree.
- **Inorder predecessor:** the largest key in the left subtree.

For a node with two children, both candidates exist. The successor is found by taking one step right, then following left pointers. The predecessor is found by taking one step left, then following right pointers.

We will use the successor in the main implementation:

1. Find the minimum node in the right subtree.
2. Copy its key into the matched node.
3. Delete that key from the right subtree.
4. Reconnect the updated right subtree and return the current node.

**The successor cannot have a left child**, because that child would contain a smaller key in the right subtree. It can still have a right child. Removing its original node therefore reduces to the leaf or one-child case.

### Dry Run: Delete `50` Using Its Successor

The root has two children. Starting at its right child `70`, follow the left pointer to `60`. Since `60` has no left child, it is the successor.

| Step | Location | Action |
| --- | --- | --- |
| 1 | Root `50` | Match; both children exist |
| 2 | Right subtree | Follow `70 -> 60`; successor key is `60` |
| 3 | Root | Copy `60` into the root's `data` field |
| 4 | Right subtree rooted at `70` | Delete key `60`; descend left |
| 5 | Original node `60` | It has only a right child, `65`; delete it and return `65` |
| 6 | Node `70` | Set `70->left` to `65` |
| 7 | Root, now containing `60` | Reconnect its right subtree and return the root |

Result:

```text
        60
       /  \
     30    70
    / \   / \
   20 40 65 80
```

Inorder: `20 30 40 60 65 70 80`.

There is briefly a copied `60` at the root and an original `60` in the right subtree. **The operation is complete only after removing the original successor node.** Leaving both would violate our distinct-key policy.

The original root object remains allocated; only its key changes. The physically deleted object is the successor node. We are deleting a **key from the tree**, not necessarily freeing the object where that key was first found.

## 5. Recursive BST Deletion in C++

The first child check below handles both a leaf and a node with only a right child. For a leaf, the saved right-child pointer is simply null.

```cpp
Node* minimumNode(Node* root) {
    // Precondition: root is not nullptr.
    while (root->left != nullptr) {
        root = root->left;
    }
    return root;
}

Node* deleteNode(Node* root, int x) {
    if (root == nullptr) {
        return nullptr;
    }

    if (x < root->data) {
        root->left = deleteNode(root->left, x);
    } else if (x > root->data) {
        root->right = deleteNode(root->right, x);
    } else {
        // Case A, or Case B with only a right child.
        if (root->left == nullptr) {
            Node* child = root->right;
            delete root;
            return child;
        }

        // Case B with only a left child.
        if (root->right == nullptr) {
            Node* child = root->left;
            delete root;
            return child;
        }

        // Case C: both children exist.
        Node* successor = minimumNode(root->right);
        int replacement = successor->data;
        root->data = replacement;
        root->right = deleteNode(root->right, replacement);
    }

    return root;
}
```

Always call it as `root = deleteNode(root, x);`. This handles root deletion without a separate parent pointer or a special top-level case.

The call to `minimumNode` is safe because we reach it only after establishing that both children exist. After the recursive deletion, `successor` may point to freed memory; the function never accesses it again.

If `x` is missing, the search eventually reaches a null child. Returning that same null pointer and reconnecting each unchanged subtree leaves the whole tree unchanged.

### Using the Inorder Predecessor Instead

The predecessor approach is symmetric. Find the maximum of the left subtree, copy its key, and delete its original node **from the left subtree**.

Here is a complete alternative deletion function:

```cpp
Node* maximumNode(Node* root) {
    // Precondition: root is not nullptr.
    while (root->right != nullptr) {
        root = root->right;
    }
    return root;
}

Node* deleteNodeUsingPredecessor(Node* root, int x) {
    if (root == nullptr) return nullptr;

    if (x < root->data) {
        root->left = deleteNodeUsingPredecessor(root->left, x);
    } else if (x > root->data) {
        root->right = deleteNodeUsingPredecessor(root->right, x);
    } else {
        if (root->left == nullptr) {
            Node* child = root->right;
            delete root;
            return child;
        }
        if (root->right == nullptr) {
            Node* child = root->left;
            delete root;
            return child;
        }

        Node* predecessor = maximumNode(root->left);
        int replacement = predecessor->data;
        root->data = replacement;
        root->left = deleteNodeUsingPredecessor(
            root->left, replacement
        );
    }

    return root;
}
```

On the original example, deleting `50` this way finds `40` along `30 -> 40`, copies `40` into the root, and removes the original leaf `40` from `30->right`:

```text
        40
       /  \
     30    70
    /     / \
   20    60 80
           \
            65
```

The final inorder sequence is again `20 30 40 60 65 70 80`. Successor and predecessor replacement can produce different tree shapes while preserving the same remaining keys.

A predecessor cannot have a right child, but it may have a left child. In that situation, its left child is promoted when the original predecessor node is deleted.

## 6. Why Do These Updates Preserve BST Ordering?

### Insertion

At each comparison, only one subtree can contain the new key in a valid BST. Recursive insertion changes only that subtree, and the new key satisfies the ancestor constraints established by the search path. Creating a leaf at the null position therefore preserves ordering. An equal key causes no change.

### Deletion with Zero or One Child

Removing a leaf cannot introduce an ordering violation. When a node has one child, every key in the promoted subtree already satisfies the constraints of all ancestors, so reconnecting that subtree preserves ordering too.

### Deletion with Two Children

Let the matched key be `v` and its successor key be `s`:

- Every key in the left subtree is smaller than `v`, and `v < s`. Therefore, all left-subtree keys are smaller than `s`.
- Since `s` is the minimum of the right subtree and keys are distinct, all other right-subtree keys are larger than `s`.
- Removing the original `s` leaves a valid right subtree containing only keys greater than the new root key.

The replacement key came from the same subtree, so it also satisfies the restrictions imposed by higher ancestors. The predecessor argument is symmetric.

This is why we choose an **extreme key** from a child subtree. An arbitrary key from the right subtree might leave smaller keys on the new root's right side.

## 7. Running the Operations

Combine the headers, node definition, and functions above with the helpers and `main` below to form a complete C++17 program. The predecessor version is an optional alternative; this demonstration uses successor deletion.

```cpp
void printInorder(const Node* root) {
    if (root == nullptr) return;

    printInorder(root->left);
    cout << root->data << ' ';
    printInorder(root->right);
}

void destroyTree(Node* root) {
    if (root == nullptr) return;

    destroyTree(root->left);
    destroyTree(root->right);
    delete root;
}

Node* makeExampleTree() {
    Node* root = nullptr;
    int keys[] = {50, 30, 70, 20, 40, 60, 80, 65};

    for (int x : keys) {
        root = insertRecursive(root, x);
    }
    return root;
}

int main() {
    Node* root = makeExampleTree();
    root = insertIterative(root, 55);
    root = insertRecursive(root, 55);  // Duplicate: no change.

    cout << "After inserting 55: ";
    printInorder(root);
    cout << '\n';

    destroyTree(root);
    root = nullptr;

    // Rebuild the original tree for each independent deletion.
    int deletions[] = {20, 60, 50};
    for (int x : deletions) {
        root = makeExampleTree();
        root = deleteNode(root, x);

        cout << "After deleting " << x << ": ";
        printInorder(root);
        cout << '\n';

        destroyTree(root);
        root = nullptr;
    }
}
```

Output, ignoring the trailing space after each inorder traversal:

```text
After inserting 55: 20 30 40 50 55 60 65 70 80
After deleting 20: 30 40 50 60 65 70 80
After deleting 60: 20 30 40 50 65 70 80
After deleting 50: 20 30 40 60 65 70 80
```

`destroyTree` releases the nodes that remain after the operations. It visits children before deleting their parent. It receives its pointer by value, so the caller explicitly resets `root` afterward to avoid retaining a dangling pointer.

## 8. Complexity Analysis

For a nonempty tree, insertion and deletion depend on its height `h`:

| Operation | Worst-case time | Auxiliary space |
| --- | --- | --- |
| Recursive insertion | `O(h)` | `O(h)` call stack |
| Iterative insertion | `O(h)` | `O(1)` |
| Recursive deletion using successor | `O(h)` | `O(h)` call stack |
| Recursive deletion using predecessor | `O(h)` | `O(h)` call stack |
| Inorder traversal or tree cleanup | `O(n)` | `O(h)` call stack |

Auxiliary-space bounds exclude the tree's storage. A successful insertion allocates one new node, and a successful deletion frees one node. Operations on an empty input take constant time and space.

### Why Is Two-Child Deletion Still `O(h)`?

The algorithm follows a path to the target, walks to its successor, and then follows that successor path again during recursive deletion. A path segment may be visited twice, but the work is still bounded by a constant multiple of the tree height. It does not search every node in either subtree.

### Balanced Versus Skewed Trees

- If the tree has logarithmic height, an update takes `O(log n)` time.
- If it is a chain, an update can take `O(n)` time.
- Inserting `n` distinct sorted keys into an initially empty ordinary BST takes `O(n^2)` total time: successive insertions walk paths of increasing length.

**These implementations preserve BST ordering, not height balance.** Even if the initial tree is balanced, repeated insertions or deletions can make it unbalanced. A self-balancing BST needs additional operations, such as rotations and metadata updates, to maintain logarithmic height.

## 9. Edge Cases and Common Mistakes

| Situation | Expected behavior or required care |
| --- | --- |
| Insert into an empty tree | Create a node and save the returned root |
| Insert a duplicate key | Return the existing tree without allocating a node |
| Delete from an empty tree | Return `nullptr` |
| Delete a missing key | Leave all keys and links unchanged |
| Delete the only node | Free it and return `nullptr` |
| Delete the root with one child | Return that child as the new root |
| Delete a node with only a left child | Promote the left subtree |
| Delete a node with only a right child | Promote the right subtree |
| Successor is the immediate right child | Delete it from `root->right`; reconnect its right child if present |
| Successor is deeper and has a right child | Promote that child into the successor's old position |
| Predecessor has a left child | Promote that child into the predecessor's old position |
| Delete the same key twice | First call removes it; second call makes no change |
| Keys include `INT_MIN` or `INT_MAX` | Direct comparisons work; no sentinel keys or arithmetic adjustments are used |
| Tree is a long chain | Recursive operations may exhaust the call stack |

Common implementation mistakes include:

- **Ignoring returned subtree roots.** Both `root = deleteNode(root, x)` and child assignments matter. Otherwise, a parent can retain a pointer to a deleted node, or an insertion can remain disconnected.
- **Copying the successor key without removing its original node.** This leaves a duplicate in a strict BST.
- **Searching for the successor in the wrong place.** For the two-child case, take the minimum of the right subtree, not the minimum of the whole tree.
- **Assuming the successor is always a leaf.** It may have a right child, as `60` does in our dry run. Dropping that child would lose valid keys.
- **Reading a node after freeing it.** Save its replacement child before `delete`, then return immediately.
- **Claiming every BST update is logarithmic.** The bound is `O(h)` unless a logarithmic-height guarantee is available.

## 10. Interview and Competitive Programming Insights

### Explain the Return Value Before Writing the Cases

Saying “this function returns the updated subtree root” makes the recursive code easier to derive. The leaf returns null, the one-child case returns the child, and the two-child case returns the existing node after updating its key and child link.

This contract also explains why deleting the overall root needs no separate algorithm.

### Clarify Duplicate Semantics

The implementations here behave like a set of unique keys. If a problem requires duplicates, establish whether deletion removes one occurrence or every occurrence.

A frequency field can keep structural keys distinct: equal insertions increment the count, and deletion decrements it when the count is greater than one. Structural deletion occurs when the final occurrence is removed.

The two-child case then needs extra care. If a replacement node stores several occurrences, copying its key and count requires **removing that entire replacement node** from its original position. Calling an ordinary “delete one occurrence” routine there could leave the same structural key in two nodes. Duplicate support therefore requires changes beyond adding a counter to insertion.

### Distinguish Keys from Node Identity

Successor replacement changes the key stored in an existing node. If nodes also store associated data, the replacement must include the corresponding data so keys and values remain paired.

If a problem requires stable node identity or retains external pointers to nodes, copying keys may not meet its requirements. Physically transplanting the successor node is another approach, but requires more pointer updates. External pointers to any freed node must not be dereferenced.

### Match the Method to the Constraints

For problems that ask you to implement BST operations, be ready to explain these pointer updates directly. For problems that only need an ordered collection, C++ `std::set` and `std::map` provide logarithmic insertion, lookup, and deletion by key without writing a custom BST.

For a `std::multiset`, `erase(value)` removes all matching occurrences. To remove just one, find an occurrence, check that the iterator is not `end()`, and erase that iterator.

The recursive deletion shown here can use linear stack space on a skewed tree. If large adversarial inputs are allowed, an iterative deletion can track the parent or a pointer to the link being changed, avoiding recursive stack growth. That changes space usage, but does not improve the height-dependent time bound of an unbalanced BST.

### Check Both Ordering and Contents

A strictly increasing inorder traversal verifies BST ordering, but it does not by itself prove that the update preserved every required key. An implementation that accidentally drops a subtree might still produce sorted output.

After an operation, compare the inorder values with the expected set of keys as well. Test root deletion, absent keys, both one-child orientations, and a successor with a right child. Those cases expose pointer mistakes that a simple leaf-deletion example misses.

## Quick Recap

- BST insertion follows comparisons to an empty position and attaches a new leaf; duplicates are ignored under our policy.
- Recursive insertion uses `O(h)` stack space; iterative insertion uses `O(1)` auxiliary space.
- Deleting a leaf returns `nullptr`; deleting a node with one child returns that child.
- With two children, copy the inorder successor or predecessor key, then delete its original node from the appropriate subtree.
- A successor has no left child; a predecessor has no right child. Either may still have one child to reconnect.
- Save every returned subtree root, including the overall `root`.
- Updates take `O(h)` time and preserve ordering. Maintaining balance requires additional machinery.

</READING_WIDGET>
