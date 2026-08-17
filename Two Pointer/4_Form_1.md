<VIDEO_WIDGET>

<VIDEO_ID>3227</VIDEO_ID>

</VIDEO_WIDGET>

<VIDEO_WIDGET>

<VIDEO_ID>3228</VIDEO_ID>

</VIDEO_WIDGET>

<VIDEO_WIDGET>

<VIDEO_ID>3229</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Two Pointers: Form 1 — Variable-Size Window

Form 0 handled windows whose size was fixed in advance. Form 1 removes that restriction.

In a **variable-size window**, the window grows and shrinks according to a condition:

- `tail` is the left pointer.
- `head` is the right pointer.
- `head` expands the window as far as the rule permits.
- After using the current window, `tail` moves forward and removes its element.

The size of the window is:

$$\text{length} = \text{head} - \text{tail} + 1$$

Unlike Form 0, both boundaries are meaningful because the correct window size is discovered while processing the array.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/5ae898ab-b7a7-4313-8987-c5c37383b4ab.png" alt="Form 1 variable-size window lifecycle" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. The Core Form 1 Pattern

The implementation begins with an empty window:

~~~cpp
int head = -1;
int tail = 0;
~~~

For every value of `tail`, we move `head` as far right as possible without breaking the window condition.

~~~cpp
while (tail < n) {
    while (head + 1 < n && check(arr[head + 1])) {
        head++;
        insert(arr[head]);
    }

    // Use the maximal window [tail, head].

    if (tail <= head) {
        erase(arr[tail]);
        tail++;
    } else {
        tail++;
        head = tail - 1;
    }
}
~~~

This gives us the central invariant:

> At the answer step, `head` is the farthest position that can be reached for the current `tail` without violating the rule.

### The Three Phases

Every outer-loop iteration has three phases:

1. **Expand:** Move `head` while the next element can be included.
2. **Use:** Update the answer using the current maximal window.
3. **Shrink:** Remove `arr[tail]` and move `tail` forward.

The `check` function must inspect the next value without changing the maintained state. The state is updated only after `head` actually moves.

---

## 2. Why Does `head` Never Move Backward?

Suppose `head` cannot include the next element for the current `tail`. We then remove `arr[tail]` and advance `tail`.

Removing an element can only make a constraint such as “at most $K$ zeros” or “at most $K$ distinct values” easier to satisfy. Therefore, the old `head` is still usable, and we only need to test positions after it.

Across the complete algorithm:

- `tail` moves at most $N$ times.
- `head` moves at most $N$ times.

Hence:

$$\text{Time Complexity} = O(N)$$

This depends on **monotonicity**. If removing from the left or adding on the right changes validity unpredictably, this pattern may not apply.

### The Form 1 Applicability Rule

Before applying the canonical Form 1 pattern, check the following implication:

$$
[\text{tail}, \text{head}] \text{ is valid}
\quad \Longrightarrow \quad
[\text{tail} + 1, \text{head}] \text{ is also valid}
$$

In words:

> If a window is valid, removing its leftmost element must not make it invalid.

This property is what allows `tail` to move forward without forcing `head` to move backward. After removing `arr[tail]`, the old `head` remains valid, so the algorithm can continue expanding from there.

For example, the rule holds for:

- Number of zeros $\le K$.
- Number of distinct values $\le K$.
- Window sum $\le K$, when all array values are non-negative.

Removing an element cannot increase any of these quantities.

This condition is sometimes called **left-removal monotonicity** or **hereditary validity**.

### A Tempting Problem Where This Pattern Does Not Work Directly

> Given an array of integers—which may be negative, positive, or zero—find the length of the longest subarray whose sum is at most $K$.

Consider:

~~~text
arr = [-5, 4, 5, -10]
K = 0
~~~

The complete array has sum $-6$, so the correct answer is $4$.

At first, this looks like a standard `sum <= K` variable-window problem. However, negative values destroy the required monotonicity.

First, consider the valid window `[-5, 4]`:

~~~text
[tail, head]     = [0, 1] -> [-5, 4] -> sum = -1 -> valid
[tail + 1, head] = [1, 1] -> [4]     -> sum =  4 -> invalid
~~~

Therefore:

$$
[0,1] \text{ is valid} \centernot\Longrightarrow [1,1] \text{ is valid}
$$

Removing the negative value `-5` increases the sum and makes the remaining window invalid. Thus, the old `head` is no longer guaranteed to remain valid when `tail` advances.

There is another problem. Starting at `tail = 0`, the standard expansion reaches `[-5, 4]`, whose sum is $-1$. It refuses to include the next value `5` because the sum would become $4 > K$. However, including the later value `-10` would bring the sum back down:

~~~text
[-5, 4, 5]      -> sum =   4 -> invalid
[-5, 4, 5, -10] -> sum =  -6 -> valid
~~~

The standard Form 1 loop stops at the temporarily invalid prefix and never reaches this valid longer window. On this example, it finds length $2$, even though the correct answer is $4$.

This is the common trap: **a condition that identifies an answer is not necessarily a condition that can maintain a Form 1 window**.

If every value were non-negative, removing the tail could only decrease the sum, and once adding a value made the sum too large, adding more values could not repair it. With arbitrary signed integers, neither fact is true, so the standard Form 1 pattern cannot be applied directly.

---

## 3. The Empty-Window Edge Case

The branch where `tail > head` is essential.

It occurs when even a one-element window cannot satisfy the expansion rule. A common example is $K = 0$ while the next array element would immediately consume a forbidden resource.

~~~cpp
if (tail <= head) {
    erase(arr[tail]);
    tail++;
} else {
    tail++;
    head = tail - 1;
}
~~~

In the empty-window case, there is nothing to erase. We advance `tail` and restore:

$$\text{head} = \text{tail} - 1$$

so the next iteration again begins with an empty window.

---

## 4. Question 1: Maximum Consecutive Ones After Flipping at Most $K$ Zeros

### Problem

Given a binary array `arr` and an integer $K$, return the maximum number of consecutive ones obtainable by flipping at most $K$ zeros into ones.

For:

~~~text
N = 9
K = 2
arr = [0, 1, 0, 1, 0, 0, 1, 1, 0]
~~~

the answer is:

~~~text
5
~~~

### Window Property

The window is valid when:

$$\text{zeroCount} \le K$$

Before including `arr[head + 1]`, we check whether it would add another zero:

~~~cpp
zeroCount + (arr[head + 1] == 0) <= k
~~~

For every `tail`, we maximize `head` and update the longest valid length.

### Dry Run

| `tail` | Maximum `head` reached | Length | Maximum length |
|---:|---:|---:|---:|
| 0 | 3 | 4 | 4 |
| 1 | 4 | 4 | 4 |
| 2 | 4 | 3 | 4 |
| 3 | 7 | 5 | 5 |
| 4 | 7 | 4 | 5 |
| 5 | 8 | 4 | 5 |
| 6 | 8 | 3 | 5 |
| 7 | 8 | 2 | 5 |
| 8 | 8 | 1 | 5 |

### Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

int longestOnesAfterFlips(const vector<int>& arr, int k) {
    int n = static_cast<int>(arr.size());

    int head = -1;
    int tail = 0;
    int zeroCount = 0;
    int answer = 0;

    while (tail < n) {
        // Maximize HEAD while the next element keeps zeros <= K.
        while (head + 1 < n &&
               zeroCount + (arr[head + 1] == 0) <= k) {
            head++;
            zeroCount += (arr[head] == 0);
        }

        answer = max(answer, head - tail + 1);

        if (tail <= head) {
            zeroCount -= (arr[tail] == 0);
            tail++;
        } else {
            tail++;
            head = tail - 1;
        }
    }

    return answer;
}

int main() {
    vector<int> arr = {0, 1, 0, 1, 0, 0, 1, 1, 0};
    int k = 2;

    cout << longestOnesAfterFlips(arr, k) << '\n';
    return 0;
}
~~~

### Edge Case: $K = 0$

For:

~~~text
arr = [0, 0, 0, 1]
K = 0
~~~

the first three tails cannot form a non-empty valid window. The empty-window branch advances them safely. At the final position, the window `[1]` is valid, so the answer is $1$.

---

## 5. Question 2: Count Subarrays with At Most $K$ Distinct Values

### Problem

Given an integer array `arr` and an integer $K$, count the subarrays containing at most $K$ distinct values.

For:

~~~text
N = 7
K = 2
arr = [2, 3, 2, 5, 2, 5, 2]
~~~

the answer is:

~~~text
20
~~~

### Maintained State

We keep:

- a frequency table for values in the current window, and
- `distinctCount`, the number of values whose frequency is positive.

Adding `x` increases `distinctCount` only if its current frequency is zero. Removing `x` decreases `distinctCount` only when its frequency becomes zero.

The next value can be added when:

$$\text{distinctCount} + [\text{frequency[next]} = 0] \le K$$

### Why Do We Add `head - tail + 1`?

Suppose the maximal valid window for one `tail` is `[tail, head]`.

Then all of these subarrays are valid:

$$[tail, tail], [tail, tail + 1], \ldots, [tail, head]$$

There are:

$$\text{head} - \text{tail} + 1$$

such endings.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/f4595ccf-f050-44ca-ae2b-3033052175c5.png" alt="Counting valid subarrays from one TAIL" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Dry Run

| `tail` | Maximum `head` reached | Valid endings from `tail` | Running total |
|---:|---:|---:|---:|
| 0 | 2 | 3 | 3 |
| 1 | 2 | 2 | 5 |
| 2 | 6 | 5 | 10 |
| 3 | 6 | 4 | 14 |
| 4 | 6 | 3 | 17 |
| 5 | 6 | 2 | 19 |
| 6 | 6 | 1 | 20 |

### Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

long long countAtMostKDistinct(const vector<int>& arr, int k) {
    if (k < 0) {
        return 0;
    }

    int n = static_cast<int>(arr.size());
    unordered_map<int, int> frequency;

    int head = -1;
    int tail = 0;
    int distinctCount = 0;
    long long answer = 0;

    while (tail < n) {
        // Maximize HEAD while the next value keeps distinctCount <= K.
        while (head + 1 < n) {
            int nextValue = arr[head + 1];
            bool isNew = (frequency.find(nextValue) == frequency.end());

            if (distinctCount + isNew > k) {
                break;
            }

            head++;
            frequency[arr[head]]++;

            if (isNew) {
                distinctCount++;
            }
        }

        // Every ending from TAIL through HEAD forms a valid subarray.
        answer += head - tail + 1;

        if (tail <= head) {
            int outgoing = arr[tail];
            frequency[outgoing]--;

            if (frequency[outgoing] == 0) {
                frequency.erase(outgoing);
                distinctCount--;
            }

            tail++;
        } else {
            tail++;
            head = tail - 1;
        }
    }

    return answer;
}

int main() {
    vector<int> arr = {2, 3, 2, 5, 2, 5, 2};
    int k = 2;

    cout << countAtMostKDistinct(arr, k) << '\n';
    return 0;
}
~~~

### Complexity

With an `unordered_map`:

$$\text{Expected Time} = O(N)$$

$$\text{Space} = O(K)$$

At most $K$ distinct values have positive frequencies in the active window. If the values lie in a small known range, a frequency vector can replace the hash map.

---

## 6. Question 3: Count Subarrays with Exactly $K$ Distinct Values

### Problem

Given an integer array `arr` and an integer $K$, count the subarrays containing exactly $K$ distinct values.

“Exactly $K$” is not directly convenient for the maximize-`head` pattern. If a window currently has fewer than $K$ distinct values, it is not yet an answer; after expansion it may become valid, and after another expansion it may become invalid.

However, “at most $K$” is monotonic. We already know how to count it.

Every subarray with at most $K$ distinct values belongs to one of two groups:

1. It has at most $K - 1$ distinct values.
2. It has exactly $K$ distinct values.

Therefore:

$$\boxed{\text{exactly}(K) = \text{atMost}(K) - \text{atMost}(K - 1)}$$

### Implementation

~~~cpp
long long countExactlyKDistinct(const vector<int>& arr, int k) {
    return countAtMostKDistinct(arr, k)
         - countAtMostKDistinct(arr, k - 1);
}
~~~

For the array:

~~~text
[2, 3, 2, 5, 2, 5, 2]
~~~

we have:

~~~text
atMost(2) = 20
atMost(1) = 7
exactly(2) = 20 - 7 = 13
~~~

> 💡 **Reusable Transformation:** The same identity works for many “exactly $K$” counting problems whenever an “at most $K$” version is monotonic and easy to compute.

---

## 7. Question 4: Shortest Subarray with At Least $K$ Distinct Values

### Problem

Given an integer array `arr` and an integer $K$, find the length of the shortest subarray containing at least $K$ distinct values.

This question changes how we use the window.

For the earlier problems, we expanded `head` while the window remained valid. Here, we expand `head` **until the window becomes valid**:

$$\text{distinctCount} \ge K$$

For each `tail`:

1. Move `head` until the window contains at least $K$ distinct values.
2. Record its length.
3. Remove `arr[tail]` and advance `tail` to search for a shorter window.

### Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

int shortestAtLeastKDistinct(const vector<int>& arr, int k) {
    if (k <= 0) {
        return 0;
    }

    int n = static_cast<int>(arr.size());
    unordered_map<int, int> frequency;

    int head = -1;
    int tail = 0;
    int distinctCount = 0;
    int answer = n + 1;

    while (tail < n) {
        // Move HEAD until the window becomes valid or the array ends.
        while (head + 1 < n && distinctCount < k) {
            head++;

            if (frequency[arr[head]] == 0) {
                distinctCount++;
            }
            frequency[arr[head]]++;
        }

        if (distinctCount >= k) {
            answer = min(answer, head - tail + 1);
        }

        if (tail <= head) {
            int outgoing = arr[tail];
            frequency[outgoing]--;

            if (frequency[outgoing] == 0) {
                frequency.erase(outgoing);
                distinctCount--;
            }

            tail++;
        } else {
            tail++;
            head = tail - 1;
        }
    }

    return (answer == n + 1 ? -1 : answer);
}
~~~

If the complete array contains fewer than $K$ distinct values, no valid subarray exists and the function returns $-1$.

---

## 8. Two Modes of Form 1

The canonical Form 1 pattern and its mirrored lower-bound variation are:

| Goal | Expansion rule | Answer step |
|---|---|---|
| Canonical Form 1: longest/count with an upper bound | Expand while the next element keeps the window valid | Use the maximal valid `head` |
| Mirrored variation: shortest with a lower bound | Expand while the current window is not yet valid | Use the first valid `head` |

The applicability rule

$$
[\text{tail},\text{head}] \text{ valid} \Longrightarrow [\text{tail}+1,\text{head}] \text{ valid}
$$

belongs to the **canonical maximal-valid-window pattern**. In the mirrored shortest-window variation, removing `tail` may make the window invalid; the next iteration then expands `head` until it becomes valid again.

The pointer movement remains the same:

- `head` never moves backward.
- `tail` advances one position per outer iteration.
- Window state is updated only when an element enters or leaves.

---

## 9. Common Mistakes

### Checking the Current Element Instead of the Next Element

The expansion condition must test `arr[head + 1]`. The maintained state already describes `[tail, head]`.

### Updating State Inside `check`

The check should be read-only. Update frequencies, zero counts, or sums only after `head` advances.

### Forgetting the Empty-Window Branch

When no single element is valid, `tail` can be greater than `head`. Do not erase an element that was never inserted.

### Counting Only the Maximal Window

For an “at most” counting problem, one maximal window represents every valid ending from `tail` through `head`. Add `head - tail + 1`, not just $1$.

### Trying to Count Exactly $K$ Directly

The property “exactly $K$” is not monotonic under extension. Convert it into:

$$\text{atMost}(K) - \text{atMost}(K - 1)$$

More generally, do not use an “exactly” condition directly as the maximal-valid-window property. First look for a monotonic “at most” or “at least” formulation.

### Reinitializing the Frequency Table for Every `tail`

Doing so destroys the linear-time benefit. Maintain the window incrementally by inserting at `head` and erasing at `tail`.

---

## 10. Form 1 Summary

- Form 1 maintains a variable-size window `[tail, head]`.
- `tail` is the left pointer and `head` is the right pointer.
- For the canonical pattern, validity must survive removal from the left: if `[tail, head]` is valid, `[tail + 1, head]` must also be valid.
- For every `tail`, `head` moves monotonically to the farthest useful position.
- Longest-window problems use `head - tail + 1` as a candidate length.
- “At most” counting problems add `head - tail + 1` valid endings.
- “Exactly $K$” is often computed as `atMost(K) - atMost(K - 1)`.
- Shortest-window problems expand until the lower-bound condition becomes true.
- Each element enters and leaves the window at most once, giving $O(N)$ pointer movement.

</READING_WIDGET>
