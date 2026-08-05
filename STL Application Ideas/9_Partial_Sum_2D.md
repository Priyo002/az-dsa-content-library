<VIDEO_WIDGET>

<VIDEO_ID>71</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Range Updates: 2D Partial Sums (2D Difference Array)

> *Updating regions of a massive 2D matrix—like applying filters in image processing or modifying spawn zones in a game engine—is a computationally devastating task. The 2D Partial Sum technique elevates the 1D Difference Array into two dimensions, allowing us to drop 4 geometric markers and update millions of cells in strict $O(1)$ time.*

---

## 1. The Challenge: Rectangular Updates

**Problem Statement:** 
You are given a 2D matrix of dimensions $N \times M$, initially filled with zeros. 
You must process $Q$ queries of the form `+ U D L R X`. Each query demands that you add the value `X` to every single cell within the rectangle bounded by the top row `U`, bottom row `D`, left column `L`, and right column `R`. After all $Q$ queries, output the final matrix.

### The Naive $O(N \times M \times Q)$ Approach
The standard approach is a nested loop traversing from row `U` to `D`, and column `L` to `R`, physically adding `X` to each cell. 
If the matrix is $1000 \times 1000$, a single query covering the whole matrix takes $1,000,000$ operations. If you have $100,000$ queries, the system will attempt $10^{11}$ operations, instantly melting the server and triggering a **Time Limit Exceeded (TLE)**.

We need to apply these massive 2D updates in $O(1)$ time.

---

## 2. The $O(1)$ Architecture: 2D Difference Array

In a 1D Difference Array, we dropped a `+X` start marker and a `-X` stop marker. 
In 2D geometry, the region expands both horizontally and vertically. Therefore, we must drop **four markers** to perfectly bound the rectangular region!

### The 4-Marker Mechanic
To add `X` to the region from `(U, L)` to `(D, R)`:
1. **The Origin:** We drop `+X` at `(U, L)`. This tells the matrix to start adding `X` from this point downwards and rightwards.
2. **The Horizontal Cutoff:** We drop `-X` at `(U, R + 1)`. This stops the addition from bleeding past the right edge of our rectangle.
3. **The Vertical Cutoff:** We drop `-X` at `(D + 1, L)`. This stops the addition from bleeding past the bottom edge of our rectangle.
4. **The Intersection Correction:** Both cutoffs will propagate downwards and rightwards. This means the region past `(D+1, R+1)` receives *two* `-X` waves. To correct this over-subtraction, we must add the intersection back! We drop `+X` at `(D + 1, R + 1)`.

All four marker drops are instantaneous $O(1)$ assignments.

### The Resolution Phase
After dropping markers for all $Q$ queries, the matrix looks like a scattered mess of coordinates. 
To resolve it into the final array, we simply perform a **Standard 2D Prefix Sum Sweep** across the entire matrix. The sweep will perfectly carry the `+X` waves across the intended rectangles, while the `-X` and `+X` cutoffs perfectly neutralize the waves everywhere else!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/22520326-ee83-4249-b3c0-121da5d6f2e8.jpg" alt="2D Partial Sum Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **Elite CP Insight: Populated Matrices Overlay Trick**
> If your starting grid already has values (like a pre-existing terrain map), building the true 2D Difference Array mathematically via `D[i][j] = A[i][j] - A[i-1][j] - A[i][j-1] + A[i-1][j-1]` is tedious and highly prone to indexing typos. 
> Instead of doing that math, elite programmers use the **Overlay Trick**:
> 1. Initialize your Difference Array `diff` with all zeros.
> 2. Run all your `update()` queries on it.
> 3. Call `resolve()` on the `diff` matrix to execute the Prefix Sum Sweep.
> 4. Finally, run a simple $O(N \times M)$ nested loop to add `diff[i][j]` directly to the original `A[i][j]`! 
> This bypasses the complex initialization math entirely while achieving the exact same performance.

---

## 3. The Code Implementation

> 💎 **Elite CP Insight: The Double Pad (`N+2`)**
> In the marker step, we must access `D + 1` and `R + 1`. If the update covers the absolute edges of the matrix (where $D = N$ or $R = M$), accessing `+1` causes an immediate Segmentation Fault!
> Beginners litter their code with `if (D + 1 <= N)` checks. Elite programmers entirely eliminate the branches by sizing the matrix to `(N + 2) \times (M + 2)`. This creates a safe "garbage boundary" on the right and bottom edges, guaranteeing that the `+1` markers always land safely in memory!

```cpp
#include <iostream>
#include <vector>

using namespace std;

class PartialSum2D {
private:
    vector<vector<long long>> diff;
    int n, m;

public:
    PartialSum2D(int rows, int cols) : n(rows), m(cols) {
        // We allocate (N+2) x (M+2) to safely absorb the D+1 and R+1 overflow markers!
        // We use 1-based indexing for rows 1..N and cols 1..M
        diff.assign(n + 2, vector<long long>(m + 2, 0));
    }
    
    // Time Complexity: O(1) per update
    void update(int U, int L, int D, int R, long long X) {
        // Shift 0-based query coordinates to 1-based
        U++; L++; D++; R++;
        
        // Drop the 4 Geometric Markers
        diff[U][L]         += X;
        diff[U][R + 1]     -= X;
        diff[D + 1][L]     -= X;
        diff[D + 1][R + 1] += X;
    }
    
    // Time Complexity: O(N * M) to resolve
    void resolve() {
        // Perform a standard 2D Prefix Sum Sweep to propagate the markers
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                diff[i][j] += diff[i - 1][j] 
                            + diff[i][j - 1] 
                            - diff[i - 1][j - 1];
            }
        }
    }
    
    // Helper to print the resolved matrix
    void printMatrix() {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                cout << diff[i][j] << " ";
            }
            cout << "\n";
        }
    }
};

int main() {
    int N = 4, M = 4;
    PartialSum2D matrix(N, M);

    // Simulated Queries
    // Add 5 to rectangle (0,0) -> (2,2)
    matrix.update(0, 0, 2, 2, 5);
    
    // Add -2 to rectangle (1,1) -> (3,3)
    matrix.update(1, 1, 3, 3, -2);
    
    // Add 10 to rectangle (0,3) -> (2,3)
    matrix.update(0, 3, 2, 3, 10);

    // 1. Process all queries instantly in O(1) time
    // ... all updates are already dropped!
    
    // 2. Resolution Phase
    matrix.resolve();
    
    cout << "Final Resolved Matrix:\n";
    matrix.printMatrix();

    return 0;
}
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   **Query Processing:** $O(1)$ per query. For $Q$ queries, it takes strictly $O(Q)$ time.
    *   **Resolution Phase:** $O(N \times M)$ for the final 2D Cumulative Sum sweep.
    *   **Total Time:** $O(Q + N \times M)$.
*   **Space Complexity:** $O(N \times M)$ auxiliary space to store the padded 2D Difference Array.

## 4. Module Summary
- The **2D Difference Array** technique allows us to update massive rectangular grids in $O(1)$ time by dropping $4$ interacting markers (`+`, `-`, `-`, `+`).
- The markers are completely resolved by executing a standard **2D Prefix Sum Sweep**, which propagates the additions while allowing the cutoffs to perfectly neutralize the overlapping waves.
- By sizing the array to `N+2` and `M+2`, we safely absorb the right and bottom cutoff markers, completely eliminating $O(Q)$ `if` statement boundaries.

> 🚨 **The CP Trap: Offline vs. Online Queries**
> Just like its 1D counterpart, the 2D Difference Array is an **Offline Algorithm**. You must collect *all* updates first, and resolve them at the very end. If a problem mixes updates and queries together (e.g., Update Range, Query Cell, Update Range), this method fails because resolving the matrix takes $O(N \times M)$ time per query! For Online mixed queries on grids, you must build a **2D Segment Tree** or a **2D Binary Indexed Tree (Fenwick Tree)**.

</READING_WIDGET>
