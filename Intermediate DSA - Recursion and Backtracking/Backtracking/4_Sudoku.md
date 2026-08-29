<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Sudoku Solver Using LCCM

## 1. Problem Statement

You are given a partially filled Sudoku board. Fill every empty cell so that:

1. Every row contains each allowed value exactly once.
2. Every column contains each allowed value exactly once.
3. Every smaller square box contains each allowed value exactly once.

The values already present on the board are **fixed clues**. We cannot change them. An input value of `0` represents an empty cell; it is not a value that we may place.

In this lesson, we will **print every valid completed board and count the total number of solutions**, matching the recursive approach discussed in the video.

### 1.1 Start with a smaller Sudoku

We will use a `4 × 4` board to understand the recursion:

| Property | Small Sudoku | Standard Sudoku |
| --- | --- | --- |
| Board size | `4 × 4` | `9 × 9` |
| Allowed values | `1, 2, 3, 4` | `1, 2, ..., 9` |
| Size of each box | `2 × 2` | `3 × 3` |
| Number of boxes | `4` | `9` |

We use two constants:

```cpp
const int boardSize = 4;
const int cellSize = 2;
```

Here, `cellSize` means the side length of a **box**, not a single board cell. For these square-box Sudokus:

```text
boardSize = cellSize × cellSize
```

Both complete programs below use `4` and `2`. To run them on a standard Sudoku, change the constants to `9` and `3` and provide `81` input values instead of `16`.

### 1.2 Example

```text
Input
0 1 0 0
0 0 4 0
0 4 0 0
0 0 3 0

Output
4 1 2 3
2 3 4 1
3 4 1 2
1 2 3 4

1
```

The first four output lines form the completed board. The final `1` is the number of solutions.

The input contains only the board: there is no test-case count or board-size value before it. The output contains each solution followed by a blank line, then the total count. If there is no solution, the output is simply `0`.

> **Interview Insight — Clarify what “solve” means:** Finding one solution, printing all solutions, counting solutions, and checking whether the solution is unique are different tasks. We enumerate all solutions here; we will discuss how the stopping condition changes for the other variants.

---

## 2. What Is the State?

The state is the information that describes the current configuration and determines what we can do next.

For the first approach, it consists of:

- `board`: the fixed clues together with the values temporarily placed by recursion.
- `(row, col)`: the cell that we are currently processing.

The counter `ans` accumulates completed solutions. It does not affect which future choices are legal.

Unlike our N-Queens representation, a one-dimensional array storing one column per row is not enough here: each Sudoku row contains several values that we must remember. We store the entire board.

### 2.1 The recursive contract

For a call `rec(row, col)`:

> All cells before the current position in row-major order have been decided. The board has no row, column, or box conflicts. Explore every way to fill the remaining empty cells without changing the clues.

Importantly, **clues in later cells are already present on the board**. A value we place now must respect those clues too.

The function must restore all its temporary placements before returning, so the caller can try another choice on the same board.

---

## 3. Designing the Scan-Based Solution with LCCM

### 3.1 Level — Which cell are we deciding?

Each level processes one cell in **row-major order**: across a row, then down to the next row.

```text
(0, 0), (0, 1), (0, 2), (0, 3),
(1, 0), (1, 1), (1, 2), (1, 3), ...
```

We represent this progress using two parameters:

```cpp
void rec(int row, int col)
```

Equivalently, a single index could represent the cell:

```text
level = row × boardSize + col
```

We will keep `(row, col)` because the row, column, and box checks naturally use these coordinates.

### 3.2 Choice — What can we put in this cell?

For an empty cell, try every value from `1` to `boardSize`.

For a prefilled cell, there is no branching choice: preserve its value and move to the next cell.

**There is no “leave this empty” branch.** Unlike K Knights, where a cell may remain unused, a completed Sudoku must fill every cell.

### 3.3 Check — Is this value legal here?

Before placing `ch` at `(row, col)`, verify that it is absent from:

- the current row,
- the current column, and
- the current box.

Passing this check means that the placement does not create an immediate conflict. It does **not** guarantee that the remaining board can be completed.

### 3.4 Move — Place, recurse, unplace

For a legal choice:

```cpp
board[row][col] = ch;   // Place.
rec(row, col + 1);      // Explore the remaining cells.
board[row][col] = 0;    // Unplace.
```

We reset the cell to `0` because this branch started from an empty cell. We never unplace a fixed clue.

| LCCM component | Sudoku interpretation |
| --- | --- |
| **Level** | Current cell `(row, col)` |
| **Choice** | Try `1` through `boardSize` if the cell is empty |
| **Check** | Scan the row, column, and box for the chosen value |
| **Move** | Place → recurse to the next cell → restore `0` |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7d6f3c9b-9347-4d0d-809b-92e455e0ebde.png" alt="The LCCM framework for one cell of a 4 by 4 Sudoku: select the current cell, try candidate values, check its row column and box, then place recurse and unplace" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Implementing the Check

### 4.1 Row and column

To test a candidate, scan the row and column for another occurrence of the same value.

The check function will also be used to validate fixed clues. Therefore, it must **exclude the cell being checked**; otherwise, every clue would conflict with itself.

```cpp
// Check the column.
for (int i = 0; i < boardSize; i++) {
    if (i != row && board[i][col] == ch) {
        return false;
    }
}

// Check the row.
for (int i = 0; i < boardSize; i++) {
    if (i != col && board[row][i] == ch) {
        return false;
    }
}
```

### 4.2 Finding the box

The top-left corner of the box containing `(row, col)` is:

```cpp
int startRow = (row / cellSize) * cellSize;
int startCol = (col / cellSize) * cellSize;
```

Integer division identifies which box we are in; multiplication converts that box index back into a board coordinate.

For example, on a `4 × 4` board, cell `(3, 2)` belongs to the box beginning at:

```text
startRow = (3 / 2) × 2 = 2
startCol = (2 / 2) × 2 = 2
```

That box contains `(2, 2)`, `(2, 3)`, `(3, 2)`, and `(3, 3)`.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/9b920cc0-4c21-46cc-b4fc-c8d8d6e28938.png" alt="A 4 by 4 Sudoku board highlighting the row, column, and 2 by 2 box constraints for the current cell" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 4.3 Validate the clues before searching

Before recursion begins, check that every input value is in `0..boardSize` and that every nonzero clue passes the same row, column, and box checks.

This lets the recursive function advance past prefilled cells without rechecking them on every visit. Every new placement is still checked against the whole current board.

**A valid partial board is not necessarily solvable.** Initial validation rejects immediate contradictions; recursion determines whether a complete solution exists.

---

## 5. Base Cases and Cell Transitions

There are three important situations:

1. **`row == boardSize`:** Every cell has been processed. Count and print the board.
2. **`col == boardSize`:** The current row is finished. Continue from `(row + 1, 0)`.
3. **The current cell is prefilled:** Preserve it and continue from `(row, col + 1)`.

Handle the boundary cases **before accessing `board[row][col]`**.

For an empty cell, if none of the values passes `check`, the loop makes no recursive call. The function returns naturally, allowing the caller to undo its last choice.

```text
rec(row, col)
    if all rows are finished:
        count and print this solution
        return

    if this row is finished:
        recurse to the first cell of the next row
        return

    if the current cell is a clue:
        recurse to the next cell
        return

    for every candidate value:
        if the candidate passes the check:
            place it
            recurse to the next cell
            unplace it
```

---

## 6. Complete Code — Row, Column, and Box Scanning

This program prints every solution and then its total count.

```cpp
#include <iostream>
using namespace std;

const int boardSize = 4;
const int cellSize = 2;

int board[boardSize][boardSize];
long long ans = 0;

bool check(int ch, int row, int col) {
    // Check the column, excluding this cell.
    for (int i = 0; i < boardSize; i++) {
        if (i != row && board[i][col] == ch) {
            return false;
        }
    }

    // Check the row, excluding this cell.
    for (int i = 0; i < boardSize; i++) {
        if (i != col && board[row][i] == ch) {
            return false;
        }
    }

    int startRow = (row / cellSize) * cellSize;
    int startCol = (col / cellSize) * cellSize;

    // Check the box, excluding this cell.
    for (int i = 0; i < cellSize; i++) {
        for (int j = 0; j < cellSize; j++) {
            int r = startRow + i;
            int c = startCol + j;

            if (r == row && c == col) {
                continue;
            }
            if (board[r][c] == ch) {
                return false;
            }
        }
    }

    return true;
}

bool validInitialBoard() {
    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            int ch = board[row][col];

            if (ch < 0 || ch > boardSize) {
                return false;
            }
            if (ch != 0 && !check(ch, row, col)) {
                return false;
            }
        }
    }
    return true;
}

void printBoard() {
    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            if (col > 0) cout << ' ';
            cout << board[row][col];
        }
        cout << '\n';
    }
    cout << '\n';
}

void rec(int row, int col) {
    // Success: all cells have been processed.
    if (row == boardSize) {
        ans++;
        printBoard();
        return;
    }

    // Move to the next row.
    if (col == boardSize) {
        rec(row + 1, 0);
        return;
    }

    // A fixed clue is preserved, not chosen again.
    if (board[row][col] != 0) {
        rec(row, col + 1);
        return;
    }

    // Choice and Check.
    for (int ch = 1; ch <= boardSize; ch++) {
        if (check(ch, row, col)) {
            // Move: place, recurse, unplace.
            board[row][col] = ch;
            rec(row, col + 1);
            board[row][col] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            cin >> board[row][col];
        }
    }

    if (!validInitialBoard()) {
        cout << 0 << '\n';
        return 0;
    }

    rec(0, 0);
    cout << ans << '\n';
    return 0;
}
```

The code supports one input board. Both implementations in this lesson assume the solution count fits in `long long`. Enumerating all completions of a very sparse `9 × 9` board can be impractical, and its count may require arbitrary-precision arithmetic.

---

## 7. Dry Run — Watching LCCM Work

Use the example board, with **0-based coordinates**:

```text
0 1 | 0 0
0 0 | 4 0
----+----
0 4 | 0 0
0 0 | 3 0
```

### 7.1 First attempt: place 2 at `(0, 0)`

At `(0, 0)`, the legal choices are `{2, 3, 4}`. We try them in increasing order.

| LCCM component | What happens |
| --- | --- |
| **Level** | `(0, 0)` |
| **Choice** | Try `2` |
| **Check** | No `2` exists in this row, column, or box |
| **Move** | Place `2`, then recurse |

The next cell `(0, 1)` is a fixed `1`, so recursion advances to `(0, 2)`.

```text
2 1 | 0 0
0 0 | 4 0
----+----
0 4 | 0 0
0 0 | 3 0
```

At `(0, 2)`:

| Candidate | Why it is rejected |
| ---: | --- |
| `1` | Already in row `0` |
| `2` | Already in row `0` |
| `3` | Already in column `2`, at `(3, 2)` |
| `4` | Already in column `2`, at `(1, 2)` |

There is no legal choice. The call returns, and the earlier placement at `(0, 0)` is undone.

Notice that `2` passed its own check. The contradiction appeared only at a later level.

### 7.2 Second attempt: place 3 at `(0, 0)`

Now try `3`. At `(0, 2)`, `2` is legal, giving:

```text
3 1 | 2 0
0 0 | 4 0
----+----
0 4 | 0 0
0 0 | 3 0
```

At `(0, 3)`, the row needs `4`. But the upper-right box already contains the clue `4` at `(1, 2)`.

This branch also fails:

1. Undo `2` at `(0, 2)`.
2. Return to the earlier call.
3. Undo `3` at `(0, 0)`.

This is why every level must restore **its own** placement before returning to its caller.

### 7.3 Third attempt: place 4 at `(0, 0)`

The search now reaches:

```text
4 1 | 2 3
2 3 | 4 1
----+----
0 4 | 0 0
0 0 | 3 0
```

There is another backtracking step at `(2, 0)`:

- Trying `1` leaves `(2, 2)` with no legal value, so undo it.
- Trying `3` lets the search continue.

The remaining successful choices are:

| Cell | Value placed |
| --- | ---: |
| `(2, 0)` | `3` |
| `(2, 2)` | `1` |
| `(2, 3)` | `2` |
| `(3, 0)` | `1` |
| `(3, 1)` | `2` |
| `(3, 3)` | `4` |

We obtain:

```text
4 1 | 2 3
2 3 | 4 1
----+----
3 4 | 1 2
1 2 | 3 4
```

After the last cell, recursion advances to `(4, 0)`. Since `row == boardSize`, it increments `ans` and prints the board.

### 7.4 Do we stop after printing?

No. The successful call returns, placements are undone, and the remaining branches are explored. For this example, no other complete solution exists, so the final count is `1`.

After the entire search, the board is restored to its original clues and zeros. The accumulated count is **not** undone.

> **Interview Insight — Local feasibility is not global success:** `check` answers “Does this placement conflict with what is currently fixed?” Recursion answers “Can all remaining cells be completed?” Confusing these two questions is a common reason for writing an incorrect greedy solver.

---

## 8. Why Optimize the Check?

Every empty-cell call currently tries up to `boardSize` values. For each value, it scans a row, a column, and a box.

Let `B = boardSize`. A box contains `cellSize² = B` cells, so one check costs `O(B)`, and trying all `B` candidates costs `O(B²)` at that empty-cell call, excluding deeper recursion.

The information we need is much smaller than the board itself:

> Which values are already used in this row, this column, and this box?

We can maintain these three sets directly using **bitmasks**. The backtracking idea stays the same; the representation of constraints becomes faster.

---

## 9. Bitmask Optimization — Representing Used Values

### 9.1 One bit per value

Use **bit position `ch` to represent value `ch`**. Bit `0` is unused.

For the `4 × 4` example:

| Value | Expression | Binary mask, written as bits `4..0` |
| ---: | --- | --- |
| `1` | `1 << 1` | `00010` |
| `2` | `1 << 2` | `00100` |
| `3` | `1 << 3` | `01000` |
| `4` | `1 << 4` | `10000` |

The programs in this lesson use `int` for masks, consistent with the rest of the module. This is safe for `4 × 4` and `9 × 9` Sudoku because we use only the low-order bits and never shift into the sign bit.

> **CP Insights** Unsigned integers have no sign bit, and their arithmetic wraps modulo `2^w`, where `w` is the number of bits in the type. This makes edge-case behavior in low-level bit manipulation more predictable. For larger masks or systems-oriented code, prefer `unsigned int` and literals such as `1u`. For our small Sudoku masks, ordinary `int` keeps the code familiar without changing the result.

If a row contains values `{1, 3}`, its mask is `01010`. Set bits mean “already used,” not “available.”

### 9.2 Maintain three groups of masks

```cpp
int takenRow[boardSize];
int takenCol[boardSize];
int takenGrid[cellSize][cellSize];
```

- `takenRow[row]`: values already present in this row.
- `takenCol[col]`: values already present in this column.
- `takenGrid[row / cellSize][col / cellSize]`: values already present in this box.

There are `cellSize` boxes along each direction because `boardSize = cellSize²`.

The masks include **all original clues**, including clues in cells that recursion has not visited yet, plus the temporary placements on the current path.

### 9.3 Combine restrictions with OR

A value is forbidden if it appears in **any** of the three groups:

```cpp
int taken = takenRow[row]
          | takenCol[col]
          | takenGrid[row / cellSize][col / cellSize];
```

Bitwise OR computes the union of the forbidden values.

### 9.4 Find the available choices

First construct a mask containing exactly the allowed value bits, `1..boardSize`:

```cpp
const int fullMask = (1 << (boardSize + 1)) - 2;
```

For `boardSize = 4`, this is `11110`.

The available values are:

```cpp
int choices = fullMask & ~taken;
```

The complement `~taken` finds unused bits, while `& fullMask` restricts them to valid Sudoku values.

**Do not use `~taken` alone:** it also sets bits beyond `boardSize`. Also, do not include bit `0`, because an empty-cell marker must never become a candidate value.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d0548c49-540d-4be1-af0a-f2f59cc50000.png" alt="Sudoku bitmask choice generation: OR the row column and box masks, complement within fullMask, and obtain legal values 2, 3, and 4" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 9.5 Place and unplace in every representation

For a value `ch`, let `bit = 1 << ch`.

On placement:

```cpp
board[row][col] = ch;
takenRow[row] |= bit;
takenCol[col] |= bit;
takenGrid[row / cellSize][col / cellSize] |= bit;
```

On undo:

```cpp
board[row][col] = 0;
takenRow[row] &= ~bit;
takenCol[col] &= ~bit;
takenGrid[row / cellSize][col / cellSize] &= ~bit;
```

Clearing the bit is safe because we placed the value only when it was absent from all three groups. No other occurrence in those groups needs that same bit to remain set.

The lecture code uses XOR (`^=`) to toggle bits during both placement and undo. This also works **under the same invariant**: the bit must be `0` before placement and `1` before undo. Here, OR-to-set and AND-with-complement-to-clear make the intended operations explicit.

Changing only the board is not enough. **The board and all three masks must be restored together.**

---

## 10. LCCM with Bitmasks

The framework does not change:

| LCCM component | Scan-based version | Bitmask version |
| --- | --- | --- |
| **Level** | Current cell `(row, col)` | Same current cell |
| **Choice** | Try every value `1..boardSize` | Visit values whose bits are set in `choices` |
| **Check** | Scan row, column, and box | Compute `fullMask & ~(rowMask \| colMask \| boxMask)` |
| **Move** | Update board → recurse → restore board | Update board and three masks → recurse → restore all four |

With masks, the check is used to **generate only legal choices**. We do not need a separate scanning check inside the loop.

### 10.1 First improvement: test candidate bits

One option is to keep the familiar loop:

```cpp
for (int ch = 1; ch <= boardSize; ch++) {
    if ((choices & (1 << ch)) != 0) {
        makeMove(ch, row, col);
        rec(row, col + 1);
        revertMove(ch, row, col);
    }
}
```

Each membership test is constant-time for a mask that fits in one machine word. This removes the row, column, and box scans, but still examines all `boardSize` possible values.

### 10.2 Further improvement: visit only set bits

If only two values are available, we can iterate twice instead of checking all values.

```cpp
while (choices != 0) {
    int bit = choices ^ (choices & (choices - 1));
    int ch = __builtin_ffs(bit) - 1;

    makeMove(ch, row, col);
    rec(row, col + 1);
    revertMove(ch, row, col);

    choices &= choices - 1;
}
```

There are three operations to understand:

1. **Isolate the lowest set bit:** `choices ^ (choices & (choices - 1))` keeps only the smallest available value's bit. It avoids relying on unary negation and works directly with our positive `int` masks.
2. **Find its position:** `__builtin_ffs(bit)` returns one more than the position of the lowest set bit. For `00100`, it returns `3`; subtracting `1` gives candidate value `2`.
3. **Remove that choice:** `choices &= choices - 1` clears the lowest set bit before the next iteration.

For example:

```text
choices = 11100  → select value 2 → remaining 11000
choices = 11000  → select value 3 → remaining 10000
choices = 10000  → select value 4 → remaining 00000
```

`__builtin_ffs` is a GCC/Clang extension used here in C++17. It accepts an `int`, matching the mask type used in this lesson. The `while` condition guarantees that the isolated bit is nonzero. See the [GCC documentation for bit-operation builtins](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html).

The lecture's power-of-two lookup table can also map a single-bit mask to its position. The builtin avoids that extra table and avoids using floating-point logarithms for an integer bit operation.

Use **either** the value-testing loop **or** the set-bit loop for an empty cell. They are alternative implementations of the same choice step.

---

## 11. Complete Code — Bitmask-Optimized Solver

Before recursion, build the masks from the fixed clues:

1. Ignore zeros.
2. Reject values outside `1..boardSize` before shifting.
3. Check whether the clue's bit is already used in its row, column, or box.
4. Only then set its bit.

Checking before setting catches duplicate clues. It also avoids the dangerous behavior of XOR initialization, where inserting the same value twice could toggle its bit back to zero.

```cpp
#include <iostream>
#include <limits>
using namespace std;

const int boardSize = 4;
const int cellSize = 2;

static_assert(boardSize == cellSize * cellSize,
              "The board must contain square boxes.");
static_assert(boardSize + 1 < numeric_limits<int>::digits,
              "The mask must stay below the sign bit of int.");

const int fullMask = (1 << (boardSize + 1)) - 2;

int board[boardSize][boardSize];
int takenRow[boardSize] = {};
int takenCol[boardSize] = {};
int takenGrid[cellSize][cellSize] = {};
long long ans = 0;

int getChoices(int row, int col) {
    int taken = takenRow[row]
              | takenCol[col]
              | takenGrid[row / cellSize][col / cellSize];
    return fullMask & ~taken;
}

void makeMove(int ch, int row, int col) {
    int bit = 1 << ch;

    board[row][col] = ch;
    takenRow[row] |= bit;
    takenCol[col] |= bit;
    takenGrid[row / cellSize][col / cellSize] |= bit;
}

void revertMove(int ch, int row, int col) {
    int bit = 1 << ch;

    board[row][col] = 0;
    takenRow[row] &= ~bit;
    takenCol[col] &= ~bit;
    takenGrid[row / cellSize][col / cellSize] &= ~bit;
}

bool initializeMasks() {
    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            int ch = board[row][col];

            if (ch == 0) {
                continue; // Zero is not a Sudoku value.
            }
            if (ch < 1 || ch > boardSize) {
                return false;
            }

            int bit = 1 << ch;
            int taken = takenRow[row]
                      | takenCol[col]
                      | takenGrid[row / cellSize][col / cellSize];

            if ((taken & bit) != 0) {
                return false; // Conflicting fixed clues.
            }

            makeMove(ch, row, col);
        }
    }
    return true;
}

void printBoard() {
    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            if (col > 0) cout << ' ';
            cout << board[row][col];
        }
        cout << '\n';
    }
    cout << '\n';
}

void rec(int row, int col) {
    if (row == boardSize) {
        ans++;
        printBoard();
        return;
    }

    if (col == boardSize) {
        rec(row + 1, 0);
        return;
    }

    if (board[row][col] != 0) {
        // All fixed clues were validated during initialization.
        rec(row, col + 1);
        return;
    }

    // Check: combine the constraints to get only legal choices.
    int choices = getChoices(row, col);

    while (choices != 0) {
        // Choice: extract the smallest available value.
        int bit = choices ^ (choices & (choices - 1));
        int ch = __builtin_ffs(bit) - 1;

        // Move: update every representation, recurse, then restore.
        makeMove(ch, row, col);
        rec(row, col + 1);
        revertMove(ch, row, col);

        choices &= choices - 1;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int row = 0; row < boardSize; row++) {
        for (int col = 0; col < boardSize; col++) {
            cin >> board[row][col];
        }
    }

    if (!initializeMasks()) {
        cout << 0 << '\n';
        return 0;
    }

    rec(0, 0);
    cout << ans << '\n';
    return 0;
}
```

The compile-time checks ensure the constants describe square boxes and keep the shifts within the mask type's width. Both `4/2` and `9/3` satisfy these conditions.

The helpers `makeMove` and `revertMove` return `void` because they modify state without returning a value. The solution count and printed boards are the same as in the scan-based version.

---

## 12. Bitmask Dry Run on the Same Puzzle

Return to cell `(0, 0)` of the original example. Write masks as bits `4..0`.

### 12.1 Generate the choices

| Mask | Values represented | Binary |
| --- | --- | --- |
| `takenRow[0]` | `{1}` | `00010` |
| `takenCol[0]` | `{}` | `00000` |
| `takenGrid[0][0]` | `{1}` | `00010` |
| Their OR | `{1}` | `00010` |
| `fullMask & ~taken` | `{2, 3, 4}` | `11100` |

We obtain exactly the same choices as the scanning check.

### 12.2 Place the lowest available value

From `11100`, the lowest set bit is `00100`, representing value `2`.

After placing it:

| State component | Before placement | After placement |
| --- | --- | --- |
| `board[0][0]` | `0` | `2` |
| `takenRow[0]` | `00010` | `00110` |
| `takenCol[0]` | `00000` | `00100` |
| `takenGrid[0][0]` | `00010` | `00110` |

### 12.3 Detect the dead end

Recursion advances past the fixed `1` at `(0, 1)` to `(0, 2)`.

```text
Row 0 uses       {1, 2} → 00110
Column 2 uses    {3, 4} → 11000
Upper-right box uses {4} → 10000

taken   = 11110
choices = fullMask & ~taken = 00000
```

There are no set bits to iterate, so this call returns immediately.

### 12.4 Undo and try the next choice

At `(0, 0)`, `revertMove(2, 0, 0)` restores:

```text
board[0][0]          = 0
takenRow[0]         = 00010
takenCol[0]         = 00000
takenGrid[0][0]     = 00010
```

The caller then removes value `2` from its local choice mask:

```text
11100 → 11000
```

The next candidate is `3`. Its branch fails as described earlier; the branch beginning with `4` eventually produces the solution.

The masks change **how quickly** we find legal choices, not which choices are legal or which boards are counted.

---

## 13. Why Both Algorithms Are Correct

### 13.1 Every printed board is valid

Initial validation ensures that the clues do not conflict. Every new placement preserves row, column, and box validity.

At the success case, every cell has been processed and none remains empty. Each row, column, and box has `boardSize` cells filled with distinct values from `1..boardSize`, so each allowed value appears exactly once.

### 13.2 Every valid completion is explored

Take any valid completed board that agrees with the clues. At each originally empty cell, its value cannot conflict with earlier choices from that same completion or with any clue.

Therefore, the scanning version accepts that choice, and the bitmask version includes its bit. Following these choices reaches the completed board.

### 13.3 No completed board is counted twice

Cells are processed in one fixed order, and each legal value is tried once at its cell. A completed board determines exactly one sequence of choices for its originally empty cells.

### 13.4 Undo preserves the search state

Each branch restores the cell it changed. In the optimized version, it also restores the three corresponding masks. Sibling branches therefore start from the same state, rather than inheriting one another's placements.

---

## 14. Time and Space Complexity

Let:

- `B = boardSize`.
- `E` be the number of initially empty cells.
- `S` be the number of valid completed boards printed.

For masks, assume the value bits fit within one machine word, as they do for `4 × 4` and `9 × 9` Sudoku.

### 14.1 The search remains exponential

Ignoring constraints, each of the `E` empty cells has up to `B` values, giving at most:

$$
B^E
$$

complete candidate assignments. Sudoku checks prune many of these branches.

For a fixed `9 × 9` board, the usual coarse exponential search bound is written as `O(9^E)`, treating board-size factors as constants. This does not mean that all `9^E` assignments are actually explored.

**Bitmasks do not turn backtracking into a polynomial-time algorithm.** With the same cell order, both versions explore the same legal recursive branches; they differ in the work required to find those branches.

### 14.2 Compare the work at a state

| Operation | Scanning | Bitmasks with set-bit iteration |
| --- | --- | --- |
| Check one candidate | `O(B)` | `O(1)` |
| Find and visit the legal choices at an empty cell, excluding recursion | `O(B²)` | `O(1 + c)`, where `c` is the number of legal choices |
| Place or undo | `O(1)` | `O(1)` |
| Validate and initialize the board | `O(B³)` upper bound | `O(B²)` |
| Print one completed board | `O(B²)` | `O(B²)` |

For a more explicit implementation-sensitive bound, let `T` be the total number of recursive calls, including fixed-cell transitions and completed boards. Safe total-time bounds are:

```text
Scanning: O(B³ + B² × T + S × B²)
Bitmask:  O(B² + T + S × B²)
```

In the bitmask version, each set-bit iteration produces one child call, so all such iterations together are accounted for by `T`. In the scanning version, an empty-cell call may spend `O(B²)` testing candidates even if none leads to a child.

Printing is output-sensitive: writing `S` boards requires `Θ(S × B²)` value outputs regardless of how fast the search is. Removing `printBoard()` saves that output work, but counting all solutions still requires exploring the search tree.

### 14.3 Space complexity

| Storage | Scanning | Bitmasks |
| --- | --- | --- |
| Board | `O(B²)` | `O(B²)` |
| Row, column, and box masks | Not used | `O(B)` machine words |
| Recursion stack | `O(B²)` | `O(B²)` |
| Stored completed boards | None | None |

Both implementations use **`O(B²)` total working space**. Even excluding the input board, their recursive stack can use `O(B²)` space.

The depth follows the number of processed cells, not just `E`: these implementations also recurse through fixed cells and row transitions. If we instead recurse over a precomputed list of empty cells, the decision depth becomes `O(E)`.

---

## 15. Interview Insights and Common Pitfalls

### 15.1 One solution, all solutions, or uniqueness?

- **One solution:** A boolean recursion can return `true` as soon as a completion is found. To leave that solved board in place, return on success before undoing its placements. Failed branches must still undo normally.
- **All solutions or the exact count:** Explore every legal branch, as the programs above do.
- **Uniqueness:** Count only until a second solution is found. Zero means unsatisfiable, one means unique after the search is exhausted, and two means not unique. Preserve the undo contract when propagating an early-stop signal.

A solution found once is not evidence that it is the only solution.

### 15.2 A stronger next step: choose the most constrained cell

Our level order is fixed. A common search improvement is to choose the remaining empty cell with the **fewest legal values**, called the **Minimum Remaining Values (MRV)** heuristic.

If a cell has zero choices, fail immediately. If it has one choice, decide it before a cell with many choices.

Under this design, the level becomes “how many empty cells have been decided,” and we select the next cell dynamically. The LCCM reasoning and make/undo operations still apply. Selecting that cell also has a cost, but it can substantially reduce the search tree.

> **Interview Insight — Two different optimizations:** Bitmasks reduce the cost of checking a state. MRV changes the order of decisions to expose contradictions earlier. Faster checks and fewer explored states address different sources of work.

### 15.3 Why not memoize only `(row, col)`?

Different branches can reach the same position with different board configurations. Their legal choices and remaining solution counts can differ.

The board and its constraints are part of the state, even though they are stored globally. Caching an answer using only the cell coordinates is incorrect.

### 15.4 Invalid clues and unsatisfiable puzzles are different

Duplicate clues in one row, column, or box are immediate input contradictions. A board without such duplicates can still have no completion.

Do not assume that successful mask initialization means `ans` must be positive.

### 15.5 Bitmask mistakes to avoid

- **Setting a bit for `0`:** Zeros mean empty cells; ignore them during initialization and exclude bit `0` from `fullMask`.
- **Shifting before checking the input range:** Reject negative or out-of-range values first.
- **Using `~taken` without `fullMask`:** This admits bits that do not represent legal values.
- **Updating only `board`:** Every trial placement must update and restore all three masks too.
- **Blindly toggling clues with XOR:** Duplicate clues can cancel a bit instead of being rejected.
- **Extracting a position from an empty mask:** `__builtin_ffs(0)` returns `0`, so subtracting `1` would produce the invalid value `-1`. Only extract a position when the choice mask is nonzero.
- **Rechecking a clue against masks that already contain it:** It would conflict with itself. Validate each clue before adding its bit, then skip fixed cells during recursion.

### 15.6 Useful sanity checks

| Test | Expected behavior |
| --- | --- |
| The example `4 × 4` puzzle | Print its one completion, then `1` |
| An already complete, valid board | Print that board, then `1` |
| Duplicate clues in a row, column, or box | Print `0` |
| A value outside `0..boardSize` | Print `0` |
| A conflict-free partial board with no completion | Print `0` after searching |
| An empty `4 × 4` board | Print all `288` completed boards, then `288` |

For every printed solution, verify that it preserves the clues and that every row, column, and box contains exactly the allowed values.

---

## 16. Final LCCM Summary

```text
State
    current board + current cell
    optimized version: also maintain row, column, and box masks

Level
    one cell in row-major order

Choice
    a value from 1..boardSize for an empty cell
    a fixed clue has no branching choice

Check
    no repetition in the row, column, or box
    scanning: inspect the board
    bitmask: compute the mask of legal values

Move
    place → recurse → unplace
    restore every representation of the constraints

Success
    every cell has been processed
    count and print the completed board

Failure
    an empty cell has no legal choice

Optimization
    encode used values as bits and visit only available values
```

The central idea is unchanged from our earlier backtracking problems: define the state, decide one level at a time, reject conflicting choices, and undo every temporary move. Bitmasks make those same decisions cheaper to check.

</READING_WIDGET>
