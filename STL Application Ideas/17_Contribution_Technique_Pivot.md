<VIDEO_WIDGET>

<VIDEO_ID>3602</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Contribution Technique: Pivot-Based (Contribution at End)

> _While Atomic Contribution looks at an element and asks "Where can I go?", Pivot-Based Contribution flips the script entirely. It looks at an index and asks, "What if I force every subarray to end exactly here?" By anchoring structures to a pivot, we merge Combinatorics with Dynamic Programming._

---

## 1. The Challenge: Sum of Product of All Subarrays

**Problem Statement:**
Given an array `arr[]` of size `N`, calculate the _product_ of elements in each possible subarray, and then find the _sum_ of all those products.

### The Naive $O(N^2)$ Trap

If the array is `[A, B, C]`, the subarrays are:

- `[A]` $\rightarrow$ Product: $A$
- `[B]`, `[A, B]` $\rightarrow$ Products: $B, A \times B$
- `[C]`, `[B, C]`, `[A, B, C]` $\rightarrow$ Products: $C, B \times C, A \times B \times C$

A beginner will use nested loops to generate every subarray and calculate the product. As always, an $O(N^2)$ approach will instantly trigger a **Time Limit Exceeded (TLE)** on arrays of size $10^5$.
We need to calculate this in strictly $O(N)$ time.

---

## 2. The $O(N)$ Architecture: Pivot State Transitions

Notice how I grouped the subarrays in the example above? I grouped them by their **Ending Index** (the Pivot).
Let's define a state:
`SOP(i)` = The Sum of Products of all subarrays that **end exactly at index $i$**.

Let's look at the transition from index $1$ to index $2$:

- Subarrays ending at `B`: `[B]` and `[A, B]`.
  - `SOP(1)` = $B + A \times B$
- Subarrays ending at `C`: `[C]`, `[B, C]`, and `[A, B, C]`.
  - Let's factor out $C$ from the longer arrays: $C + C \times (B + A \times B)$
  - Substitute `SOP(1)` into the equation: $C + C \times \text{SOP(1)}$

### The Mathematical Formula

Every time we move to a new pivot $i$, we take _all_ the subarrays that ended at the previous pivot $i-1$, append our new element `arr[i]` to them, and then add a brand new subarray that contains _only_ `arr[i]`.

Because we are calculating products, appending `arr[i]` simply multiplies the previous sum of products by `arr[i]`:
**$$ SOP(i) = arr[i] + (SOP(i-1) \times arr[i]) $$**
**$$ SOP(i) = arr[i] \times (1 + SOP(i-1)) $$**

This is an incredibly powerful Dynamic Programming state transition. We only need to track the `SOP` of the previous index to instantly calculate the `SOP` of the current index! The total answer is just the sum of all $SOP(i)$.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/89d1595a-a21a-4ddf-9db1-921729ae6f87.png" alt="Pivot Based Contribution" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 📝 **Dry Run: `arr = [2, 3, 4]`**
>
> - **i = 0 (Pivot `2`):** `SOP = 2`. Total Answer = **2**
> - **i = 1 (Pivot `3`):** `SOP = 3 + (2 * 3) = 9`. Total Answer = 2 + 9 = **11**
>   - _(Verification: `[3]`=3, `[2,3]`=6. 3+6 = 9)_
> - **i = 2 (Pivot `4`):** `SOP = 4 + (9 * 4) = 40`. Total Answer = 11 + 40 = **51**
>   - _(Verification: `[4]`=4, `[3,4]`=12, `[2,3,4]`=24. 4+12+24 = 40)_
> - **Final Answer: 51.** Computed in strictly $O(N)$ operations!

---

## 3. The Code Implementation

> 🚨 **The FAANG Modulo Trap**
> Products grow exponentially. A subarray of twenty `10`s is $10^{20}$, which shatters the absolute limit of a 64-bit `long long` integer. Standard competitive programming problems will _always_ ask you to return the answer modulo $10^9 + 7$. You must apply the modulo operator at _every single addition and multiplication step_ to prevent catastrophic overflow!

```cpp
#include <iostream>
#include <vector>

using namespace std;

const long long MOD = 1e9 + 7;

long long sumOfProductOfSubarrays(const vector<long long>& arr) {
    int n = arr.size();
    if (n == 0) return 0;

    // ans stores the global sum of all SOPs
    long long ans = arr[0] % MOD;

    // sop stores the Sum of Products ending at the current pivot
    long long sop = arr[0] % MOD;

    for (int i = 1; i < n; i++) {
        // State Transition: SOP(i) = arr[i] + (arr[i] * SOP(i-1))
        // We apply modulo arithmetic at every arithmetic operation!
        long long expanded_previous = (sop * arr[i]) % MOD;
        sop = (expanded_previous + arr[i]) % MOD;

        // Add the current pivot's contribution to the global answer
        ans = (ans + sop) % MOD;
    }

    return ans;
}

int main() {
    vector<long long> arr = {2, 3, 4};

    // Expected Output: 51
    cout << "Sum of Products of all Subarrays: " << sumOfProductOfSubarrays(arr) << "\n";

    return 0;
}
```

---

## 4. Real-World Application: Kadane's Algorithm

The absolute most famous application of the Pivot-Based Contribution technique is **Kadane's Algorithm**, which solves the classic "Maximum Subarray Sum" problem.

**Problem Statement:**
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

If we apply our Pivot-Based logic, we group the subarrays by their ending index.
Let's define our state:
`MaxSum(i)` = The maximum sum of a subarray that **ends exactly at index $i$**.

When moving to the next pivot $i$, we only have two choices:

1. **Extend:** Take the absolute best subarray that ended at index $i-1$, and append `nums[i]` to it. (Value: `nums[i] + MaxSum(i-1)`)
2. **Start Fresh:** Ignore everything that came before, and start a brand new subarray starting exactly at `nums[i]`. (Value: `nums[i]`)

### The Mathematical Formula

**$$ MaxSum(i) = \max(nums[i], nums[i] + MaxSum(i-1)) $$**

Because we only care about the best possible sum, we track the global maximum across all $i$!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxSubArray(vector<int>& nums) {
    // max_ending_here tracks MaxSum(i) for the current pivot
    int max_ending_here = nums[0];

    // global_max tracks the absolute best answer seen so far
    int global_max = nums[0];

    for (int i = 1; i < nums.size(); i++) {
        // State Transition: Do we extend the previous subarray, or start fresh?
        max_ending_here = max(nums[i], nums[i] + max_ending_here);

        // Update the global maximum
        global_max = max(global_max, max_ending_here);
    }

    return global_max;
}
```

Notice how this is the exact same architectural blueprint as our Sum of Products problem! We simply replaced multiplication with addition, and the running sum with a running maximum.

## 5. Module Summary

- **Pivot-Based Contribution** is the art of grouping combinatorial structures by their _ending index_.
- By defining a state based on the ending index, we can leverage **Dynamic Programming** state transitions to build current answers directly off of previous answers, shattering $O(N^2)$ loops into strict $O(N)$ linear scans.
- When dealing with subarray products, always anticipate massive 64-bit integer overflows and aggressively apply Modulo Arithmetic (`1e9 + 7`) at every discrete mathematical step.

</READING_WIDGET>
