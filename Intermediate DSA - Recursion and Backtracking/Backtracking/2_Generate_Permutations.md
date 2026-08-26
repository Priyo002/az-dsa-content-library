<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Generate All Unique Permutations Using LCCM

## 1. Problem Statement

Given an array of numbers that may contain duplicates, print all its **unique permutations** in **lexicographically increasing order**.

### Example

```text
Input
3
1 1 2

Output
1 1 2
1 2 1
2 1 1
```

The array has `3! = 6` permutations if the two copies of `1` are treated as different objects. However, only three value sequences are unique.

This problem is an excellent application of the **LCCM backtracking framework**:

- **Level**
- **Choice**
- **Check**
- **Move**

---

## 2. What Is a Permutation?

A permutation is an arrangement that uses every element exactly once.

For the array:

```text
[1, 2, 3]
```

all elements are distinct, so the number of permutations is:

```text
3! = 6
```

They are:

```text
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
```

### 2.1 What changes when duplicates are present?

Consider:

```text
[1, 1, 2]
```

To understand the duplication, temporarily label the two equal values as different physical occurrences:

```text
[1ₐ, 1ᵦ, 2]
```

Swapping `1ₐ` and `1ᵦ` creates a different arrangement of occurrences, but it does not create a different sequence of values:

```text
[1ₐ, 1ᵦ, 2] → [1, 1, 2]
[1ᵦ, 1ₐ, 2] → [1, 1, 2]
```

Similarly:

```text
[1ₐ, 2, 1ᵦ] → [1, 2, 1]
[1ᵦ, 2, 1ₐ] → [1, 2, 1]

[2, 1ₐ, 1ᵦ] → [2, 1, 1]
[2, 1ᵦ, 1ₐ] → [2, 1, 1]
```

Therefore, we must not build separate recursive branches for equal occurrences.

### 2.2 Number of unique permutations

Suppose an array has `N` elements, and its distinct values have frequencies:

```text
c₁, c₂, ..., cD
```

where:

```text
c₁ + c₂ + ... + cD = N
```

The number of unique permutations is:

```text
                  N!
P = --------------------------------
    c₁! × c₂! × ... × cD!
```

This expression is called a **multinomial coefficient**. It generalizes the binomial coefficient to arrangements containing multiple groups of indistinguishable objects.

The denominator removes the overcounting caused by rearranging equal copies among themselves. Rearranging the `cᵢ` copies of one value in `cᵢ!` ways does not create new value sequences, so we divide by `cᵢ!` for every distinct value.

For `[1, 1, 2]`:

```text
frequency(1) = 2
frequency(2) = 1

     3!
P = ---- = 3
     2!
```

> **Interview Insight — Count the output before designing the algorithm:** If all `N` values are distinct, there are `N!` answers. No algorithm can print them faster than the size of that output. Backtracking is appropriate because the output itself is factorial.

---

## 3. The Central Idea: Choose a Value, Not an Occurrence

A naive implementation might keep a `used[]` array and choose an unused index at every level. For duplicate values, different indices can hold the same value, so this creates repeated branches.

Instead, store the remaining frequency of every distinct value:

```text
frequency[value] = number of unused copies of value
```

For `[1, 1, 2]`, the initial frequency map is:

```text
1 → 2
2 → 1
```

At a recursive level, our choices are the distinct values whose remaining frequency is positive.

There is only one branch labelled `1`, regardless of whether we imagine using `1ₐ` or `1ᵦ`. Once that branch is selected, the remaining frequency of `1` decreases from `2` to `1`.

This single decision removes duplicate permutations at their source. We do not generate duplicates and remove them later.

> **Interview Insight — Prefer generation without duplication:** Generating all `N!` indexed arrangements and inserting them into a `set` is correct, but it wastes time and memory. A stronger backtracking design ensures that every recursive branch represents a distinct value sequence.

---

## 4. Defining the State

The state of the recursion contains two pieces of information.

### 4.1 The current prefix

```text
current = values already selected for the permutation
```

For example:

```text
current = [1, 2]
```

means that positions `0` and `1` have already been fixed.

### 4.2 The remaining frequency map

```text
frequency[value] = unused copies of this value
```

If the original array is `[1, 1, 2]` and `current = [1, 2]`, then:

```text
frequency = {1 → 1, 2 → 0}
```

The prefix and the frequency map must remain consistent:

```text
current.size() + sum of all remaining frequencies = N
```

### 4.3 Recursive invariant

Before `rec(level)` begins:

- `current` contains exactly `level` values,
- `current[0 ... level - 1]` is the fixed prefix of the permutation,
- `frequency[x]` is the number of unused copies of value `x`, and
- every completion of this state must use exactly the values remaining in the frequency map.

The job of `rec(level)` is to print every unique completion of this prefix in lexicographically increasing order.

---

## 5. Applying the LCCM Framework

| Part | Question | Answer for this problem |
| --- | --- | --- |
| **Level** | Which part of the answer are we deciding? | The index `level` in the permutation |
| **Choice** | What can be placed at this index? | Any distinct value present in the frequency map |
| **Check** | Is this value still available? | `frequency[value] > 0` |
| **Move** | How do we explore this decision? | Use one copy, append it, recurse, then restore both changes |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/979f492a-ac19-4c9e-a5f3-b62f936840d0.png" alt="The Level, Choice, Check, and Move stages for generating unique permutations with a frequency map" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 5.1 Level

The level is the index that we are currently filling:

```text
level 0 → choose the value at index 0
level 1 → choose the value at index 1
level 2 → choose the value at index 2
...
```

Because exactly one value is appended at every recursive step:

```text
level == current.size()
```

### 5.2 Choice

The possible choices are the **distinct values** in the frequency map.

For:

```text
frequency = {1 → 2, 2 → 1}
```

the choices are `1` and `2`, not `1ₐ`, `1ᵦ`, and `2`.

### 5.3 Check

A value can be placed only when at least one unused copy remains:

```cpp
remaining > 0
```

If the remaining frequency is zero, that value has already been used as many times as it occurs in the input.

### 5.4 Move

When choosing a value:

```cpp
remaining--;
current.push_back(value);

rec(level + 1);

current.pop_back();
remaining++;
```

The move has two state changes:

1. consume one copy from the frequency map, and
2. append the selected value to the current prefix.

Backtracking performs their inverse operations in reverse order:

1. remove the value from the prefix, and
2. restore its frequency.

After the undo, the next choice sees exactly the same state that existed before the current choice was made.

> **Interview Insight — Undo every changed component:** Here, both `current` and `frequency` belong to the state. Restoring only one of them breaks the recursive invariant and corrupts sibling branches.

---

## 6. Base Case

When:

```text
level == N
```

all `N` positions have been decided. The current prefix is now a complete permutation.

```cpp
if (level == n) {
    print(current);
    return;
}
```

No additional duplicate check is required at the base case. Duplicate branches were never created because each recursive choice was a distinct value.

---

## 7. LCCM Pseudocode

```text
rec(level):
    if level == N:
        print current
        return

    for each distinct value in increasing order:
        if frequency[value] > 0:
            frequency[value]--
            append value to current

            rec(level + 1)

            remove the last value from current
            frequency[value]++
```

The map provides two useful properties at once:

- one entry for every distinct value, and
- iteration over those values in increasing order.

---

## 8. Dry Run for `[1, 1, 2]`

Initially:

```text
N = 3
current = []
frequency = {1 → 2, 2 → 1}
```

### 8.1 Start at level 0

```text
rec(0)
```

The map visits choices in the order `1`, then `2`.

Choose `1`:

```text
frequency[1]--
current.push_back(1)

current = [1]
frequency = {1 → 1, 2 → 1}
```

Now call `rec(1)`.

### 8.2 Build the first permutation

At `level = 1`, choose `1` again because one copy remains:

```text
current = [1, 1]
frequency = {1 → 0, 2 → 1}
```

Call `rec(2)`.

At `level = 2`:

- `1` fails the check because its frequency is `0`.
- `2` passes the check.

Choose `2`:

```text
current = [1, 1, 2]
frequency = {1 → 0, 2 → 0}
```

Call `rec(3)`. Since `level == N`, print:

```text
1 1 2
```

### 8.3 Backtrack and build the second permutation

Return to `rec(2)` and undo the choice `2`:

```text
current = [1, 1]
frequency = {1 → 0, 2 → 1}
```

There are no more valid choices at level `2`, so return to `rec(1)` and undo its choice `1`:

```text
current = [1]
frequency = {1 → 1, 2 → 1}
```

The next choice at level `1` is `2`:

```text
current = [1, 2]
frequency = {1 → 1, 2 → 0}
```

At level `2`, the only available value is `1`:

```text
current = [1, 2, 1]
frequency = {1 → 0, 2 → 0}
```

The base case prints:

```text
1 2 1
```

### 8.4 Return to the root and build the third permutation

After completely exploring every permutation beginning with `1`, backtracking restores the initial state:

```text
current = []
frequency = {1 → 2, 2 → 1}
```

The next root choice is `2`:

```text
current = [2]
frequency = {1 → 2, 2 → 0}
```

The only available value for the next two levels is `1`:

```text
[2]
[2, 1]
[2, 1, 1]
```

The base case prints:

```text
2 1 1
```

### 8.5 Complete recursive tree

```text
[]
├── choose 1 → [1]
│   ├── choose 1 → [1, 1]
│   │   └── choose 2 → [1, 1, 2]  PRINT
│   └── choose 2 → [1, 2]
│       └── choose 1 → [1, 2, 1]  PRINT
└── choose 2 → [2]
    └── choose 1 → [2, 1]
        └── choose 1 → [2, 1, 1]  PRINT
```

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/a177113d-3aed-49a7-b752-f87145cd8e14.png" alt="Recursion tree containing the three unique permutations of 1, 1, 2 with one branch per distinct value" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The output is:

```text
1 1 2
1 2 1
2 1 1
```

---

## 9. Why Are the Permutations Unique?

At every level, there is at most one branch for each distinct value.

For the initial state of `[1, 1, 2]`, the root has only these branches:

```text
choose value 1
choose value 2
```

It does not have separate branches for the first copy of `1` and the second copy of `1`.

The frequency tells us how many times the branch labelled `1` may be selected across different levels. It does not create multiple identical branches at the same level.

Therefore, every root-to-leaf path corresponds to one distinct sequence of values.

### A useful contrast

```text
Index-based choices:
choose index 0 containing 1
choose index 1 containing 1
→ two branches can produce the same prefix

Frequency-based choices:
choose value 1
→ exactly one branch produces that prefix
```

> **Interview Insight — Identify what makes two choices equivalent:** If two choices produce the same state and the same remaining subproblem, they should usually not exist as separate branches. Equal unused occurrences are equivalent in this problem.

---

## 10. Why Is the Output Lexicographically Increasing?

Lexicographic order compares two sequences at their first different position. The sequence with the smaller value at that position comes first.

Two properties guarantee the required order.

### 10.1 `std::map` keeps keys sorted

For the input:

```text
[3, 1, 2, 1]
```

the frequency map iterates through its keys as:

```text
1, 2, 3
```

regardless of the input order.

### 10.2 Depth-first search completes one prefix first

The recursion prints every permutation beginning with the smaller choice before moving to a larger choice.

For example, every permutation beginning with `1` is printed before any permutation beginning with `2`. Among the permutations beginning with `1`, every permutation beginning with `[1, 1]` is printed before those beginning with `[1, 2]`.

This applies recursively at every position, so the complete output is lexicographically increasing.

No final call to `sort(permutations.begin(), permutations.end())` is required.

> **Interview Insight — Ordering is a property of traversal:** If choices are visited in sorted order and DFS completely explores one choice before the next, the leaves are produced in lexicographic order automatically.

---

## 11. Clean Runnable C++ Code

```cpp
#include <bits/stdc++.h>
using namespace std;

void rec(
    int level,
    int n,
    map<long long, int>& frequency,
    vector<long long>& current
) {
    // Base case: all positions have been decided.
    if (level == n) {
        for (long long value : current) {
            cout << value << ' ';
        }
        cout << '\n';
        return;
    }

    // std::map visits distinct values in increasing order.
    for (auto& entry : frequency) {
        long long value = entry.first;
        int& remaining = entry.second;

        // Check: is one copy of this value still available?
        if (remaining == 0) {
            continue;
        }

        // Move: choose this value for the current level.
        remaining--;
        current.push_back(value);

        // Explore every completion of this prefix.
        rec(level + 1, n, frequency, current);

        // Backtrack: restore the state for the next choice.
        current.pop_back();
        remaining++;
    }
}

void solve() {
    int n;
    cin >> n;

    map<long long, int> frequency;

    for (int i = 0; i < n; i++) {
        long long value;
        cin >> value;
        frequency[value]++;
    }

    vector<long long> current;
    current.reserve(n);

    rec(0, n, frequency, current);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

### Why this implementation is clean

- It contains only the headers and state required by the problem.
- It prints permutations directly instead of storing all of them.
- The frequency map is passed by reference rather than copied at every call.
- The current prefix is passed by reference and restored through backtracking.
- The map structure is never modified during traversal; only its stored counts change, so the iteration remains valid.
- The increasing key order of `std::map` gives lexicographic output naturally.

---

## 12. Correctness

We prove that the algorithm prints every unique permutation exactly once and in increasing lexicographic order.

### 12.1 Every printed sequence is a valid permutation

The algorithm chooses a value only when its remaining frequency is positive. It immediately decreases that frequency before recursing.

Therefore, no value can be used more times than it occurs in the input.

The base case is reached only after exactly `N` values have been selected. Since the total initial frequency is `N`, every input occurrence has then been used exactly once.

Hence, every printed sequence is a valid permutation of the input multiset.

### 12.2 Every unique permutation is printed

Consider any valid unique permutation. At level `0`, its first value has positive frequency, so the algorithm considers that choice. After consuming it, the second value has positive remaining frequency at level `1`, so that choice is also considered.

Repeating this argument for all `N` positions gives a root-to-leaf path for the complete permutation.

Hence, every unique permutation is printed.

### 12.3 No permutation is printed more than once

At a particular level and state, the loop creates only one branch for each distinct value. Two identical copies never create separate choices.

A complete sequence uniquely determines the value chosen at every level. Therefore, two different root-to-leaf paths cannot print the same sequence.

Hence, no permutation is printed more than once.

### 12.4 The printing order is lexicographically increasing

The map visits smaller values before larger values. DFS prints every completion of the smaller prefix before exploring the next larger choice.

Therefore, the first differing value between two consecutively ordered groups is increasing, and the same reasoning applies recursively inside each group.

Hence, all permutations are printed in lexicographically increasing order.

---

## 13. Time Complexity

Let:

- `N` be the length of the array,
- `D` be the number of distinct values,
- `c₁, c₂, ..., cD` be their frequencies, and
- `P` be the number of unique permutations:

```text
                  N!
P = --------------------------------
    c₁! × c₂! × ... × cD!
```

### 13.1 Unavoidable output cost

The algorithm prints `P` permutations, each containing `N` values. Printing alone takes:

```text
Θ(P × N)
```

This is an unavoidable lower bound for any algorithm that explicitly prints every answer.

### 13.2 Frequency-map construction

Building a `std::map` from `N` input values takes:

```text
O(N log D)
```

### 13.3 Choice-scanning overhead

This implementation keeps all `D` keys in the map, including values whose current frequency is zero. Therefore, every non-leaf recursive state scans `D` possible values.

If `S` is the number of valid prefix states in the recursion tree, the traversal overhead is:

```text
O(D × S)
```

Since every generated prefix can be extended to at least one complete permutation:

```text
S ≤ 1 + P × N
```

A safe complete bound is therefore:

```text
O(N log D + D × S + P × N)
```

For the common worst case where all values are distinct:

```text
D = N
P = N!
```

and the running time is dominated by generating and printing factorially many answers. It is commonly stated as:

```text
O(N × N!)
```

> **Interview Insight — Give output-sensitive complexity:** Saying only `O(N!)` ignores that every answer contains `N` values. `Θ(P × N)` describes the unavoidable output work, while `O(D × S)` exposes the extra scan performed by this particular frequency-map implementation.

---

## 14. Space Complexity

Excluding the output stream:

- the frequency map stores `D` entries: `O(D)`,
- `current` stores at most `N` values: `O(N)`, and
- the recursion stack has depth `N`: `O(N)`.

Therefore, the auxiliary space complexity is:

```text
O(N + D) = O(N)
```

because `D ≤ N`.

### What if we store every permutation?

If we use:

```cpp
vector<vector<long long>> answers;
```

and copy `current` at every base case, the stored output requires:

```text
Θ(P × N)
```

additional space.

Printing directly avoids this output-storage cost.

> **Interview Insight — Clarify whether output space is counted:** Interviewers often expect auxiliary space and stored-result space to be reported separately.

---

## 15. Important Nuances

### 15.1 Why not generate everything and use a `set`?

One possible solution is:

1. generate all index-based permutations,
2. insert each permutation into a set, and
3. print the set.

This can generate up to `N!` leaves even when the number of unique permutations `P` is much smaller. It also stores all unique answers.

The frequency-map solution directly generates only the required value sequences.

### 15.2 Why not sort the final answer?

Sorting is unnecessary because:

- `std::map` iterates over values in increasing order, and
- DFS completely explores each smaller prefix before the next larger prefix.

If `unordered_map` were used instead, uniqueness would still be correct, but the output order would not be guaranteed.

### 15.3 Can we erase a key when its frequency becomes zero?

Do not erase and reinsert map entries while traversing the same map with a range-based loop. Structural modifications can invalidate the current traversal logic and make restoration harder.

Keep every distinct key in the map and change only its count.

### 15.4 Why pass the map by reference?

Passing the frequency map by value would copy it at every recursive call. Backtracking is designed to mutate one shared state and restore it, avoiding repeated full copies.

### 15.5 Sorted array + `used[]`: the faster recursive alternative

Another standard solution sorts the array, uses a `used[]` array, and skips an equal value when its previous equal occurrence has not been used in the current prefix:

```cpp
if (i > 0 && values[i] == values[i - 1] && !used[i - 1]) {
    continue;
}
```

The complete decision rule is:

```cpp
for (int i = 0; i < n; i++) {
    if (used[i]) {
        continue;
    }

    if (i > 0 && values[i] == values[i - 1] && !used[i - 1]) {
        continue;
    }

    used[i] = true;
    current.push_back(values[i]);

    rec(level + 1);

    current.pop_back();
    used[i] = false;
}
```

#### Why does the duplicate-skip condition work?

After sorting, equal values are adjacent. Imagine that the two copies in `[1, 1, 2]` are internally labelled:

```text
[1ₐ, 1ᵦ, 2]
```

The condition forces equal occurrences to be selected in their left-to-right order:

```text
1ₐ before 1ᵦ
```

At the root:

- choosing `1ₐ` is allowed,
- choosing `1ᵦ` is skipped because `1ₐ` is equal and has not been used in the current prefix.

After `1ₐ` has been placed, choosing `1ᵦ` at the next level is allowed because `used[i - 1]` is now `true`.

Therefore, the algorithm removes only equivalent sibling branches. It does **not** prevent multiple equal values from appearing in the same permutation.

This creates one canonical order for identical occurrences and ensures that each value sequence is generated exactly once.

> **Interview Insight — Read the condition as a sibling rule:** “Skip this copy if the equal copy immediately before it is still unused.” If the previous equal copy is already part of the prefix, the current copy is allowed at a deeper level.

#### Why is it usually faster in practice?

The sorted-array approach uses contiguous storage:

- `values` is a contiguous vector,
- `used` is a contiguous array or vector, and
- the choice loop scans memory sequentially.

This is cache-friendly and avoids the pointer chasing of a tree-based `std::map`. Sorting costs `O(N log N)` once, after which the recursive search works entirely with arrays.

For strict time limits, low-latency code, or the standard **Permutations II** interview problem, the sorted-array + `used[]` approach is generally the faster recursive implementation.

The frequency-map approach remains valuable because it expresses the mathematical choice directly: choose one distinct value whose remaining count is positive.

### 15.6 Performance nuance: `std::map` as a teaching tool

`std::map` is usually implemented as a Red-Black Tree. Its nodes are separately allocated and connected through pointers. Repeated traversal can therefore cause more cache misses than scanning a vector.

In the runnable frequency-map code, this line binds directly to the stored count:

```cpp
int& remaining = entry.second;
```

Consequently, decrementing and restoring `remaining` do not perform a fresh `O(log D)` lookup. However:

- building the map performs `O(log D)` insertions,
- every recursive state still walks through up to `D` tree nodes, and
- tree traversal has larger constant factors and poorer memory locality than contiguous arrays.

The practical choice is therefore:

| Goal | Preferred implementation |
| --- | --- |
| Learn frequency-based LCCM clearly | Ordered frequency map |
| Fast recursive implementation | Sorted vector + `used[]` |
| Add constraints or pruning based on remaining counts | Frequency-based state may remain more natural |

> **CP Insight — Asymptotic complexity is not the whole runtime:** Two implementations may explore the same recursion tree but have noticeably different execution times because of allocation, pointer chasing, branch prediction, and cache locality.

### 15.7 C++ Pro Tip: `std::next_permutation`

For this exact task—print every unique permutation in lexicographic order—C++ already provides a highly practical iterative solution:

```cpp
sort(values.begin(), values.end());

do {
    for (long long value : values) {
        cout << value << ' ';
    }
    cout << '\n';
} while (next_permutation(values.begin(), values.end()));
```

Starting from the sorted arrangement is essential. `next_permutation` repeatedly transforms the vector into the next lexicographically greater value sequence. When duplicate values are present, it naturally moves between distinct value arrangements without producing duplicate output.

For `[1, 1, 2]`, it visits:

```text
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
```

Its important properties are:

- unique permutations are handled naturally,
- output is lexicographically increasing,
- the permutation is modified in place,
- auxiliary space is `O(1)`, excluding input storage, and
- there is no recursion-stack overhead.

Sorting takes `O(N log N)`. Each call to `next_permutation` takes `O(N)` in the worst case, so enumerating and printing all `P` unique permutations takes:

```text
O(N log N + P × N)
```

For production code and competitive programming, `std::next_permutation` is usually the gold-standard solution to this exact enumeration problem.

The LCCM solution is still essential to learn because it generalizes to problems where:

- only some arrangements are valid,
- partial states can be pruned,
- extra constraints must be checked while constructing the answer, or
- the recursion must count, optimize, or stop early instead of enumerating everything.

> **Interview Insight — Know both levels of abstraction:** Use `next_permutation` when the task is exactly “enumerate all permutations.” Use LCCM when the permutation is only the search space and the real problem adds constraints.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/dee78b8a-5ce1-48c7-82ed-cc5ad63a3a1b.png" alt="Comparison of frequency map, sorted array with used flags, and next_permutation approaches" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 16. Common Mistakes

### Mistake 1: Treating equal indices as different choices

This produces duplicate leaves when equal values occur at different positions.

### Mistake 2: Forgetting to restore the frequency

```cpp
remaining++;
```

is necessary after the recursive call. Without it, later branches incorrectly believe that a copy is unavailable.

### Mistake 3: Forgetting to remove the last chosen value

```cpp
current.pop_back();
```

restores the prefix to its state before the choice.

### Mistake 4: Using `unordered_map` and expecting sorted output

An `unordered_map` does not define an increasing iteration order.

### Mistake 5: Sorting all answers afterward without need

The traversal already produces the required order when choices come from a `std::map`.

### Mistake 6: Copying the complete state in every call

Passing `frequency` and `current` by value adds unnecessary copying. Mutate, recurse, and undo instead.

### Mistake 7: Storing all answers when the task only asks to print

Storing every permutation increases memory consumption to `Θ(P × N)`.

---

## 17. Final LCCM Summary

```text
State
    current prefix + remaining frequencies

Level
    index currently being filled

Choice
    one distinct value from the ordered frequency map

Check
    remaining frequency of the value is positive

Move
    consume one copy
    append the value
    recurse to the next level
    remove the value
    restore one copy

Base case
    level == N, so print the completed permutation
```

The two central ideas are:

1. **Equal occurrences must be treated as one choice with a frequency.**
2. **Trying distinct values in increasing order makes DFS print the unique permutations in lexicographic order.**

</READING_WIDGET>
