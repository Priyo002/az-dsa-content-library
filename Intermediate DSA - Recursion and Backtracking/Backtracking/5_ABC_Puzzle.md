<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# ABC Puzzle — Row-by-Row Backtracking Using LCCM

## 1. Problem Statement

You are given an integer `N` and two strings, `R` and `C`, each of length `N` containing only `A`, `B`, and `C`.

Fill an initially empty `N × N` grid. A cell may contain `A`, `B`, or `C`, or remain empty, represented by `.`.

The completed grid must satisfy all four conditions:

1. Every row contains exactly one `A`, one `B`, and one `C`.
2. Every column contains exactly one `A`, one `B`, and one `C`.
3. The first nonempty cell from the left in row `i` contains `R[i]`.
4. The first nonempty cell from the top in column `j` contains `C[j]`.

Find and print **one** valid grid, or report that none exists. We use **0-based indexing** in the explanation and code.

### Constraints

- `3 ≤ N ≤ 5`.
- Both strings have length `N` and contain only `A`, `B`, and `C`.

The missing symbols and bounds in the supplied statement are restored from [AtCoder ABC326 D — ABC Puzzle](https://atcoder.jp/contests/abc326/tasks/abc326_d?lang=en).

### Input format

```text
N
R
C
```

There is one test case, with no test-case count before `N`.

### Output format

If no valid grid exists, print:

```text
No
```

Otherwise, print `Yes`, followed by `N` strings of length `N` describing the grid. Use `.` for empty cells. Any valid answer is accepted.

### Sample 1

```text
Input
5
ABCBC
ACAAB

Output
Yes
AC..B
.BA.C
C.BA.
BA.C.
..CBA
```

Every row and column contains each letter exactly once. Reading the first nonempty character of each row gives `ABCBC`; reading the first nonempty character of each column gives `ACAAB`.

### Sample 2

```text
Input
3
AAA
BBB

Output
No
```

For `N = 3`, each row must occupy all three cells. The first row would therefore have to equal `C = "BBB"`, but a row must contain one of each letter. This is impossible.

> **Interview Insight — Clarify the output goal:** This problem asks for one witness, not the number of solutions or every solution. Once a valid grid is saved, we can stop searching.

---

## 2. Choose a Whole Row, Not an Independent Cell

A direct cell-by-cell enumeration gives each cell four choices: `.`, `A`, `B`, or `C`. Before pruning, that creates `4^(N²)` complete assignments. For `N = 5`, this is `4^25`, which is far too large.

But most of those assignments violate the row condition immediately.

Every valid row must be a unique permutation of:

```text
A, B, C, followed by N - 3 copies of '.'
```

For `N = 5`, examples include:

```text
AC..B
.BA.C
..CAB
```

Instead of deciding one independent cell at a time, we can decide **one complete valid row** at each level.

This directly reuses the frequency-map technique from **Generate All Unique Permutations**. Repeated dots are equal values, so they must not create duplicate branches.

### 2.1 Divide the constraints between generation and checking

| Requirement | Where we enforce it |
| --- | --- |
| One `A`, one `B`, one `C` per row | Generate rows from fixed character frequencies |
| Leftmost letter of row `i` equals `R[i]` | Choose from a bucket indexed by that first letter |
| Topmost letter of column `j` equals `C[j]` | Check whenever a column receives its first letter |
| One `A`, one `B`, one `C` per column | Validate the completed grid at the base case |

We keep the supplied solution's design: **column letter coverage is checked at the end**, not maintained as an additional constraint during every move.

> **CP Insight — Reduce the search space through construction:** A generator that makes row constraints automatic is much more useful than generating arbitrary grids and checking every rule afterward.

---

## 3. First Recursion: Generate All Unique Rows

### 3.1 State

We maintain:

```text
s       = the row prefix built so far
freq    = remaining copies of each character
level   = the next position in this row
```

Initially:

```text
freq['A'] = 1
freq['B'] = 1
freq['C'] = 1
freq['.'] = N - 3
s = ""
```

Before `generate(level)` begins, `s.size() == level`, and the frequencies describe exactly the unused characters.

### 3.2 LCCM for row generation

| Part | Row-generation meaning |
| --- | --- |
| **Level** | The current position in the row |
| **Choice** | A distinct character from the frequency map |
| **Check** | Its remaining frequency is positive |
| **Move** | Decrement its count, append it, recurse, then undo both changes |

```cpp
remaining--;
s.push_back(ch);
generate(level + 1);
s.pop_back();
remaining++;
```

We change only the map's stored counts; we never erase entries while iterating.

### 3.3 Group rows by their first nonempty character

When `level == N`, scan the finished row from left to right and find its first character other than `.`.

Store the row in the corresponding bucket:

```text
all_positions[0] → rows whose first nonempty character is A
all_positions[1] → rows whose first nonempty character is B
all_positions[2] → rows whose first nonempty character is C
```

For example:

```text
AC..B → bucket A
.BA.C → bucket B
..CAB → bucket C
```

Every generated row contains all three letters, so the first nonempty character always exists. Return immediately after storing the row so that it enters exactly one bucket.

### 3.4 How many choices have we created?

The total number of unique rows is:

$$
P = \frac{N!}{(N-3)!} = N(N-1)(N-2).
$$

We can also obtain this by choosing distinct positions for `A`, `B`, and `C`.

Each bucket has the same size:

$$
B = \frac{P}{3} = 2\binom{N}{3}.
$$

To see why, choose the three occupied positions. The leftmost letter is fixed by the bucket; the other two letters can be arranged in two ways.

| `N` | All row patterns `P` | Patterns per bucket `B` | Complete row combinations before pruning `B^N` |
| ---: | ---: | ---: | ---: |
| 3 | 6 | 2 | 8 |
| 4 | 24 | 8 | 4,096 |
| 5 | 60 | 20 | 3,200,000 |

This is the search-space reduction that makes the given small constraints manageable.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/131ee112-ebc7-48f3-aa4b-a5d86cab35c3.png" alt="ABC Puzzle row generation for N equals 5: sixty unique permutations are grouped into three buckets of twenty patterns by their first nonempty letter, and R selects the required bucket" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Second Recursion: Build the Grid from Top to Bottom

The recursive function is:

```cpp
rec(level, curr_done)
```

Its state consists of:

- `level`: the row we are about to choose.
- `curr_sol`: the rows already chosen, in top-to-bottom order.
- `curr_done`: a bitmask recording which columns already contain a letter.

`sol_found` and `final_sol` record the search result. They are not temporary branch state and are not undone.

### Recursive invariant

Before `rec(level, curr_done)` begins:

1. `curr_sol` contains exactly `level` rows.
2. Every chosen row contains one of each letter and has the required leftmost letter.
3. Bit `j` of `curr_done` is set exactly when column `j` contains a nonempty cell among those rows.
4. In every such column, the topmost letter already matches `C[j]`.

**We do not claim that the columns have no duplicate letters yet.** That condition is deliberately deferred to the final check.

### LCCM for grid construction

| Part | Grid-search meaning |
| --- | --- |
| **Level** | The current row `level` |
| **Choice** | A row in `all_positions[R[level] - 'A']` |
| **Check** | Any newly started column must begin with its required letter |
| **Move** | Append the row, recurse with the updated mask, then remove the row |

The same LCCM framework appears twice, but with different meanings: the first recursion decides a **character**, while the second decides an **entire row**.

---

## 5. What Does the `done` Bitmask Actually Mean?

Use bit `j` to represent column `j`:

```cpp
1 << j
```

The bit has only two meanings:

- `0`: no previous row has placed a letter in this column.
- `1`: the column's topmost letter has already been placed and checked.

It does **not** mean that the column is full, contains all three letters, or has no duplicates. A more descriptive reading of `done` is “topmost character decided.”

Initially:

```cpp
int none_done = 0;
```

The mask with every column started is:

```cpp
int all_done = (1 << n) - 1;
```

For `N = 5`, this is `11111` in binary.

### 5.1 Checking a candidate row

At column `pos`, there are three cases:

| Candidate cell | Previous bit | Action |
| --- | --- | --- |
| `.` | Either | Ignore it; no new letter is placed |
| A letter | `1` | No topmost-letter check is needed |
| A letter | `0` | This becomes the topmost letter, so it must equal `C[pos]` |

The rejection condition is:

```cpp
if (row[pos] != '.' &&
    (done & (1 << pos)) == 0 &&
    row[pos] != C[pos]) {
    return false;
}
```

Because rows are processed from top to bottom, a newly placed letter cannot change an earlier topmost letter.

> **Interview Insight — Use the traversal order in the proof:** We can settle the topmost condition at the first insertion only because future decisions are in lower rows. This check would not be sufficient if rows were filled in an arbitrary order.

### 5.2 Updating the mask

For every nonempty cell of the chosen row:

```cpp
done |= (1 << pos);
```

Use **OR**, not XOR. Placing another letter in an already started column must leave its bit set, not toggle it back to zero.

`newDone` receives its mask by value and returns the updated copy. The caller's mask is unchanged, so there is no explicit mask undo.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/aaf7fa4f-7027-402d-a8f1-3166e9f0b0a2.png" alt="Adding row dot B A dot C below A C dot dot B starts column 2 with the required A and changes the column-start mask from 10011 to 10111; set bits record started columns, not complete columns" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The shared vector `curr_sol`, however, must be restored:

```cpp
curr_sol.push_back(row);
rec(level + 1, newDone(curr_done, row));
curr_sol.pop_back();
```

---

## 6. Base Case: Why Are Three Distinct Letters Enough?

When `level == n`, all rows have been chosen. Now validate the columns.

The supplied `is_valid` function inserts each column's nonempty characters into a `set<char>` and requires its size to be `3`.

At first glance, this seems weaker than “exactly one of each”: a column containing `A, A, B, C` also has three distinct letters.

**The check is correct here because of the row invariant and a global counting argument.**

1. Each of the `N` generated rows contains exactly three letters.
2. The whole grid therefore contains exactly `3N` letters.
3. If every column contains all three distinct letters, each column contains at least three letters.
4. Across `N` columns, that already requires at least `3N` letters.
5. Since there are exactly `3N`, every column must contain exactly three letters.
6. Those three letters are distinct, so they are precisely one `A`, one `B`, and one `C`.

If one column had a duplicate in addition to all three letters, another column would have fewer than three letters and fail validation.

> **Interview Insight — A set does not count multiplicity:** `st.size() == 3` alone does not prove uniqueness within an arbitrary column. Its sufficiency here depends on checking **every column** and knowing the exact total number of letters from row generation.

### Is `curr_done == all_done` enough?

No. It says only that no column is completely empty.

For example, with `N = 3`, `R = "AAA"`, and `C = "ABC"`, choosing `ABC` for every row passes the row-leftmost and topmost checks. All columns are started, but their letters are `AAA`, `BBB`, and `CCC`, so the final column check rejects the grid.

Conversely, passing `is_valid` already implies that every column is nonempty. The `all_done` condition is logically redundant at success, but we retain it to make the intended completion test explicit and to match the supplied approach.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/6d5aeab6-1c44-4dfe-9a3a-85cc92f9dfcd.png" alt="A grid with three identical ABC rows passes the topmost checks but fails column validation; a counting argument shows that three distinct letters in every column and exactly 3N letters overall imply one of each letter per column" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 7. Dry Run — Follow the Sample's Successful Branch

Use:

```text
N = 5
R = ABCBC
C = ACAAB
```

The following follows the supplied sample grid as **one successful path**. It is not a claim that the program visits this path first.

Masks below are written as bits `4..0`, so column `0` is the rightmost bit.

| Row level | Required first letter | Chosen row | Newly started columns | Mask after placement |
| ---: | --- | --- | --- | --- |
| 0 | `A` | `AC..B` | `0, 1, 4` | `10011` |
| 1 | `B` | `.BA.C` | `2` | `10111` |
| 2 | `C` | `C.BA.` | `3` | `11111` |
| 3 | `B` | `BA.C.` | None | `11111` |
| 4 | `C` | `..CBA` | None | `11111` |

### 7.1 First row

For `AC..B`, all occupied columns are new:

- Column `0` starts with `A`, matching `C[0]`.
- Column `1` starts with `C`, matching `C[1]`.
- Column `4` starts with `B`, matching `C[4]`.

Columns `2` and `3` stay unstarted because their cells are dots.

### 7.2 Rejecting a candidate in the second row

At level `1`, suppose we try `B.CA.`. It belongs to the correct `B` bucket, but column `2` has not started yet.

This row would start column `2` with `C`, while `C[2] == 'A'`. Reject it without appending it to `curr_sol`.

The sample row `.BA.C` passes instead: its `A` starts column `2` correctly. Its letters in columns `1` and `4` lie below existing topmost letters and need no new topmost check.

### 7.3 The mask is full before the grid is finished

After `C.BA.`, every column has started. Still, two rows remain to be chosen, and the column multiplicities remain unchecked.

After all five sample rows are chosen, the column strings are:

```text
Column 0: A.CB.
Column 1: CB.A.
Column 2: .AB.C
Column 3: ..ACB
Column 4: BC..A
```

Each contains exactly one of each letter, so we save the grid in `final_sol` and set `sol_found = true`.

### 7.4 Restoring the working state

As recursion returns, each caller removes the row it appended. The saved `final_sol` is a separate copy, so it remains intact.

After the undo, an early return propagates success without trying additional candidates. If a complete grid had failed validation instead, recursion would undo and try the next candidate normally.

---

## 8. Clean Runnable C++ Code

This is the supplied two-stage approach with read-only parameters passed by `const` reference and immediate stopping after a solution is saved. We keep the frequency generator, first-letter buckets, column-start mask, and final set-based validation.

```cpp
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

int n;
string R, C;

map<char, int> freq;
string s;
vector<string> all_positions[3];

vector<string> curr_sol, final_sol;
bool sol_found = false;
int all_done;

// Generate unique permutations of A, B, C, and n - 3 dots.
void generate(int level) {
    if (level == n) {
        for (char ch : s) {
            if (ch != '.') {
                all_positions[ch - 'A'].push_back(s);
                return;
            }
        }
        return;
    }

    for (auto& entry : freq) {
        char ch = entry.first;
        int& remaining = entry.second;
        if (remaining == 0) continue;

        remaining--;
        s.push_back(ch);
        generate(level + 1);
        s.pop_back();
        remaining++;
    }
}

// Check only columns whose topmost letter is being placed now.
bool check(const string& row, int done) {
    for (int pos = 0; pos < n; pos++) {
        if (row[pos] != '.' &&
            (done & (1 << pos)) == 0 &&
            row[pos] != C[pos]) {
            return false;
        }
    }
    return true;
}

int newDone(int done, const string& row) {
    for (int pos = 0; pos < n; pos++) {
        if (row[pos] != '.') {
            done |= (1 << pos);
        }
    }
    return done;
}

// Called only after n valid rows have been chosen.
bool is_valid(const vector<string>& sol) {
    for (int col = 0; col < n; col++) {
        set<char> letters;
        for (int row = 0; row < n; row++) {
            if (sol[row][col] != '.') {
                letters.insert(sol[row][col]);
            }
        }
        if (letters.size() != 3) return false;
    }
    return true;
}

void rec(int level, int curr_done) {
    if (sol_found) return;

    if (level == n) {
        if (curr_done == all_done && is_valid(curr_sol)) {
            final_sol = curr_sol;
            sol_found = true;
        }
        return;
    }

    int first_ch = R[level] - 'A';
    for (const string& row : all_positions[first_ch]) {
        if (!check(row, curr_done)) continue;

        curr_sol.push_back(row);
        rec(level + 1, newDone(curr_done, row));
        curr_sol.pop_back();

        // Restore our placement before propagating success.
        if (sol_found) return;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> R >> C;

    freq['A'] = freq['B'] = freq['C'] = 1;
    freq['.'] = n - 3;
    generate(0);

    all_done = (1 << n) - 1;
    rec(0, 0);

    if (!sol_found) {
        cout << "No\n";
    } else {
        cout << "Yes\n";
        for (const string& row : final_sol) {
            cout << row << '\n';
        }
    }
    return 0;
}
```

The program handles one test case. If adapted for several cases, clear the buckets, frequency map, working strings and vectors, saved answer, and success flag before each case.

---

## 9. Why the Algorithm Is Correct

### 9.1 Row generation is complete and has no duplicates

At each position, the generator tries every distinct character with a positive remaining count. Every valid row corresponds to exactly one sequence of these choices.

Each choice consumes one available occurrence, so a completed row contains the required multiset. Equal dots do not create separate choices, so no row is generated twice. Grouping by its first nonempty letter puts it in exactly the bucket needed by any compatible row requirement.

### 9.2 Every reported grid is valid

Every chosen row comes from the required bucket, so it satisfies its letter counts and leftmost condition.

Whenever a column receives its first letter, `check` verifies that letter against `C`. Top-to-bottom processing ensures it remains the topmost letter.

At the base case, every column contains all three letters. The `3N` counting argument proves that each occurs exactly once. Therefore, every saved and printed grid satisfies all conditions.

### 9.3 A valid grid cannot be missed

Consider any valid grid. Every one of its rows is generated and stored in the bucket selected at that row's level.

If recursion has chosen the preceding rows of this grid, its next row passes `check`: every newly started column has the required topmost letter because the grid is valid.

Thus, none of the choices on this path is incorrectly pruned. The completed grid passes final validation. The search either reaches it or stops earlier after finding another valid grid, which also satisfies the task.

Consequently, printing `No` after the search finishes means that no valid grid exists.

### 9.4 Termination and restoration

Both recursive functions increase their level and stop at `n`. Every temporary append has a matching removal; row generation also restores its frequency decrement. The mask is passed by value. Sibling branches therefore start from the correct original state.

---

## 10. Time and Space Complexity

Let:

$$
P = N(N-1)(N-2), \qquad B = P/3.
$$

### 10.1 Row generation

There are `P` unique rows, each of length `N`. Scanning and storing them costs `O(NP)` time and space.

The generator's prefix tree has at most `1 + NP` nodes: every prefix lies on a path to a completed row. At each node, we scan at most four map entries. Thus the generation work also fits within `O(NP)`.

The map's size is at most four, so there is no growing `log N` factor for map operations here.

### 10.2 Grid search

Ignoring pruning and early success, the search has at most `B^N` complete row combinations and `O(B^N)` nodes, since `B ≥ 2`.

- Checking a candidate row, updating its mask, and copying it into `curr_sol` each take `O(N)`.
- Final column validation takes `O(N²)` per completed candidate.
- Each set contains at most three distinct letters, so its operations have constant cost with respect to `N`.

A conservative total bound is:

$$
O(NP + N^2 B^N).
$$

For `N = 5`, there are at most `20^5 = 3,200,000` complete row combinations **before** topmost-letter pruning. Actual work depends on `R`, `C`, rejected prefixes, and when the first solution is found. This remains an exponential search intended for the given small bounds.

> **CP Insight — Count candidate patterns, not just recursion depth:** The grid recursion is only `N` levels deep, but up to `B` row choices branch at every level. A shallow recursion can still perform substantial work.

### 10.3 Space

| Storage | Cost |
| --- | --- |
| All generated row patterns | `O(NP)` |
| Current grid and saved solution | `O(N²)` |
| Row-generation string and either recursive stack | `O(N)` |
| Frequency map and temporary column set | `O(1)` |

Total working space is:

$$
O(NP + N^2).
$$

The two recursive phases run one after the other; their depths do not multiply. We store all **row patterns**, not all complete grids.

---

## 11. Common Mistakes and Interview Insights

### 11.1 Confusing leftmost with the first cell

`R[i]` need not appear in column `0`. Leading dots are allowed. Likewise, a column's topmost letter need not appear in row `0`.

Always find the first **nonempty** cell.

### 11.2 Rechecking `C[j]` for every letter in a column

Only the first letter placed in a column must match `C[j]`. Later letters are below it and may differ. Use the mask to distinguish these cases.

### 11.3 Treating all columns started as success

The mask tracks only whether a column has begun. Do not stop at `curr_done == all_done` before all rows are chosen, and do not skip `is_valid` at the base case.

### 11.4 Counting dots as column characters

The set must exclude `.`. We want coverage of `A`, `B`, and `C`, not three arbitrary symbols from the four-character alphabet.

### 11.5 Forgetting that partial columns may contain duplicates

In this implementation, `check` verifies only the topmost condition. A branch may pass every incremental check and still fail column validation at the end.

Do not describe its invariant as “all partial columns are valid.” The precise invariant is weaker, and the correctness proof must include the final check.

### 11.6 Memoizing only `(level, curr_done)`

These parameters do not contain the full state. Two prefixes may start the same columns but contain different letters below their topmost cells. Their possible completions can differ.

`curr_sol` is also part of the logical state, even though it is stored globally. Caching only the two parameters would lose information needed by final column validation.

### 11.7 Returning before undoing a successful move

Here, we save a separate copy of the answer and promise to restore `curr_sol`. Therefore, pop the current row before returning on success. Printing the working vector after full unwinding would print nothing; print `final_sol` instead.

### 11.8 Expecting the exact sample grid

The judge accepts any valid grid. The frequency map determines generation order, but the solution does not rely on reproducing the sample output. Validate the rules, not equality with one reference grid.

### Useful sanity checks

| Input or situation | What to verify |
| --- | --- |
| `N = 3`, `R = ABC`, `C = ABC` | A cyclic arrangement such as `ABC / BCA / CAB` is valid |
| `N = 3`, `R = AAA`, `C = BBB` | Print `No`; the top row cannot meet the column requirements |
| `N = 3`, `R = AAA`, `C = ABC` | Print `No`; topmost checks alone do not enforce column counts |
| `N = 4` | Each generated row has exactly one dot; each bucket has eight rows |
| `N = 5` | Each generated row has exactly two dots; each bucket has twenty unique rows |
| Sample 1 | Print a valid grid, not necessarily the displayed sample grid |

---

## 12. Final LCCM Summary

```text
Phase 1: Generate row patterns
    Level  = one character position
    Choice = a distinct character with remaining frequency
    Check  = frequency is positive
    Move   = consume → append → recurse → remove → restore
    Base   = store the row by its first nonempty letter

Phase 2: Assemble the grid
    Level  = one row, from top to bottom
    Choice = a generated row whose first letter matches R[level]
    Check  = newly started columns must match C
    Move   = append row → recurse with updated mask → remove row
    Base   = validate all columns; save one valid answer

Stopping
    Stop after finding one solution, while restoring temporary state.

Key distinction
    A started column is not necessarily a valid completed column.
```

The central lesson is to choose the right unit of recursion. By generating valid rows first, we enforce row constraints by construction, use top-to-bottom order to check column beginnings early, and leave only column coverage for the final validation.

</READING_WIDGET>
