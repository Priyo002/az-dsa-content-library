<VIDEO_WIDGET>

<VIDEO_ID>3592</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Application: Prefix Sum + Binary Search

> _Knowing a data structure is one thing. Combining two completely different algorithms to shatter a time complexity barrier is what gets you hired at FAANG. This module demonstrates how Prefix Sums naturally unlock the power of Binary Search._

---

## 1. The Challenge: Multi-Query Optimization

**Problem Statement:**
You are given a shop with $N$ items, where each item has a price $P_i$.
You must answer $M$ queries. For each query, a customer walks in with a specific `budget`. You must output the maximum number of items they can purchase.

### The Naive Approach

To maximize the number of items bought, you should obviously buy the cheapest items first.

1. Sort the prices array: $O(N \log N)$.
2. For each query, iterate through the sorted array, deducting prices from the budget until you run out of money: $O(N)$.
   **Total Time:** $O(N \log N + M \times N)$.

If $N = 10^5$ and $M = 10^5$, the $M \times N$ loop will execute $10^{10}$ times, instantly triggering a **Time Limit Exceeded (TLE)**!

We need to process each customer's query in significantly less time than $O(N)$.

---

## 2. The $O(\log N)$ Architecture: Prefix Sums + `upper_bound`

How can we avoid looping through the array for every customer? We use a **Prefix Sum**.

If our sorted prices are: `[3, 5, 8, 12, 15]`
The cumulative prefix sum is: `[3, 8, 16, 28, 43]`

This prefix array tells us:

- Buying 1 item costs $3$.
- Buying 2 items costs $8$.
- Buying 3 items costs $16$.

**The Golden Property of Prefix Sums:** Because item prices are positive, a prefix sum array is _strictly monotonically increasing_. And whenever data is monotonically increasing, we can use **Binary Search**!

> 🚨 **The CP Trap: Zero-Cost Items and Weak Monotonicity**
> What if an item costs $\$0$? If the prices are `[3, 5, 0, 8]`, the prefix sum becomes `[3, 8, 8, 16]`. The array is no longer _strictly_ increasing; it is **weakly monotonic** (non-decreasing).
> `std::upper_bound` is a masterpiece here because it inherently supports weakly monotonic arrays by mathematically seeking the _first strictly greater_ element, cleanly bypassing duplicate values.
> _(Warning: If items can have negative costs, monotonicity is destroyed completely, and Binary Search will fatally fail!)_

Instead of simulating the purchases one by one, we can simply ask the Prefix Sum array: _"Where does my budget fit in?"_
By using C++ STL's `std::upper_bound`, we can binary search the Prefix Sum array in $O(\log N)$ time, instantly returning the maximum number of items the customer can afford!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7e579dd2-5ff5-4382-9dad-99d9939b3401.jpg" alt="Prefix Sum and Binary Search Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

> 💎 **Elite CP Insight: 1-Based Prefix Mapping**
> The reference code modifies the original array in place to build the cumulative sum. While memory efficient, pointer arithmetic with `upper_bound` on 0-based arrays can get very confusing.
> Elite programmers use the **1-Based Prefix Array Trick** (size $N+1$). `prefix[k]` explicitly stores the exact cost of buying exactly `k` items. When `upper_bound` finds the first cost that exceeds our budget, subtracting the `prefix.begin()` iterator gives us the exact number of items we _can_ afford, with zero "-1" offset arithmetic!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // 1. Setup Phase
    int n = 5; // Number of items
    vector<int> prices = {12, 3, 15, 8, 5};

    // Always sort first to prioritize buying the cheapest items!
    sort(prices.begin(), prices.end());
    // Sorted: {3, 5, 8, 12, 15}

    // 2. Precomputation Phase: 1-Based Prefix Sum
    // prefix[k] will store the exact cost to buy 'k' items.
    vector<long long> prefix(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + prices[i];
    }
    // prefix: {0, 3, 8, 16, 28, 43}

    // 3. Query Phase
    vector<long long> queries = {7, 16, 30, 50}; // Budgets

    for (long long budget : queries) {
        // upper_bound finds the FIRST element strictly greater than the budget
        auto it = upper_bound(prefix.begin(), prefix.end(), budget);

        // The index of this element represents the number of items we CANNOT afford.
        // Therefore, (index - 1) represents the number of items we CAN afford!
        // Because of our 1-based indexing, the iterator arithmetic perfectly evaluates:
        // 💡 Systems Insight: This O(1) subtraction ONLY works because std::vector uses Random Access Iterators!
        // On a std::set or std::list, you would need std::distance(), which degrades to O(N) time.
        int max_items = (it - prefix.begin()) - 1;

        cout << "Budget: $" << budget << " -> Max Items: " << max_items << "\n";
    }

    return 0;
}
```

### Complexity Breakdown

- **Time Complexity:**
  - **Sorting Phase:** $O(N \log N)$ to sort the prices.
  - **Precomputation Phase:** $O(N)$ to build the prefix sum array.
  - **Query Phase:** $O(M \log N)$. We run $M$ queries, and `upper_bound` takes $O(\log N)$ per query.
  - **Total Time:** $O((N + M) \log N)$. This completely shatters the $O(M \times N)$ naive approach!
- **Space Complexity:** $O(N)$ auxiliary space for the prefix sum array.

## 4. Module Summary

- Sorting greedily ensures we maximize the item count by buying the cheapest items first.
- A **Prefix Sum** array constructed from positive numbers is guaranteed to be strictly increasing, unlocking the ability to use $O(\log N)$ **Binary Search**.
- By leveraging STL `std::upper_bound` combined with a $1$-based prefix array, we can instantly locate the maximum affordable items without complex index-offset math.
- Combining these techniques drops query resolution time from linear to logarithmic, allowing systems to handle millions of queries flawlessly.

</READING_WIDGET>
