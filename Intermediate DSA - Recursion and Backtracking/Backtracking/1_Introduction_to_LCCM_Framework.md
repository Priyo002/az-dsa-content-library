<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to the LCCM Framework

Backtracking problems often look very different on the surface. One problem asks us to place queens, another asks us to fill a Sudoku, and another asks us to generate valid arrangements. However, their recursive solutions usually follow the same structure:

1. Decide what part of the solution to build next.
2. Try every possible choice for that part.
3. Reject choices that cannot lead to a valid solution.
4. Make a valid choice, explore recursively, and then undo it.

We organize these four ideas using the **LCCM framework**:

- **Level**
- **Choice**
- **Check**
- **Move**

We will understand this framework through the classic **N-Queens problem**.

---

## 1. The N-Queens Problem

You are given an `N × N` chessboard. Count the number of ways to place exactly `N` queens such that no two queens attack each other.

A queen can attack another queen if both queens are in:

- the same row,
- the same column, or
- the same diagonal.

Instead of trying to place queens in arbitrary cells, we will place **exactly one queen in every row**. This immediately guarantees that two queens can never be in the same row.

Therefore, while placing a queen, we only need to check:

- column conflicts, and
- diagonal conflicts.

This row-by-row construction is the first important design decision in the solution.

---

## 2. What Is a State?

A **state** describes the current configuration of the partial solution.

For N-Queens, the state must tell us:

- which rows already contain queens,
- the column chosen for each of those rows, and
- enough information to decide whether the next queen can be placed safely.

### 2.1 A direct representation

We could store the complete chessboard using an `N × N` matrix. A cell would indicate whether a queen is present there.

However, our construction always places exactly one queen in a row. Storing every cell is therefore unnecessary.

### 2.2 A compact one-dimensional representation

We can represent the board using a one-dimensional array:

```text
queens[row] = column in which the queen of this row is placed
```

The index represents the row, and its value represents the selected column.

For example, for `N = 4`:

```text
queens = [1, 3, -1, -1]
```

means:

- the queen in row `0` is placed in column `1`,
- the queen in row `1` is placed in column `3`, and
- rows `2` and `3` have not been decided yet.

We use `-1` to represent an undecided row.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7b7f8972-e260-4e1a-8dd3-995063fbe17a.png" alt="A partially filled N-Queens board represented by the one-dimensional state array queens equals 1, 3, -1, -1" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> **Interview Insight — Compress the state:** Before using a full grid, ask what information future recursive calls actually need. Because N-Queens has exactly one queen per row, an `N × N` board can be compressed into an array of size `N`.

### 2.3 The recursive invariant

Before `rec(level)` begins:

- rows `0` through `level - 1` have already been decided,
- every decided row contains exactly one queen,
- the placed queens do not attack one another, and
- rows `level` through `N - 1` are still undecided.

The job of `rec(level)` is to count every valid way to complete the undecided rows.

Writing this invariant before writing the code makes the meaning of every parameter and operation much clearer.

---

## 3. Understanding LCCM

For the N-Queens problem, the framework becomes:

| Part | Question to ask | N-Queens answer |
| --- | --- | --- |
| **Level** | What part of the solution are we deciding now? | The current row |
| **Choice** | What are the possible decisions at this level? | Any column from `0` to `N - 1` |
| **Check** | Is this choice feasible for the current state? | The new queen must not share a column or diagonal with an earlier queen |
| **Move** | How do we explore after selecting the choice? | Place the queen, recurse for the next row, and then unplace it |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/4771079b-8043-4d2b-aace-418cc240a898.png" alt="The Level, Choice, Check, and Move stages of the LCCM framework applied to N-Queens" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 3.1 Level — how do we make progress?

The level represents the part of the solution that we are currently deciding.

In this problem:

```text
level = current row
```

Therefore:

- `rec(0)` decides row `0`,
- `rec(1)` decides row `1`,
- `rec(2)` decides row `2`, and so on.

Every recursive call increases `level` by one, so the partial solution grows one row at a time.

### 3.2 Choice — what can we do at this level?

At the current row, the queen can potentially be placed in any column:

```text
0, 1, 2, ..., N - 1
```

These are all the choices that the recursive function must consider.

Some choices will be rejected by the check, but they must still be considered before we can determine whether they are feasible.

### 3.3 Check — is the choice feasible?

Suppose we want to place a queen at `(row, col)`. For every previously placed queen `(previousRow, previousCol)`, we check two possible conflicts.

#### Same column

```text
previousCol == col
```

#### Same diagonal

Two cells are on the same diagonal when the absolute row difference equals the absolute column difference:

```text
abs(row - previousRow) == abs(col - previousCol)
```

We do not need to check for a row conflict because each recursive level places only one queen in its row.

> **Interview Insight — Use the construction to remove checks:** A good state design can make some constraints true automatically. Here, choosing one row per recursive level eliminates the same-row check entirely.

### 3.4 Move — place, recurse, and unplace

Once a choice passes the check, we perform three operations:

```cpp
queens[level] = choice;      // place
ans += rec(level + 1);       // explore
queens[level] = -1;          // unplace
```

The first operation changes the state. The recursive call explores every solution containing that decision. The final operation restores the state so that the next choice starts from the same original configuration.

This restoration is the essence of backtracking.

> **Interview Insight — State the undo operation explicitly:** When explaining a backtracking solution, identify both the state change and its exact inverse. If shared state is modified but not restored, sibling branches of the recursion tree interfere with one another.

---

## 4. The General LCCM Template

The general structure of an LCCM solution is:

```text
rec(level):
    if all levels have been decided:
        return the contribution of one complete solution

    answer = 0

    for every choice at this level:
        if the choice is feasible:
            place the choice
            answer += rec(next level)
            unplace the choice

    return answer
```

In compact form:

```text
rec(level)

    base case

    for every choice ch:
        if check(level, ch):
            place(ch)
            rec(nextLevel)
            unplace(ch)
```

LCCM describes the recursive case, but a complete recursive solution also needs:

- a **base case**, which recognizes a complete solution, and
- an **answer-combination rule**, such as summing the number of valid completions.

For N-Queens, reaching `level == N` means that all `N` rows contain valid queens. That completed arrangement contributes exactly `1` to the answer.

---

## 5. Complete C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 10;

int n;
int queens[MAX_N];

bool check(int row, int col) {
    // Rows [0 ... row - 1] already contain queens.
    for (int previousRow = 0; previousRow < row; previousRow++) {
        int previousCol = queens[previousRow];

        // Same column.
        if (previousCol == col) {
            return false;
        }

        // Same diagonal.
        if (abs(row - previousRow) == abs(col - previousCol)) {
            return false;
        }
    }

    return true;
}

long long rec(int level) {
    // Invariant:
    // Rows [0 ... level - 1] have already been decided and are valid.
    // Count all valid ways to decide rows [level ... n - 1].

    // Base case: all rows have been decided.
    if (level == n) {
        return 1;
    }

    long long ans = 0;

    // Choice: try every column in the current row.
    for (int choice = 0; choice < n; choice++) {
        // Check whether this choice preserves validity.
        if (check(level, choice)) {
            // Move: place the queen.
            queens[level] = choice;

            // Explore every completion containing this placement.
            ans += rec(level + 1);

            // Backtrack: undo the placement.
            queens[level] = -1;
        }
    }

    return ans;
}

void solve() {
    cin >> n;

    memset(queens, -1, sizeof(queens));

    cout << rec(0) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

This implementation assumes `N <= 10` because the state is stored in `queens[10]`. If the constraints allow a larger `N`, use a suitably sized array or a `vector<int>`.

---

## 6. Dry Run for N = 4

For `N = 4`, the algorithm finds two valid arrangements:

```text
[1, 3, 0, 2]
[2, 0, 3, 1]
```

All row and column numbers are zero-based. For example, `[1, 3, 0, 2]` means that the queens are placed at:

```text
(0, 1), (1, 3), (2, 0), (3, 2)
```

Let us trace how the first solution is found.

### 6.1 Starting state

```text
queens = [-1, -1, -1, -1]
rec(0)
```

At `level = 0`, no queen has been placed. Every column is initially feasible.

The algorithm tries the choices from left to right. The branch beginning with column `0` is explored completely but produces no solution. It is then undone. The algorithm next tries column `1`.

### 6.2 Building the first solution

| Step | Level | State before the choice | Choice | Check and action |
| --- | ---: | --- | ---: | --- |
| 1 | `0` | `[-1, -1, -1, -1]` | `1` | Valid. Place at `(0, 1)` and call `rec(1)`. |
| 2 | `1` | `[1, -1, -1, -1]` | `0` | Invalid: diagonal conflict with `(0, 1)`. |
| 3 | `1` | `[1, -1, -1, -1]` | `1` | Invalid: same column as `(0, 1)`. |
| 4 | `1` | `[1, -1, -1, -1]` | `2` | Invalid: diagonal conflict with `(0, 1)`. |
| 5 | `1` | `[1, -1, -1, -1]` | `3` | Valid. Place at `(1, 3)` and call `rec(2)`. |
| 6 | `2` | `[1, 3, -1, -1]` | `0` | Valid. Place at `(2, 0)` and call `rec(3)`. |
| 7 | `3` | `[1, 3, 0, -1]` | `2` | Valid. Place at `(3, 2)` and call `rec(4)`. |
| 8 | `4` | `[1, 3, 0, 2]` | — | `level == N`, so one complete solution is found. Return `1`. |

At the base case, the arrangement is already guaranteed to be valid. Every queen was checked before it was placed, so there is no need to validate the entire board again.

### 6.3 How backtracking restores the state

After `rec(4)` returns `1`, execution resumes inside `rec(3)`:

```text
[1, 3, 0, 2]   complete solution
[1, 3, 0, -1]  unplace the queen from row 3
```

After all remaining choices for row `3` are examined, `rec(3)` returns to `rec(2)`:

```text
[1, 3, 0, -1]
[1, 3, -1, -1] unplace the queen from row 2
```

The algorithm then tries the remaining choices for row `2`. When every choice under the current prefix has been explored, it continues moving upward and undoing decisions.

This is why the order is important:

```text
place → recurse → unplace
```

The unplace operation does not erase a valid answer that was already counted. It only restores the shared state so that the next branch can be explored correctly.

### 6.4 The complete top-level search

The search from the first row can be summarized as:

```text
rec(0)
├── place row 0 at column 0 → 0 solutions
├── place row 0 at column 1 → 1 solution: [1, 3, 0, 2]
├── place row 0 at column 2 → 1 solution: [2, 0, 3, 1]
└── place row 0 at column 3 → 0 solutions

Total = 0 + 1 + 1 + 0 = 2
```

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/443215a3-0ccf-49cb-9d01-f543d4a826c3.png" alt="The N equals 4 backtracking search showing two valid N-Queens arrangements" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Every node in this search represents a state. Every edge represents one feasible choice and its corresponding move.

---

## 7. Why the Algorithm Is Correct

The recursive invariant gives us a direct correctness argument.

### 7.1 Every counted arrangement is valid

- Initially, no queen has been placed, so the empty state is valid.
- Before placing a queen, `check(level, choice)` verifies that it does not attack any earlier queen.
- Therefore, after every move, all placed queens remain mutually non-attacking.
- The base case is reached only after one queen has been placed in every row.

Hence, every arrangement counted at the base case is a valid N-Queens arrangement.

### 7.2 Every valid arrangement is considered

At every row, the algorithm tries every column. Any column belonging to a valid final arrangement passes the check against the already chosen prefix. Therefore, the recursion contains a path corresponding to every valid arrangement.

### 7.3 No arrangement is counted twice

An arrangement is uniquely represented by its sequence of column choices:

```text
queens[0], queens[1], ..., queens[N - 1]
```

Two different root-to-leaf paths cannot produce the same sequence. Therefore, every valid arrangement is counted exactly once.

---

## 8. Complexity

The same-column check prevents two rows from choosing the same column. Therefore, the number of candidate partial arrangements is bounded by the number of column permutations.

- **Search complexity:** conservatively `O(N × N!)`, because the recursion explores up to `O(N!)` arrangements and `check()` scans up to `N` earlier rows.
- **State space:** `O(N)` for the `queens` array.
- **Recursion stack:** `O(N)`, because one recursive call is active for each row.

The diagonal checks prune many branches, so the actual search is usually much smaller than this upper bound.

> **Interview Insight — Optimize the check when needed:** Column and diagonal occupancy can be maintained in three arrays or bitmasks. The identifiers `col`, `row + col`, and `row - col + N - 1` uniquely represent the attacked column and diagonals. This reduces each feasibility check from `O(N)` to `O(1)`.

---

## 9. Changing What the Recursion Produces

The LCCM structure remains the same even when the required output changes.

### Count all solutions

Return `1` at a complete solution and add the answers from all branches:

```cpp
ans += rec(level + 1);
```

### Find any one solution

Return a boolean and stop as soon as a recursive call succeeds.

### Generate every solution

At the base case, copy the current `queens` array into a list of answers.

> **Interview Insight — Separate search from aggregation:** LCCM describes how the state space is explored. Counting, finding one answer, minimizing a cost, and listing solutions differ mainly in the base-case contribution and the way child results are combined.

---

## 10. Common Mistakes

### Mistake 1: Returning `0` at a complete solution

For a counting problem, a valid completed arrangement contributes one solution. Therefore, the base case must return `1`.

### Mistake 2: Forgetting to unplace

Without:

```cpp
queens[level] = -1;
```

the state from one branch leaks into the next branch.

### Mistake 3: Using the wrong diagonal condition

The correct condition is:

```cpp
abs(row - previousRow) == abs(col - previousCol)
```

### Mistake 4: Checking undecided rows

Only rows `0` through `level - 1` contain queens. The check should not inspect future rows whose values are still `-1`.

### Mistake 5: Not defining what `rec(level)` means

Without a precise recursive invariant, the base case, state changes, and returned value become much harder to reason about.

### Mistake 6: Using a fixed array that is smaller than the constraints

The sample implementation uses `queens[10]`, so it is valid only when `N <= 10`.

---

## 11. LCCM Design Checklist

Before implementing a backtracking solution, answer these questions:

1. **State:** What information completely describes the current partial solution?
2. **Level:** What part of the solution will this recursive call decide?
3. **Choice:** What are all possible decisions at this level?
4. **Check:** Which choices can still lead to a valid solution?
5. **Move:** What state must be changed before recursion?
6. **Undo:** How will that state be restored afterward?
7. **Base case:** When is the solution complete?
8. **Aggregation:** Do we count, list, optimize, or stop at the first solution?

For N-Queens, the answers are:

```text
State       → queens[row] = selected column
Level       → current row
Choice      → a column from 0 to N - 1
Check       → no previous queen shares its column or diagonal
Move        → place, recurse to the next row, and unplace
Base case   → level == N
Aggregation → sum the number of completed arrangements
```

Once these decisions are clear, the recursive code becomes a direct translation of the framework.

</READING_WIDGET>
