<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Kth Move in Tower of Hanoi — Count and Skip Recursive Blocks

## 1. Problem Statement

There are three rods, numbered `1`, `2`, and `3`, and `N` disks of different sizes. Disk `1` is the smallest and disk `N` is the largest.

Initially, all disks are on rod `1`, with the largest at the bottom. We want to move the entire tower to rod `3`, using rod `2` as temporary storage.

The usual rules apply:

1. Move only one disk at a time.
2. Move only the top disk of a rod.
3. Never place a larger disk on top of a smaller disk.

Follow the standard recursive Tower of Hanoi procedure:

- Move the top `N - 1` disks from the source to the auxiliary rod.
- Move disk `N` from the source to the target rod.
- Move the `N - 1` disks from the auxiliary rod to the target rod.

Given `N` and `K`, print **which disk moves, from which rod, and to which rod on the Kth move** of this procedure.

`K` is **1-based**: `K = 1` means the first move. We need one move, not the entire sequence or the board after `K` moves.

### Input and output convention for this lesson

The supplied notes do not specify judge constraints or an exact output format. For the runnable program here, we use:

- `1 ≤ N ≤ 63`.
- `1 ≤ K ≤ 2^N - 1`.
- One test case, with no test-case count.

These are the supported limits of this lesson's implementation, not a claim about an external judge's constraints.

```text
Input
N K

Output
Moving disk D from S to T
```

Here, `D` is the disk number, `S` is its source rod, and `T` is its destination rod. The wrapper prints `Invalid input` for numeric inputs outside the supported range. Adapt the final print statement if a judge expects only the rod numbers.

### Example

```text
Input
3 4

Output
Moving disk 3 from 1 to 3
```

Moving three disks takes seven moves. The fourth move is the central move of the largest disk.

> **Interview Insight — Define the ordering first:** “The Kth thing” is meaningful only after fixing an order. We are querying the move sequence produced by the standard recursive procedure, not an arbitrary legal sequence that may contain extra moves.

---

## 2. From Generating Everything to Finding One Thing

In the Recursion Foundation lesson, our function generated every move:

```cpp
void move(int n, int source, int target, int aux) {
    if (n == 1) {
        cout << source << " -> " << target << '\n';
        return;
    }

    move(n - 1, source, aux, target);
    cout << source << " -> " << target << '\n';
    move(n - 1, aux, target, source);
}
```

A direct way to find the Kth move is to maintain a counter while generating moves and stop when it reaches `K`. This is correct, but it still generates all `K - 1` earlier moves.

If `K` is near the end, we do almost as much work as printing the whole sequence.

The **Kth Solution pattern** asks a different question:

> Can we count the number of outputs in a recursive block without generating them?

If we can, we can skip whole blocks that do not contain the desired position.

Here, an output is a **move in a process**, rather than a complete solution. The same count-and-skip reasoning still applies.

---

## 3. Count the Moves in a Hanoi Instance

Let `M(n)` be the number of moves generated when moving `n` disks.

We use `M`, rather than `T`, to distinguish the **length of the full move sequence** from the **running time of the Kth-move query** that we will analyze later.

For one disk:

$$
M(1) = 1.
$$

For `n` disks, the two smaller instances each generate `M(n - 1)` moves, with one move between them:

$$
M(n) = 2M(n-1) + 1.
$$

### 3.1 Expand the recurrence

$$
\begin{aligned}
M(n)
&= 2M(n-1) + 1 \\
&= 2\bigl[2M(n-2) + 1\bigr] + 1 \\
&= 2^2M(n-2) + 2 + 1 \\
&= 2^2\bigl[2M(n-3) + 1\bigr] + 2 + 1 \\
&= 2^3M(n-3) + 2^2 + 2 + 1.
\end{aligned}
$$

Notice that each expansion reduces the argument by one more: after three expansions, the remaining term is `M(n - 3)`.

After `j` expansions:

$$
M(n) = 2^jM(n-j) + \sum_{i=0}^{j-1}2^i.
$$

We use `j` for the number of expansions so that it is not confused with the requested move index `K`.

### 3.2 Reach the base case

For `n ≥ 2`, choose `j = n - 1`, so that `n - j = 1`:

$$
\begin{aligned}
M(n)
&= 2^{n-1}M(1) + \sum_{i=0}^{n-2}2^i \\
&= 2^{n-1} + \frac{2^{n-1}-1}{2-1} \\
&= 2^{n-1} + 2^{n-1} - 1 \\
&= 2^n - 1.
\end{aligned}
$$

The formula also gives `M(1) = 1`, as required. It is convenient to define `M(0) = 0` for an empty subproblem.

| Number of disks | Number of moves |
| ---: | ---: |
| 0 | 0 |
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 5 | 31 |

We now know the length of a smaller Hanoi sequence **without executing it**.

---

## 4. Split the Sequence into Three Blocks

Consider an instance with `n` disks and rod roles `(source, target, aux)`.

Let:

$$
L = M(n-1) = 2^{n-1}-1.
$$

The move sequence consists of three consecutive blocks:

| Block | Action | Number of moves | Positions within this instance |
| --- | --- | ---: | --- |
| Left | Move `n - 1` disks from `source` to `aux` | `L` | `1` through `L` |
| Middle | Move disk `n` from `source` to `target` | `1` | `L + 1` |
| Right | Move `n - 1` disks from `aux` to `target` | `L` | `L + 2` through `2L + 1` |

Define the middle move's position:

$$
mid = L + 1 = 2^{n-1}.
$$

The answer must be in exactly one of these blocks.

### Case 1: `K < mid` — the left block

We need the Kth move of the first smaller instance:

```cpp
kthMove(n - 1, source, aux, target, k);
```

The local index stays `k` because nothing precedes this block within the current instance.

### Case 2: `K == mid` — the middle move

The answer is immediately known:

```text
Move disk n from source to target.
```

There is no need to visit either smaller instance.

### Case 3: `K > mid` — the right block

The first `L` moves and the middle move have already been skipped. That is `L + 1 = mid` moves in total.

The position relative to the right block is therefore:

$$
K' = K - mid.
$$

Recurse into:

```cpp
kthMove(n - 1, aux, target, source, k - mid);
```

> **CP Insight — Subtract everything you skip:** In the right block, subtract `L + 1`, not just `L`. The middle move also comes before the desired move. At `K = mid + 1`, the new local index must be exactly `1`.

<img src="images/toh-three-blocks.png" alt="The Hanoi move sequence splits into a left subproblem, the central move, and a right subproblem; compare K with mid and subtract mid when entering the right block" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 5. State and Recursive Contract

Our function is:

```cpp
kthMove(n, source, target, aux, k)
```

Its meaning is:

> Return the Kth move in the standard sequence that transfers disks `1..n` from `source` to `target`, using `aux` as the spare rod.

Every call satisfies:

$$
n \ge 1, \qquad 1 \le k \le 2^n - 1.
$$

The rod labels stay the same, but their **roles** change between calls:

| Selected block | New source | New target | New auxiliary | New index |
| --- | --- | --- | --- | --- |
| Left | `source` | `aux` | `target` | `k` |
| Right | `aux` | `target` | `source` | `k - mid` |

Passing the rods in the wrong order can identify the correct disk while reporting the wrong movement.

### 5.1 Why do disk numbers remain meaningful?

Both smaller instances operate on disks `1..n-1`. Disk `n` is excluded after its central move is identified or skipped. Thus, the central disk in a recursive call is still the disk numbered `n` in the original puzzle.

### 5.2 Why do we not simulate the rods?

The standard procedure already tells us which smaller transfer happens next. The parameters describe that transfer, even when we skip its earlier moves.

We are computing a move's identity, not physically executing the skipped steps. Larger disks that remain below the active smaller tower do not change its recursive move sequence.

### 5.3 Base case

For `n = 1`, the only valid local index is `k = 1`. Return the move of disk `1` from `source` to `target`.

An explicit base case also ensures that we never recurse to zero disks and then attempt a shift by `n - 1 = -1`.

### 5.4 How this differs from backtracking

In our earlier LCCM lessons, several choices might lead to valid answers, so we explored branches and restored shared state.

Here, the block sizes identify **one** relevant branch. There is no guessing, shared board mutation, or place/unplace operation.

We keep the discipline of stating the recursive contract, but this is **count-and-skip recursion**, not a search through every possible choice.

---

## 6. Dry Run: `N = 3`, `K = 6`

For reference, the complete sequence for moving three disks from rod `1` to rod `3` is:

| Move number | Disk | From | To |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 3 |
| 2 | 2 | 1 | 2 |
| 3 | 1 | 3 | 2 |
| 4 | 3 | 1 | 3 |
| 5 | 1 | 2 | 1 |
| 6 | 2 | 2 | 3 |
| 7 | 1 | 1 | 3 |

This table helps us verify the answer. The optimized algorithm does **not** generate it.

### Step 1: Start with three disks

```text
kthMove(3, source=1, target=3, aux=2, k=6)

mid = 2^(3 - 1) = 4
```

The blocks are:

- Moves `1..3`: move two disks from `1` to `2`.
- Move `4`: move disk `3` from `1` to `3`.
- Moves `5..7`: move two disks from `2` to `3`.

Since `6 > 4`, enter the right block. Skip four moves, giving local index `6 - 4 = 2`.

### Step 2: Query the right subproblem

```text
kthMove(2, source=2, target=3, aux=1, k=2)

mid = 2^(2 - 1) = 2
```

Now `k == mid`, so this is the central move of disk `2`:

```text
Moving disk 2 from 2 to 3
```

We answered the query using two function calls, without generating the five earlier moves.

<img src="images/toh-k6-dry-run.png" alt="For N equals 3 and K equals 6, skip the first four moves and query local move 2 of the right block, yielding disk 2 from rod 2 to rod 3" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 7. Dry Run: A Path Through Both Left and Right Blocks

Consider `N = 4`, `K = 5`, again moving from rod `1` to rod `3`.

| Call | `n` | Source | Target | Auxiliary | Local `k` | `mid` | Decision |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 4 | 1 | 3 | 2 | 5 | 8 | Left: keep `k = 5` |
| 2 | 3 | 1 | 2 | 3 | 5 | 4 | Right: set `k = 1` |
| 3 | 2 | 3 | 2 | 1 | 1 | 2 | Left: keep `k = 1` |
| 4 | 1 | 3 | 1 | 2 | 1 | — | Base case |

The answer is:

```text
Moving disk 1 from 3 to 1
```

Notice two independent updates:

1. The rod roles change when we select a smaller transfer.
2. The local index changes only when we skip a preceding block.

For the original sample `N = 3`, `K = 4`, neither descent is needed: the first call has `mid = 4` and returns disk `3`, from `1` to `3`, immediately.

<img src="images/toh-rod-role-path.png" alt="For N equals 4 and K equals 5, follow left, right, then left while updating source target and auxiliary roles; the answer is disk 1 from rod 3 to rod 1" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 8. Clean Runnable C++ Code

The function returns a small `Move` object so that the recursive logic is separate from output formatting.

```cpp
#include <iostream>
using namespace std;

struct Move {
    int disk;
    int from;
    int to;
};

// Precondition: 1 <= n <= 63 and 1 <= k <= 2^n - 1.
Move kthMove(int n, int source, int target, int aux,
             unsigned long long k) {
    if (n == 1) {
        return {1, source, target};
    }

    unsigned long long mid = 1ULL << (n - 1);

    if (k < mid) {
        return kthMove(n - 1, source, aux, target, k);
    }

    if (k == mid) {
        return {n, source, target};
    }

    return kthMove(n - 1, aux, target, source, k - mid);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long inputK;
    if (!(cin >> n >> inputK)) return 0;

    // Check the disk count before evaluating any shift.
    if (n < 1 || n > 63 || inputK < 1) {
        cout << "Invalid input\n";
        return 0;
    }

    unsigned long long k = static_cast<unsigned long long>(inputK);
    unsigned long long totalMoves = (1ULL << n) - 1;

    if (k > totalMoves) {
        cout << "Invalid input\n";
        return 0;
    }

    Move answer = kthMove(n, 1, 3, 2, k);
    cout << "Moving disk " << answer.disk
         << " from " << answer.from
         << " to " << answer.to << '\n';

    return 0;
}
```

### Why use `1ULL`?

The literal `1` has type `int`. Assigning `1 << exponent` to a wider variable does not make the shift itself wider; it has already been evaluated using the left operand's type.

`1ULL` performs the shift using `unsigned long long`. Under our supported range:

- Computing `totalMoves` shifts by at most `63`.
- Computing `mid` shifts by at most `62`.
- The largest valid `K` is `2^63 - 1`, which fits in `long long`.

Validate `n` **before** shifting. A negative shift count or a count at least the bit width of the left operand is invalid.

> **CP Insight — Use exact integer arithmetic for block boundaries:** Do not write `2 ^ n`: in C++, `^` is XOR, not exponentiation. Avoid floating-point `pow` for these integer ranks and boundaries. An exact shift, with a suitable type and checked exponent, directly expresses the intended power of two.

---

## 9. Why the Algorithm Is Correct

We prove correctness by induction on `n`, assuming the function receives a valid local index.

### Base case

For one disk, the sequence contains exactly one move: disk `1` from `source` to `target`. The only valid query is `k = 1`, and the function returns that move.

### Inductive step

Assume the function correctly answers valid queries for `n - 1` disks.

For `n` disks, the sequence has a left block of `mid - 1` moves, a central move at `mid`, and a right block of `mid - 1` moves.

- **If `k < mid`:** The desired move is in the left block. Its local index is unchanged, and the recursive call uses exactly that block's source, target, and auxiliary roles. It is correct by the induction hypothesis.
- **If `k == mid`:** The desired move is disk `n` from `source` to `target`, which is returned directly.
- **If `k > mid`:** The desired move is in the right block. Subtracting `mid` removes exactly the moves preceding that block. The recursive call uses the right block's rod roles, so it is correct by the induction hypothesis.

These cases are disjoint and cover every valid index.

### The recursive index stays valid

In the left case:

$$
1 \le k \le mid - 1 = 2^{n-1}-1.
$$

In the right case, since `k ≤ 2^n - 1 = 2mid - 1`:

$$
1 \le k-mid \le mid - 1 = 2^{n-1}-1.
$$

Thus every child call satisfies the same contract. Each descent reduces `n`, so the process terminates at a central move or the one-disk base case.

---

## 10. Time and Space Complexity

### Full generation versus one query

The original procedure visits both smaller instances:

$$
M(n) = 2M(n-1)+1 = 2^n-1.
$$

Generating all moves therefore takes `Θ(2^N)` time. Keeping all of them would also require `Θ(2^N)` storage; streaming them needs only the recursive stack.

The Kth-move function visits **at most one** smaller instance and performs constant work per call. Its worst-case running time satisfies:

$$
Q(n) = Q(n-1) + O(1) = O(n).
$$

| Approach | Worst-case time | Auxiliary space |
| --- | --- | --- |
| Generate every move and store it | `Θ(2^N)` | `Θ(2^N)` |
| Generate sequentially and stop at `K` | `O(N + K)` | `O(N)` |
| Count blocks and follow only the relevant one | `O(N)` | `O(N)` |

The `N` term for sequential generation accounts for descending to the first move; its worst case over all valid `K` is still exponential.

For a query at the top-level middle position, the optimized function returns in `O(1)` time. The first move may require descending through all `N` levels, giving the `O(N)` worst case.

We assume fixed-width integer operations are constant-time within the stated bounds. The recursive implementation uses `O(N)` stack frames; it does not store the full move sequence or the rods.

> **Interview Insight — Do not reuse the wrong recurrence:** `2Q(n-1)+1` describes exploring both children. Our query chooses one child, so its time recurrence is `Q(n-1)+O(1)`. The full sequence can be exponentially long while one indexed move is found in linear time.

---

## 11. Common Mistakes and Useful Insights

### 11.1 Mixing 0-based and 1-based indexing

This lesson uses `1 ≤ K ≤ 2^N - 1`. The central move is at `2^(N-1)`, not `2^(N-1) - 1`.

If using a 0-based index elsewhere, derive its boundaries separately instead of mixing conventions.

### 11.2 Subtracting only the left block

The right block begins after the left block **and** the middle move. Its index is `k - mid`, not `k - (mid - 1)`.

### 11.3 Keeping the rod roles unchanged

The left child transfers to the old auxiliary rod. The right child starts from the old auxiliary rod. Reusing `(source, target, aux)` unchanged describes the wrong subproblem.

### 11.4 Exploring both recursive calls

The point of counting is to avoid the irrelevant branch. Return immediately from the selected case. Generating the left branch before deciding whether `K` lies in the right branch loses the improvement.

### 11.5 Recomputing the move count recursively

Do not execute another two-branch recursion merely to calculate a block's size. We derived a closed form precisely so that each size comparison takes constant time.

### 11.6 Ignoring the query range

For `N = 3`, only moves `1..7` exist. Query `0` or `8` does not describe a move in the process. Without validation, recursion may return a meaningless answer rather than signal the invalid index.

### 11.7 Confusing the selected move with the state after it

The output identifies one disk transfer. Reconstructing the positions of every disk after `K` moves is a different task and is not needed here.

### 11.8 Does this need memoization?

No. A single query follows one path with strictly decreasing `n`; it does not repeatedly solve the same subproblem. The useful optimization is skipping counted blocks, not caching repeated work.

### Boundary tests

| `N` | `K` | Expected result |
| ---: | ---: | --- |
| 1 | 1 | Disk `1`, rod `1` to rod `3` |
| 2 | 1 | Disk `1`, rod `1` to rod `2` |
| 2 | 2 | Disk `2`, rod `1` to rod `3` |
| 2 | 3 | Disk `1`, rod `2` to rod `3` |
| 3 | 4 | Disk `3`, rod `1` to rod `3` |
| 3 | 5 | Disk `1`, rod `2` to rod `1` |
| 3 | 6 | Disk `2`, rod `2` to rod `3` |
| 4 | 5 | Disk `1`, rod `3` to rod `1` |
| 3 | 0 or 8 | `Invalid input` under our wrapper's convention |
| 63 | `2^62` | Disk `63`, rod `1` to rod `3` |

For small `N`, generate the full sequence and compare the optimized answer at every index. This checks disk numbers, rod-role changes, and boundary arithmetic together.

---

## 12. The Reusable Kth Solution Pattern

The important idea is broader than Tower of Hanoi:

1. Fix the order in which the process produces outputs.
2. Divide its output sequence into consecutive blocks.
3. Count how many outputs each block contains.
4. Locate the block containing the desired rank.
5. Subtract the sizes of all skipped blocks to obtain a local rank.
6. Recurse only inside the chosen block, or return if that block is one output.

For this problem:

```text
State
    disk count + source/target/auxiliary roles + local K

Block sizes
    2^(n-1) - 1, then 1, then 2^(n-1) - 1

Boundary
    mid = 2^(n-1)

Decision
    K < mid  → left child, same K
    K = mid  → move disk n from source to target
    K > mid  → right child, K becomes K - mid

Progress
    only one smaller instance is visited

Complexity
    O(N) worst-case time and O(N) recursive stack space
```

We are not making the complete Hanoi process shorter. It still contains `2^N - 1` moves. We are using its recursive structure to **find one move without executing the moves before it**.

</READING_WIDGET>
