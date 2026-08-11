<VIDEO_WIDGET>

<VIDEO_ID>3591</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Monotonic Deque

> _The "Sliding Window Maximum" problem is a legendary FAANG interview question. It perfectly bridges the gap between simple two-pointer windows and complex data structures. Let's master the Monotonic Deque, an architecture so fast it crushes the Priority Queue's $O(N \log N)$ time into a flawless $O(N)$._

---

## 1. The Core Intuition

**The Problem:** Given an array of integers `nums` and a sliding window of size `k`, find the maximum element inside the window as it slides from the far left to the far right.

**Example:**
Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`
Output: `[3, 3, 5, 5, 6, 7]`

**Approach 1: The Brute Force ($O(N \times K)$)**
For every element, scan the next $K$ elements to find the maximum. On an array of size $10^5$ with a window of size $50,000$, this triggers an instant Time Limit Exceeded (TLE).

**Approach 2: The Priority Queue ($O(N \log N)$)**
We could throw elements into a Max-Heap as the window slides. But Priority Queues don't support random `.erase()`! To "delete" elements that fall out of the window, we must store pairs of `{value, index}` and do "lazy deletion" when the top element's index is finally out of bounds. This is clever, but the $O(\log N)$ push/pop overhead is still too slow for elite competitive programming.

**The Elite Approach: Monotonic Deque ($O(N)$)**
Think about the nature of the window. If you see a massive number like `100`, any small numbers like `5` or `12` that came _before_ it are utterly useless!
Why? Because `100` is both **larger** and **will survive longer** in the sliding window than the older numbers!

We need a data structure that lets us:

1. **Evict old numbers from the Front** (when the window slides past them).
2. **Purge weak numbers from the Back** (when a new, larger number arrives).

The only STL container that supports $O(1)$ operations at both ends is the **Deque (Double-Ended Queue)**!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/2e108cb2-8722-4bc6-becc-29899e807303.jpg" alt="Monotonic Deque Mechanics" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. The Monotonic Deque Algorithm

We will maintain a `std::deque` of **Indices** (not values!), ensuring the values they point to are in strictly decreasing order.

### The Algorithm:

For every index `i` from $0$ to $N-1$:

1. **Evict the Old:** Check the index sitting at the `front()` of the deque. If it is $\le i - k$, it has mathematically fallen out of the sliding window. `pop_front()`!
2. **Purge the Weak:** Look at the `back()` of the deque. If the value there is $\le$ the current number `nums[i]`, it is completely useless. `pop_back()` until you find a stronger number or the deque empties.
3. **Save Yourself:** Push the current index `i` to the `back()` of the deque.
4. **Record the Answer:** If our window has fully formed ($i \ge k - 1$), the absolute maximum for this window is sitting perfectly at the `front()`! Record `nums[dq.front()]`.

### The Code Implementation

```cpp
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

vector<int> maxSlidingWindow(const vector<int>& nums, int k) {
    vector<int> result;
    deque<int> dq; // Stores INDICES, not values!

    for (int i = 0; i < nums.size(); i++) {
        // 1. Evict the Old (Window slided past this index)
        // Using a 'while' and '<=' makes this template universally safe
        // for Dynamic Sliding Windows where the left bound jumps!
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }

        // 2. Purge the Weak (Destroy useless smaller numbers)
        while (!dq.empty() && nums[dq.back()] <= nums[i]) {
            dq.pop_back();
        }

        // 3. Save Yourself
        dq.push_back(i);

        // 4. Record the Answer (Once the first window is fully formed)
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }

    return result;
}
```

> 💡 **CP Insight: The Duplicate Lifespan**
> Why do we use `<=` instead of `<` to purge weak numbers? If the current number is exactly equal to the number at the back of the deque, the older number is mathematically useless! Because the newer number arrived later, it will survive in the sliding window longer. Purging duplicates keeps our deque perfectly minimal!

---

## 3. Complexity Analysis

> 🚨 **The CP Trap: The "Nested Loop" Illusion**
> Just like the Monotonic Stack, beginners see a `while` loop inside a `for` loop and panic, assuming the code is $O(N^2)$.
> **Look at the deque mechanics:** Every index is `push_back()` exactly **once**. Therefore, an index can be popped (either from the front or back) at most **once**. The `while` loop executes a total of $N$ times across the _entire program_.
> This guarantees an absolute, flawless **$O(N)$ Time Complexity**!

---

## 4. Elite CP Insights

> 💡 **Systems Insight: Storing Indices vs Values**
> The golden rule of Sliding Windows is: **Always store Indices, never Values!**
> If you store values, you have no mathematical way to know if the `dq.front()` element has fallen out of the left side of your window. By storing indices, checking expiration is a simple $O(1)$ math equation: `dq.front() == i - k`.

> 💡 **Variation: Sliding Window Minimum**
> To find the minimum element in every window, you only need to change a single character! Change `nums[dq.back()] <= nums[i]` to `nums[dq.back()] >= nums[i]`. Now, the deque purges larger elements and maintains a strictly increasing order, keeping the smallest element safely at the front.

</READING_WIDGET>
