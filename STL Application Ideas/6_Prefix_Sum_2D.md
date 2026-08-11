<VIDEO_WIDGET>

<VIDEO_ID>72</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Range Queries: 2D Prefix Sums

> *Image processing, heatmaps, and spatial data analytics all require incredibly fast operations on 2D matrices. If a system takes $O(N \times M)$ time to analyze a region of a grid, the system is dead on arrival. 2D Prefix Sums elevate our 1D logic into a geometric masterclass.*

---

## 1. The Challenge: Rectangular Queries

**Problem Statement:** 
You are given a 2D matrix of dimensions $N \times M$. You must answer $Q$ queries of the form `? U L D R`, asking for the sum of all elements inside the rectangle defined by the Top-Left corner `(U, L)` and the Bottom-Right corner `(D, R)`.

### The Naive $O(N \times M)$ Approach
The beginner approach is to use a nested `for` loop, iterating through every row from `U` to `D` and every column from `L` to `R`. 
If you are querying a massive matrix (like a $4000 \times 4000$ 4K image heatmap) thousands of times a second, these nested loops will instantly trigger a **Time Limit Exceeded (TLE)**. We need a way to sum millions of cells in strict $O(1)$ time.

---

## 2. The $O(1)$ Architecture: Inclusion-Exclusion

Just like in 1D, we precompute a `Prefix Sum Matrix`. 
`P[i][j]` stores the sum of all elements in the rectangle starting from the absolute top-left `(0, 0)` down to `(i, j)`.

### Building the 2D Prefix Array
To calculate `P[i][j]`, we don't need to re-sum everything. We use the **Principle of Inclusion-Exclusion**:
1. Take the current cell value: `Arr[i][j]`.
2. Add the rectangle above it: `P[i-1][j]`.
3. Add the rectangle to its left: `P[i][j-1]`.
4. Wait! We just added the top-left diagonal region *twice*! We must subtract it once to correct the math: `- P[i-1][j-1]`.

Formula: `P[i][j] = Arr[i][j] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]`

### Querying an Arbitrary Rectangle
When asked for the sum inside `(U, L)` to `(D, R)`, we use the exact same geometry in reverse:
1. Start with the massive rectangle from `(0,0)` to `(D, R)`: `P[D][R]`.
2. Chop off the extra region directly above our target: `- P[U-1][R]`.
3. Chop off the extra region directly to the left of our target: `- P[D][L-1]`.
4. We just chopped off the top-left intersection *twice*! We must add it back to correct the math: `+ P[U-1][L-1]`.

Formula: `Sum = P[D][R] - P[U-1][R] - P[D][L-1] + P[U-1][L-1]`

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7df89a3c-4462-4f27-b0a9-b3fc84a2795d.jpg" alt="2D Prefix Sum Inclusion Exclusion Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

> 💎 **Elite CP Insight: Eradicating Branches**
> Standard implementations are plagued by `if (i > 0)` and `if (L > 0)` checks to prevent out-of-bounds errors on the `i-1` accesses. 
> Elite programmers use the **1-Based Indexing Trick**. By padding the 2D array with an extra row at the top and an extra column at the left (all initialized to `0`), we guarantee that `i-1` and `j-1` are always valid memory addresses. This eliminates all `if` statements, allowing branch predictor hardware to run at maximum velocity!

```cpp
#include <iostream>
#include <vector>

using namespace std;

class PrefixSum2D {
private:
    // We use long long to prevent massive cumulative sums from overflowing 32-bit limits.
    vector<vector<long long>> P;

public:
    // Time Complexity: O(N * M) to build
    PrefixSum2D(const vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return;
        
        int n = matrix.size();
        int m = matrix[0].size();
        
        // Allocate (N+1) x (M+1) to utilize the 1-Based Indexing Trick
        // Row 0 and Col 0 remain entirely 0.
        P.assign(n + 1, vector<long long>(m + 1, 0));
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                // i+1 and j+1 are the 1-based coordinates
                // We add matrix[i][j] (0-based) to the geometric bounding boxes
                P[i + 1][j + 1] = matrix[i][j] 
                                + P[i][j + 1] 
                                + P[i + 1][j] 
                                - P[i][j];
            }
        }
    }
    
    // Time Complexity: O(1) per query
    long long query(int U, int L, int D, int R) {
        // Shift the 0-based query coordinates to our 1-based Prefix Matrix
        U++; L++; D++; R++;
        
        // Strict O(1) Inclusion-Exclusion geometry
        return P[D][R] 
             - P[U - 1][R] 
             - P[D][L - 1] 
             + P[U - 1][L - 1];
    }
};

int main() {
    vector<vector<int>> matrix = {
        {3, 0, 1, 4, 2},
        {5, 6, 3, 2, 1},
        {1, 2, 0, 1, 5},
        {4, 1, 0, 1, 7},
        {1, 0, 3, 0, 5}
    };

    // 1. Build Phase (O(N * M))
    PrefixSum2D prefix2D(matrix);

    // 2. Query Phase (O(1))
    // Querying the subgrid from (Top-Left: 1, 1) to (Bottom-Right: 2, 2)
    // Values: {6, 3} + {2, 0} = 11
    int result = prefix2D.query(1, 1, 2, 2);
    
    cout << "Sum in the rectangle: " << result << "\n";

    return 0;
}
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   **Precomputation:** $O(N \times M)$. We iterate through the matrix exactly once.
    *   **Query:** $O(1)$. It requires exactly $4$ array lookups and $3$ arithmetic operations.
    *   **Total Time:** $O(N \times M + Q)$.
*   **Space Complexity:** $O(N \times M)$ auxiliary space to store the padded 2D Prefix Sum matrix.

## 4. Module Summary
- The **Principle of Inclusion-Exclusion** is the mathematical foundation for fast 2D geometry calculations, allowing us to find intersecting area sums by adding/subtracting overlapping bounding boxes.
- Padding the matrix by $+1$ dimension on the top and left allows us to completely eradicate $O(N \times M)$ branch-prediction checks (`if (i > 0)`).
- This architecture scales effortlessly to spatial rendering engines, financial heatmaps, and massive geospatial data analytics.

</READING_WIDGET>
