<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bitmasking

Suppose we have `N` items and want to try every possible selection. For each item, there are two choices: include it or leave it out. A binary digit records exactly that decision: `1` means included, and `0` means excluded.

**Bitmasking represents a subset using the bits of an integer.** Once a subset is stored as a number, we can add an item, remove an item, check membership, and combine subsets using bitwise operations.

We will first connect bit positions to set elements, then enumerate subsets, count subsets satisfying a sum condition, and finally generate the subsets of a chosen subset using **submasks**.

All code uses **C++17**. Bit positions are **zero-based from the right**. For items numbered from `1` to `N`, bit `i` represents item `i + 1`. For an array, bit `i` represents `arr[i]`.

## 1. Understanding a Bitmask

Consider the set:

$$
S = \{1, 2, 3, 4, 5\}.
$$

We need five bits to record whether each of its five elements is selected.

```text
Bit position:  4  3  2  1  0
Item:          5  4  3  2  1
Mask:          0  1  0  1  0
Selected:         yes   yes
```

The mask `01010` represents `{2, 4}`. Its decimal value is `10`, so the integer `10` can store this subset.

The leading zero is shown to make the five-item universe visible. The integer itself does not remember how many leading zeros we intended; we keep `N` separately.

### Mask Width Is Different from Subset Size

A mask displayed using `N` bits describes a selection from **`N` available items**. The size of the selected subset is the **number of set bits**, not the number of displayed bits.

For example, `10101` uses five positions but selects only three items: `{1, 3, 5}`.

### Example: `1010110 = 86`

For a universe containing items `1` through `7`:

```text
Bit position:  6  5  4  3  2  1  0
Item:          7  6  5  4  3  2  1
Mask:          1  0  1  0  1  1  0
Selected:      7     5     3  2
```

The set bits are at positions `1`, `2`, `4`, and `6`. Therefore:

$$
86 = 2^1 + 2^2 + 2^4 + 2^6,
$$

and the represented subset is **`{2, 3, 5, 7}`**, with size **4**.

Read numeric bit positions from the right. If we label items from left to right in a drawing, we must explicitly reverse their mapping in code. Using one consistent convention avoids that confusion.

## 2. Why Are There Exactly `2^N` Masks?

Each of the `N` items has two independent possibilities: selected or not selected. By the multiplication principle, the number of subsets is:

$$
\underbrace{2 \times 2 \times \cdots \times 2}_{N\text{ times}} = 2^N.
$$

Every subset produces one unique bit pattern, and every `N`-bit pattern produces one unique subset. Thus, iterating through the integers from `0` to `2^N - 1` visits every subset exactly once.

For `S = {1, 2, 3}`:

| Decimal mask | Binary mask | Subset |
| --- | --- | --- |
| `0` | `000` | `{ }` |
| `1` | `001` | `{1}` |
| `2` | `010` | `{2}` |
| `3` | `011` | `{1, 2}` |
| `4` | `100` | `{3}` |
| `5` | `101` | `{1, 3}` |
| `6` | `110` | `{2, 3}` |
| `7` | `111` | `{1, 2, 3}` |

Two masks are especially useful:

- **Empty subset:** `0`, because no item is selected.
- **Full subset:** `(1ULL << N) - 1`, because all of the lowest `N` bits are set.

`1ULL` is an unsigned `long long` literal. The shift `1ULL << N` computes `2^N` when `N` is a valid shift count. In the programs below, `N <= 20`, so the shifts fit comfortably within this type.

## 3. Basic Operations on a Subset

Let `mask` represent a subset, and let `i` be a valid zero-based bit position. Build a mask containing only that position:

```cpp
unsigned long long bit = 1ULL << i;
```

The familiar bit operations now become set operations on a single item:

| Operation | C++ expression | Meaning |
| --- | --- | --- |
| Set bit `i` | `mask \|= bit` | Insert item `i + 1` |
| Clear bit `i` | `mask &= ~bit` | Remove item `i + 1` |
| Check bit `i` | `(mask & bit) != 0` | Test whether item `i + 1` is present |
| Toggle bit `i` | `mask ^= bit` | Remove the item if present; insert it otherwise |

### Dry Run on `01010`

Each operation below starts independently from `mask = 01010`, representing `{2, 4}`.

| Operation | Calculation | Result |
| --- | --- | --- |
| Insert item `1` | `01010 OR 00001` | `01011` → `{1, 2, 4}` |
| Remove item `2` | `01010 AND 11101` | `01000` → `{4}` |
| Check item `4` | `01010 AND 01000` | `01000`, nonzero → present |
| Toggle item `3` | `01010 XOR 00100` | `01110` → `{2, 3, 4}` |

The complement in the second row is displayed using five bits. In C++, the higher bits of `~(1ULL << 1)` are also ones, so they preserve the higher bits of `mask`.

### Two Common Errors

**Use `~`, not `!`, to clear a bit.** Bitwise NOT flips every bit. Logical NOT produces only `true` or `false`; `!(1ULL << i)` is false for a valid shift, so ANDing with it would clear the entire mask.

**A membership test returns a bit value, not necessarily `1`.** Checking bit `3` can produce `8`. Write `(mask & (1ULL << i)) != 0`, and keep the parentheses around the AND expression.

## 4. Operations Between Two Subsets

Suppose `a` and `b` are masks over the same universe of `N` items. Each bit position can be processed independently.

| Set operation | Mask expression |
| --- | --- |
| Union: items in either subset | `a \| b` |
| Intersection: items in both subsets | `a & b` |
| Symmetric difference: items in exactly one subset | `a ^ b` |
| Difference: items in `a` but not in `b` | `a & ~b` |
| Check whether `a` is a subset of `b` | `(a & b) == a` |
| Check whether the subsets are disjoint | `(a & b) == 0` |
| Complement within the universe | `fullMask & ~a` |

Here, `fullMask = (1ULL << N) - 1`, with `N` smaller than the type's bit width. All input masks must use only the lowest `N` bits.

For example:

```text
a = 01010  -> {2, 4}
b = 00110  -> {2, 3}

a | b = 01110  -> {2, 3, 4}
a & b = 00010  -> {2}
a ^ b = 01100  -> {3, 4}
a & ~b = 01000 -> {4}
```

Using `~a` alone also sets positions outside our universe. ANDing with `fullMask` keeps only valid items.

These operations take **`O(1)` time when a mask fits in one machine word**, as it does in our examples. A representation spanning multiple words requires processing those words.

## 5. Shared C++ Helpers

Use the following headers, type alias, and printing function with the implementations in this lesson:

```cpp
#include <iostream>
#include <vector>
using namespace std;

using Mask = unsigned long long;

// Bit i represents arr[i]. Print the selected values in index order.
void printSubset(const vector<long long>& arr, Mask mask) {
    cout << "{ ";
    for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
        if ((mask & (1ULL << i)) != 0) {
            cout << arr[i] << ' ';
        }
    }
    cout << "}";
}
```

The functions below assume **`0 <= N <= 20`**, where `N` is the number of items. The printing problem itself specifies `1 <= N <= 20`; allowing `N = 0` also lets us handle an empty input naturally. Every mask passed to `printSubset` must refer to positions in its array.

For the sum problem, we additionally assume that all possible subset sums fit in `long long`.

## 6. Problem: Print All Subsets of `{1, 2, ..., N}`

Given `N`, where `1 <= N <= 20`, print every subset of:

$$
S = \{1, 2, \ldots, N\}.
$$

### Algorithm

1. Store the items `1` through `N` in an array.
2. Iterate `mask` from `0` to `(1ULL << N) - 1`.
3. For each bit position `i`, include item `i + 1` if that bit is set.
4. Finish the current subset before moving to the next mask.

### C++ Implementation

```cpp
void printAllSubsets(int n) {
    vector<long long> items(n);
    for (int i = 0; i < n; ++i) {
        items[i] = i + 1;
    }

    Mask limit = 1ULL << n;
    for (Mask mask = 0; mask < limit; ++mask) {
        printSubset(items, mask);
        cout << '\n';
    }
}
```

For `N = 3`, the output is:

```text
{ }
{ 1 }
{ 2 }
{ 1 2 }
{ 3 }
{ 1 3 }
{ 2 3 }
{ 1 2 3 }
```

Mask `0` already prints the empty subset. There is no need to print it separately, and the number `0` should not be printed as though it were an element of `S`.

The loop uses `mask < limit`, not `mask <= limit`. The value `2^N` has a bit set outside the `N` available positions.

### Why Does It Work?

Each subset has exactly one membership pattern across the `N` items. The outer loop visits every such pattern once, and `printSubset` prints exactly the positions marked with `1`. Therefore, every subset appears exactly once.

### Complexity

- **Time:** `O(N · 2^N)`. There are `2^N` masks, and each is scanned across `N` positions.
- **Auxiliary space:** `O(N)` for the `items` vector in this implementation. The mask traversal itself needs `O(1)` additional space, and subsets are printed without being stored.

Across all subsets, each item appears in exactly half of them. For `N >= 1`, the total number of printed elements is `N · 2^(N - 1)`. Printing every subset therefore already requires substantial work, even if we optimize how set bits are visited.

## 7. Problem: Count Subsets with Sum at Least a Given Value

Given an array `arr` of `N` items and a threshold `value`, count the subsets whose element sum is **greater than or equal to** `value`.

Each array position is a separate item. The empty subset is included among the candidates and has sum `0`.

### Example

```text
arr = [2, 3, 5]
value = 5
```

| Mask | Selected values | Sum | Sum at least `5`? |
| --- | --- | --- | --- |
| `000` | `{ }` | `0` | No |
| `001` | `{2}` | `2` | No |
| `010` | `{3}` | `3` | No |
| `011` | `{2, 3}` | `5` | Yes |
| `100` | `{5}` | `5` | Yes |
| `101` | `{2, 5}` | `7` | Yes |
| `110` | `{3, 5}` | `8` | Yes |
| `111` | `{2, 3, 5}` | `10` | Yes |

The answer is **`5`**.

### Algorithm

For each mask, start a fresh sum at zero. Scan the array positions and add `arr[i]` only when bit `i` is set. After computing the complete sum, increment the answer if it reaches the threshold.

### C++ Implementation

```cpp
long long countSubsetsAtLeast(const vector<long long>& arr,
                             long long value) {
    int n = static_cast<int>(arr.size());
    Mask limit = 1ULL << n;
    long long count = 0;

    for (Mask mask = 0; mask < limit; ++mask) {
        long long sum = 0;

        for (int i = 0; i < n; ++i) {
            if ((mask & (1ULL << i)) != 0) {
                sum += arr[i];
            }
        }

        if (sum >= value) {
            ++count;
        }
    }

    return count;
}
```

### Why Does It Work?

The mask loop visits every selection of array positions once. For a given mask, the inner loop adds exactly its selected elements, so the resulting sum is the subset's sum. We increment the count exactly when that sum satisfies the condition.

Negative values do not invalidate this algorithm because it always computes the entire subset sum. Do not stop adding values as soon as a partial sum reaches the threshold: a later selected negative value may reduce it again.

### Complexity

- **Time:** `O(N · 2^N)`, not `O(2^N)`, because each mask performs `N` membership checks.
- **Auxiliary space:** `O(1)`, excluding the input array. We keep only a few counters, the mask, and the current sum.

**CP insight:** If we store previously computed subset sums, we can reuse the sum for `mask & (mask - 1)` and add the value corresponding to the removed bit. With constant-time identification of that bit's position, this computes all subset sums in `O(2^N)` time using `O(2^N)` extra space. The direct version above is often the clearest starting point.

### Repeated Values Still Represent Different Items

For `arr = [2, 2]`, masks `01` and `10` select different positions even though both print `{2}`. Bitmask enumeration generates **subsets of positions**. If a problem asks for unique subsets by value, duplicate handling requires additional logic.

## 8. Understanding Submasks

A **submask** of `mask` uses only positions that are already set in `mask`. In set language, it represents a subset of the subset represented by `mask`.

For example:

```text
mask = 10110 -> selected bit positions {1, 2, 4}
```

Its submasks are:

```text
10110, 10100, 10010, 10000, 00110, 00100, 00010, 00000
```

If `mask` contains `k` set bits, it has **`2^k` submasks**, including zero. Each selected position can either remain selected or be removed.

A candidate `sub` is a submask of `mask` exactly when:

```cpp
(sub & mask) == sub
```

We could test every possible candidate, but there is a way to jump directly between valid submasks.

## 9. Generate Submasks with `(sub - 1) & mask`

Start from `sub = mask`. After processing a nonzero submask, update it using:

```cpp
sub = (sub - 1) & mask;
```

### Why Does This Update Work?

For a positive `sub`, subtracting one:

1. Clears its rightmost set bit.
2. Sets all lower positions to `1`.
3. Leaves all higher positions unchanged.

ANDing with `mask` then removes positions that were not available in the original subset.

Equivalently, treat the set positions of `mask` as the only usable digits of a binary counter. This update performs one decrement on those digits, skipping all forbidden positions. It produces the next smaller submask without duplicates or omissions.

### Dry Run for `mask = 10110`

| Current `sub` | `sub - 1` | `(sub - 1) & mask` |
| --- | --- | --- |
| `10110` | `10101` | `10100` |
| `10100` | `10011` | `10010` |
| `10010` | `10001` | `10000` |
| `10000` | `01111` | `00110` |
| `00110` | `00101` | `00100` |
| `00100` | `00011` | `00010` |
| `00010` | `00001` | `00000` |

Notice the transition from `10000` to `00110`: lower positions can become selected again. The operation does more than simply remove one selected item.

### Nonempty Submasks Only

```cpp
for (Mask sub = mask; sub != 0; sub = (sub - 1) & mask) {
    // Process sub.
}
```

This visits `2^k - 1` submasks and excludes the empty subset. If `mask` is zero, the loop runs zero times.

### Include the Empty Submask

```cpp
Mask sub = mask;
while (true) {
    // Process sub, including zero.
    if (sub == 0) {
        break;
    }
    sub = (sub - 1) & mask;
}
```

The check must come **after processing zero but before updating it**. With our unsigned type, subtracting one from zero wraps to an all-ones value. ANDing that value with `mask` returns `mask`, which would restart the enumeration.

For `mask = 0`, this version processes the empty subset once and stops.

## 10. Problem: Print All Subsets of Every Subset

Given an array of `N` items, enumerate every outer subset. For each outer subset, print all of its subsets, including the empty subset.

For `arr = [1, 2]`, the required groups are:

```text
Subset 0: { }
Subset 1: { 1 } { }
Subset 2: { 2 } { }
Subset 3: { 1 2 } { 2 } { 1 } { }
```

`Subset 3` refers to outer mask `11`, representing `{1, 2}`. Its submasks are visited in descending numeric order: `11`, `10`, `01`, `00`.

### C++ Implementation

```cpp
void printSubsetsOfEverySubset(const vector<long long>& arr) {
    int n = static_cast<int>(arr.size());
    Mask limit = 1ULL << n;

    for (Mask mask = 0; mask < limit; ++mask) {
        cout << "Subset " << mask << ": ";

        Mask sub = mask;
        while (true) {
            printSubset(arr, sub);

            if (sub == 0) {
                break;
            }

            cout << ' ';
            sub = (sub - 1) & mask;
        }

        cout << '\n';
    }
}
```

The outer loop visits every subset once. For each one, the inner loop visits all and only its submasks, including zero, so every required group is complete.

### Why Are There `3^N` Mask–Submask Pairs?

For one fixed mask with `k` set bits, the submask loop runs `2^k` times. Across **all** outer masks, the total is:

$$
\sum_{k=0}^{N} \binom{N}{k} 2^k = (1 + 2)^N = 3^N.
$$

There is also a direct counting argument. For each item in a pair `(mask, sub)`, there are three valid states:

| State | In `mask`? | In `sub`? |
| --- | --- | --- |
| Not selected by the outer subset | No | No |
| Selected only by the outer subset | Yes | No |
| Selected by both | Yes | Yes |

An item cannot be in `sub` without being in `mask`. With three independent choices for each of `N` items, there are exactly `3^N` valid pairs.

**`O(3^N)` is the total across all masks**, not the cost of the inner loop for one mask, and it should not be multiplied by another `2^N` factor.

### Complexity of the Printing Code

- **Time:** `O(N · 3^N)`, because `printSubset` scans `N` positions for each pair.
- **Auxiliary space:** `O(1)`, excluding the input array and streamed output.

If processing a submask takes constant time, the traversal instead takes `O(3^N)`. Excluding zero from each inner loop produces `3^N - 2^N` pairs, which has the same asymptotic bound.

## 11. Running the Examples Together

Combine the shared headers and helper from Section 5, the three problem functions, and this `main` to form a complete C++17 program:

```cpp
int main() {
    cout << "All subsets of {1, 2}:\n";
    printAllSubsets(2);

    vector<long long> values = {2, 3, 5};
    cout << "Subsets with sum at least 5: "
         << countSubsetsAtLeast(values, 5) << '\n';

    cout << "Subsets of every subset of {1, 2}:\n";
    vector<long long> items = {1, 2};
    printSubsetsOfEverySubset(items);

    return 0;
}
```

Output:

```text
All subsets of {1, 2}:
{ }
{ 1 }
{ 2 }
{ 1 2 }
Subsets with sum at least 5: 5
Subsets of every subset of {1, 2}:
Subset 0: { }
Subset 1: { 1 } { }
Subset 2: { 2 } { }
Subset 3: { 1 2 } { 2 } { 1 } { }
```

## 12. Interview and Competitive Programming Insights

### Let the Constraints Suggest Subset Enumeration

An input size near `20` often suggests trying all subsets:

```text
2^20      = 1,048,576 masks
20 * 2^20 = 20,971,520 bit checks
3^20      = 3,486,784,401 mask-submask pairs
```

These are very different workloads. A direct `O(N · 2^N)` computation may be reasonable, depending on the time limit and work per check. Enumerating every submask of every mask at `N = 20` is usually too expensive, and printing the results adds substantial output cost.

Do not transfer the feasibility of the first printing problem to the second one just because both use bitmasks.

### Compact Representation Does Not Remove Exponential Work

Bitmasking makes a subset cheap to store and manipulate, but there are still `2^N` different subsets. Using a wider integer lets us represent larger sets; it does not make exhaustive enumeration practical for them.

If the input is too large, the problem's structure must provide another approach. For example, some subset-sum problems can use **meet in the middle**: split the array, generate each half's subset sums, and combine them. That technique belongs to a later lesson.

### Recognize a Future DP State

A mask can describe which items have already been used. Pairing it with another value, such as `dp[mask][last]`, can represent both the visited set and the last chosen item. This is the basis of many assignment and route-planning dynamic programs.

Similarly, submask iteration is useful when a transition considers choosing a group from a set of available items. First decide what each bit means; then decide how the state changes.

### Clarify What Counts as a Subset

Before coding, establish whether the problem includes the empty subset, treats equal-valued items as distinct positions, or requires only subsets of a particular size. These choices change which masks should contribute to the answer.

For a required size `K`, only masks containing exactly `K` set bits qualify. The set-bit counting techniques from the previous lesson can check this condition.

## 13. Common Questions and Pitfalls

### How Do I Toggle a Range of Bits?

Build a mask with ones in the desired interval, then XOR it with the number. To toggle zero-based positions `2` through `5`, inclusive:

```cpp
num ^= (0b1111ULL << 2);
```

This toggles four positions. Under our item mapping, those are items `3` through `6`.

### Can I Set a Bit Only When Another Bit Is Set?

Yes. For example, to insert item `5` only when item `2` is present:

```cpp
if ((mask & (1ULL << 1)) != 0) {
    mask |= (1ULL << 4);
}
```

If item `2` is absent, this code leaves item `5` unchanged; it does not remove it.

### Does `x & -x` Give the Position of the Rightmost Set Bit?

It gives a **single-bit mask**, not an index. For unsigned `Mask x`, `x & (0ULL - x)` isolates the lowest set bit. For example, `101100` produces `000100`, whose numeric value is `4`; the bit position is `2`.

For `x = 0`, the result is zero and there is no set-bit position. Finding an index requires an additional step, such as counting trailing zeros with a suitable operation that handles its input correctly.

### Can Masks Help with Range Queries?

A mask can select a range of bit positions within one integer. That is different from answering queries over an array interval. For example, array range queries asking which categories appear may use category masks combined with bitwise OR in a segment tree, provided the category universe is small enough.

The mask represents the categories; the data structure organizes the array ranges.

### What Should I Watch for in C++?

- **Use a sufficiently wide unsigned type.** `1ULL << i` shifts an unsigned `long long`; storing `1 << i` in a wider variable afterward does not widen the original shift.
- **Keep shift counts valid.** A shift count must be nonnegative and smaller than the type's width. Even an unsigned shift by the full width is invalid. Our enumeration code assumes `N <= 20`.
- **Do not use `^` for exponentiation in code.** C++ interprets `2 ^ N` as XOR. For the bounded inputs here, `1ULL << N` gives `2^N` without floating-point arithmetic.
- **Distinguish position from value.** For `arr = [10, 20, 30]`, bit `1` selects `arr[1]`, which is `20`; it does not mean the value `1` is selected.
- **Reset per-subset state.** Initialize `sum` inside the outer mask loop so different subsets do not share an accumulated total.
- **Check sum capacity separately from mask capacity.** A small number of items can still have large values. The sum code assumes every subset sum fits in `long long`.
- **Handle the zero submask deliberately.** A loop conditioned on `sub != 0` excludes it; a loop including it must stop before applying the update to zero.

Ordinary integer bitwise operations use numeric bit positions and are independent of byte order in memory. Endianness becomes relevant when interpreting raw bytes or serializing a mask, not when checking `mask & (1ULL << i)`.

## 14. Edge Cases to Check

| Case | Expected behavior |
| --- | --- |
| `N = 1` | Two subsets: empty and the single item |
| Empty input array | One subset, the empty subset |
| Empty input in the sum problem | Answer `1` if `value <= 0`; otherwise `0` |
| Threshold `0` and all values nonnegative | All `2^N` subsets qualify, including empty |
| Negative array values | Compute the full sum before checking the threshold |
| Repeated values | Distinct position selections remain distinct masks |
| Outer mask `0` | Exactly one submask when empty is included: `0` |
| Outer mask with `k` set bits | Exactly `2^k` submasks including empty |

## Quick Recap

- A bitmask stores membership: bit `i` represents item `i + 1` or array position `i`.
- `N` available items produce `2^N` subsets; the selected subset's size is its number of set bits.
- OR inserts, AND with a complemented bit removes, AND checks, and XOR toggles.
- Scanning all `N` positions for every subset takes `O(N · 2^N)` time.
- `(sub - 1) & mask` generates the next smaller submask when `sub` is nonzero.
- All mask–submask pairs total `3^N`; scanning `N` positions per pair takes `O(N · 3^N)` time.
- Include the empty subset exactly when the problem requires it, and stop submask enumeration safely at zero.

</READING_WIDGET>
