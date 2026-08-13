<VIDEO_WIDGET>

<VIDEO_ID>3231</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Two Pointers: Form 2 — Divergence Type

In Form 0 and Form 1, the pointers described a window that moved from left to right. Form 2 begins differently:

- `tail` starts at the left end.
- `head` starts at the right end.
- The pointers move toward each other.
- At every step, we use the current pair and prove that one endpoint can be discarded.

Even though the course calls this the **Divergence Type**, the pointers physically converge. The name emphasizes that they begin at two separated ends and make different movement decisions.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/4fca4f80-5dab-4b30-a4f6-278893d238e6.png" alt="Form 2 divergence pattern" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. The Core Form 2 Pattern

The basic structure is:

~~~cpp
int tail = 0;
int head = n - 1;

while (tail < head) {
    // 1. Use the current pair (tail, head).

    // 2. Prove that one endpoint can be eliminated.
    if (shouldMoveTail()) {
        tail++;
    } else {
        head--;
    }
}
~~~

The loop condition is `tail < head` because the current state represents a pair of different indices.

The important part is not that the pointers begin at opposite ends. The important part is this:

> Every pointer movement must safely eliminate all answers involving the discarded endpoint.

If we cannot prove which side is safe to discard, we cannot apply Form 2 merely because an array has two ends.

---

## 2. How to Recognize Form 2

Consider Form 2 when:

1. The answer depends on a pair of positions.
2. The candidates have an ordered structure, often a sorted array or two opposite boundaries.
3. Both endpoints give useful information about the current answer.
4. A comparison between the endpoints proves that one side cannot participate in a better future answer.

Form 2 reduces a two-dimensional search space of pairs into one path of pointer movements.

Initially, there are:

$$
\frac{N(N-1)}{2}
$$

possible pairs. If one endpoint is eliminated at every step, only $O(N)$ pairs need to be examined.

---

## 3. Problem: Maximum Value of $F(i,j)$

Given an array `arr` of $N$ non-negative integers, find the maximum value of:

$$
F(i,j)=|i-j|\times\min(arr[i],arr[j])
$$

over every pair satisfying:

$$
0\le i<j<N
$$

Because $i<j$, we can write the distance as:

$$
|i-j|=j-i
$$

Therefore:

$$
F(i,j)=(j-i)\times\min(arr[i],arr[j])
$$

For example:

~~~text
N = 9
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
~~~

the answer is:

~~~text
49
~~~

It is obtained from indices $1$ and $8$:

$$
F(1,8)=(8-1)\times\min(8,7)=7\times7=49
$$

> **Constraint Note:** The elimination proof below assumes the values are non-negative, as in the container-height interpretation of this problem. With arbitrary negative values, reducing the width can improve a negative product, so the standard movement proof is no longer valid.

---

## 4. Brute-Force Approach

The direct solution checks every pair:

~~~cpp
long long answer = 0;

for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        answer = max(answer,
                     (j - i) * min(arr[i], arr[j]));
    }
}
~~~

There are $O(N^2)$ pairs, so:

$$
\text{Time Complexity}=O(N^2)
$$

We need to avoid considering every possible partner for every index.

---

## 5. What Controls the Score?

The score has two parts:

$$
\underbrace{(head-tail)}_{\text{width}}
\times
\underbrace{\min(arr[tail],arr[head])}_{\text{limiting height}}
$$

At the beginning, the width is as large as possible. Every pointer movement makes the width smaller.

Therefore, if we want a better score after shrinking the width, we must try to improve the limiting height. The limiting height is always the smaller endpoint.

This gives the movement rule:

- If `arr[tail] < arr[head]`, move `tail` forward.
- If `arr[tail] > arr[head]`, move `head` backward.
- If both values are equal, either endpoint may be moved.

In code:

~~~cpp
if (arr[tail] < arr[head]) {
    tail++;
} else {
    head--;
}
~~~

Moving the taller endpoint cannot help: the shorter endpoint would remain the limiting height while the width becomes smaller.

---

## 6. Why Is Moving the Smaller Endpoint Safe?

Suppose:

$$
arr[tail]\le arr[head]
$$

For the current pair, the score is:

$$
(head-tail)\times arr[tail]
$$

Now keep `tail` fixed and choose any position $k$ between `tail` and `head`:

$$
tail<k<head
$$

Its width is smaller:

$$
k-tail<head-tail
$$

Its limiting height cannot exceed `arr[tail]`:

$$
\min(arr[tail],arr[k])\le arr[tail]
$$

Since the values are non-negative:

$$
(k-tail)\times\min(arr[tail],arr[k])
\le
(head-tail)\times arr[tail]
$$

We have already evaluated the best possible pair that can use this `tail`. No closer `head` can produce a better score with it.

Therefore, we can safely discard the current `tail` and execute:

~~~cpp
tail++;
~~~

The argument is symmetric when:

$$
arr[head]<arr[tail]
$$

In that case, no pair using the current `head` can beat the pair we just evaluated, so we execute:

~~~cpp
head--;
~~~

This elimination proof is the central invariant of Form 2.

---

## 7. Dry Run

For:

~~~text
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
~~~

we begin with:

~~~text
tail = 0
head = 8
~~~

| `tail` | `head` | `arr[tail]` | `arr[head]` | Current score | Best answer | Pointer moved |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 8 | 1 | 7 | $8\times1=8$ | 8 | `tail++` |
| 1 | 8 | 8 | 7 | $7\times7=49$ | 49 | `head--` |
| 1 | 7 | 8 | 3 | $6\times3=18$ | 49 | `head--` |
| 1 | 6 | 8 | 8 | $5\times8=40$ | 49 | `head--` |
| 1 | 5 | 8 | 4 | $4\times4=16$ | 49 | `head--` |
| 1 | 4 | 8 | 5 | $3\times5=15$ | 49 | `head--` |
| 1 | 3 | 8 | 2 | $2\times2=4$ | 49 | `head--` |
| 1 | 2 | 8 | 6 | $1\times6=6$ | 49 | `head--` |

After the last movement, `tail == head`, so no pair remains. The maximum score is $49$.

Notice that the algorithm does not inspect every pair. Each comparison eliminates one complete group of pairs sharing the smaller endpoint.

---

## 8. Complete Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

void init() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

void solve() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    if (n < 2) {
        cout << 0 << endl;
        return;
    }

    int tail = 0;
    int head = n - 1;
    int answer = 0;

    while (tail < head) {
        int width = head - tail;
        int limitingHeight = min(arr[tail], arr[head]);

        answer = max(answer, width * limitingHeight);

        // Eliminate the endpoint with the smaller value.
        if (arr[tail] < arr[head]) {
            tail++;
        } else {
            head--;
        }
    }

    cout << answer << endl;
}

int32_t main() {
    init();

    int _t = 1;
    cin >> _t;

    while (_t--) {
        solve();
    }

    return 0;
}
~~~

---

## 9. Complexity Analysis

The pointers begin $N-1$ positions apart. Every iteration moves exactly one pointer inward.

- `tail` can move right at most $N-1$ times.
- `head` can move left at most $N-1$ times.
- No pointer moves backward.

Therefore:

$$
\text{Time Complexity}=O(N)
$$

Only a few variables are maintained:

$$
\text{Extra Space}=O(1)
$$

---

## 10. Common Mistakes

### Moving the Larger Endpoint

The smaller endpoint limits the current score. Moving the larger endpoint preserves the same limiting value but reduces the width, so it cannot create an improvement for the retained smaller endpoint.

### Moving Both Pointers

Move only the endpoint that the proof allows us to eliminate. Moving both pointers can skip a pair containing the answer.

### Updating the Answer After Moving a Pointer

The current pair must be evaluated before either endpoint is discarded.

~~~cpp
answer = max(answer,
             (head - tail) * min(arr[tail], arr[head]));

// Move a pointer only after using the pair.
~~~

### Using `tail <= head`

The function is defined for $i<j$. When `tail == head`, there is only one index, not a valid pair.

### Applying the Pattern Without an Elimination Proof

Starting at opposite ends is not sufficient. Before moving a pointer, prove that every skipped pair involving that endpoint cannot improve the answer.

### Ignoring the Non-Negative Constraint

The proof compares products after reducing the width. It relies on the limiting height being non-negative. Do not reuse this exact movement rule for arbitrary signed values without a new proof.

---

## 11. Form 2 Summary

- `tail` starts at index $0$ and represents the left pointer.
- `head` starts at index $N-1$ and represents the right pointer.
- Evaluate the current pair before moving either pointer.
- Use the endpoint values to prove which side can be eliminated.
- For this problem, move the endpoint with the smaller height.
- If the endpoint values are equal, either side may be eliminated.
- Each iteration reduces the remaining search space.
- Each pointer moves at most $N$ times, giving $O(N)$ time and $O(1)$ extra space.
- The key Form 2 question is: **Which endpoint can be discarded without losing the optimal answer?**

</READING_WIDGET>
