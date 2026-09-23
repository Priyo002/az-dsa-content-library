<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# 0–1 BFS Application: Minimum Wind Changes

A grid problem may look like a simulation, but choosing the right **edge cost** can turn it into a shortest-path problem.

Here, moving with the wind is free. Moving in another direction requires changing the wind in the cell we are leaving, which costs 1. These two possible costs let us use 0–1 BFS.

## 1. Problem Statement

A traveller wants to sail across an `n × m` sea grid in his ship, Merry. Each cell contains a number describing its wind direction:

| Value | Direction | Change in row | Change in column |
| --- | --- | --- | --- |
| 1 | Right `→` | 0 | +1 |
| 2 | Left `←` | 0 | -1 |
| 3 | Down `↓` | +1 | 0 |
| 4 | Up `↑` | -1 | 0 |

The ship can leave a cell only in that cell's wind direction. You may change the direction of any cell to another of these four directions at a cost of **1 per changed cell**.

Find the minimum number of changes needed to travel from the **top-left** cell to the **bottom-right** cell, without leaving the grid.

The problem uses coordinates `(1, 1)` to `(n, m)`. The C++ code uses zero-based coordinates: `(0, 0)` to `(n - 1, m - 1)`.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/d1085eeb-e06c-4ab9-9d40-09b17410623d.png" alt="Five-row six-column sea grid with directional wind arrows, cream background, blue cells, rounded border and AlgoZenith logo" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Wind arrows may point outside the grid. Such an arrow does not permit leaving the grid; a different direction must be chosen and paid for if we need to leave that cell along a valid move.

There are no walls. With wind changes allowed, the destination is always reachable in a nonempty rectangular grid.

## 2. Model the Grid as a Directed Weighted Graph

Treat each cell as a vertex. From a cell `(x, y)`, consider an edge to each neighbour that exists: right, left, down, or up.

The cost of an edge is:

$$
w = \begin{cases}
0, & \text{if the move follows the wind at }(x,y),\\
1, & \text{otherwise.}
\end{cases}
$$

For example, if the current cell points right:

- Moving right costs 0, provided the neighbour exists.
- Moving left, down, or up costs 1, provided that neighbour exists.

### Check the Cell We Are Leaving

The crucial comparison is with **`grid[x][y]`**, not the destination cell's arrow.

The current wind determines how the ship can leave the current cell. The destination's wind matters only when the ship later leaves that destination.

Consequently, **we do not need to change the bottom-right cell's wind**: the journey ends upon reaching it.

### Why Are the Edges Directed?

Movement between adjacent cells is possible in both directions after suitable changes, but its cost can differ by direction.

Suppose two horizontally adjacent cells both point right. Moving from the left cell to the right cell costs 0. Moving back costs 1 because the right cell would need to point left.

We generate each cell's outgoing costs separately rather than assuming both directions have the same weight.

## 3. Why Does Path Cost Equal the Required Changes?

For a path without repeated cells, each cell is left at most once. Every move that disagrees with its cell's original arrow requires one change, while every matching move is free. Thus, the sum of edge costs is exactly the number of changes for that path.

All edge costs are nonnegative, so a shortest path can be chosen without repeated cells: removing a loop cannot increase its cost. We can therefore realize an optimal graph path by assigning each of its cells the direction used to leave it, with no conflicting assignments.

Conversely, any successful set of wind changes gives a route to the destination. A route without repeated cells uses at most one changed direction per visited cell, so its graph cost is no greater than the total number of changed cells. Together, these observations show that minimizing the graph's path cost gives the minimum number of wind changes.

**Do not modify `grid` while exploring.** Different candidate paths are alternatives; a change considered for one candidate must not alter the costs seen by another candidate.

## 4. Apply 0–1 BFS

Maintain `dist[x][y]`, the smallest cost found so far for reaching a cell.

1. Set every distance to `INF`, except `dist[0][0] = 0`.
2. Put `(0, 0)` in a deque.
3. Remove a cell from the front. If it is already settled, skip this duplicate entry; otherwise settle it.
4. Examine each valid neighbouring cell `(nx, ny)`.
5. Calculate the cost `w` from the current cell's wind and the direction of this move.
6. If `dist[x][y] + w` strictly improves `dist[nx][ny]`, update it:
   - Push the neighbour to the **front** if `w == 0`.
   - Push it to the **back** if `w == 1`.
7. Return `dist[n - 1][m - 1]`.

As in the previous lesson, a cell's first discovery is provisional. A later zero-cost route may improve it. Mark a cell settled when removing it for processing, **not when inserting it**.

The deque processes useful candidates in increasing total cost. A weight-0 move stays at the current cost level, while a weight-1 move belongs to the next level. Duplicate entries are skipped after their cell has been settled.

## 5. Direction Arrays and the Cost Formula

Choose the direction-array order to match the input codes exactly:

```cpp
const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};
// Direction indices: 0 = right, 1 = left, 2 = down, 3 = up.
```

For direction index `k`, the input's direction code is `k + 1`:

```cpp
int nx = x + dx[k];
int ny = y + dy[k];
int w = (grid[x][y] == k + 1) ? 0 : 1;
```

This is an equality test, not a numeric difference between direction codes. For example, changing code 1 to code 4 still costs 1, not 3.

Check boundaries before accessing the neighbour's distance or state.

## 6. Small Dry Run

Consider this `2 × 3` grid:

```text
Codes:       Arrows:
1 2 3        → ← ↓
4 1 4        ↑ → ↑
```

Use **zero-based coordinates** throughout this dry run. The source is `(0, 0)` and the destination is `(1, 2)`.

The zero-cost movement between `(0, 0)` and `(0, 1)` forms a loop. Following existing arrows alone cannot reach the destination, so at least one change is needed.

Scan neighbours in the order right, left, down, up. Deque contents below are shown front to back.

| Cell processed | Successful improvements | Deque after processing |
| --- | --- | --- |
| — | `dist[0][0] = 0` | `[(0,0)]` |
| `(0,0)` | Right to `(0,1)` costs 0; down to `(1,0)` costs 1 | `[(0,1), (1,0)]` |
| `(0,1)` | Right to `(0,2)` and down to `(1,1)` both cost 1 | `[(1,0), (0,2), (1,1)]` |
| `(1,0)` | No improvement | `[(0,2), (1,1)]` |
| `(0,2)` | Down to `(1,2)` costs 0, so its distance is 1 | `[(1,2), (1,1)]` |
| `(1,2)` | No improvement | `[(1,1)]` |
| `(1,1)` | No improvement | `[]` |

Final distances:

```text
0 0 1
1 1 1
```

One optimal route is:

```text
(0,0) -> (0,1) -> (0,2) -> (1,2)
   0         1         0          total cost = 1
```

Change the arrow at `(0,1)` from left to right. The other two moves follow their existing arrows. The destination points up, but its direction does not matter because we stop there.

## 7. Applying the Model to the Illustrated Grid

Reading the illustration row by row gives:

```text
1 3 2 1 4 1
3 3 2 3 1 4
3 4 3 2 2 2
1 4 1 3 1 4
2 4 3 4 4 1
```

The minimum cost from the top-left corner to each cell is:

```text
0 0 1 2 2 3
1 0 1 2 3 3
1 0 1 2 2 2
1 1 1 1 2 2
2 2 2 1 2 3
```

The bottom-right value is **3**. One optimal route, now using **one-based coordinates** to match the problem statement, is:

```text
(1,1) -> (1,2) -> (2,2) -> (3,2) -> (3,3)
       -> (4,3) -> (4,4) -> (4,5) -> (4,6) -> (5,6)
```

It requires these three changes:

| Cell, one-based | Original direction | Required direction |
| --- | --- | --- |
| `(3,2)` | Up, code 4 | Right, code 1 |
| `(4,4)` | Down, code 3 | Right, code 1 |
| `(4,6)` | Up, code 4 | Down, code 3 |

Every other move on this route follows the original wind. The route demonstrates a cost of 3, and the shortest-distance calculation establishes that no cheaper route exists.

## 8. Complete C++17 Implementation

### Input

- First line: positive integers `n m`.
- Next `n` lines: `m` integers each, all between 1 and 4.

### Output

Print the minimum number of wind-direction changes.

```cpp
#include <deque>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>
using namespace std;

const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};

int minCost(const vector<vector<int>>& grid) {
    int n = static_cast<int>(grid.size());
    int m = static_cast<int>(grid[0].size());
    const int INF = numeric_limits<int>::max();

    vector<vector<int>> dist(n, vector<int>(m, INF));
    vector<vector<char>> settled(n, vector<char>(m, false));
    deque<pair<int, int>> dq;

    dist[0][0] = 0;
    dq.push_front({0, 0});

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        if (settled[x][y]) continue;
        settled[x][y] = true;

        for (int k = 0; k < 4; ++k) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (settled[nx][ny]) continue;

            // Cost depends on the cell being left, not the destination.
            int w = (grid[x][y] == k + 1) ? 0 : 1;
            int candidate = dist[x][y] + w;

            if (candidate < dist[nx][ny]) {
                dist[nx][ny] = candidate;
                if (w == 0) dq.push_front({nx, ny});
                else dq.push_back({nx, ny});
            }
        }
    }

    return dist[n - 1][m - 1];
}

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> grid(n, vector<int>(m));

    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < m; ++y) cin >> grid[x][y];
    }

    cout << minCost(grid) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
```

Every enqueued cell has a finite distance, so the implementation never adds to `INF`. The function expects a nonempty rectangular grid, as specified in the input.

The grid is passed by const reference: the algorithm computes the best cost without actually changing any arrows.

## 9. Sample Runs

### Sample 1: The Small Dry Run

Input:

```text
2 3
1 2 3
4 1 4
```

Output:

```text
1
```

### Sample 2: The Illustrated Grid

Input:

```text
5 6
1 3 2 1 4 1
3 3 2 3 1 4
3 4 3 2 2 2
1 4 1 3 1 4
2 4 3 4 4 1
```

Output:

```text
3
```

### Sample 3: No Change Needed

Input:

```text
2 2
1 3
4 2
```

Output:

```text
0
```

Follow right from the top-left, then down from the top-right. The arrow at the destination does not need to change.

### Sample 4: Start Equals Destination

Input:

```text
1 1
4
```

Output:

```text
0
```

No movement is required, even though the arrow points outside the grid.

## 10. Complexity

There are `V = n × m` vertices and at most four outgoing edges per cell, so `E = O(n × m)`.

- Each cell is settled once and examines at most four directions.
- Only successful relaxations insert entries into the deque.
- Duplicate removals are skipped without scanning the cell's neighbours again.

Therefore:

- **Time:** `O(V + E) = O(n × m)`.
- **Space:** `O(n × m)` for distances, settled flags, and the deque.

The graph is implicit: neighbours are generated from coordinates, so no adjacency list is needed.

A standard binary-heap implementation of Dijkstra's algorithm would also work, with `O(n × m × log(n × m))` time for this grid. The restriction to weights 0 and 1 allows the simpler linear-time deque approach.

## 11. Common Mistakes and Useful Checks

- **Looking at the destination's arrow:** compare the move with `grid[x][y]`, the cell being left.
- **Following only the existing arrow:** consider all four valid moves; the other directions are allowed at cost 1.
- **Wrong direction-array order:** `k + 1` must match right, left, down, up exactly.
- **Charging for the destination:** no departure is needed from the bottom-right cell.
- **Changing arrows during BFS:** keep the original grid unchanged while evaluating alternative routes.
- **Marking visited on discovery:** a discovered cell's tentative cost can still improve.
- **Enqueuing equal-cost routes:** use strict improvement, not `<=`, to avoid unnecessary repeated work around zero-cost loops.
- **Confusing minimum cost with minimum moves:** an optimal route can be longer in steps while changing fewer arrows.

For a single-destination optimization, you may return when the destination is removed as an unsettled cell and finalized, but **not when it is first inserted**.

Useful sanity checks:

- A `1 × 1` grid always has answer 0.
- In a single row, only the first `m - 1` cells need to point right; count how many do not.
- In a single column, only the first `n - 1` cells need to point down; count how many do not.
- For any grid, `0 <= answer <= n + m - 2`: a route using only right and down takes that many steps and needs at most one change per step.

## Quick Recap

- Each cell is a vertex, and each valid move is a directed edge.
- Following the current cell's wind costs 0; changing it costs 1.
- Use relaxation and a deque: cost 0 to the front, cost 1 to the back.
- Keep the input grid unchanged and settle cells on removal.
- The destination's shortest-path cost equals the minimum number of wind changes.

</READING_WIDGET>
