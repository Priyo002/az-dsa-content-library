<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Greedy and the Exchange Argument

> *A greedy solution makes a choice now and commits to it. The important question is: why can this choice never prevent us from reaching an optimal answer? In this session, we will answer that question by comparing two choices, swapping them, and measuring exactly what changes.*

## 1. What Makes an Algorithm Greedy?

A **greedy algorithm** constructs a solution by repeatedly making a locally preferred choice, without exploring every possible continuation.

For example, we might try to:

- Pair the smallest available value with the smallest available value.
- Solve the problem with the highest score first.
- Choose the task that takes the least time.

These are candidate rules. Calling a rule greedy does not make it correct.

Suppose we want to make an amount of `6` using the fewest coins, with unlimited coins of denominations `[1, 3, 4]`. Taking the largest possible coin first gives `4 + 1 + 1`, using three coins. But `3 + 3` uses only two.

The local choice looked attractive, yet it prevented the best answer.

**Our goal is to derive a rule and prove that following it preserves an optimal solution.** Sorting and heaps may implement that rule efficiently, but the data structure is not the proof.

## 2. The Exchange Argument

An exchange argument compares a solution with another solution obtained by changing a small part of it.

For ordering problems, that change is often a swap of two elements.

### A Reusable Proof Structure

1. State the proposed greedy ordering.
2. Start with an optimal arrangement that may differ from that ordering.
3. Identify a pair that violates the proposed order.
4. Swap the pair and show that the solution stays valid.
5. Prove that the objective does not become worse.
6. Repeat until the arrangement follows the greedy rule.

Because each exchange preserves or improves the objective, there is an optimal solution consistent with our rule.

The last step matters. Showing that one swap is beneficial is not enough unless we can explain how a finite sequence of such swaps reaches the desired arrangement. For sorting-based proofs, each adjacent inversion swap reduces the number of inversions, so the process must terminate.

> **Interview Insight:** “Sorting seems to work” is a guess. “Every adjacent inversion can be removed without reducing the answer” is the beginning of a correctness proof.

---

## 3. Problem 1: Maximum and Minimum Dot Product

We are given two arrays of equal length:

$$
A=[a_1,a_2,\ldots,a_n],\qquad B=[b_1,b_2,\ldots,b_n].
$$

Their dot product is:

$$
A\cdot B=\sum_{i=1}^{n}a_i b_i.
$$

We may rearrange the elements before pairing them. Find:

1. The maximum possible dot product.
2. The minimum possible dot product.

Each element must be used exactly once. Elements may be negative, zero, repeated, or positive.

For this lesson, use:

- $1\le n\le 10^5$.
- $-10^9\le a_i,b_i\le 10^9$.

Allowing either array to be rearranged is sufficient: what matters is which values are paired, not the order in which we write the pairs.

### Running Example

Let both arrays contain `[1, 2, 3]`.

| Pairing | Dot product |
| --- | --- |
| `[1, 2, 3]` with `[1, 2, 3]` | $1+4+9=14$ |
| `[1, 2, 3]` with `[3, 2, 1]` | $3+4+3=10$ |

This suggests:

- **Maximum:** sort both arrays in the same direction.
- **Minimum:** sort the arrays in opposite directions.

Let us prove both claims, including for negative numbers.

## 4. Deriving the Rule by Comparing Two Pairings

Consider values with:

$$
a_i\le a_j,\qquad b_i\le b_j.
$$

There are two ways to match these two pairs.

**Same-order pairing:**

$$
P=a_i b_i+a_j b_j.
$$

**Crossed pairing:**

$$
Q=a_i b_j+a_j b_i.
$$

Subtract:

$$
\begin{aligned}
P-Q
&=a_i b_i+a_j b_j-a_i b_j-a_j b_i\\
&=a_j(b_j-b_i)-a_i(b_j-b_i)\\
&=(a_j-a_i)(b_j-b_i).
\end{aligned}
$$

Both differences are nonnegative, so:

$$
\boxed{a_i b_i+a_j b_j\ge a_i b_j+a_j b_i.}
$$

Pairing smaller with smaller and larger with larger is at least as good for maximization. Crossing those pairings is at least as good for minimization.

Notice that we used the signs of the **differences**, not the signs of the original values. The proof remains valid when the arrays contain negative numbers.

### From One Pair to the Entire Array

Sort `A` in ascending order.

For maximization, suppose the paired `B` sequence has an adjacent inversion: `b[i] > b[i + 1]`. Swapping these two `B` values changes the sum by:

$$
(a_{i+1}-a_i)(b_i-b_{i+1})\ge 0.
$$

Every other product stays unchanged. Removing this inversion cannot decrease the sum. Repeating this operation eventually sorts `B` in ascending order.

Therefore, **ascending with ascending gives a maximum dot product**.

For minimization, if `b[i] < b[i + 1]`, swapping them changes the sum by:

$$
(a_{i+1}-a_i)(b_i-b_{i+1})\le 0.
$$

Repeatedly removing these violations makes `B` descending without increasing the sum.

Therefore, **ascending with descending gives a minimum dot product**.

This result is known as the **rearrangement inequality**. The exchange argument explains why it holds.

### What About Equal Elements?

If either difference is zero, the two pairings have equal value. The optimal arrangement does not need to be unique.

For example, when all values in `A` are equal, every ordering of `B` gives the same dot product.

## 5. A Dry Run with Negative Values

Consider:

```text
A = [-2, 1, 3]
B = [4, -1, 2]
```

Sort both arrays:

```text
A = [-2, 1, 3]
B = [-1, 2, 4]
```

Maximum:

$$
(-2)(-1)+(1)(2)+(3)(4)=2+2+12=16.
$$

For the minimum, reverse the pairing order of `B`:

$$
(-2)(4)+(1)(2)+(3)(-1)=-8+2-3=-9.
$$

We do not need separate logic for negative values. The same sorting rule handles all signs.

## 6. C++ Implementation: Dot Products

**Input:** `n`, then the `n` elements of `A`, then the `n` elements of `B`.

**Output:** the maximum dot product, followed by the minimum dot product, each on its own line.

Under the stated bounds, a product can have magnitude $10^{18}$ and a sum can have magnitude $10^{23}$. A signed 64-bit integer is not sufficient for the answer.

The following complete program uses C++17 with the GCC/Clang `__int128` extension. The helper prints its decimal representation. On a compiler without this extension, use a suitable multiprecision integer type.

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

using i128 = __int128_t;

void printInt128(i128 value) {
    if (value == 0) {
        cout << '0';
        return;
    }
    if (value < 0) {
        cout << '-';
        value = -value;
    }
    string digits;
    while (value > 0) {
        digits.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(digits.begin(), digits.end());
    cout << digits;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n), b(n);
    for (auto& value : a) cin >> value;
    for (auto& value : b) cin >> value;

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    i128 maximum = 0;
    i128 minimum = 0;
    for (int i = 0; i < n; ++i) {
        maximum += i128(a[i]) * b[i];
        minimum += i128(a[i]) * b[n - 1 - i];
    }

    printInt128(maximum);
    cout << '\n';
    printInt128(minimum);
    cout << '\n';
}
```

Example input:

```text
3
-2 1 3
4 -1 2
```

Output:

```text
16
-9
```

**Complexity:** sorting takes $O(n\log n)$ time; summation takes $O(n)$. The arrays use $O(n)$ storage, with $O(\log n)$ additional sorting stack space in the usual `std::sort` implementation.

> **CP Insight: Promote Before Multiplying.** Assigning an overflowing expression to a larger variable does not repair it. Write `i128(a[i]) * b[i]` so multiplication itself uses the wider type. If the element bounds were only $10^5$, the dot-product magnitude would be at most $10^{15}$, and `long long` would suffice.

---

## 7. Problem 2: Choosing the Order of Contest Problems

There are `n` problems. Problem `i` has:

- Initial score $S_i$.
- Score decay per unit of time $D_i$.
- Time required to solve it $T_i$.

If it is **completed** at time $C_i$, its contribution is:

$$
S_i-D_i C_i.
$$

Find an order that maximizes:

$$
\sum_{i=1}^{n}(S_i-D_i C_i).
$$

### Conventions That Determine the Problem

- We start at time `0` and solve one problem at a time.
- All problems are available at the start.
- Every problem must be completed exactly once, without interruption.
- Scores may become negative; they are not clamped to zero.
- There is no contest deadline or option to select only a subset.
- $T_i>0$ and $D_i\ge 0$.

We may process problems consecutively: inserting idle time cannot improve the score because all decay rates are nonnegative.

For the implementation, assume $1\le n\le 10^5$, $0\le S_i,D_i\le 10^9$, and $1\le T_i\le 10^9$. These are explicit working bounds for the lesson.

### The Example from the Lecture

| Problem | Initial score $S_i$ | Decay $D_i$ | Time $T_i$ |
| --- | --- | --- | --- |
| 1 | 100 | 20 | 5 |
| 2 | 200 | 50 | 3 |

Order `1 -> 2`:

$$
(100-20\cdot5)+(200-50\cdot8)=0-200=-200.
$$

Order `2 -> 1`:

$$
(200-50\cdot3)+(100-20\cdot8)=50-60=-10.
$$

The better order is `2 -> 1`. A negative optimal score is valid because solving every problem is mandatory.

## 8. Remove the Part That Does Not Depend on the Order

Rewrite the objective:

$$
\sum_i S_i-\sum_i D_i C_i.
$$

Every problem is solved, so $\sum_i S_i$ is fixed. Maximizing the score is equivalent to minimizing:

$$
\sum_i D_i C_i.
$$

The initial scores affect the final answer, but **they do not affect the optimal ordering** under these assumptions.

Sorting by the initial score alone therefore has no justification.

## 9. Deriving the Comparator with an Adjacent Swap

Consider two adjacent problems `i` and `j`. Let `t` be the time already spent before this pair.

If we solve `i` before `j`, their total contribution is:

$$
F_{ij}=S_i-D_i(t+T_i)+S_j-D_j(t+T_i+T_j).
$$

If we solve `j` before `i`, it is:

$$
F_{ji}=S_j-D_j(t+T_j)+S_i-D_i(t+T_j+T_i).
$$

Subtracting cancels the initial scores, the existing elapsed time, and each problem's own processing penalty:

$$
F_{ij}-F_{ji}=D_iT_j-D_jT_i.
$$

Therefore, putting `i` first is at least as good exactly when:

$$
\boxed{D_iT_j\ge D_jT_i.}
$$

Because both processing times are positive, this is equivalent to:

$$
\boxed{\frac{D_i}{T_i}\ge\frac{D_j}{T_j}.}
$$

**Sort by decreasing decay per unit of processing time.**

In the running example:

```text
Problem 1: D/T = 20/5 = 4
Problem 2: D/T = 50/3
```

Problem 2 belongs first.

### Why Must the Pair Be Adjacent?

Problems before the pair are unchanged. Problems after the pair still start after exactly $T_i+T_j$ additional time, so their completion times are unchanged as well.

Only the two displayed contributions need to be compared.

If we swap two non-adjacent problems with different durations, the completion times of problems between them may change. Ignoring those contributions would make the proof incomplete.

### Why Does This Give a Global Optimum?

Take any order with an adjacent pair whose ratios increase. Swapping that pair does not reduce the score. Repeatedly remove these inversions until all ratios are nonincreasing.

This transforms an optimal order into the greedy order without worsening its score. Thus the sorted order is optimal.

This scheduling rule is commonly called **Smith's rule**. Here, the decay rates act as weights in a weighted completion-time objective.

## 10. Implement the Comparison Without Division

We do not need to calculate a floating-point ratio. Compare cross products instead:

```text
i comes before j if D[i] * T[j] > D[j] * T[i]
```

Use a **strict** comparison for sorting. When ratios tie, either order gives the same total score; we can break ties by original problem index to make the output deterministic.

The ratio rule is transitive because it orders the numerical quantities $D_i/T_i$. Cross multiplication computes that same ordering exactly.

> **CP Insight:** A local comparison is not automatically a valid sorting comparator. It must define a consistent ordering. Here, positive denominators let us interpret the comparison as an ordering of ratios, which establishes consistency.

### Special Cases

- `D[i] = 0`: its score does not decay. It can go after problems with positive decay.
- Equal ratios: either relative order has the same value.
- Equal durations: larger decay belongs first.
- Equal positive decay rates: shorter duration belongs first.
- `n = 1`: complete the only problem at time `T[0]`, not at time zero.

## 11. C++ Implementation: Contest Scheduling

**Input:** `n`, followed by `n` lines containing `score decay time`.

**Output:** an optimal ordering of the original **1-based** problem indices, followed by the maximum total score on the next line.

Elapsed time is at most $10^{14}$, which fits in `long long`. The accumulated decay penalty can approach $10^{28}$, so the score uses `__int128`.

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

using i128 = __int128_t;

struct Problem {
    long long score, decay, time;
    int id;
};

void printInt128(i128 value) {
    if (value == 0) {
        cout << '0';
        return;
    }
    if (value < 0) {
        cout << '-';
        value = -value;
    }
    string digits;
    while (value > 0) {
        digits.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(digits.begin(), digits.end());
    cout << digits;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Problem> problems(n);
    for (int i = 0; i < n; ++i) {
        cin >> problems[i].score >> problems[i].decay >> problems[i].time;
        problems[i].id = i + 1;
    }

    sort(problems.begin(), problems.end(),
         [](const Problem& a, const Problem& b) {
             i128 left = i128(a.decay) * b.time;
             i128 right = i128(b.decay) * a.time;
             if (left != right) return left > right;
             return a.id < b.id;
         });

    long long elapsed = 0;
    i128 totalScore = 0;
    for (int i = 0; i < n; ++i) {
        const Problem& problem = problems[i];
        elapsed += problem.time;
        totalScore += i128(problem.score) - i128(problem.decay) * elapsed;
        if (i > 0) cout << ' ';
        cout << problem.id;
    }
    cout << '\n';
    printInt128(totalScore);
    cout << '\n';
}
```

Example input:

```text
2
100 20 5
200 50 3
```

Output:

```text
2 1
-10
```

**Complexity:** $O(n\log n)$ time and $O(n)$ storage for the problem records, plus the sorting stack.

## 12. Common Mistakes and Interview Follow-Ups

| Mistake | Why it fails |
| --- | --- |
| Sorting by initial score | The sum of initial scores is constant. |
| Sorting only by decay | Duration affects how much a problem delays all later problems. |
| Sorting only by duration | Decay determines the cost of delaying each problem. |
| Using integer division for `D/T` | Distinct ratios can truncate to the same integer. |
| Returning `>=` in the comparator | An element must not compare strictly before itself. |
| Adding score before increasing elapsed time | The score is awarded at completion, not at start. |
| Clamping negative scores to zero | This changes the objective and invalidates the cancellation used in the proof. |
| Swapping distant tasks while ignoring tasks between them | Their completion times may also change. |

**Why not sort only by decay?** Consider `(D, T) = (10, 100)` and `(9, 1)`. The first problem has slightly greater decay but takes much longer. The second has the larger ratio and should come first. Initial scores can be any fixed values because they cancel.

**What if solving problems is optional?** Then the selected set is no longer fixed, and neither is the sum of initial scores. The ratio rule still describes the best order for a chosen set, but it does not by itself choose that set.

**What if there is a deadline or each score is clamped to zero?** Re-derive the objective before reusing the rule. Those changes introduce selection or nonlinear behavior that the proof above does not cover.

**How can we check a proposed rule during a contest?** For very small `n`, enumerate all permutations and compare the greedy result with the true optimum. This is useful for finding counterexamples and implementation bugs. It supports testing; it does not replace the proof for arbitrary inputs.

## 13. Practice Check

1. For `A = [-3, 2]` and `B = [-4, 5]`, find the maximum and minimum dot products.
2. Two tasks have `(D, T) = (6, 3)` and `(10, 5)`. Which should go first?
3. Why does the scheduling swap calculation not depend on the elapsed time before the pair?
4. Why does the dot-product rule still work for negative elements?

**Answers:**

1. Maximum: $12+10=22$. Minimum: $-15-8=-23$.
2. Both ratios are `2`, so either order gives the same score.
3. Both arrangements contain the same penalty $t(D_i+D_j)$, which cancels.
4. The proof depends on the signs of sorted differences, not on the individual values.

## Quick Recap

- A greedy rule needs a correctness argument.
- Compare two arrangements and cancel the unchanged terms.
- For dot products, the difference is $(a_j-a_i)(b_j-b_i)$.
- Same-order sorting maximizes the dot product; opposite-order sorting minimizes it.
- For contest scheduling, the difference is $D_iT_j-D_jT_i$.
- Sort contest problems by decreasing $D_i/T_i$, using exact cross products.
- Explain why each exchange preserves feasibility and why repeated exchanges reach the greedy arrangement.

In the next session, we will use a different local comparison: instead of swapping two tasks, we will move a meeting point and compare how much total distance increases and decreases.

</READING_WIDGET>

<!-- Editorial source map: lecture images 1–12; Algozenith_DSA/Greedy/dotProduct.cpp and calculateMaximumScore.cpp. Both dot-product variants are retained. Working scheduling bounds are supplied because the source does not specify them. Code corrects narrow arithmetic and the inconsistent score variable in the lecture screenshot. No video ID has been assigned. -->
