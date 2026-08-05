<VIDEO_WIDGET>

<VIDEO_ID>76</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Range Queries: 1D Prefix Sums

> *In high-frequency data analytics, recalculating the same information over and over is the fastest way to crash a server. Prefix Sums introduce the concept of **Precomputation**—doing the heavy lifting once so that future queries can be answered instantly.*

---

## 1. The Challenge: Sub-Array Queries

**Problem Statement:** 
You are given a static array `A` of size `N`. You must answer `Q` queries of the form `? L R`, where each query asks for the sum of all elements in the range `[L, R]` (inclusive).

### The Naive $O(N)$ Approach
The beginner's instinct is to run a `for` loop from `L` to `R` for every single query, adding up the elements. 
If the array size $N$ is $10^5$, and we receive $Q = 10^5$ queries, the worst-case scenario (querying from $0$ to $N-1$) requires $10^{10}$ operations. This will immediately trigger a **Time Limit Exceeded (TLE)** in competitive programming or bottleneck a production system.

We need a way to answer these range queries in $O(1)$ time.

---

## 2. The $O(1)$ Architecture: Prefix Sums

A **Prefix Sum** (or cumulative sum) array stores the sum of all elements from the start of the array up to the current index. 
By precomputing this cumulative data, we can find the sum of *any* arbitrary sub-array using simple subtraction.

### The Mathematics of Cancellation
Suppose you have an array `A = [3, 2, 4, 1, 5]`.
The Prefix Sum array `P` would be `[3, 5, 9, 10, 15]`.
- `P[4]` represents the sum of indices `0` to `4` (Total: $15$).
- `P[1]` represents the sum of indices `0` to `1` (Total: $5$).

If we want the sum of the range `[2, 4]`, we take the total sum up to index $4$ and **subtract** the sum up to index $1$. 
`Sum[2...4] = P[4] - P[1] = 15 - 5 = 10`.
*(Check: $4 + 1 + 5 = 10$. It matches perfectly!)*

The universal formula is:
$$\text{Sum}(L, R) = P[R] - P[L - 1]$$

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/1cb7cd5b-89f6-4a12-ab05-fb2d4c894399.jpg" alt="1D Prefix Sum Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

> 💎 **Elite CP Insight: 1-Based Indexing**
> In the standard formula `P[R] - P[L-1]`, what happens if $L = 0$? We attempt to access `P[-1]`, resulting in a **Segmentation Fault (Out of Bounds)**! 
> Beginners fix this by adding an ugly `if (L == 0)` check. 
> Elite programmers fix this by using **1-Based Indexing**. We make the array size $N + 1$ and set `P[0] = 0`. Now, querying the range from the very beginning (`L = 1`) safely evaluates to `P[R] - P[0]`, entirely eliminating the need for `if` statements!

```cpp
#include <iostream>
#include <vector>

using namespace std;

// Time Complexity: O(N) to build
vector<long long> buildPrefixSum(const vector<int>& A) {
    int n = A.size();
    
    // We create an array of size N + 1 to utilize the 1-Based Indexing trick!
    // prefix[0] is safely initialized to 0.
    vector<long long> prefix(n + 1, 0);
    
    for (int i = 0; i < n; i++) {
        // prefix[i+1] stores the sum of A[0] through A[i]
        prefix[i + 1] = prefix[i] + A[i];
    }
    
    return prefix;
}

// Time Complexity: O(1) per query
long long queryRange(const vector<long long>& prefix, int L, int R) {
    // Because of 1-based indexing, we map 0-indexed L and R to 1-indexed.
    // L_1based = L + 1, R_1based = R + 1
    // Formula: prefix[R_1based] - prefix[L_1based - 1]
    // Which simplifies directly to:
    return prefix[R + 1] - prefix[L];
}

int main() {
    // Example: [3, 2, 4, 1, 5]
    vector<int> A = {3, 2, 4, 1, 5};
    
    // 1. Precompute (O(N) Time)
    vector<long long> prefix = buildPrefixSum(A);
    
    // 2. Query (O(1) Time)
    // Query range [2, 4] -> Should return 4 + 1 + 5 = 10
    int L = 2, R = 4;
    cout << "Sum of range [" << L << ", " << R << "] is: " 
         << queryRange(prefix, L, R) << "\n";
         
    return 0;
}
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   **Precomputation:** $O(N)$ to iterate through the array once and build the prefix sums.
    *   **Query:** $O(1)$. It's a single mathematical subtraction.
    *   **Total Time:** $O(N + Q)$ for $Q$ queries, drastically outperforming the naive $O(N \times Q)$.
*   **Space Complexity:** $O(N)$ auxiliary space to store the prefix sum array.

> 🚨 **The Systems Trap: Static vs. Dynamic Data**
> Prefix Sums are mathematically beautiful, but they have a fatal flaw: they only work efficiently on **Static Data**. If a system introduces an `update(index, val)` function to modify the original array, Prefix Sums instantly degrade. Changing a single value at index `0` forces you to recalculate the *entire* prefix sum array, making updates $O(N)$. If your data is dynamic (frequent updates), you must abandon Prefix Sums and use a **Segment Tree** or a **Fenwick Tree (Binary Indexed Tree)**.

## 4. Module Summary
- Recalculating the same data for overlapping ranges is a massive performance leak. 
- **Prefix Sums** utilize $O(N)$ precomputation space to reduce range queries to strictly $O(1)$ time complexity.
- By utilizing a $0$-padded `N+1` array (the **1-Based Indexing trick**), we eliminate edge cases and out-of-bounds errors, writing cleaner, branchless code.
- Always use `long long` for Prefix Sums, as accumulating $10^5$ elements can easily overflow a standard 32-bit integer!

> 💡 **Elite CP Insight: The Difference Array**
> If a Prefix Sum solves $O(1)$ Range Queries but requires $O(N)$ updates, what solves $O(1)$ Range Updates (e.g., "Add $X$ to all elements from $L$ to $R$") but allows point queries? The mathematical inverse of the Prefix Sum: **The Difference Array**. Mentioning this inverse relationship during an interview proves a senior-level understanding of array mathematics!

</READING_WIDGET>
