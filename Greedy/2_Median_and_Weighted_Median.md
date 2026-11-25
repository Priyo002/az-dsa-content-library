<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Greedy on a Number Line: Median and Weighted Median

> *Where should people meet so that their total travel distance is as small as possible? The midpoint of the extreme locations may look reasonable, but every person contributes to the answer. We will compare the cost of moving left and right, then extend the same reasoning to people with different travel costs.*

## 1. From Exchanging Tasks to Moving a Point

In the previous session, we compared two arrangements by swapping a pair. Here, the decision is a location on a number line.

Instead of asking whether a swap helps, we ask:

**If we move the meeting point slightly to the right, how does the total cost change?**

This is a local improvement argument. It is related to greedy reasoning, although it is not a pairwise exchange proof like the scheduling proof.

The key observation will be that moving toward one side helps the points on that side and hurts the points on the other side. The best location balances these effects.

## 2. Problem 1: Minimum Total Distance

We are given `n` integer coordinates:

$$
x_1,x_2,\ldots,x_n.
$$

Choose a meeting point `p` that minimizes:

$$
F(p)=\sum_{i=1}^{n}|p-x_i|.
$$

Every location contributes equally. Coordinates may be negative, zero, or repeated.

Use the following working bounds:

- $1\le n\le 10^5$.
- $-10^9\le x_i\le 10^9$.

The mathematical problem allows any real meeting point. Since the input coordinates are integers, an integer optimal point always exists; our implementation returns one such point and its minimum cost.

### The Lecture Example

For locations `[1, 3, 7]`:

$$
F(p)=|p-1|+|p-3|+|p-7|.
$$

| Meeting point `p` | Distances | Total cost |
| --- | --- | --- |
| 1 | $0+2+6$ | 8 |
| 2 | $1+1+5$ | 7 |
| 3 | $2+0+4$ | 6 |
| 4 | $3+1+3$ | 7 |
| 7 | $6+4+0$ | 10 |

The best point is `3`, the median.

We need an argument that works for every input, not just this example.

## 3. What Happens When We Move Right?

Suppose `p` lies in a gap between input coordinates. Let:

- `L` be the number of points to its left.
- `R` be the number of points to its right.

Move from `p` to `p + delta`, where `delta > 0` is small enough that we do not cross any input coordinate.

- Each point on the left becomes `delta` farther away.
- Each point on the right becomes `delta` closer.

Therefore:

$$
F(p+\delta)-F(p)=(L-R)\delta.
$$

This gives three possibilities:

| Balance | Effect of moving right |
| --- | --- |
| `L < R` | Cost decreases. |
| `L > R` | Cost increases. |
| `L = R` | Cost stays unchanged within the gap. |

If more people are on the right, moving right helps more people than it hurts. If more people are on the left, we should move left instead.

As we sweep from left to right, `L` only increases and `R` only decreases. The slope never decreases. The function is **convex and piecewise linear**, so once moving right starts increasing the cost, continuing farther right cannot uncover a better minimum.

### The Exact Shape for `[1, 3, 7]`

Expanding the absolute values gives:

$$
F(p)=
\begin{cases}
11-3p, & p\le 1,\\
9-p, & 1\le p\le 3,\\
p+3, & 3\le p\le 7,\\
3p-11, & p\ge 7.
\end{cases}
$$

The slopes are `-3`, `-1`, `+1`, and `+3`. The function decreases until `3` and increases afterward. Its minimum is `F(3) = 6`.

No calculus is required: the slope simply counts how many distances increase and how many decrease.

## 4. Why the Median Minimizes Absolute Distance

Sort the coordinates:

$$
x_1\le x_2\le\cdots\le x_n.
$$

A median is a point with at most half the observations strictly to its left and at most half strictly to its right. Repeated coordinates count as separate observations.

### Odd Number of Points

If $n=2m+1$, the median is:

$$
\boxed{p=x_{m+1}.}
$$

To the left of this coordinate, more than half the points lie to the right, so moving right reduces the cost. To its right, more than half lie to the left, so moving left reduces the cost.

Thus the middle coordinate is optimal.

### Even Number of Points

If $n=2m$, **every point in the closed interval**:

$$
\boxed{[x_m,x_{m+1}]}
$$

is optimal.

Between the two middle coordinates, there are equally many observations on each side, so the cost stays constant.

For example, with `[1, 3, 7, 9]`, every point in `[3, 7]` gives cost `12`:

```text
p = 3: 2 + 0 + 4 + 6 = 12
p = 5: 4 + 2 + 2 + 4 = 12
p = 7: 6 + 4 + 0 + 2 = 12
```

If integer output is required, any integer in this interval works. We can simply choose one of the two middle coordinates; averaging them is unnecessary.

## 5. Another Proof: Pair the Extremes

For any two locations `a <= b`:

$$
|p-a|+|p-b|\ge b-a.
$$

Equality holds exactly when `p` lies in `[a, b]`.

Now pair the sorted coordinates from the outside inward:

```text
(x[1], x[n]), (x[2], x[n - 1]), ...
```

Each pair has the smallest possible contribution whenever `p` lies between its endpoints.

- For even `n`, the intersection of all these intervals is the interval between the two middle coordinates.
- For odd `n`, one middle coordinate remains unpaired. Choosing it minimizes every pair and makes the unpaired contribution zero.

This proves the same median rule directly, without reasoning about movement.

> **Interview Insight:** The movement proof explains how to discover the answer. The paired-extremes proof gives a short way to justify it once discovered.

## 6. C++ Implementation: Ordinary Median

**Input:** `n`, followed by `n` coordinates.

**Output:** one optimal meeting point and the minimum total distance, separated by a space.

The implementation chooses the lower median: index `(n - 1) / 2` in a zero-based sorted vector.

```cpp
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> x(n);
    for (auto& coordinate : x) cin >> coordinate;

    sort(x.begin(), x.end());
    long long point = x[(n - 1) / 2];

    long long cost = 0;
    for (long long coordinate : x) {
        cost += abs(point - coordinate);
    }

    cout << point << ' ' << cost << '\n';
}
```

Example input:

```text
3
1 3 7
```

Output:

```text
3 6
```

Each distance is at most $2\cdot10^9$, and the total is at most $2\cdot10^{14}$, so `long long` is sufficient under these bounds.

**Complexity:** $O(n\log n)$ time and $O(n)$ storage for the coordinates, plus the sorting stack.

---

## 7. Problem 2: Different Travel Costs

Now each location has a nonnegative weight $w_i$. Traveling one unit from that location costs $w_i$ units.

Choose `p` to minimize:

$$
G(p)=\sum_{i=1}^{n}w_i|p-x_i|.
$$

The lecture writes these weights as $k_i$. We use $w_i$ to distinguish them from the team size `k` used in the next session.

For the implementation, use the same coordinate bounds and integer weights:

$$
0\le w_i\le 10^9.
$$

The nonnegative-weight assumption is essential to the balancing argument. Zero weights are allowed and contribute no cost.

### Why the Ordinary Median May Fail

Consider the lecture example:

| Coordinate | Weight |
| --- | --- |
| 1 | 1 |
| 3 | 1 |
| 7 | 3 |

The ordinary median of the three coordinates is `3`, but:

$$
G(3)=1\cdot2+1\cdot0+3\cdot4=14.
$$

At `7`:

$$
G(7)=1\cdot6+1\cdot4+3\cdot0=10.
$$

The location at `7` has enough weight to change the optimal answer.

We must balance **total weight**, not the number of distinct locations.

## 8. Deriving the Weighted Median

Suppose `p` lies between coordinates. Let:

- $W_L$ be the total weight strictly to the left.
- $W_R$ be the total weight strictly to the right.

For a move of size $\delta$ that crosses no coordinate:

$$
G(p+\delta)-G(p)=(W_L-W_R)\delta.
$$

The same argument now applies to weights:

- If more weight lies on the right, moving right lowers the cost.
- If more weight lies on the left, moving left lowers the cost.
- If the two sides have equal weight, the cost is constant throughout that gap.

Let $W=\sum_i w_i>0$. A **weighted median** is any point `p` satisfying:

$$
\boxed{W_L\le\frac W2\quad\text{and}\quad W_R\le\frac W2.}
$$

Weight located exactly at `p` belongs to neither strict side.

### Why This Condition Works at a Coordinate

Let $W_E$ be the weight located exactly at `p`.

For a small rightward move, that weight also becomes farther away. The change per unit distance is:

$$
W_L+W_E-W_R=W-2W_R.
$$

For a small leftward move, the change per unit distance is:

$$
W_R+W_E-W_L=W-2W_L.
$$

Both are nonnegative precisely when neither strict side contains more than half the total weight.

The piecewise-linear slopes never decrease because every crossed coordinate has nonnegative weight. Thus a point satisfying these conditions is a global minimum.

## 9. Integer Weights as Repeated Points

For positive integer weights, imagine replacing `(x[i], w[i])` with `w[i]` copies of `x[i]`.

For the example:

```text
Coordinates: [1, 3, 7]
Weights:     [1, 1, 3]

Conceptual expanded list: [1, 3, 7, 7, 7]
```

The median is `7`, which gives the weighted answer.

This interpretation is useful for understanding the rule, but we should **not build the expanded list**. Its length is `W`, which may be much larger than `n`.

Instead, prefix sums let us locate the middle position without expansion.

## 10. Find the Weighted Median with Prefix Sums

Sort `(coordinate, weight)` pairs by coordinate. Define:

$$
P_i=\sum_{j=1}^{i}w_j.
$$

For positive integer total weight, the lower median of the expanded list is at the 1-based position:

$$
r=\left\lceil\frac W2\right\rceil.
$$

Find the first prefix with:

$$
P_i\ge r.
$$

Then `x[i]` is one weighted median.

### The Larger Lecture Example

```text
Coordinates:    [1, 3, 5, 9]
Weights:        [3, 1, 2, 3]
Prefix weights: [3, 4, 6, 9]
```

Here `W = 9`, so the target rank is `5`.

| Coordinate | Prefix weight | Reached rank 5? |
| --- | --- | --- |
| 1 | 3 | No |
| 3 | 4 | No |
| 5 | 6 | Yes |

The weighted median is `5`.

Its cost is:

$$
3|5-1|+1|5-3|+2|5-5|+3|5-9|
=12+2+0+12=26.
$$

### Why This Prefix Rule Satisfies the Definition

Before the first prefix that reaches `r`, the cumulative weight is less than `r`, and therefore at most $W/2$. After that coordinate, the remaining weight is at most $W-r\le W/2$.

If multiple entries share the same coordinate, their weights at the chosen point do not belong to either strict side. The condition still holds without explicitly merging duplicates.

> **CP Insight: Use Total Weight, Not `n / 2`.** The middle position belongs to the conceptual list of `W` copies. For the example above, `n / 2 = 2` would select coordinate `1`, which is wrong. The correct target is `ceil(9 / 2) = 5`.

## 11. Ties, Zero Weights, and Real Weights

### An Interval of Optimal Points

For `(1, 2)` and `(7, 2)`, total weight is `4`. The cost is:

$$
2|p-1|+2|p-7|.
$$

Every point in `[1, 7]` gives cost `12`. Choosing the first prefix reaching rank `2` returns the lower endpoint `1`, which is a valid optimum.

More generally, if the cumulative weight reaches exactly half at one positive-weight coordinate, every point up to the next positive-weight coordinate is optimal. Zero-weight locations inside the interval do not change it.

### All Weights Are Zero

Then `G(p) = 0` for every point. There is no positive target rank. Our code explicitly returns the smallest input coordinate with cost zero.

### What If Weights Are Real Numbers?

The balance condition still works for nonnegative real weights with positive total weight. Use the first cumulative weight reaching `W / 2`; the integer-rank interpretation and ceiling operation are specific to integer weights. Numerical precision needs separate care for floating-point inputs.

## 12. C++ Implementation: Weighted Median

**Input:** `n`, followed by `n` lines containing `coordinate weight`.

**Output:** one optimal meeting point and the minimum weighted cost, separated by a space.

Total weight is at most $10^{14}$, so prefix sums fit in `long long`. The weighted cost can be as large as $2\cdot10^{23}$, so the code uses the GCC/Clang `__int128` extension for products and the answer.

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

using i128 = __int128_t;

void printInt128(i128 value) {
    if (value == 0) {
        cout << '0';
        return;
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
    vector<pair<long long, long long>> points(n);
    for (auto& [coordinate, weight] : points) {
        cin >> coordinate >> weight;
    }
    sort(points.begin(), points.end());

    vector<long long> prefix(n);
    long long totalWeight = 0;
    for (int i = 0; i < n; ++i) {
        totalWeight += points[i].second;
        prefix[i] = totalWeight;
    }

    if (totalWeight == 0) {
        cout << points.front().first << " 0\n";
        return 0;
    }

    long long target = totalWeight / 2 + totalWeight % 2;
    int index = int(lower_bound(prefix.begin(), prefix.end(), target)
                    - prefix.begin());
    long long meetingPoint = points[index].first;

    i128 cost = 0;
    for (const auto& [coordinate, weight] : points) {
        i128 distance = i128(meetingPoint) - coordinate;
        if (distance < 0) distance = -distance;
        cost += distance * weight;
    }

    cout << meetingPoint << ' ';
    printInt128(cost);
    cout << '\n';
}
```

Example input:

```text
4
1 3
3 1
5 2
9 3
```

Output:

```text
5 26
```

The print helper only needs to handle nonnegative values because a weighted distance with nonnegative weights cannot be negative.

**Complexity:** sorting takes $O(n\log n)$; prefix construction and cost evaluation take $O(n)$; `lower_bound` takes $O(\log n)$. Overall time is $O(n\log n)$ and storage is $O(n)$.

For a single query, a running cumulative sum can replace the prefix vector and binary search. The prefix version directly illustrates how we locate a rank in compressed frequency data.

## 13. Median, Mean, and Midpoint Solve Different Problems

The word “center” is not enough to determine an algorithm. The objective function matters.

| Objective on a number line | An optimal point |
| --- | --- |
| $\sum_i \lvert p-x_i\rvert$ | Any median |
| $\sum_i w_i\lvert p-x_i\rvert$, nonnegative weights with positive total | Any weighted median |
| $\sum_i (p-x_i)^2$ | Arithmetic mean |
| $\max_i \lvert p-x_i\rvert$ | Midpoint of the minimum and maximum coordinates |

For `[1, 3, 7]`, the mean is `11/3`, the extreme midpoint is `4`, and the median is `3`. Only the median minimizes the total absolute distance.

> **Interview Insight:** Before answering “use the median,” state whether the objective is a sum of distances, a sum of squared distances, or the maximum distance. These similar-looking problems have different optimal choices.

## 14. Edge Cases and Common Mistakes

| Case | Expected behavior |
| --- | --- |
| One location with positive weight | Meet there; cost is zero. |
| All coordinates equal | Meet at that coordinate; cost is zero. |
| Even number of unweighted points | Every point between the two middle coordinates is optimal. |
| A location has more than half the total weight | Its coordinate is the unique optimum. |
| Half the total weight lies on each side of a gap | The entire gap is optimal. |
| Zero-weight locations | They do not affect the cost. |
| All weights zero | Every meeting point is optimal. |
| Repeated coordinates | Keep them or combine their weights; both work. |
| Negative coordinates | Sorting and absolute differences work normally. |

Common implementation errors include:

- Sorting the coordinates separately from their weights, which breaks the association.
- Using the ordinary middle index for a weighted problem.
- Using `W / 2` with truncation when `W` is odd. For `W = 5`, target rank `2` is not the median rank `3`.
- Expanding each weight into repeated coordinates, which can require enormous memory.
- Forgetting that several locations can be optimal.
- Computing a weighted product in a narrow type before assigning it to a wider answer.

## 15. Interview and Competitive Programming Insights

**Selection can avoid a full sort for the ordinary median.** If only one median and its cost are needed, `nth_element` can place the chosen median at its sorted rank without sorting the entire array. Its usual non-parallel overload has average linear complexity; follow it with one linear cost scan. Sorting remains a straightforward deterministic $O(n\log n)$ approach.

**Recognize the two-dimensional Manhattan extension.** For points `(x[i], y[i])`, the objective is:

$$
\sum_i\bigl(|p_x-x_i|+|p_y-y_i|\bigr)
=\sum_i|p_x-x_i|+\sum_i|p_y-y_i|.
$$

The two coordinates can be optimized independently. Choose a median of the x-coordinates and a median of the y-coordinates. With a weight on each point, use weighted medians in each dimension. This applies to Manhattan distance with an unrestricted meeting location; Euclidean distance is a different problem.

**A minimizer need not be unique.** If asked to return the smallest optimal coordinate, the lower-median convention is useful. If asked for all optimal coordinates, describe the full interval instead.

**Convexity does not mean numerical search is necessary.** The objective is convex, but its exact structure gives a direct median solution. Sorting and selecting the median avoids repeated cost evaluations and numerical tolerance choices.

## 16. Practice Check

1. For `[2, 4, 10, 12]`, what is the full interval of optimal meeting points?
2. For coordinates `[1, 3, 7]` and weights `[1, 1, 3]`, what are the weighted median and minimum cost?
3. For coordinates `[0, 10]` with weights `[5, 5]`, is `p = 6` optimal?
4. Why is it unnecessary to create the expanded list of repeated points?

**Answers:**

1. `[4, 10]`; every point in this interval gives total distance `16`.
2. Weighted median `7`, minimum cost `10`.
3. Yes. Every point in `[0, 10]` gives weighted cost `50`.
4. Prefix sums identify the coordinate containing the median rank using only the original `n` records.

## Quick Recap

- Moving right increases distances to points on the left and decreases distances to points on the right.
- The balance of these changes leads to the median.
- With weights, balance total weight on the two sides.
- For positive integer total weight `W`, find the first prefix reaching `ceil(W / 2)`.
- Even splits can create an interval of optimal meeting points.
- Sorting pairs, scanning prefix weights, and evaluating the final cost gives an $O(n\log n)$ solution.

In the next session, we will return to an exchange argument for selecting team members. Sorting will control a minimum value, while a heap will maintain the best remaining choices.

</READING_WIDGET>
