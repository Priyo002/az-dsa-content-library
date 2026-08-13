<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Two Pointers: Form 0 — Fixed-Size Sliding Window

Form 0 is the simplest version of the Two Pointer technique. We are asked to process every contiguous subarray of an exact size $K$.

The window size never changes, so we do not need to maintain two independent pointers. We use only one moving pointer:

> `head` represents the rightmost element of the current window.

The starting position is calculated directly from `head` and $K$:

$$\text{start} = \text{head} - K + 1$$

This is why Form 0 is sometimes called the **single-pointer sliding window**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/5b7683ea-70d2-4104-aebb-b2a23f0a0dfa.png" alt="A fixed-size window moving with a single HEAD pointer" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. Why Do We Need a Sliding Window?

Suppose an array contains $N$ elements and we need to calculate something for every subarray of size $K$.

A direct solution rebuilds each window independently. Since there are approximately $N$ windows and every window contains $K$ elements, this can require:

$$O(NK)$$

But two consecutive windows overlap heavily.

If the current window is:

$$[a_i, a_{i+1}, \ldots, a_{i+K-1}]$$

then the next window is:

$$[a_{i+1}, a_{i+2}, \ldots, a_{i+K}]$$

Only two things changed:

1. $a_i$ left the window.
2. $a_{i+K}$ entered the window.

Instead of rebuilding the next window, we update only these two changes.

---

## 2. The Form 0 Invariant

For every position of `head`, the active window ends at `head`.

Once the first complete window has formed:

$$\text{window} = [\text{head} - K + 1,\ \text{head}]$$

The index that has just expired is:

$$\text{expired index} = \text{head} - K$$

Notice the difference:

- `head - K + 1` is the first index **inside** the current window.
- `head - K` is the index immediately **before** the current window.

### The Three Actions

At every position of `head`:

1. **Add** the current element `arr[head]`.
2. **Remove** `arr[head - K]` if that index exists.
3. **Process** the answer once the window contains exactly $K$ elements.

The general shape is:

~~~cpp
for (int head = 0; head < n; head++) {
    add(arr[head]);

    if (head - k >= 0) {
        remove(arr[head - k]);
    }

    if (head >= k - 1) {
        process_current_window();
    }
}
~~~

> 💡 **Why is there no `tail`?** The left boundary is always `head - K + 1`. Since it can be calculated instantly, maintaining another pointer would be redundant.

---

## 3. Problem: Minimum in Every Subarray of Size $K$

Given an integer array `arr` of size $N$ and an integer $K$, find the minimum element in every contiguous subarray of size $K$.

Assume:

$$1 \le K \le N$$

### Example

For:

~~~text
arr = [3, 1, 4, 2, 8, 6, 5, 7]
K = 3
~~~

the windows are:

| Window | Elements | Minimum |
|---|---|---:|
| 1 | `[3, 1, 4]` | 1 |
| 2 | `[1, 4, 2]` | 1 |
| 3 | `[4, 2, 8]` | 2 |
| 4 | `[2, 8, 6]` | 2 |
| 5 | `[8, 6, 5]` | 5 |
| 6 | `[6, 5, 7]` | 5 |

Therefore, the answer is:

~~~text
1 1 2 2 5 5
~~~

We will solve this problem in two ways:

1. Using a `multiset` — simpler and broadly reusable.
2. Using a monotonic `deque` — more specialized and optimal.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/849cbcc4-ef47-4ae0-ad4b-0ba2637f9fd5.png" alt="Multiset and monotonic deque approaches for tracking a window minimum" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Approach 1: Maintaining the Window with a Multiset

A `multiset` stores values in sorted order and allows duplicates. Both properties are important:

- Sorted order gives us the minimum immediately.
- Duplicate support lets the window contain repeated values safely.

If `window` is the multiset for the current window, its minimum is:

~~~cpp
*window.begin()
~~~

### Window Update

For every `head`:

1. Insert `arr[head]`.
2. If `head - K` is valid, erase one occurrence of `arr[head - K]`.
3. If `head >= K - 1`, the window is complete and its minimum can be recorded.

### The Duplicate-Erasure Trap

This is incorrect:

~~~cpp
window.erase(value);
~~~

It erases **every occurrence** of `value` from a `multiset`.

We need to erase only the occurrence that left the window:

~~~cpp
window.erase(window.find(value));
~~~

### Complete Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> minimumsUsingMultiset(const vector<int>& arr, int k) {
    int n = static_cast<int>(arr.size());
    vector<int> answer;

    if (k <= 0 || k > n) {
        return answer;
    }

    multiset<int> window;

    for (int head = 0; head < n; head++) {
        // The current element enters the window.
        window.insert(arr[head]);

        // The element K positions behind HEAD has expired.
        if (head - k >= 0) {
            int expired = arr[head - k];
            window.erase(window.find(expired));
        }

        // A complete window exists from HEAD - K + 1 to HEAD.
        if (head >= k - 1) {
            answer.push_back(*window.begin());
        }
    }

    return answer;
}

int main() {
    vector<int> arr = {3, 1, 4, 2, 8, 6, 5, 7};
    int k = 3;

    vector<int> answer = minimumsUsingMultiset(arr, k);

    for (int value : answer) {
        cout << value << ' ';
    }
    cout << '\n';

    return 0;
}
~~~

### Complexity Analysis

The multiset contains at most $K$ elements.

- Each insertion takes $O(\log K)$.
- Each deletion takes $O(\log K)$.
- Reading the minimum from `begin()` takes $O(1)$.

Across all $N$ positions:

$$\text{Time Complexity} = O(N \log K)$$

$$\text{Auxiliary Space} = O(K)$$

The logarithm is $\log K$, not $\log N$, because the multiset stores only the current window.

---

## 5. Approach 2: Maintaining Candidates with a Monotonic Deque

The multiset keeps every element from the current window. But do we really need all of them?

Consider the values `4` and `2`, where `2` appears later.

As long as `2` remains inside the window, `4` can never become the minimum:

- `2` is smaller than `4`.
- `2` will expire later because it is newer.

Therefore, `4` is no longer useful and can be discarded.

A **monotonic deque** stores only indices that are still candidates for becoming the minimum.

### The Deque Invariants

The deque maintains three properties:

1. Its indices are in increasing order.
2. Their corresponding array values are in non-decreasing order.
3. Every stored index belongs to the current window.

Because the values are ordered, the front always represents the minimum:

~~~cpp
arr[dq.front()]
~~~

### Action 1: Remove Expired Indices

At position `head`, the active window starts at `head - K + 1`.

Therefore, an index has expired when:

$$\text{index} \le \text{head} - K$$

Expired indices are removed from the **front**.

### Action 2: Remove Dominated Candidates

Before inserting `head`, remove indices from the back while:

$$arr[dq.back()] \ge arr[head]$$

The current value is smaller or equal and will remain in the window longer. The older value can never be the minimum again.

### Action 3: Insert and Answer

Insert `head` at the back. Once `head >= K - 1`, the index at the front gives the minimum for the complete window.

### Complete Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> minimumsUsingDeque(const vector<int>& arr, int k) {
    int n = static_cast<int>(arr.size());
    vector<int> answer;

    if (k <= 0 || k > n) {
        return answer;
    }

    // Stores indices of useful candidates.
    deque<int> dq;

    for (int head = 0; head < n; head++) {
        // Remove indices that are outside the current window.
        while (!dq.empty() && dq.front() <= head - k) {
            dq.pop_front();
        }

        // Remove candidates dominated by arr[head].
        while (!dq.empty() && arr[dq.back()] >= arr[head]) {
            dq.pop_back();
        }

        // HEAD becomes the newest candidate.
        dq.push_back(head);

        // The front stores the minimum of a complete window.
        if (head >= k - 1) {
            answer.push_back(arr[dq.front()]);
        }
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    for (int& value : arr) {
        cin >> value;
    }

    vector<int> answer = minimumsUsingDeque(arr, k);

    for (int value : answer) {
        cout << value << ' ';
    }
    cout << '\n';

    return 0;
}
~~~

---

## 6. Why Is the Deque Solution $O(N)$?

The nested `while` loops can make the algorithm look quadratic, but consider the lifetime of one index:

1. It is inserted into the deque exactly once.
2. It is removed from the deque at most once.

An index may be removed because it expired or because a newer value dominated it, but it cannot be removed twice.

Across the complete algorithm, there are at most $N$ insertions and $N$ removals:

$$\text{Time Complexity} = O(N)$$

The deque stores at most $K$ useful indices:

$$\text{Auxiliary Space} = O(K)$$

This is another example of **amortized analysis**: one iteration may perform several removals, but the total number of removals across all iterations is linear.

---

## 7. Multiset vs. Monotonic Deque

| Property | Multiset | Monotonic Deque |
|---|---|---|
| What it stores | Every value in the window | Only useful candidate indices |
| Minimum lookup | $O(1)$ | $O(1)$ |
| Insert/remove cost | $O(\log K)$ | $O(1)$ amortized |
| Total time | $O(N \log K)$ | $O(N)$ |
| Extra space | $O(K)$ | $O(K)$ |
| Ease of adaptation | Easier and more general | Faster but specialized |

Use a multiset when you need a simple ordered representation of the whole window or must support operations beyond minimum/maximum.

Use a monotonic deque when the problem asks specifically for a minimum or maximum across every fixed-size window and linear time matters.

> 💡 **Sliding-Window Maximum:** The same deque pattern works for maximum values. Reverse the monotonic comparison so that values remain in non-increasing order and the maximum stays at the front.

---

## 8. Common Mistakes

### Processing Before the First Window Is Complete

The first answer is available only when:

$$\text{head} \ge K - 1$$

Before that point, fewer than $K$ elements have been seen.

### Removing the Wrong Index

At position `head`, the expired index is `head - K`, not `head - K + 1`. The latter is still the first element of the current window.

### Erasing Every Duplicate from the Multiset

Use an iterator when erasing. Removing by value deletes all equal occurrences.

### Storing Values Instead of Indices in the Deque

Expiry is determined by position, so the deque must store indices. Values alone cannot tell us when an element has left the window.

### Removing Dominated Elements from the Wrong End

- Expired indices leave from the **front**.
- Dominated candidates leave from the **back**.

Mixing these operations breaks the deque invariants.

---

## 9. Form 0 Summary

- Form 0 processes every contiguous range of an exact size $K$.
- Only `head` moves; the window starts at `head - K + 1`.
- The element at `head - K` expires whenever a new element enters.
- A multiset solves sliding-window minimum in $O(N \log K)$ time.
- A monotonic deque improves it to $O(N)$ time by retaining only useful candidates.
- The core pattern is always the same: **add, remove the expired element, then process the complete window**.

</READING_WIDGET>
