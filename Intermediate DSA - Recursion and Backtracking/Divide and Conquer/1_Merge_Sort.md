<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to Divide and Conquer — Merge Sort

## 1. The Three-Step Approach

In earlier lessons, we used recursion to describe a problem in terms of smaller instances. **Divide and Conquer** gives this idea a particular structure:

> **Divide → Conquer → Combine**

1. **Divide:** Break the current problem into smaller subproblems of the same kind.
2. **Conquer:** Solve those subproblems, usually recursively. Handle sufficiently small instances directly.
3. **Combine:** Use their solutions to construct the answer to the current problem.

The recursive calls do not solve unrelated tasks. Each solves a smaller version of the problem we already know how to describe.

For merge sort, the three steps become:

| Step | Merge sort interpretation |
| --- | --- |
| Divide | Split the current array range into two nearly equal halves |
| Conquer | Sort each half recursively |
| Combine | Merge the two sorted halves into one sorted range |

The key observation is:

> If two halves are already sorted, we can combine them in linear time.

We will first understand that merge operation, then place it inside the recursive algorithm.

<img src="images/merge-sort-three-steps.png" alt="Merge sort divides the sample array into two halves, sorts each half recursively, and merges them into 1, 2, 2, 3, 4, 5" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Recursion Versus Divide and Conquer

These are related ideas, not competing alternatives.

**Recursion is a way to express computation:** a function calls itself on a smaller or simpler state.

**Divide and Conquer is an algorithm-design strategy:** split a problem into smaller subproblems, solve them, and combine their answers.

A recursive implementation of merge sort uses both ideas. However, merely calling a function recursively does not make it divide and conquer.

### 2.1 Independent subproblems in merge sort

Suppose we split an inclusive range `a[l..r]` at `mid`:

```text
Left subproblem:  sort a[l..mid]
Right subproblem: sort a[mid+1..r]
```

The two ranges contain different **positions**. Sorting the left range does not require the right range's sorted answer, and vice versa. Once both are sorted, the parent merges them.

The halves may contain equal values. “Non-overlapping” refers to the positions and subproblem states, not to the values being distinct.

### 2.2 Contrast with naive Fibonacci recursion

In the direct recursion:

```text
F(n) = F(n-1) + F(n-2)
```

the computation of `F(n-1)` itself includes `F(n-2)`. The same subproblem is therefore reached through multiple branches.

This is **overlapping subproblem computation**, unlike sorting two disjoint array ranges. It is why naive Fibonacci is not the independent-subproblem model of divide and conquer that we use here.

| Question | General recursion | Divide and conquer, as illustrated by merge sort |
| --- | --- | --- |
| What does it describe? | A self-calling computation | A way to decompose and solve a problem |
| Must it split the input into independent parts? | No | The smaller parts can be solved independently |
| Can different branches repeat the same subproblem? | Yes | Merge sort's sibling ranges do not overlap |
| What happens after child calls? | Depends on the recursive contract | Their answers are combined |
| Is explicit recursive code required? | Yes, for a recursive implementation | Not inherently; the strategy can also be organized iteratively |

The lecture's shorthand “divide and conquer is a subset of recursion” is useful for the **recursive forms studied in this module**. More precisely, strategy and implementation are different concepts: divide-and-conquer algorithms are commonly recursive, but need not use self-calling functions.

> **Interview Insight — Look beyond the function call:** Identify the subproblems, explain whether they overlap, and describe the combine step. “It uses recursion” does not explain why an algorithm is divide and conquer.

---

## 3. Problem Statement: Sort an Array

Given an array of `N` integers, arrange its elements in **nondecreasing order** using merge sort.

Preserve every occurrence of every element. Sorting does not remove duplicates.

### Input and output convention

No external judge bounds or format were supplied. The runnable program in this lesson uses one test case:

```text
Input
N
a[0] a[1] ... a[N-1]

Output
The N values in nondecreasing order
```

We assume `N` is a nonnegative value representable by `int`, the array fits in memory, and the elements fit in `long long`. There is no test-case count before `N`.

For `N = 0`, the output is an empty line.

### Example

```text
Input
6
5 1 4 2 3 2

Output
1 2 2 3 4 5
```

This example includes a duplicate so that we can also examine how ties are handled.

---

## 4. The Merge Operation

Suppose we already have two sorted sequences:

```text
A = [1, 4, 5]
B = [2, 2, 3]
```

We want a sorted output containing all six elements.

Because both sequences are sorted, the smallest remaining element must be at the front of one of them. There is no need to search deeper into either sequence.

### 4.1 Three pointers

As in the lecture's `A`, `B`, and `C` example, use:

- `i`: the next unread element of `A`.
- `j`: the next unread element of `B`.
- `k`: the next position to fill in output `C`.

While both inputs still have elements:

1. Compare `A[i]` and `B[j]`.
2. Copy the smaller one into `C[k]`.
3. Advance the pointer for the input we used.
4. Advance `k`.

On equal values, take from the **left sequence**. We will explain why this preserves stability.

<img src="images/merge-sort-three-pointers.png" alt="The merge pointers compare unread values 4 and 2, copy 2 from B into the six-cell output buffer, leave i at 1, and advance j to 1 and k to 2" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 4.2 Dry run of one merge

| Step | Next in `A` | Next in `B` | Action | Output so far |
| ---: | --- | --- | --- | --- |
| 1 | `1` | `2` | Take `1` from `A` | `[1]` |
| 2 | `4` | `2` | Take `2` from `B` | `[1, 2]` |
| 3 | `4` | `2` | Take the next `2` from `B` | `[1, 2, 2]` |
| 4 | `4` | `3` | Take `3` from `B` | `[1, 2, 2, 3]` |
| 5 | `4` | Exhausted | Copy remaining `4` from `A` | `[1, 2, 2, 3, 4]` |
| 6 | `5` | Exhausted | Copy remaining `5` from `A` | `[1, 2, 2, 3, 4, 5]` |

### 4.3 Why are leftover loops necessary?

The comparison loop stops as soon as **either** input runs out. The other input may still contain elements.

Those remaining elements are already sorted and belong after the output prefix. Copy them in order. Without these loops, the merge silently loses values.

### 4.4 The merge invariant

Before each iteration:

> The output prefix contains exactly the consumed elements, in sorted order. The two input pointers identify the first unread elements of their sorted sequences.

The smaller unread head is the next smallest remaining element. Appending it preserves the invariant. Once both inputs are exhausted, every element has been copied exactly once.

### 4.5 Cost of merging

For lengths `p` and `q`, merging writes exactly `p + q` output elements. Neither input pointer moves backward.

Therefore:

$$
\text{Merge time} = \Theta(p+q).
$$

When both inputs are nonempty, at most `p + q - 1` head-to-head comparisons are needed. Even if fewer comparisons occur, copying all output elements still takes linear time.

---

## 5. Define the Recursive Contract

We will use **inclusive indices** throughout:

```cpp
mergeSort(a, temp, l, r)
```

Its contract is:

> Sort the original elements of `a[l..r]` into nondecreasing order, preserving their multiplicities and leaving array positions outside this range unchanged.

`temp` is a reusable scratch buffer with the same length as `a`. It is not a second answer that must remain sorted between calls.

### Base case

```cpp
if (l >= r) return;
```

- `l == r`: a one-element range is already sorted.
- `l > r`: the range is empty.

The initial call for an empty array is `(l, r) = (0, -1)`, so it returns before any array access.

### Divide

```cpp
int mid = l + (r - l) / 2;
```

The children are:

```text
[l..mid] and [mid+1..r]
```

They cover the parent range without overlap or missing positions. For a nontrivial range, each is strictly smaller than the parent, so recursion makes progress.

### Conquer

```cpp
mergeSort(a, temp, l, mid);
mergeSort(a, temp, mid + 1, r);
```

By the recursive contract, both halves are sorted when these calls return.

### Combine

```cpp
mergeRanges(a, temp, l, mid, r);
```

This call assumes that the two halves are sorted. It merges them into `temp[l..r]`, then copies that result back into `a[l..r]`.

> **Interview Insight — State what is true before combining:** The merge routine does not sort arbitrary inputs by itself. Its linear-time logic relies on both child ranges already being sorted.

---

## 6. Clean Runnable C++ Code

The lecture uses separate arrays `A`, `B`, and `C` to explain merging. In this implementation, the two input sequences are adjacent ranges in `a`, and `temp` acts as the merge output.

We allocate the buffer once and reuse it throughout the recursion.

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Preconditions: a[l..mid] and a[mid+1..r] are sorted.
void mergeRanges(vector<long long>& a, vector<long long>& temp,
                 int l, int mid, int r) {
    int i = l;
    int j = mid + 1;
    int k = l;

    while (i <= mid && j <= r) {
        // Take the left element on ties to preserve stability.
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
        }
    }

    while (i <= mid) {
        temp[k++] = a[i++];
    }

    while (j <= r) {
        temp[k++] = a[j++];
    }

    for (int pos = l; pos <= r; pos++) {
        a[pos] = temp[pos];
    }
}

void mergeSort(vector<long long>& a, vector<long long>& temp,
               int l, int r) {
    if (l >= r) return;

    int mid = l + (r - l) / 2;

    // Divide and conquer: sort the two disjoint ranges.
    mergeSort(a, temp, l, mid);
    mergeSort(a, temp, mid + 1, r);

    // Combine their sorted results.
    mergeRanges(a, temp, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 0) return 0;

    vector<long long> a(n);
    for (long long& value : a) cin >> value;

    vector<long long> temp(n);
    mergeSort(a, temp, 0, n - 1);

    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';
    return 0;
}
```

### Mapping the pointers to the lecture

| Lecture representation | Range-based implementation |
| --- | --- |
| `A[i]`, starting at `i = 0` | `a[i]`, starting at `i = l` |
| `B[j]`, starting at `j = 0` | `a[j]`, starting at `j = mid + 1` |
| `C[k]`, starting at `k = 0` | `temp[k]`, starting at `k = l` |
| End of `A` | `i > mid` |
| End of `B` | `j > r` |

We are not creating slices during the divide step. We pass index boundaries, which takes constant time.

---

## 7. Full Dry Run: Divide Down, Merge Up

Use the sample:

```text
[5, 1, 4, 2, 3, 2]
```

At the root, `l = 0`, `r = 5`, and `mid = 2`.

### 7.1 Divide into smaller ranges

```text
[5, 1, 4, 2, 3, 2]
        /                 \
   [5, 1, 4]           [2, 3, 2]
    /      \            /      \
 [5, 1]    [4]       [2, 3]     [2]
  /  \                /  \
[5]  [1]            [2]  [3]
```

A singleton needs no work. The useful sorting happens as the calls return and merge their results.

The drawing shows the decomposition, not simultaneous execution. Our code fully processes the left child before beginning the right child.

### 7.2 Finish the left half

1. Merge `[5]` and `[1]` to obtain `[1, 5]`.
2. Merge `[1, 5]` and `[4]` to obtain `[1, 4, 5]`.

The root's left range is now sorted:

```text
[1, 4, 5 | 2, 3, 2]
```

### 7.3 Finish the right half

1. Merge `[2]` and `[3]` to obtain `[2, 3]`.
2. Merge `[2, 3]` and `[2]` to obtain `[2, 2, 3]`.

Both root children are now sorted:

```text
[1, 4, 5 | 2, 2, 3]
```

The entire range is **not** sorted yet: `5` still appears before `2`.

### 7.4 Combine at the root

Merge `[1, 4, 5]` and `[2, 2, 3]`, as in the earlier pointer dry run:

```text
[1, 2, 2, 3, 4, 5]
```

Copying this merged result back completes the root's contract.

> **Interview Insight — Sorted halves are not a sorted whole:** Concatenation is not the combine step. The merge must account for elements from one half that belong between elements of the other.

---

## 8. Stability: Why Take the Left Element on a Tie?

A sorting algorithm is **stable** if equal keys retain their original relative order.

Imagine that the equal `2`s in our example carry identity labels:

```text
Original order: 2a appears before 2b
```

At one merge, they may appear in different halves:

```text
Left  = [2a, 3]
Right = [2b]
```

The labels distinguish occurrences; comparisons use only the numeric value.

Using `<=` takes `2a` first:

```text
[2a, 2b, 3]
```

Using `<` with a right-side `else` takes `2b` first:

```text
[2b, 2a, 3]
```

Both results are numerically sorted, but only the first preserves the original order of equal keys.

The reference slide's strict `<` comparison is sufficient for sorting plain numbers. We deliberately use `<=` to make this implementation stable.

Stability follows recursively: each child preserves the order inside its own range, and left-first ties preserve the order of equal elements split across ranges. Every original position in the left half precedes every position in the right half.

> **Interview Insight — Sorting correctly and sorting stably are different claims:** Duplicates do not make a numeric output incorrect. Stability matters when equal keys belong to distinguishable records whose existing order should be preserved.

---

## 9. Why Merge Sort Is Correct

We prove that `mergeSort` satisfies its contract by induction on the range length.

### Base case

An empty or one-element range is already sorted and contains exactly its original elements. The function makes no changes.

### Inductive step

Assume the function correctly sorts smaller ranges.

For a range of length at least two:

1. The split partitions it into two smaller, disjoint ranges covering all original positions.
2. By the induction hypothesis, both child calls return sorted versions of their ranges, with all occurrences preserved.
3. The merge invariant ensures that merging these sorted halves produces a sorted sequence containing every element exactly once.
4. Copy-back writes that result only to the current range.

Thus the parent range is sorted, its multiset of elements is unchanged, and positions outside it are untouched.

Both children are strictly smaller, so repeated division eventually reaches the base case. The algorithm therefore terminates and sorts the original array.

---

## 10. Time Complexity: `T(n) = 2T(n/2) + O(n)`

Let `n` denote the length of the current range.

For a power-of-two size:

$$
T(n) = 2T(n/2) + \Theta(n), \qquad T(1) = \Theta(1).
$$

The terms come directly from the code:

- Two child calls, each on half the range: `2T(n/2)`.
- Merge into `temp`: `Θ(n)`.
- Copy back into `a`: another `Θ(n)`.
- Compute the midpoint and pass boundaries: `O(1)`.

Two linear passes are still linear, not quadratic.

### 10.1 Work at each level

| Depth | Number of subproblems | Size per subproblem | Total merge work at that depth |
| ---: | ---: | ---: | --- |
| 0 | 1 | `n` | `Θ(n)` |
| 1 | 2 | `n/2` | `Θ(n)` |
| 2 | 4 | `n/4` | `Θ(n)` |
| `d` | `2^d` | `n/2^d` | `Θ(n)` while merging is needed |

At any merging level, the ranges together contain `n` elements:

$$
2^d \cdot \frac{n}{2^d} = n.
$$

The range size reaches one when:

$$
\frac{n}{2^d} = 1
\quad\Longrightarrow\quad
d = \log_2 n.
$$

There are `log₂ n` merging levels, each costing `Θ(n)`. The `n` singleton leaves contribute only another `Θ(n)` total.

Therefore:

$$
T(n) = \Theta(n\log n).
$$

<img src="images/merge-sort-level-cost.png" alt="Merge sort splits ranges into halves and quarters, with linear total merge work at each of logarithmically many merging levels, yielding Theta n log n time" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 10.2 Expanding the recurrence

For the simplified recurrence `T(n) = 2T(n/2) + cn`:

$$
\begin{aligned}
T(n)
&= 2\bigl[2T(n/4) + cn/2\bigr] + cn \\
&= 4T(n/4) + 2cn \\
&= 8T(n/8) + 3cn.
\end{aligned}
$$

After `j` expansions:

$$
T(n) = 2^jT(n/2^j) + jcn.
$$

Set `j = log₂ n`:

$$
T(n) = nT(1) + cn\log_2 n = \Theta(n\log n).
$$

### 10.3 What if `n` is odd?

The halves differ in size by one:

$$
T(n) = T(\lceil n/2\rceil) + T(\lfloor n/2\rfloor) + \Theta(n).
$$

The tree remains balanced, with `Θ(log n)` height, and the same `Θ(n log n)` bound holds. No padding to a power of two is needed.

### 10.4 Best, average, and worst cases

For this implementation, all three are `Θ(n log n)` for `n ≥ 2`.

Even an already sorted array is divided recursively, merged into the buffer, and copied back at each level. The number of comparisons may change, but these linear writes remain.

Empty and one-element inputs take constant sorting work.

> **CP Insight — Analyze the implementation you actually wrote:** This code does not test whether a merge can be skipped. Do not claim a linear best case for it merely because the input happens to be sorted.

---

## 11. Space Complexity

The implementation uses:

- One buffer `temp` containing `N` elements: `O(N)`.
- A balanced recursion stack: `O(log N)` for `N ≥ 2`.
- A constant number of indices per active call.

Thus the total auxiliary space is:

$$
O(N) + O(\log N) = O(N).
$$

### Why not `O(N log N)`?

The same buffer is reused. We do not allocate a separate `N`-element array at every level.

The two child calls also execute sequentially, not simultaneously. The recursion stack contains one active root-to-leaf path, not the entire recursion tree.

The buffer can be reused safely because each merge fills every buffer position it will read back. Old contents from earlier merges are irrelevant.

### Is this in-place?

No. It updates the input vector, but it also needs a linear-size buffer. Modifying the original array does not, by itself, mean an algorithm uses constant auxiliary space.

> **Interview Insight — Separate time from peak memory:** Work is accumulated across all recursive calls. Space counts what must coexist at one moment. Summing all allocations or all tree nodes is not automatically a peak-space analysis.

---

## 12. Common Mistakes and CP Insights

### 12.1 Mixing interval conventions

This lesson uses `[l..r]`, including both endpoints. The children are `[l..mid]` and `[mid+1..r]`, and the merge conditions use `<=`.

Do not mix these boundaries with a half-open implementation that treats `r` as excluded.

### 12.2 Failing to shrink a range

For two elements, the midpoint must lead to two singletons. Calling again on the original range causes infinite recursion.

The combination of `l >= r`, `mid = l + (r-l)/2`, and the two child ranges ensures progress.

### 12.3 Forgetting leftover elements

The main comparison loop uses `&&`, because both current elements must exist before comparing them. After it stops, copy the unread remainder of either half.

### 12.4 Overwriting unread input

Writing the merged output directly into the beginning of `a[l..r]` can destroy elements that a pointer has not consumed yet. The separate buffer avoids this problem.

### 12.5 Forgetting copy-back

The parent reads its inputs from `a`, not from the previous child's temporary output. If the child does not copy its sorted result back, the parent's precondition is not established.

### 12.6 Passing the array by value

The sorting functions take vectors by reference. Copying `a` on every call wastes work and prevents the intended updates from reaching the caller.

The split itself should pass boundaries, not copy whole arrays unnecessarily.

### 12.7 Assuming two recursive calls mean exponential time

The size reduction matters. Merge sort has two calls on about `n/2` elements, not two calls on `n-1` elements. Counting children without tracking subproblem size gives the wrong recurrence.

### 12.8 Assuming every divide-and-conquer algorithm costs `O(n log n)`

Its cost depends on the number of children, their sizes, and the work outside recursion. Merge sort obtains this bound because it has two balanced children and a linear combine step.

### 12.9 Allocating scratch storage repeatedly

One reusable buffer makes the memory bound explicit and avoids repeated buffer allocation. Only the current range is copied during a merge; copying the entire original array at every call would do unnecessary work.

### Sanity checks

| Input situation | What to verify |
| --- | --- |
| Empty array | No invalid access; output an empty line |
| One element | Element remains unchanged |
| Two reversed elements | Both are sorted and retained |
| Already sorted array | Same values and order |
| Reverse-sorted array | Fully sorted result |
| All equal values | Every occurrence remains |
| Negative values and duplicates | Numeric order is correct |
| Odd length | Neither half loses a position |
| Equal-key records with identity labels | Left-first ties preserve their relative order |

For testing, compare the result with a trusted sorting routine and verify that no occurrences are lost. To test stability, use distinguishable records compared only by their key; plain equal integers cannot reveal a reordered tie.

---

## 13. Final Divide-and-Conquer Summary

```text
Contract
    Sort a[l..r], preserving its elements and all outside positions.

Base case
    An empty or one-element range is already sorted.

Divide
    Split into [l..mid] and [mid+1..r].

Conquer
    Recursively sort both halves.

Combine
    Merge using two input pointers and one output pointer.
    Copy leftovers, then copy the merged range back.

Stability
    Take from the left half when keys are equal.

Time
    T(n) = 2T(n/2) + Θ(n) → Θ(n log n).

Auxiliary space
    One O(N) buffer plus an O(log N) stack → O(N).
```

The core idea is not just to make recursive calls. It is to arrange the problem so that **smaller answers can be combined efficiently into a larger answer**. Merge sort makes this structure explicit: divide the range, trust the child contracts, and merge their sorted results.

</READING_WIDGET>
