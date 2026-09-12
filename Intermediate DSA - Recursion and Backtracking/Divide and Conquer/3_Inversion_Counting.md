<VIDEO_WIDGET>

<VIDEO_ID>69</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Inversion Counting — Count Pairs While Merging

## 1. What Does an Inversion Mean?

Given an array, find the number of **inversions** in it.

An inversion is a pair of indices `(i, j)` such that:

$$
i < j \quad\text{and}\quad a[i] > a[j]
$$

In words, a larger element appears before a smaller element. The pair is out of order relative to nondecreasing sorting.

Both conditions matter:

- `i < j` describes the positions in the original array.
- `a[i] > a[j]` describes the values at those positions.
- Equal values do **not** form an inversion.

### Example from the lecture

```text
Index:  0  1  2  3  4  5
Array:  3  1  5  2  6  3
```

The inversion pairs are:

| Indices `(i, j)` | Values `(a[i], a[j])` |
| --- | --- |
| `(0, 1)` | `(3, 1)` |
| `(0, 3)` | `(3, 2)` |
| `(2, 3)` | `(5, 2)` |
| `(2, 5)` | `(5, 3)` |
| `(4, 5)` | `(6, 3)` |

Therefore, the answer is **5**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/2b600ff4-9d83-4e68-aece-ecf15410493e.png" alt="AlgoZenith diagram showing the five inversion index pairs in 3, 1, 5, 2, 6, 3 and explaining why equal values are not inversions" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The pair `(0, 5)` is not an inversion because both values are `3`. Also, inversions need not involve adjacent elements: `(2, 5)` is a valid pair.

> **Key Observation:** We count pairs of positions, not distinct pairs of values. In `[2, 2, 1]`, both occurrences of `2` form an inversion with `1`, so the answer is `2`.

---

## 2. The Direct Approach: Check Every Pair

For every index `i`, check all indices `j > i`:

```cpp
long long bruteForce(const vector<long long>& a) {
    long long answer = 0;
    int n = static_cast<int>(a.size());

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (a[i] > a[j]) {
                ++answer;
            }
        }
    }
    return answer;
}
```

There are:

$$
\frac{n(n-1)}{2}
$$

pairs to examine. Each comparison takes constant time, so this approach takes **Θ(n²) time** and **O(1) auxiliary space**.

It is a useful starting point and a good correctness checker for small inputs. To improve it, we need to count multiple inversions together rather than visiting every pair separately.

---

## 3. Divide the Inversions into Three Groups

Recall merge sort: split a range into two halves, sort them recursively, and merge their sorted answers.

For an inclusive range `a[l..r]`, choose:

```text
mid = l + (r - l) / 2

Left half:  a[l..mid]
Right half: a[mid+1..r]
```

Every inversion belongs to exactly one of three groups:

1. **Left inversions:** Both elements belong to the left half.
2. **Right inversions:** Both elements belong to the right half.
3. **Cross inversions:** The first element belongs to the left half and the second belongs to the right half.

Thus:

$$
\boxed{\text{Total} = \text{Left} + \text{Right} + \text{Cross}}
$$

There is no fourth case with the first index in the right half and the second in the left half: that would violate `i < j`.

The recursive calls can count the first two groups. The important question is:

> Once both halves are sorted, can we count all cross inversions during the merge?

### Why sorting the halves is safe

Sorting a half changes the order within it, but its internal inversions have already been counted by its recursive call.

For cross inversions, every element originating in the left half was before every element originating in the right half. Sorting within those halves does not change this membership. We only need to determine which left values are greater than which right values.

Do not sort the entire array before starting the count. That would discard the original ordering without recording its inversions.

---

## 4. The Merge Step: Count a Whole Suffix at Once

Let `A` be the sorted left half and `B` the sorted right half. Use pointers `i` and `j` to their next unmerged elements.

### Case 1: A[i] ≤ B[j]

Take `A[i]` into the merged output.

Since `B` is sorted, all unmerged right elements are at least `B[j]`. Therefore:

$$
A[i] \le B[j] \le B[j+1] \le \cdots
$$

`A[i]` does not form an inversion with any of those remaining right elements. Advance `i` without adding to the count.

### Case 2: A[i] > B[j]

Take `B[j]` into the merged output.

Because `A` is sorted, every remaining element in `A` is at least `A[i]`:

$$
A[i], A[i+1], \ldots, A[|A|-1] > B[j]
$$

All these elements form inversions with this one right element. Add:

$$
\boxed{|A|-i}
$$

Then advance `j`.

For example:

```text
Remaining left:  [3, 5, 8]
Current right:   2

3 > 2, 5 > 2, 8 > 2

Add 3 inversions in one step.
```

This is the central improvement: **one comparison identifies an entire group of inversion pairs**.

### Mapping the lecture's formula to array indices

The lecture uses separate vectors and adds `A.size() - i`. Our implementation keeps both halves in one array and uses inclusive indices:

```text
Remaining left range: a[i..mid]
Number of elements:  mid - i + 1
```

So its counting line is:

```cpp
cross += mid - i + 1;
```

### Important: handle equality correctly

For strict inversions, the merge condition must take the left element when values are equal:

```cpp
if (a[i] <= a[j]) {
    // Take from the left; do not count an inversion.
} else {
    // a[i] > a[j]: count the remaining left elements.
}
```

Using `<` in the first branch and counting unconditionally in `else` would also count equal pairs. The lecture's displayed snippet needs this adjustment for arrays with duplicates, including its example array.

> **Interview Insight — Derive the inequality from the definition:** An inversion uses strict `>`. The equality branch is a correctness decision, not just a sorting preference.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/3b32cf3f-4603-45b6-aa94-b65064fd0cdf.png" alt="AlgoZenith merge diagram showing that right value 2 forms two inversions with remaining left values 3 and 5; count mid minus i plus one and do not count equality" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 5. The Recursive Contract

Define `countAndSort(a, temp, l, r)` to do two things:

1. Return the inversion count of the range as it was when the call began.
2. Leave `a[l..r]` sorted in nondecreasing order.

The sorted range is the useful additional result that allows the parent to count its cross inversions efficiently.

### Base case

If `l >= r`, the range contains at most one element. It is already sorted and contains no inversion pairs, so return `0`.

### Recursive transition

```text
leftCount  = countAndSort(left half)
rightCount = countAndSort(right half)
crossCount = mergeAndCount(the two sorted halves)

return leftCount + rightCount + crossCount
```

This is modified merge sort: the merge still sorts, but also returns a count.

---

## 6. Complete C++ Implementation

No judge-specific constraints or input format were supplied. The program below uses one test case:

```text
Input
n
a[0] a[1] ... a[n-1]

Output
The number of inversions
```

Assume `n` is nonnegative, fits in `int`, and the array fits in memory. Values fit in `long long`. The algorithm sorts the input array as a side effect; copy it first if the original order is needed later.

```cpp
#include <iostream>
#include <vector>
using namespace std;

long long mergeAndCount(vector<long long>& a,
                        vector<long long>& temp,
                        int l, int mid, int r) {
    int i = l;
    int j = mid + 1;
    int k = l;
    long long cross = 0;

    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            cross += mid - i + 1;
            temp[k++] = a[j++];
        }
    }

    while (i <= mid) {
        temp[k++] = a[i++];
    }
    while (j <= r) {
        temp[k++] = a[j++];
    }

    for (int pos = l; pos <= r; ++pos) {
        a[pos] = temp[pos];
    }
    return cross;
}

long long countAndSort(vector<long long>& a,
                      vector<long long>& temp,
                      int l, int r) {
    if (l >= r) {
        return 0;
    }

    int mid = l + (r - l) / 2;
    long long answer = countAndSort(a, temp, l, mid);
    answer += countAndSort(a, temp, mid + 1, r);
    answer += mergeAndCount(a, temp, l, mid, r);
    return answer;
}

long long countInversions(vector<long long>& a) {
    if (a.size() < 2) {
        return 0;
    }
    vector<long long> temp(a.size());
    return countAndSort(a, temp, 0, static_cast<int>(a.size()) - 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 0) {
        return 0;
    }

    vector<long long> a(n);
    for (long long& value : a) {
        cin >> value;
    }

    cout << countInversions(a) << '\n';
    return 0;
}
```

### Why do the leftover loops add nothing?

If the right half is exhausted, every right element has already had its inversions counted when it was taken. Copying the remaining left elements introduces no new pairs to count.

If the left half is exhausted, there are no remaining left elements to pair with the remaining right elements. Just copy them.

### Why use long long for the answer?

A strictly decreasing array has every possible pair inverted:

$$
\text{Maximum inversions} = \frac{n(n-1)}{2}
$$

For `n = 100000`, that is `4,999,950,000`, which exceeds a signed 32-bit integer. The return types and all accumulated counts must therefore be wide enough, even when array values are small.

> **CP Insight — Widen before multiplying:** To compute the maximum count in C++, write `1LL * n * (n - 1) / 2`. Assigning an already-overflowed `int` expression to `long long` does not repair it.

---

## 7. Dry Run on the Lecture's Array

### Sample input

```text
6
3 1 5 2 6 3
```

### Sample output

```text
5
```

### Step 1: Count within the two halves

Split the array into `[3, 1, 5]` and `[2, 6, 3]`.

| Original half | Internal inversions | Count | Sorted result |
| --- | --- | --- | --- |
| `[3, 1, 5]` | `(3, 1)` | `1` | `[1, 3, 5]` |
| `[2, 6, 3]` | `(6, 3)` | `1` | `[2, 3, 6]` |

The recursive calls return `1` each. They also prepare the sorted halves needed for the final merge.

### Step 2: Count cross inversions during the final merge

```text
Left:  [1, 3, 5]
Right: [2, 3, 6]
```

| Comparison | Action | Newly counted pairs | Added |
| --- | --- | --- | --- |
| `1 ≤ 2` | Take left `1` | None | `0` |
| `3 > 2` | Take right `2` | Left `3` and `5` with right `2` | `2` |
| `3 ≤ 3` | Take left `3` | Equal values are not an inversion | `0` |
| `5 > 3` | Take right `3` | Left `5` with right `3` | `1` |
| `5 ≤ 6` | Take left `5` | None | `0` |
| Left exhausted | Copy right `6` | None | `0` |

Cross inversions: `2 + 1 = 3`.

The final merged array is `[1, 2, 3, 3, 5, 6]`, and:

$$
\text{Total} = 1 + 1 + 3 = \boxed{5}
$$

The sorted result is a side effect. The requested output is the count, not the sorted array.

---

## 8. Why Is Every Inversion Counted Exactly Once?

We prove the recursive contract by induction on the range length.

For a range of length at most one, returning `0` is correct and the range is sorted.

For a larger range, assume both recursive calls correctly count their internal inversions and sort their ranges. Every inversion in the parent is either left-only, right-only, or cross-boundary. These categories are disjoint.

During the merge:

- Taking a left value no greater than the current right value cannot miss a pair with any remaining right value.
- Taking a smaller right value counts precisely the remaining left values, all of which are greater than it.
- Each right value is taken once, so none of its counted cross pairs is counted twice.

The merge therefore counts exactly the cross inversions and produces a sorted parent range. Adding the three counts proves the contract.

Another way to see the lack of double counting: any pair of original positions is first separated into different halves at one particular recursive call. If it is an inversion, that call's merge counts it as a cross inversion. Ancestors receive it through their child count instead of counting it again.

---

## 9. Time and Space Complexity

For a range of length `n`, the two recursive calls handle approximately half the elements each. Merging and copying back take `Θ(n)` time:

$$
T(n) = 2T(n/2) + \Theta(n)
$$

More precisely, odd lengths split into `⌈n/2⌉` and `⌊n/2⌋`. There are `O(log n)` levels, and the total merge work at each level is `O(n)`.

Therefore, for this implementation:

- **Time:** `Θ(n log n)` for `n ≥ 2`, including already sorted input.
- **Shared temporary array:** `O(n)` space.
- **Recursion stack:** `O(log n)` space.
- **Total auxiliary space:** `O(n)`.

The count can be quadratic in `n`, but computing it need not take quadratic time. We return the number of pairs; we do not list every inversion.

---

## 10. Why Care About Inversions? Adjacent Swaps

Inversions measure how far an array is from sorted order in terms of **adjacent swaps**.

Consider two adjacent unequal values. Swapping them changes the inversion count by exactly one in magnitude:

- Swapping an inverted adjacent pair removes one inversion.
- Swapping an ordered adjacent pair creates one inversion.

Their relationships with every other element have the same combined contribution before and after the swap. Only their mutual ordering changes.

### Bubble sort and the minimum adjacent-swap count

Bubble sort swaps adjacent pairs only when the left value is greater than the right value. Each such swap reduces the inversion count by exactly `1`.

A sorted array has `0` inversions. If the initial count is `I`, bubble sort performs exactly `I` swaps.

Moreover, an adjacent swap cannot reduce the count by more than one. Any adjacent-swap sorting procedure therefore needs at least `I` swaps, and bubble sort achieves that bound:

$$
\boxed{\text{Minimum adjacent swaps to sort} = I}
$$

This statement remains true with duplicate values: swapping equal values is unnecessary and changes nothing.

Do not confuse the number of swaps with the number of comparisons or loop iterations.

> **Interview Insight — Specify the allowed operation:** The inversion count is not generally the minimum number of arbitrary swaps. For `[3, 2, 1]`, there are `3` inversions, but one swap of the first and last elements sorts the array. It takes `3` adjacent swaps.

---

## 11. Swap Parity: When Does the Lecture's Claim Apply?

Parity means whether a number is even or odd. The lecture connects inversion parity with the parity of the number of swaps used to sort.

For **distinct elements**, every swap of two different positions changes the inversion count by an odd number, so inversion parity flips.

### Why does an arbitrary swap flip parity for distinct values?

Suppose positions `p < q` contain `x < y`, and we swap them.

- The pair `(p, q)` creates one inversion.
- Each value strictly between `x` and `y` at an index between `p` and `q` creates two additional inversions.
- Other values make no net change to the total.

If there are `t` such intermediate values, the change is:

$$
1 + 2t
$$

which is odd. Swapping in the reverse direction negates this change, but it remains odd.

Thus, if a distinct-element array starts with `I` inversions and reaches sorted order after `s` swaps of different positions:

$$
\boxed{s \bmod 2 = I \bmod 2}
$$

Different algorithms may use different numbers of swaps, but those counts have the same parity. Here, a “swap” exchanges two different positions; self-swaps do not count as such a move.

### Important qualification: duplicate values

The screenshot's wording that every swap of unequal elements flips inversion parity is too broad for arrays with duplicates and arbitrary, non-adjacent swaps.

Consider:

```text
Before: [2, 1, 1]   Inversions = 2
Swap the first and last elements.
After:  [1, 1, 2]   Inversions = 0
```

We swapped unequal values, but the inversion count changed by `2`, an even number. Its parity did not flip.

Therefore, keep these conclusions separate:

| Situation | Valid conclusion |
| --- | --- |
| Distinct elements, swaps of different positions | Every swap flips inversion parity |
| Duplicates allowed, adjacent unequal swaps | Every such swap flips parity because the change is exactly `±1` |
| Duplicates allowed, arbitrary swaps | Strict inversion parity need not flip |
| Bubble sort swaps only inverted adjacent pairs | Swap count equals the initial inversion count, even with duplicates |

For the lecture's example, the strict inversion count is `5`, so bubble sort performs `5` swaps. Since that example contains duplicate `3`s, do not extend this to an unrestricted claim about every arbitrary-swap sorting algorithm.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7157e7d9-340b-4ad0-b610-650898b7ed0d.png" alt="AlgoZenith comparison of adjacent swaps, parity-flipping arbitrary swaps with distinct values, and the duplicate-value counterexample 2, 1, 1 to 1, 1, 2 whose inversion count changes from 2 to 0" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> **CP Insight — Check the assumptions before using parity:** If a problem involves a permutation of distinct elements, inversion parity can constrain the parity of a swap sequence. If duplicates or different move rules are allowed, establish the property for those rules before applying it.

---

## 12. Common Mistakes and Useful Tests

- **Counting equality:** Take from the left on `<=`; only strict `>` contributes inversions.
- **Adding just one:** When the right value is smaller, count all remaining left elements, not only the current one.
- **Missing the inclusive endpoint:** With indices `i..mid`, add `mid - i + 1`.
- **Returning only cross inversions:** Include both recursive counts as well.
- **Not sorting or copying back:** The parent relies on both child ranges being sorted.
- **Overflowing the count:** Use `long long` throughout the count calculation.
- **Assuming the input is preserved:** This implementation modifies the array.
- **Overgeneralizing swap parity:** Distinctness and adjacency matter.

| Array | Expected count | What it checks |
| --- | --- | --- |
| `[]` | `0` | Empty input |
| `[7]` | `0` | Base case |
| `[1, 2, 3]` | `0` | Sorted input |
| `[3, 2, 1]` | `3` | Every pair inverted |
| `[2, 2, 2]` | `0` | Equal values |
| `[2, 2, 1]` | `2` | Repeated values count by position |
| `[-1, -3, -2]` | `2` | Negative values |
| `[3, 1, 5, 2, 6, 3]` | `5` | Lecture example |

For testing, compare the optimized answer with the quadratic implementation on many small arrays, especially arrays with repeated values. Also verify that the optimized function leaves the array sorted.

---

## 13. Quick Recap

An inversion is a pair with **`i < j` and `a[i] > a[j]`**.

Modified merge sort counts inversions in three disjoint groups:

$$
\text{Left inversions} + \text{Right inversions} + \text{Cross inversions}
$$

During the merge, a smaller right element forms an inversion with every remaining left element. This lets us count a whole suffix at once and achieve **O(n log n) time** with **O(n) auxiliary space**.

The inversion count also gives the minimum number of adjacent swaps needed to sort. For distinct elements, its parity matches the parity of any sorting sequence made of swaps of different positions.

> **The reusable idea:** Let recursion return a useful structure as well as an answer. Sorted halves make it possible to count many cross-boundary pairs with one comparison.

</READING_WIDGET>
