<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# K Knights — Backtracking Using LCCM

## 1. Problem Statement

You are given `K` knights and an empty `N × N` chessboard. Count the number of ways to place exactly `K` knights such that no two knights attack each other.

- A cell can contain at most one knight.
- The knights are identical: exchanging two knights does not create a new arrangement.
- An arrangement is determined by its set of occupied cells.
- Rotations and reflections count as different arrangements if they occupy different sets of cells. We are not grouping arrangements by symmetry.

Assume `N >= 1` and `K >= 0`.

### Input format

Two integers `N` and `K`.

### Output format

Print the number of valid arrangements.

### Example

```text
Input
3 2

Output
28
```

There are `36` ways to choose two cells from a `3 × 3` board. Eight of these pairs attack each other, leaving `28` valid arrangements. We will obtain this count through backtracking.

---

## 2. How Does a Knight Attack?

A knight moves in an L-shape:

- two cells along one direction, and
- one cell perpendicular to that direction.

A knight at `(row, col)` can attack these eight positions, provided they are inside the board:

```text
(row - 2, col - 1)    (row - 2, col + 1)
(row - 1, col - 2)    (row - 1, col + 2)
(row + 1, col - 2)    (row + 1, col + 2)
(row + 2, col - 1)    (row + 2, col + 1)
```

For example, a knight at `(0, 0)` on a `3 × 3` board attacks `(1, 2)` and `(2, 1)`.

Knights jump over pieces. We only need to inspect the destination cells; pieces between the two cells do not block an attack.

### Why is this different from N-Queens?

In N-Queens, at most one queen can be placed in each row. That allowed us to use the row as the recursive level.

Knights do not attack along an entire row or column. Two knights in the same row can be perfectly safe.

Therefore, placing exactly one knight per row would miss valid arrangements. Our recursive level must represent something different.

> **Interview Insight — Reuse the framework, not the old state:** LCCM still applies, but the level and choices must follow the new problem's constraints. The row-by-row queen placement cannot be copied directly into this problem.

---

## 3. The Main Idea: Decide Each Cell Once

Process the board in row-major order: finish one row from left to right, then move to the next row.

For `N = 3`, assign these cell indices:

```text
0  1  2
3  4  5
6  7  8
```

At every cell, we make one of two decisions:

1. **Place** a knight, if the cell is safe.
2. **Skip** the cell and leave it empty.

Both choices advance to the next cell.

### Converting an index to board coordinates

For a cell index `level`:

```cpp
int row = level / n;
int col = level % n;
```

For example, when `N = 3` and `level = 5`:

```text
row = 5 / 3 = 1
col = 5 % 3 = 2
```

So we are deciding cell `(1, 2)`.

### Why not place the first knight, then the second, and so on?

If each knight could choose any unused cell, the same final board could be reached through different placement orders:

```text
Place at cell 0, then cell 1.
Place at cell 1, then cell 0.
```

These are the same arrangement because the knights are identical.

The cell-by-cell method avoids this duplication. Cell `0` is always decided before cell `1`, so each final arrangement has exactly one decision path.

> **Interview Insight — Count combinations, not placement orders:** A valid answer is a set of `K` occupied cells. Giving every cell a fixed decision order avoids counting a board repeatedly in different knight-placement orders.

---

## 4. State and Recursive Invariant

We maintain:

```text
board[row][col] = 1 if the cell currently contains a knight
board[row][col] = 0 otherwise

level  = index of the cell being decided
placed = number of knights currently on the board
```

The recursive function is:

```cpp
rec(level, placed)
```

### What does this function mean?

Given the decisions already made for cells before `level`, count the valid ways to complete the remaining cells so that the final board contains exactly `K` knights.

Before each call:

- cells `0` through `level - 1` have been decided,
- exactly `placed` of those cells contain knights,
- none of the placed knights attack each other, and
- all cells from `level` onward are undecided and currently empty.

Notice that `placed` is not necessarily equal to `level`. Skipping a cell increases `level` without increasing `placed`.

---

## 5. Applying the LCCM Framework

| Part | Question | K-Knights answer |
| --- | --- | --- |
| **Level** | What are we deciding now? | Whether to occupy the current cell |
| **Choice** | What decisions are possible? | Place a knight or skip the cell |
| **Check** | Is this choice feasible? | Placement must not attack an existing knight; skipping introduces no conflict |
| **Move** | How do we explore the decision? | Update the board if placing, recurse to the next cell, then undo the placement |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/65ca4bc0-e364-4f45-a03d-27d6084485c5.png" alt="K-Knights LCCM using the current cell as the level, with place or skip choices and one knight already placed" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 5.1 Level — the current cell

There are `N × N` cells. The level advances by one in both branches:

```text
level → level + 1
```

We stop examining cells when `level == N × N`.

### 5.2 Choice — place or skip

Unlike N-Queens, every row can contain zero, one, or multiple knights. Deciding individual cells gives us that flexibility.

The code explores the placement branch first, followed by the skip branch. Either order gives the same count.

### 5.3 Check — can we safely place a knight?

We could inspect all eight possible attacking positions. Since there are only eight, this would still take `O(1)` time.

However, the recursive invariant allows us to inspect just four:

```text
(row - 2, col - 1)    (row - 2, col + 1)
(row - 1, col - 2)    (row - 1, col + 2)
```

Why are these enough?

- Only cells earlier in row-major order can contain knights.
- A knight never attacks another cell in the same row.
- The four remaining attack positions lie in later rows, which are still empty.

For each of the four earlier positions, first check whether it lies inside the board. If it contains a knight, reject the placement.

This optimization is valid because of our fixed traversal order. An arbitrary placement order would require checking all eight positions.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7621a799-ce08-46c2-86ef-284a8b561113.png" alt="A knight at row 2, column 2 attacks eight cells; the four in earlier rows are checked during row-major backtracking" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 5.4 Move — update, recurse, and restore

For the placement choice:

```cpp
board[row][col] = 1;
ans += rec(level + 1, placed + 1);
board[row][col] = 0;
```

For the skip choice:

```cpp
ans += rec(level + 1, placed);
```

Skipping does not modify the board, so it needs no undo operation.

Also, `placed` is passed by value. Calling `rec(level + 1, placed + 1)` does not change the caller's `placed`, so there is no `placed--` afterward. The shared board is what we must explicitly restore.

---

## 6. Base Cases and Early Pruning

### 6.1 We have placed exactly K knights

```cpp
if (placed == k) {
    return 1;
}
```

The current placement is valid because every knight passed the safety check.

Even if some cells have not been examined, there is exactly one way to finish: leave all remaining cells empty. Therefore, we can count this arrangement immediately.

This also handles `K = 0`: the empty board is one valid arrangement.

### 6.2 All cells are exhausted

```cpp
if (level == totalCells) {
    return 0;
}
```

Because the success case was checked first, reaching this line means there are no cells left but fewer than `K` knights have been placed.

The order matters: a valid arrangement completed in the last cell must return `1`, not `0`.

### 6.3 Too few cells remain

The number of undecided cells is:

```text
remainingCells = totalCells - level
```

The number of knights still required is:

```text
needed = K - placed
```

If `remainingCells < needed`, this branch cannot succeed even if every remaining cell were safe.

```cpp
if (totalCells - level < k - placed) {
    return 0;
}
```

For example, on a `3 × 3` board, `rec(8, 0)` with `K = 2` has only one cell left but still needs two knights. It immediately returns `0`.

> **CP Insight — Prune using an optimistic upper bound:** Pretend every remaining cell is usable. If even this optimistic situation cannot supply enough knights, the branch is certainly impossible. Having enough cells, however, does not guarantee success; attacks may still prevent placement.

---

## 7. Clean Runnable C++ Code

```cpp
#include <iostream>
#include <vector>
using namespace std;

int n, k;
int totalCells;
vector<vector<int>> board;

bool check(int row, int col) {
    // Only earlier rows can contain attacking knights.
    const int dr[4] = {-2, -2, -1, -1};
    const int dc[4] = {-1, 1, -2, 2};

    for (int direction = 0; direction < 4; direction++) {
        int previousRow = row + dr[direction];
        int previousCol = col + dc[direction];

        if (previousRow >= 0 && previousRow < n &&
            previousCol >= 0 && previousCol < n) {
            if (board[previousRow][previousCol] == 1) {
                return false;
            }
        }
    }

    return true;
}

long long rec(int level, int placed) {
    // Success: all remaining cells must stay empty.
    if (placed == k) {
        return 1;
    }

    // Failure: no cells remain, but we still need knights.
    if (level == totalCells) {
        return 0;
    }

    // Prune if too few cells remain to reach k.
    if (totalCells - level < k - placed) {
        return 0;
    }

    int row = level / n;
    int col = level % n;
    long long ans = 0;

    // Choice 1: place a knight here, if safe.
    if (check(row, col)) {
        board[row][col] = 1;
        ans += rec(level + 1, placed + 1);
        board[row][col] = 0;  // Undo before exploring the next choice.
    }

    // Choice 2: leave this cell empty.
    ans += rec(level + 1, placed);

    return ans;
}

void solve() {
    cin >> n >> k;
    totalCells = n * n;

    if (k > totalCells) {
        cout << 0 << '\n';
        return;
    }

    board.assign(n, vector<int>(n, 0));
    cout << rec(0, 0) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

No board-size limits were specified in the problem statement. This is a combinatorial backtracking solution: its practicality depends on both `N` and `K`, as explained in Section 10. The code assumes that `N × N` fits in `int` and the final count fits in `long long`; larger exact counts require an arbitrary-precision integer type.

---

## 8. Dry Run: N = 3, K = 2

We use the following cell indices:

```text
0  1  2
3  4  5
6  7  8
```

Initially, the board is empty and we call `rec(0, 0)`.

### 8.1 The first successful arrangement

The code tries placement before skipping.

| Call | Occupied cells on entry | Decision | Next step |
| --- | --- | --- | --- |
| `rec(0, 0)` | `{}` | Place at cell `0`; no earlier knights exist | Call `rec(1, 1)` |
| `rec(1, 1)` | `{0}` | Place at cell `1`; two knights in the same row do not attack | Call `rec(2, 2)` |
| `rec(2, 2)` | `{0, 1}` | `placed == K` | Return `1` |

Cells `2` through `8` are implicitly left empty. The arrangement `{0, 1}` is counted once.

### 8.2 Undo and explore another choice

After `rec(2, 2)` returns, its caller removes the knight from cell `1`:

```text
Occupied cells: {0, 1} → {0}
```

The caller then explores its skip branch:

```text
Skip cell 1.
Call rec(2, 1).
```

Cell `2` is safe with cell `0`, so placing there reaches another success:

```text
Occupied cells: {0, 2}
Call rec(3, 2) → return 1
```

This illustrates the two roles of backtracking: count one completion, then restore the board to explore another completion of the same prefix.

### 8.3 Reject an attacking choice

Eventually, the branch containing cell `0` skips cells `1`, `2`, `3`, and `4`, reaching:

```text
rec(5, 1)
Occupied cells = {0}
```

Cell `5` is `(1, 2)`, and cell `0` is `(0, 0)`:

```text
Row difference    = 1
Column difference = 2
```

They form a knight move, so `check(1, 2)` returns `false`.

The placement branch is not explored. The skip branch is still explored:

```text
rec(5, 1)
    place at cell 5 → rejected
    skip cell 5     → rec(6, 1)
```

Cell `6` is safe with cell `0`, so the search can still find the arrangement `{0, 6}`.

Rejecting one cell does not mean the entire prefix is impossible.

### 8.4 Count every branch

We can group the complete search by the smallest occupied cell. The second knight must have a larger cell index, preventing duplicate pairs.

| Smallest occupied cell | Valid cells for the second knight | Count |
| ---: | --- | ---: |
| `0` | `1, 2, 3, 4, 6, 8` | `6` |
| `1` | `2, 3, 4, 5, 7` | `5` |
| `2` | `4, 5, 6, 8` | `4` |
| `3` | `4, 5, 6, 7` | `4` |
| `4` | `5, 6, 7, 8` | `4` |
| `5` | `7, 8` | `2` |
| `6` | `7, 8` | `2` |
| `7` | `8` | `1` |
| `8` | None | `0` |

```text
Answer = 6 + 5 + 4 + 4 + 4 + 2 + 2 + 1 + 0 = 28
```

This table summarizes groups of leaves; the code itself reaches them through place/skip decisions, not by a separate two-knight algorithm.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/89fcb7ae-e9a5-4fe1-9e35-6d4904b9d50c.png" alt="Two example branches for N equals 3 and K equals 2: cells 0 and 1 are safe, cells 0 and 5 attack, and 36 candidate pairs yield 28 valid arrangements" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 9. Why the Algorithm Is Correct

### 9.1 Every counted arrangement is valid

The empty board is valid. A knight is placed only if it does not attack any earlier knight, so validity is preserved after each placement. Skipping cannot introduce an attack.

The success case is reached only after exactly `K` knights have been placed. Therefore, every counted board is valid.

### 9.2 Every valid arrangement is considered

Take any valid arrangement. Scan its cells in row-major order:

- take the placement branch for an occupied cell, and
- take the skip branch for an empty cell.

Every required placement passes the check because the final arrangement has no attacks. The remaining-cell prune cannot remove this path because enough cells remain to hold its remaining knights.

Thus every valid arrangement has a path in the search.

### 9.3 No arrangement is counted twice

Each occupied-cell set determines exactly one sequence of place/skip decisions. Two paths that differ at a cell disagree about whether that cell is occupied, so they cannot represent the same arrangement.

When `K` knights have been placed, returning early also introduces no duplicates: all remaining cells must be empty.

---

## 10. Time and Space Complexity

Let `M = N × N` be the number of cells.

### 10.1 Candidate arrangements: choose K cells from M

The important restriction is that we want **exactly `K` knights**, not an arbitrary subset of the board.

For `0 <= K <= M`, the number of ways to choose their occupied cells is:

$$
\binom{M}{K} = \binom{N^2}{K} = \frac{M!}{K!(M-K)!}
$$

Ignoring attacks, each such set reaches exactly one completed-candidate leaf. Because the recursion stops immediately when `placed == K`, it does not continue exploring the remaining cells after completing that set.

Therefore, **the maximum number of completed candidate arrangements, before attack pruning, is `C(M, K)`**. Attack checks can only reduce this number.

For example, on an `8 × 8` board:

| Knights `K` | Candidate arrangements before attack pruning |
| ---: | ---: |
| `1` | `C(64, 1) = 64` |
| `2` | `C(64, 2) = 2,016` |
| `3` | `C(64, 3) = 41,664` |

These counts are far smaller than `2^64`. For a fixed small `K`, `C(M, K)` grows like `M^K / K!` as `M` increases. This explains why small-`K` searches can be practical on boards larger than a blanket `O(2^(N²))` bound might suggest.

### 10.2 A sharper bound for this implementation

Completed candidate arrangements are not all the leaves in the recursion tree: some branches return `0` because too few cells remain. We must also account for these failures and the internal calls.

To bound the code above, ignore knight attacks but **retain both cardinality stopping rules**:

1. stop when `K` knights have been placed, and
2. stop when the remaining cells cannot supply the missing knights.

In this unrestricted place/skip tree:

- completed-candidate leaves: `C(M, K)`,
- failure leaves: `C(M, K - 1)`, taking this as `0` when `K = 0`.

The total number of leaves is therefore, by Pascal's identity:

$$
L = \binom{M}{K} + \binom{M}{K-1} = \binom{M+1}{K}
$$

These counts follow the place/skip recurrence: placing reduces the number of knights still needed by one, while skipping does not. Each step reduces the number of remaining cells by one.

Without attack rejections, every internal node has two children. A full binary tree with `L` leaves has `2L - 1` nodes, so this unrestricted search makes:

```text
2 × C(M + 1, K) - 1 recursive calls
```

The real attack checks only remove branches from that tree. Since each call performs `O(1)` work, including at most four attack checks, the recursive search is bounded by:

```text
O(C(M + 1, K))
```

Including the `O(M)` initialization of the board, the total time bound is:

```text
O(M + C(M + 1, K)), where M = N²
```

This is sharper than the valid but coarse `O(2^M)` bound and makes the dependence on `K` explicit. If `K > M`, the code returns `0` before allocating the board.

> **Interview Insight — Small K helps, but check the actual numbers:** A combination-sensitive bound explains the improvement; it does not make arbitrarily large boards cheap. For example, `K = 2` still gives quadratic growth in `M`, and the cell-by-cell recursion can still reach depth `M`.

### 10.3 Space complexity

- Board storage: `O(N²)`.
- Recursion stack: up to `O(N²)` calls.
- Work inside one call: `O(1)`.

The total auxiliary space is:

```text
O(N²)
```

> **Interview Insight — Stack depth follows the level:** The depth is bounded by the number of cells, not the number of knights. A skip also makes a recursive call, even though `placed` does not increase.

---

## 11. Edge Cases and Sanity Checks

| Input situation | Expected result | Reason |
| --- | --- | --- |
| `K = 0` | `1` | The empty board is one arrangement |
| `K = 1` | `N²` | A single knight can occupy any cell |
| `K > N²` | `0` | There are not enough cells |
| `N = 1, K = 1` | `1` | Only one available cell |
| `N = 2, K = 2` | `6` | No knight move fits inside a `2 × 2` board; choose any two of four cells |
| `N = 2, K = 4` | `1` | All four cells can be occupied safely |
| `N = 3, K = 2` | `28` | The dry-run result |

---

## 12. Common Mistakes and Interview Nuances

### Mistake 1: Allowing only one knight per row

This excludes valid arrangements. Knights do not attack every cell in their row.

### Mistake 2: Counting different placement orders

The knights are identical. Fix the order in which cells are considered instead of choosing arbitrary positions for labelled knights.

### Mistake 3: Forgetting the skip branch

Even if a cell is safe, some valid solutions leave it empty. A greedy “place whenever possible” strategy cannot count all arrangements.

### Mistake 4: Forgetting to undo the placement

The board must be restored before exploring the skip branch. Otherwise, that branch inherits a knight that it was supposed to omit.

### Mistake 5: Accessing a cell before checking boundaries

Knight offsets can produce negative or out-of-range coordinates. Validate both indices before reading `board[previousRow][previousCol]`.

### Mistake 6: Checking only four directions without the traversal invariant

The four-position check works because later rows are empty. With arbitrary placement order, check all eight attack positions.

### Mistake 7: Memoizing only `(level, placed)`

Two calls can have the same `level` and `placed` but different occupied cells. Those earlier knights may forbid different future placements.

The board configuration is part of the state, even though it is stored globally rather than passed as a parameter. A cache indexed only by `(level, placed)` would be incorrect.

> **Interview Insight — State is more than the function signature:** Memoization requires every piece of information that affects future choices. For larger boards, a row-mask formulation can exploit the fact that knight attacks reach only the previous two rows, but that is a different state design—not a simple cache added to this function.

---

## 13. Final LCCM Summary

```text
State
    board configuration + current cell + number of knights placed

Level
    one cell in row-major order

Choice
    place or skip

Check
    placement must not conflict with an earlier knight

Move
    place → recurse to the next cell → unplace
    skip  → recurse to the next cell without changing the board

Success
    exactly K knights have been placed

Failure / pruning
    no cells remain, or too few cells remain to reach K

Aggregation
    add the counts from the placement and skip branches
```

The key design decision is to make **cells the levels**. This permits multiple knights in a row, supports pruning, and gives each arrangement a unique decision path.

</READING_WIDGET>
