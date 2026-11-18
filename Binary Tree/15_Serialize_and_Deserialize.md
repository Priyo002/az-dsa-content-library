<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Serialize and Deserialize a Binary Tree

A binary tree exists in memory as nodes connected by pointers. Those pointers cannot describe the tree in a file or a message: their addresses are meaningful only within the process that created them.

**Serialization** converts the tree into a string. **Deserialization** reads that string and constructs a new tree with the same values and structure.

The central question is: **how do we preserve both the node values and the positions of missing children?** We will solve it using two traversal orders: BFS, which records positions level by level, and DFS preorder, which records one complete subtree at a time.

## 1. Problem Statement

Implement two operations:

```cpp
string serialize(TreeNode* root);
TreeNode* deserialize(const string& data);
```

For every valid input tree, the following round trip must preserve its structure and values:

```text
Original tree → serialize → String → deserialize → Identical tree
```

The reconstructed nodes have new memory addresses. We require structural equality, not pointer equality.

Assume that:

- The input is a finite binary tree, with no cycles or shared child nodes.
- Each value fits in a C++ `int`. Values may repeat, be negative, or be zero.
- The tree is not necessarily a binary search tree.
- Serialization must not modify the original tree.
- Each deserializer receives a complete, valid string produced by its matching serializer.

We will use C++17. Let `n` be the number of real nodes, `h` the height measured in nodes, and `w` the maximum number of real nodes on any level. An empty tree has height `0`.

### Running Example

```text
           1
         /   \
        2     3
         \   /
         -4 2
```

This tree contains five nodes. The repeated value `2`, the negative value `-4`, and the missing children are intentional: our format must handle all three without ambiguity.

## 2. Why Node Values Alone Are Not Enough

Consider these trees:

```text
Tree A:              Tree B:

    1                    1
   /                      \
  2                        2
```

Both have preorder `1,2`. Their level-order sequences of real nodes are also `1,2`. A decoder cannot determine whether `2` was a left child or a right child.

We therefore record missing child positions using a **null marker**, written as `#`.

For example, preorder with null markers gives:

```text
Tree A: 1,2,#,#,#
Tree B: 1,#,2,#,#
```

The strings now distinguish the trees. `#` represents an empty subtree; it is not a node whose value happens to be special.

### How Is This Different from Reconstruction from Two Traversals?

In the earlier reconstruction problem, we were given inorder and preorder sequences containing only node values. Preorder identified the root, while inorder identified the boundary between its left and right subtrees. Distinct values were required by that reconstruction method to locate each root unambiguously.

Here, **we design the representation ourselves and explicitly encode the structure**. Preorder with null markers already tells us where each subtree ends, so a second traversal and an inorder-position map are unnecessary. Repeated values cause no problem because positions, rather than value uniqueness, determine the connections.

Plain preorder of a general binary tree is insufficient. Preorder **with null markers** is sufficient.

## 3. Design the String Format First

Both approaches will use the same token rules, but different traversal orders:

| Component | Encoding |
| --- | --- |
| Real node | Decimal integer, such as `12`, `0`, or `-4` |
| Empty subtree or child position | `#` |
| Token separator | Comma `,` |
| Empty tree | `#` |

We keep every null marker, use no spaces, and omit a trailing comma. For example, a single node containing `12` becomes `12,#,#` in both approaches.

Separators matter: the text `123` cannot tell us whether we meant one value `123`, the values `1` and `23`, or the values `12` and `3`. Each comma-delimited token must be read as a whole before converting it to an integer. Reading one character at a time as a node would fail for both multi-digit and negative values.

Do not use a numeric sentinel such as `-1` for null unless the problem explicitly excludes that value. `#` cannot collide with any integer value.

### How Many Tokens Are Written?

A nonempty binary tree with `n` nodes has `2n` child pointers. Exactly `n - 1` connect to real children, so the number of null child pointers is:

$$
2n - (n - 1) = n + 1.
$$

Both full encodings therefore contain:

```text
n value tokens + (n + 1) null tokens = 2n + 1 tokens
```

The empty tree is represented by one `#`, which also agrees with `2n + 1` for `n = 0`.

### Shared Node Definition and Parsing Helpers

Place these definitions before either codec. The two codec classes can coexist in one program.

```cpp
#include <cassert>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    explicit TreeNode(int value)
        : val(value), left(nullptr), right(nullptr) {}
};

void appendToken(string& data, const string& token) {
    if (!data.empty()) data += ',';
    data += token;
}

// Precondition: a complete token remains in the valid input string.
string readToken(const string& data, size_t& pos) {
    size_t end = data.find(',', pos);
    if (end == string::npos) end = data.size();

    string token = data.substr(pos, end - pos);
    pos = (end < data.size()) ? end + 1 : end;
    return token;
}
```

`pos` is the starting index of the next unread token. `readToken` finds the next comma, extracts that token, and advances the cursor. If there is no next comma, it reads through the end of the string.

For `12,-7,#`, the calls return `"12"`, `"-7"`, and `"#"`, moving `pos` from `0` to `3`, then `6`, then `7`. Integer tokens are converted using `stoi`; `#` must be checked before that conversion.

The cursor is passed by reference so every call advances the same position. The input string is passed by reference as well. We copy only the current token, not the remaining suffix or an entire array of tokens.

These are valid-input helpers, not general validators for external data. We will discuss malformed strings separately.

## 4. Approach 1: BFS Serialization and Deserialization

### Serialization: Record Every Queued Position

Ordinary BFS places real nodes in a queue. For serialization, we also enqueue their null children so missing positions are preserved.

1. Push the root, even if it is null.
2. Pop the front pointer.
3. If it is null, append `#` and continue.
4. Otherwise, append its value, then enqueue its left and right child pointers in that order.
5. Repeat until the queue is empty.

**A null pointer produces one token and no further queue entries.** Enqueuing children for a null entry would never terminate and would not describe a real tree.

### Serialization Dry Run

Queue entries below are shown from front to back. Subscripts distinguish the two nodes containing `2`; they are explanatory labels and are not part of the encoding.

```text
2a = left child of 1
2b = left child of 3
```

| Popped position | Token written | Queue after processing |
| --- | --- | --- |
| `1` | `1` | `2a, 3` |
| `2a` | `2` | `3, #, -4` |
| `3` | `3` | `#, -4, 2b, #` |
| Null | `#` | `-4, 2b, #` |
| `-4` | `-4` | `2b, #, #, #` |
| `2b` | `2` | `#, #, #, #, #` |
| Five null positions | `#,#,#,#,#` | Empty |

The complete BFS string is:

```text
1,2,3,#,-4,2,#,#,#,#,#
```

The `#` after `3` is essential: it reserves the missing left child of the first `2`, so `-4` is attached as that node's right child.

### Deserialization: Give Each Real Parent Two Child Tokens

Read the first token to determine the root. If it is `#`, return `nullptr`. Otherwise, create the root and put it in a queue.

Now repeatedly pop one real parent and read exactly two tokens:

- The first describes its left child.
- The second describes its right child.

For each non-null token, create the child, attach it, and enqueue it. For `#`, leave that pointer null.

The decoder queues **only real nodes**, because only real nodes need children assigned. Null child tokens are consumed immediately.

### C++ Implementation

```cpp
class BFSCodec {
public:
    string serialize(TreeNode* root) {
        string data;
        queue<TreeNode*> pending;
        pending.push(root);

        while (!pending.empty()) {
            TreeNode* node = pending.front();
            pending.pop();

            if (node == nullptr) {
                appendToken(data, "#");
                continue;
            }

            appendToken(data, to_string(node->val));
            pending.push(node->left);
            pending.push(node->right);
        }

        return data;
    }

    TreeNode* deserialize(const string& data) {
        size_t pos = 0;
        string token = readToken(data, pos);
        if (token == "#") return nullptr;

        TreeNode* root = new TreeNode(stoi(token));
        queue<TreeNode*> pending;
        pending.push(root);

        while (!pending.empty()) {
            TreeNode* parent = pending.front();
            pending.pop();

            token = readToken(data, pos);
            if (token != "#") {
                parent->left = new TreeNode(stoi(token));
                pending.push(parent->left);
            }

            token = readToken(data, pos);
            if (token != "#") {
                parent->right = new TreeNode(stoi(token));
                pending.push(parent->right);
            }
        }

        return root;
    }
};
```

No level-size loop is needed. FIFO order already ensures that parents receive their children in the same order in which the serializer visited them.

### Deserialization Dry Run

Read `1`, create the root, and initialize the queue to `[1]`. The remaining tokens are assigned as follows:

| Parent popped | Left token | Right token | Queue after attaching children |
| --- | --- | --- | --- |
| `1` | `2` | `3` | `2a, 3` |
| `2a` | `#` | `-4` | `3, -4` |
| `3` | `2` | `#` | `-4, 2b` |
| `-4` | `#` | `#` | `2b` |
| `2b` | `#` | `#` | Empty |

Every token has been consumed, and every real node has both child positions assigned. The result is the original shape, including the right child `-4` and both occurrences of `2`.

### Why Does BFS Decoding Work?

The serializer writes the root first and then emits child positions in left-to-right order for real parents in BFS order. Null positions do not generate descendants.

The decoder maintains exactly that order of real parents in its queue. When it pops a parent, the next two tokens must describe that parent's left and right children. Creating and enqueuing the non-null children preserves the same order for subsequent parents.

Starting with the correct root, each step therefore restores the correct child pointers. When the queue is empty, the complete tree has been restored.

## 5. Approach 2: DFS Preorder with Null Markers

### Serialization: Encode One Subtree at a Time

Preorder visits:

```text
Root → Left subtree → Right subtree
```

Extend it with a rule for empty subtrees:

```text
encode(null) = #
encode(node) = value, encode(left), encode(right)
```

A real node always has two subtree encodings after its value. A null marker completes an empty subtree immediately.

For the running example:

```text
Left subtree of 1:   2,#,-4,#,#
Right subtree of 1:  3,2,#,#,#

Complete string:    1,2,#,-4,#,#,3,2,#,#,#
```

Notice that this differs from the BFS string. The format includes the traversal convention, not just the comma and null-marker rules. A BFS string must go to the BFS decoder, and a preorder string must go to the preorder decoder.

### Deserialization: Each Call Consumes Exactly One Subtree

At the current cursor:

1. Read one token.
2. If it is `#`, return `nullptr`.
3. Otherwise, create a node with that value.
4. Recursively decode its left subtree.
5. Recursively decode its right subtree.
6. Return the node.

The important contract is: **a call returns the decoded subtree and leaves the shared cursor immediately after that subtree's encoding**.

We do not search for a dividing index between the left and right subtrees. The recursive calls consume exactly the tokens belonging to each side.

### C++ Implementation

```cpp
class DFSCodec {
private:
    void write(TreeNode* node, string& data) {
        if (node == nullptr) {
            appendToken(data, "#");
            return;
        }

        appendToken(data, to_string(node->val));
        write(node->left, data);
        write(node->right, data);
    }

    TreeNode* read(const string& data, size_t& pos) {
        string token = readToken(data, pos);
        if (token == "#") return nullptr;

        TreeNode* node = new TreeNode(stoi(token));
        node->left = read(data, pos);
        node->right = read(data, pos);
        return node;
    }

public:
    string serialize(TreeNode* root) {
        string data;
        write(root, data);
        return data;
    }

    TreeNode* deserialize(const string& data) {
        size_t pos = 0;
        return read(data, pos);
    }
};
```

The cursor is local to each public `deserialize` call, so using the same codec object repeatedly does not retain an old position. Recursive calls share that cursor by reference.

Serialization appends to one shared string. Returning a separate string from every recursive call and repeatedly concatenating subtree strings can copy the same content many times, leading to quadratic work on a skewed tree.

### Dry Run: Follow the Recursive Calls

Number the tokens from `0` to `10`:

```text
Token index:  0  1  2   3  4  5  6  7  8  9 10
Token:       1  2  #  -4  #  #  3  2  #  #  #
```

These are token indices for explanation; the code's `pos` is a character index in the string.

| Token index | Subtree being decoded | Action |
| --- | --- | --- |
| 0 | Whole tree | Create `1`; begin its left subtree |
| 1 | Left of `1` | Create `2`; begin its left subtree |
| 2 | Left of the first `2` | Return null |
| 3 | Right of the first `2` | Create `-4` |
| 4 | Left of `-4` | Return null |
| 5 | Right of `-4` | Return null; finish `-4`, then finish the first `2` |
| 6 | Right of `1` | Create `3`; begin its left subtree |
| 7 | Left of `3` | Create the second `2` |
| 8 | Left of the second `2` | Return null |
| 9 | Right of the second `2` | Return null; finish the second `2` |
| 10 | Right of `3` | Return null; finish `3`, then finish `1` |

After token `5`, the entire left subtree of `1` is complete. The next token, `3`, therefore starts its right subtree. No subtree sizes or value comparisons are needed.

### Why Does Preorder Decoding Work?

Use structural induction on the subtree being serialized.

- **Empty subtree:** Serialization writes `#`. Deserialization reads it and returns null, consuming exactly one token.
- **Nonempty subtree:** Serialization writes the root value, then the complete left encoding, then the complete right encoding. Deserialization creates the same root value. By the induction hypothesis, its first recursive call reconstructs and consumes exactly the left subtree. Its second call therefore starts at the correct position and reconstructs exactly the right subtree.

Connecting these children produces the original subtree and leaves the cursor at the next unread token. Applied to the root, this proves the round trip for the whole tree.

## 6. Complexity and Choosing an Approach

Let `L` be the number of characters in the encoded string. Both methods emit and consume `2n + 1` tokens. The cursor only moves forward, so delimiter searches and token parsing scan `O(L)` characters in total.

Appending to the shared string takes amortized `O(L)` total time under the usual dynamic-string growth model. Each real node is allocated once during deserialization.

For fixed-width `int` values, each token has a bounded number of characters, so `L = O(n + 1)`. For nonempty trees, this gives the usual `O(n)` bounds:

| Approach | Serialization time | Deserialization time | Auxiliary space, excluding input and output |
| --- | --- | --- | --- |
| BFS | `O(n)` | `O(n)` | `O(w)` queue |
| DFS preorder | `O(n)` | `O(n)` | `O(h)` recursion stack |

For an empty tree, both operations take constant time and space.

The BFS serializer also queues null positions, but each real node contributes only two child positions. The queue contains positions from at most two consecutive levels, so its size remains `O(w)` for nonempty trees. It is not an array containing every position of a hypothetical complete tree.

Keep these storage costs separate:

- The serialized output string occupies `O(L)` space.
- The reconstructed output tree occupies `O(n)` space.
- The shown parser copies only one bounded-size integer or null token per active call; it does not first split the entire input into a token vector.

An implementation using `istringstream` may hold an additional copy of the input string, while splitting into a vector stores all tokens. Account for that `O(L)` storage if using those alternatives.

On a balanced tree, DFS uses `O(log n)` call-stack space, while BFS may queue `O(n)` nodes. On a chain, BFS uses `O(1)` queue space, while recursive DFS uses `O(n)` stack space and may exceed the runtime's call-stack limit. For very deep trees, choose BFS or implement DFS with an explicit stack.

## 7. Verify the Round Trip

The strongest basic check compares the reconstructed tree's values **and structure** with the original. Comparing only ordinary preorder values would miss some left/right placement errors.

Place this driver after the shared definitions and both codecs:

```cpp
bool identical(TreeNode* a, TreeNode* b) {
    if (a == nullptr || b == nullptr) return a == b;
    return a->val == b->val
        && identical(a->left, b->left)
        && identical(a->right, b->right);
}

void deleteTree(TreeNode* root) {
    if (root == nullptr) return;
    stack<TreeNode*> pending;
    pending.push(root);

    while (!pending.empty()) {
        TreeNode* node = pending.top();
        pending.pop();
        if (node->left != nullptr) pending.push(node->left);
        if (node->right != nullptr) pending.push(node->right);
        delete node;
    }
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->right = new TreeNode(-4);
    root->right->left = new TreeNode(2);

    BFSCodec bfs;
    DFSCodec dfs;
    string bfsData = bfs.serialize(root);
    string dfsData = dfs.serialize(root);
    TreeNode* bfsCopy = bfs.deserialize(bfsData);
    TreeNode* dfsCopy = dfs.deserialize(dfsData);

    assert(identical(root, bfsCopy));
    assert(identical(root, dfsCopy));
    assert(bfs.serialize(bfsCopy) == bfsData);
    assert(dfs.serialize(dfsCopy) == dfsData);
    assert(bfs.serialize(nullptr) == "#");
    assert(dfs.serialize(nullptr) == "#");
    assert(bfs.deserialize("#") == nullptr);
    assert(dfs.deserialize("#") == nullptr);

    cout << "BFS: " << bfsData << '\n';
    cout << "DFS: " << dfsData << '\n';
    cout << "Both round trips preserve the tree.\n";

    deleteTree(root);
    deleteTree(bfsCopy);
    deleteTree(dfsCopy);
}
```

Output:

```text
BFS: 1,2,3,#,-4,2,#,#,#,#,#
DFS: 1,2,#,-4,#,#,3,2,#,#,#
Both round trips preserve the tree.
```

Each deserializer allocates new nodes with `new`; the caller owns the returned tree and must release it. The equality helper is recursive and suitable for these small examples. Use an iterative comparison when testing very deep trees.

## 8. Edge Cases and Format Boundaries

| Case | BFS encoding | DFS preorder encoding |
| --- | --- | --- |
| Empty tree | `#` | `#` |
| Single node `12` | `12,#,#` | `12,#,#` |
| Root `1`, only left child `2` | `1,2,#,#,#` | `1,2,#,#,#` |
| Root `1`, only right child `2` | `1,#,2,#,#` | `1,#,2,#,#` |
| Root `1`, children `2` and `3` | `1,2,3,#,#,#,#` | `1,2,#,#,3,#,#` |
| Root `0`, only left child `-12` | `0,-12,#,#,#` | `0,-12,#,#,#` |
| Root `5`, children both `5` | `5,5,5,#,#,#,#` | `5,5,#,#,5,#,#` |

Also test longer left-only and right-only chains, broad trees, alternating missing children, and `INT_MIN`/`INT_MAX`. No arithmetic is performed on node values; `to_string` and `stoi` handle valid values throughout the `int` range.

### Can We Remove Trailing Null Markers?

For BFS, a compact format can omit the trailing run of `#` tokens **if its decoder explicitly treats all remaining child positions as null once the input ends**. Interior null markers must remain because they determine which child receives each subsequent value.

For example, the running BFS encoding could be shortened to:

```text
1,2,3,#,-4,2
```

That is a different format contract. The BFS decoder shown above expects two explicit tokens per real parent and does not accept this shortened form. Similarly, the shown DFS decoder requires the complete preorder encoding; do not remove markers without defining and implementing a compatible decoding rule.

Keeping all markers makes the initial implementation easier to derive, trace, and verify.

### What If the Input String Is Malformed?

Our problem contract guarantees valid serializer output. An empty string is therefore invalid; the empty-tree string is `#`.

If validation is required, extend the parser and decoder to reject:

- Missing tokens, such as `1,#` in the full format.
- Extra tokens after a complete tree, such as `#,#`.
- Empty tokens, unexpected separators, or tokens such as `12x`.
- Integer values outside the supported range.

`stoi` alone is not a strict validator: it can parse the numeric prefix of `12x`. Use its consumed-character count, or a checked `from_chars` parser, to require a complete integer token. Also check that a token remains before reading and that the entire input has been consumed after building the tree.

If decoding can fail after some nodes have been allocated, release that partial tree or use an ownership strategy that cleans it up automatically. The interview implementations above rely on valid input and do not provide malformed-input handling.

## 9. Interview and Competitive Programming Insights

- **State the format before writing code.** Specify the traversal order, separator, null marker, empty-tree encoding, and whether trailing nulls are retained. Most decoder bugs begin with an unclear agreement between the two operations.
- **Explain why duplicates work.** Neither method searches for a node by value. Each token is assigned to a particular position determined by the queue or recursive call.
- **Do not store node addresses or reuse the original root.** The decoder must reconstruct from the string alone, even if the original tree no longer exists.
- **Keep the left/right order consistent.** BFS enqueues left before right; DFS writes and reads the complete left subtree before the right subtree.
- **Reset parser state for every call.** A member or global index left over from an earlier decode will break subsequent calls. A local cursor passed by reference avoids this issue.
- **Do not confuse this BFS format with heap indexing.** Children of array index `i` are not necessarily at `2i + 1` and `2i + 2` here: null positions do not contribute child entries. The queue determines parent-child relationships.
- **Use BST properties only when promised.** A BST can sometimes be encoded without null markers and rebuilt using ordering bounds, with a clear duplicate policy. That reasoning does not apply to a general binary tree.

### Follow-up: Validate a Full Preorder Encoding Without Building a Tree

Track the number of unfilled child positions, often called **slots**:

1. Start with one slot for the root.
2. Before each token, require at least one available slot.
3. Every token consumes one slot.
4. A real node creates two new child slots; `#` creates none.
5. After the last token, require exactly zero slots.

For `1,2,#,#,#`:

```text
Before any token: 1 slot
Read 1:          2 slots
Read 2:          3 slots
Read #:          2 slots
Read #:          1 slot
Read #:          0 slots → valid
```

Checking only that there are `n + 1` null markers is insufficient: `#,1,#` has the correct total counts but closes the tree before all tokens have been read. The slot rule catches that invalid prefix.

After checking token syntax, this validates the full preorder structure in `O(L)` time and `O(1)` auxiliary space without allocating nodes. It is a useful follow-up when the task asks only whether a serialization is valid.

## 10. Quick Recap

- Serialization must preserve structure as well as values. Null markers distinguish missing left and right children.
- BFS writes queued positions in level order; its decoder assigns two child tokens to each queued real parent.
- DFS preorder writes a root followed by its left and right encodings; each recursive decoding call consumes exactly one subtree.
- Both complete formats use `2n + 1` tokens and support repeated, negative, and multi-digit values.
- Both operations take `O(n)` time for fixed-width integers. BFS uses `O(w)` auxiliary space, while recursive DFS uses `O(h)`.
- Unlike reconstruction from ordinary inorder and preorder, explicit null markers provide the structural information directly, so a second traversal is unnecessary.

</READING_WIDGET>
