<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Fractal Form — Build a Picture with Recursion

## 1. What Is Fractal Form?

In the earlier lessons, recursion helped us explore arrangements, select a particular move, and combine answers from smaller subproblems. Here, recursion describes the **shape of the output itself**.

A fractal construction repeatedly applies the same rule at smaller scales. A small model determines the large picture, and parts of that picture contain smaller copies of the same construction.

For this problem, the rule is:

> A black model cell becomes a solid black block. A white model cell becomes a smaller copy of the construction, as long as steps remain.

We produce a finite picture after `k` steps, not an infinitely detailed object.

---

## 2. Problem Statement

Kalevitch creates an `n × n` model on graph paper. Each cell is either:

- `.` — white;
- `*` — black.

Starting with a clean white square, he performs the following process:

1. Divide the square into `n²` equal squares and paint them according to the model.
2. Divide every square that remains white into `n²` smaller squares and apply the same model inside it.
3. Repeat the second step until a total of `k` steps have been performed.

Already black squares remain completely black. They are not replaced by another copy of the model.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/19a7a127-7e8a-473e-864b-20247f15b3c2.png" alt="Fractal construction from step 0 to step 3 for the model with a black top-right cell: only white regions are subdivided while black regions remain solid" style="max-width: 100%; height: auto; box-sizing: border-box; border: 3px solid #0b2d72; border-radius: 12px; padding: 12px;" identifier="az-img-upload">

*From left to right: steps 0, 1, 2, and 3 for the model `.* / ..`. Black regions remain black; only white regions are subdivided.*

Print the final picture as an `nᵏ × nᵏ` character matrix.

### Constraints

- `2 ≤ n ≤ 3`.
- `1 ≤ k ≤ 5`.
- The model contains at least one white cell.

### Input

```text
n k
model[0]
model[1]
...
model[n-1]
```

Each model row contains exactly `n` characters.

### Output

Print exactly `nᵏ` lines, each containing `nᵏ` characters. Do not put spaces between cells.

### Example 1

Input:

```text
2 3
.*
..
```

Output:

```text
.*******
..******
.*.*****
....****
.***.***
..**..**
.*.*.*.*
........
```

### Example 2

Input:

```text
3 2
.*.
***
.*.
```

Output:

```text
.*.***.*.
*********
.*.***.*.
*********
*********
*********
.*.***.*.
*********
.*.***.*.
```

---

## 3. Think in Blocks, Not Individual Paint Operations

Let `F(t)` denote the picture obtained from a white square after `t` steps.

For `t = 0`, no painting has happened. At the final output resolution, this is one white cell:

```text
F(0) = .
```

To build `F(t)` for `t > 0`, create an `n × n` arrangement of blocks, each with side length `n^(t-1)`:

- If the corresponding model cell is `*`, fill the entire block with `*`.
- If it is `.`, place `F(t-1)` inside that block.

For the model:

```text
.*
..
```

the four block positions are:

```text
Top-left:     F(t-1)
Top-right:    solid black block
Bottom-left:  F(t-1)
Bottom-right: F(t-1)
```

The side length therefore satisfies:

$$
S(0)=1, \qquad S(t)=nS(t-1)
$$

and hence:

$$
\boxed{S(t)=n^t}
$$

The number of cells in the final answer is `n^(2k)`, not `n² × k`.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/f44ce332-065e-4ba8-a5fe-1a9e0767e710.png" alt="AlgoZenith fractal progression from one white square to the 2 by 2 model and its 4 by 4 expansion; black blocks remain solid while white blocks repeat the model" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Define the Recursive State

Instead of repeatedly resizing intermediate pictures, allocate the final answer once, initially filled with `.`.

Use the function:

```text
draw(row, col, size, remaining)
```

Its parameters mean:

| Parameter | Meaning |
| --- | --- |
| `row` | Top row of the current square in the final answer |
| `col` | Leftmost column of the current square |
| `size` | Side length of the current square |
| `remaining` | Number of model applications still needed inside this square |

### Recursive contract

Before a call, its square is white. The function draws the picture for `remaining` steps inside that square and does not modify any cell outside it.

The state maintains:

$$
\text{size}=n^{\text{remaining}}
$$

The initial call is:

```text
draw(0, 0, n^k, k)
```

Although `size` can be derived from `remaining`, passing both makes the coordinate calculations easy to read. They must always satisfy the invariant above.

### Base case

If `remaining == 0`, the square has side length `1`. It represents a white cell that survived all `k` steps.

The answer was initialized with dots, so there is nothing to write. Return immediately.

---

## 5. Apply the LCCM Framework

We can use the same **Level, Choice, Check, Move** questions from the backtracking lessons to organize this recursion, while recognizing that this problem has no competing choices to search.

| Part | Fractal construction |
| --- | --- |
| **Level** | The current scale, represented by `remaining` steps |
| **Choice** | Visit each of the `n²` child positions `(i, j)` in the model |
| **Check** | Read whether `model[i][j]` is black or white |
| **Move** | Fill a black child block, or recurse into a white child block |

Here, “choice” means which child region to process next. We must process every child, and its content is forced by the model.

### Calculate the child coordinates

Each child has side length:

```text
childSize = size / n
```

The model position `(i, j)` maps to:

```text
childRow = row + i * childSize
childCol = col + j * childSize
```

For a black model cell, paint the rectangle:

```text
Rows:    childRow ... childRow + childSize - 1
Columns: childCol ... childCol + childSize - 1
```

For a white model cell, call:

```text
draw(childRow, childCol, childSize, remaining - 1)
```

### Why is there no undo step?

In N-Queens or Sudoku, we undo a placement to explore an alternative configuration. Here, there is exactly one required picture.

Sibling calls work on disjoint regions. A painted black block is final, and a white child call never needs to erase work done elsewhere. Undoing the paint would destroy part of the answer.

> **Interview Insight — Recursion is not always backtracking:** Use the framework to define progress and transitions, but add an undo step only when exploring alternatives requires restoring shared state. This is deterministic recursive construction.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/5a7f191a-5c8c-433c-95ab-690e7e2e9742.png" alt="AlgoZenith diagram of draw(0, 0, 8, 3): recurse into blocks at (0,0), (4,0), and (4,4), fill the block at (0,4) black, and stop at remaining equals zero without undoing completed regions" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 6. Complete C++ Implementation

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int n, k;
vector<string> model;
vector<string> picture;

void fillBlack(int row, int col, int size) {
    for (int r = row; r < row + size; ++r) {
        for (int c = col; c < col + size; ++c) {
            picture[r][c] = '*';
        }
    }
}

void draw(int row, int col, int size, int remaining) {
    if (remaining == 0) {
        return;
    }

    int childSize = size / n;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int childRow = row + i * childSize;
            int childCol = col + j * childSize;

            if (model[i][j] == '*') {
                fillBlack(childRow, childCol, childSize);
            } else {
                draw(childRow, childCol, childSize, remaining - 1);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    model.resize(n);
    for (string& row : model) {
        cin >> row;
    }

    int side = 1;
    for (int step = 0; step < k; ++step) {
        side *= n;
    }

    picture.assign(side, string(side, '.'));
    draw(0, 0, side, k);

    for (const string& row : picture) {
        cout << row << '\n';
    }
    return 0;
}
```

We compute `n^k` using integer multiplication. In C++, `^` is XOR, not exponentiation; floating-point `pow` is unnecessary here.

---

## 7. Dry Run: Model .* / ..

Use the first sample's model:

```text
.*
..
```

### After one step

Each model cell corresponds to one output cell:

```text
.*
..
```

Thus `F(1)` is exactly the model.

### After two steps

Each block now has side length `2`.

- Top-left: put `F(1)`.
- Top-right: put a solid `2 × 2` black block.
- Bottom-left: put `F(1)`.
- Bottom-right: put `F(1)`.

This gives:

```text
.***
..**
.*.*
....
```

Notice that the top-right block contains four stars, not another `.* / ..` pattern. It was already black at the first step.

### After three steps: trace the root call

The final side length is `2³ = 8`:

```text
draw(0, 0, 8, 3)
childSize = 4
```

| Model position | Character | Child top-left | Action |
| --- | --- | --- | --- |
| `(0, 0)` | `.` | `(0, 0)` | `draw(0, 0, 4, 2)` |
| `(0, 1)` | `*` | `(0, 4)` | Fill rows `0..3`, columns `4..7` black |
| `(1, 0)` | `.` | `(4, 0)` | `draw(4, 0, 4, 2)` |
| `(1, 1)` | `.` | `(4, 4)` | `draw(4, 4, 4, 2)` |

Each recursive call with `remaining = 2` draws the `4 × 4` picture from the previous step inside its assigned region.

The result is:

```text
.*******
..******
.*.*****
....****
.***.***
..**..**
.*.*.*.*
........
```

### Follow one branch down to the base case

```text
draw(0, 0, 8, 3)
  draw(0, 0, 4, 2)
    draw(0, 0, 2, 1)
      draw(0, 0, 1, 0) → return; cell (0,0) stays white
      fillBlack(0, 1, 1)
      draw(1, 0, 1, 0) → return
      draw(1, 1, 1, 0) → return
```

At every descent, the side length is divided by `n` and `remaining` decreases by one. After the child returns, the parent continues with its next block. No paint is undone.

Although the story performs painting one stage at a time, our program completes one white region recursively before visiting the next. These orders produce the same picture because the regions do not overlap.

---

## 8. Why Is the Construction Correct?

We prove the recursive contract by induction on `remaining`.

### Base case

For `remaining = 0`, no further painting is needed. The single initially white cell remains white, as required.

### Recursive step

Assume the function correctly draws every smaller white square for `remaining - 1` steps.

The current square is partitioned into `n²` disjoint child squares that cover it completely.

- A black model position must remain black throughout all later steps. Filling its entire child square is correct.
- A white model position must undergo the same process for one fewer step. By the induction hypothesis, its recursive call produces the correct child picture.

Every child is handled according to the model, no cell outside the current square is changed, and no child overwrites another. Therefore, the entire current square is correct.

Applying this to `draw(0, 0, n^k, k)` proves that the printed matrix is the required picture.

---

## 9. Time and Space Complexity

Let:

$$
S=n^k, \qquad M=S^2=n^{2k}
$$

Here `M` is the number of characters in the output matrix.

### Painting cost

The nested loops in `fillBlack` may look expensive, but painted black blocks are disjoint. We never recurse into a black block, so no final cell is painted black twice.

Across all calls, the total black-painting work is at most `M` cell assignments.

### Recursive traversal cost

Let `w` be the number of white cells in the model. Only those positions generate recursive calls. At depth `d`, there are `w^d` calls, and each non-base call examines `n²` model positions.

The total child-processing work is:

$$
O\left(n^2\sum_{d=0}^{k-1}w^d\right)
\le O\left(n^2\sum_{d=0}^{k-1}n^{2d}\right)
=O(n^{2k})
$$

This also covers the all-white model, where every position recurses.

Initializing and printing the matrix each take `Θ(M)` time. Therefore:

- **Total time:** `Θ(n^(2k))`.
- **Output matrix storage:** `Θ(n^(2k))`.
- **Model storage:** `O(n²)`.
- **Recursion stack:** `O(k)`.

At the largest allowed values, `S = 3⁵ = 243`, so the output has `59,049` cells.

> **CP Insight — Compare work with output size:** Printing the required matrix already takes `Ω(n^(2k))` time. This solution is linear in the number of output cells, even though that number grows exponentially with the number of steps.

---

## 10. Sanity Checks and Common Mistakes

### A useful white-cell count

Initially there is one white region. Each step replaces every white region with exactly `w` white children. Consequently, after `k` steps:

$$
\text{White cells}=w^k
$$

and:

$$
\text{Black cells}=n^{2k}-w^k
$$

For the first sample, `w = 3` and `k = 3`: there must be `27` dots and `37` stars. This does not verify their positions, but it is a useful additional test.

### Cases to test

- **`k = 1`:** The output must be exactly the model.
- **All-white model:** The entire final matrix must be dots. The constraints allow this.
- **Exactly one white model cell:** Exactly one final cell remains white, regardless of `k`.
- **Asymmetric model:** Helps catch row/column transposition.
- **Maximum `n` and `k`:** Verify the output is `243 × 243`.

### Mistakes to avoid

1. **Applying the model inside black blocks.** Only white blocks recurse.
2. **Painting one cell instead of a whole block.** Early black cells represent large areas in the final matrix.
3. **Using `row + i` instead of `row + i * childSize`.** Model positions must be scaled to block positions.
4. **Forgetting the parent offset.** Child coordinates are relative to the current square, not always the whole picture.
5. **Recursing with the same remaining depth.** Each child uses `remaining - 1`.
6. **Adding an undo step.** Completed blocks are part of the final answer, not temporary choices.
7. **Confusing `n^k` with `n*k` or C++ XOR.** Compute the side length by repeated multiplication.

---

## 11. Quick Recap

Fractal form appears when the same construction repeats inside smaller regions.

For this problem, a recursive state identifies a square by its top-left corner, side length, and remaining depth. Split it into `n²` children:

- **Black model cell:** Fill the child square completely.
- **White model cell:** Recurse with one fewer step.
- **No remaining steps:** Leave the cell white.

The LCCM questions help organize the state and transitions, but this is deterministic construction rather than a backtracking search. The children occupy disjoint regions, so no undo or separate merge step is needed.

> **The reusable idea:** When a picture contains smaller instances of the same rule, let one recursive call own one region of the final output.

</READING_WIDGET>
