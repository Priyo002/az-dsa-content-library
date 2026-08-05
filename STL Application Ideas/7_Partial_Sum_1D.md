<VIDEO_WIDGET>

<VIDEO_ID>79</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Range Updates: 1D Partial Sums (Difference Array)

> *If Prefix Sums are the ultimate weapon for $O(1)$ Range Queries on static data, Partial Sums (often called the **Difference Array** technique) are the ultimate weapon for $O(1)$ Range Updates. Mastering both gives you complete control over 1D array manipulation.*

---

## 1. The Challenge: Sub-Array Updates

**Problem Statement:** 
You are given an array of size `N`, initially filled with zeros. You must process `Q` queries of the form `+ L R X`. Each query demands that you add the value `X` to every single element in the range `[L, R]` (inclusive). After all `Q` queries are processed, output the final array.

### The Naive $O(N \times Q)$ Approach
The standard approach is to use a `for` loop from `L` to `R`, physically adding `X` to each element. 
If $N = 10^5$ and $Q = 10^5$, and a query asks us to add to the range `[1, 100000]`, a single query takes $10^5$ operations. Processing all queries will take $10^{10}$ operations, resulting in an immediate **Time Limit Exceeded (TLE)**. 

We must find a way to apply a range update in strictly $O(1)$ time.

---

## 2. The $O(1)$ Architecture: The Difference Array

Instead of iterating through the range `[L, R]`, what if we just drop a "marker" at the start of the range, and another "marker" at the end to tell the system to stop? This is the core concept of a **Difference Array** (or Partial Sum array).

> 🚨 **The Systems Trap: Initializing Populated Arrays**
> The standard tutorial assumes the array starts with all zeros. But what if the initial array already has values, like `A = [3, 2, 4]`? 
> Beginners will create a separate "update overlay" array, run the prefix sum on it, and then run a second loop to add it to `A`. 
> But the mathematical definition of a Difference Array `D` is literally: **`D[i] = A[i] - A[i-1]`**. 
> If you initialize your Difference Array using this exact formula from the start, the exact same `+X` and `-X` logic works perfectly, and the final Prefix Sum sweep instantly reconstructs the fully updated array in a single pass!

### The Marker Mechanic
When tasked with adding `X` to the range `[L, R]`:
1. We go to index `L` and add `X`. This acts as a marker: *"Start adding X from here."*
2. We go to index `R + 1` and subtract `X`. This acts as the cutoff marker: *"Stop adding X from here onwards."*

Both of these operations are strictly $O(1)$!

### The Resolution Phase (Prefix Sum)
After processing all $Q$ queries by dropping $O(1)$ markers, the array looks like a chaotic mess of positive and negative numbers. How do we retrieve the actual final values?
We perform a single **Cumulative Prefix Sum** sweep from left to right. 
As the prefix sum sweeps across the array, it picks up the `+X` marker at `L` and carries it across the target range. When it hits the `-X` marker at `R+1`, they cancel out to $0$, perfectly neutralizing the addition for the rest of the array!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/f38bd718-4fce-43dc-adab-0f034acdaabe.jpg" alt="1D Partial Sum Difference Array Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

> 💎 **Elite CP Insight: Branchless `R + 1`**
> In the marker step, we must subtract `X` at index `R + 1`. If $R$ is the very last element of the array ($N$), then $R + 1$ is out of bounds! Beginners handle this by writing an `if (R + 1 <= N)` safety check.
> Elite programmers eliminate the branch entirely by sizing the array to `N + 2`. This guarantees that `R + 1` always safely resolves inside allocated memory, making the code faster and cleaner!

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    // Example: Array of size 5, with 3 queries.
    int N = 5;
    int Q = 3;
    
    // We allocate N + 2 to support 1-based indexing AND the R+1 marker seamlessly.
    // Index 0 is unused. Indices 1 through N are our target array. Index N+1 is for the overflow marker.
    vector<long long> diff(N + 2, 0);

    // Simulated Queries
    // Query 1: Add 10 to range [2, 4]
    // Query 2: Add 5 to range [1, 3]
    // Query 3: Add -2 to range [1, 5]
    vector<vector<int>> queries = {
        {2, 4, 10},
        {1, 3, 5},
        {1, 5, -2}
    };

    // 1. Process all queries in O(1) time each
    for (auto& q : queries) {
        int L = q[0];
        int R = q[1];
        int X = q[2];

        // Drop the Start Marker
        diff[L] += X;
        
        // Drop the End Marker (Safely guaranteed to exist due to N + 2 sizing)
        diff[R + 1] -= X;
    }

    // 2. Resolution Phase: Sweep the array with a Prefix Sum
    for (int i = 1; i <= N; ++i) {
        diff[i] += diff[i - 1];
    }

    // Print the final array
    cout << "Final Array: ";
    for (int i = 1; i <= N; ++i) {
        cout << diff[i] << " ";
    }
    cout << "\n";

    return 0;
}
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   **Query Processing:** $O(1)$ per query. For $Q$ queries, it takes $O(Q)$ time.
    *   **Resolution Phase:** $O(N)$ for the final cumulative prefix sum sweep.
    *   **Total Time:** $O(N + Q)$. This is vastly superior to the naive $O(N \times Q)$ approach.
*   **Space Complexity:** $O(N)$ auxiliary space for the difference array.

## 4. Module Summary
- Repeatedly iterating over ranges to update values causes massive performance bottlenecks.
- The **Partial Sum / Difference Array** technique allows us to perform range updates in $O(1)$ time by dropping start and end markers (`+X` at `L`, and `-X` at `R+1`).
- The markers are resolved into their true final values using a single $O(N)$ **Prefix Sum** sweep at the very end.
- By sizing our array to `N + 2` and using 1-based indexing, we avoid all Out-Of-Bounds errors and `if` statement branches.

</READING_WIDGET>
