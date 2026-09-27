<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Shortest Path Idea 1: Minimum Walls to Break

A shortest path does not always mean the fewest moves. Sometimes we want to minimize a different quantity, such as the number of obstacles removed.

The key is to assign an edge cost that measures exactly what the problem asks us to minimize.

## 1. Problem Statement

You are given an `n × m` rectangular grid containing:

| Symbol | Meaning |
| --- | --- |
| `.` | Empty cell; entering it is free |
| `#` | Wall; break it to enter, at a cost of 1 |
| `S` | Starting cell |
| `E` | Ending cell |

There is exactly one `S` and one `E`. From a cell, you may move **up, down, left, or right**, as long as you remain inside the grid. Diagonal movement is not allowed.

Find the **minimum number of wall cells that must be broken** to create a route from `S` to `E`.

Entering `S`, `E`, or `.` costs zero. Every `#` can be broken; there are no permanently impassable cells and no fixed wall-breaking budget. Consequently, a route always exists in a valid rectangular grid after breaking enough walls.

## 2. Turn the Grid into a Weighted Graph

### Vertices and Edges

- Each cell is a vertex, including wall cells.
- A move to an in-bounds orthogonal neighbour is an edge.
- Generate neighbours when needed; there is no need to build an adjacency list explicitly.

Unlike the earlier grid problem with impassable obstacles, **do not reject a neighbour because it contains `#`**. It is a valid move with a cost.

### Charge for the Destination Cell

For a move from `(x, y)` to `(nx, ny)`, assign:

$$
w = \begin{cases}
1, & \text{if } \operatorname{grid}[nx][ny] = \texttt{\#},\\
0, & \text{otherwise.}
\end{cases}
$$

In code:

```cpp
int cost = (grid[nx][ny] == '#') ? 1 : 0;
```

We are paying to enter the next cell, so we inspect the **destination**, not the current cell. This differs from the wind-direction problem, where a move's cost depended on the cell being left.

Although movement is possible in both directions, the edge costs need not be equal. Moving from `.` into `#` costs 1, whereas moving from that `#` back into `.` costs 0. Generate outgoing costs separately for each cell.

## 3. Why Does This Count Walls Correctly?

For a route without repeated cells, each wall is entered at most once. Its total edge cost is exactly the number of wall cells on that route.

What about a wall that has already been broken? Would entering it again incorrectly charge another unit?

We do not need such a route to obtain an optimum:

1. All graph edge costs are nonnegative, so removing a loop cannot increase a route's cost. A minimum-cost graph route can be chosen without repeated cells.
2. Break the walls on that simple route. This realizes the route using exactly its graph cost in wall breaks.
3. Conversely, any successful set of broken walls gives a route from `S` to `E`. Remove loops from that route; the resulting simple route uses no more walls than were broken.

Therefore, minimizing the graph's total edge cost gives exactly the minimum number of distinct walls that must be broken.

**Do not modify the grid during exploration.** Different candidate routes are alternatives. Treating a wall considered by one candidate as already broken for another would mix their costs. A distance per cell is sufficient; no “set of broken walls” is needed in the algorithm's state.

## 4. Choose the Algorithm: 0–1 BFS

Every edge has weight either `0` or `1`, so this is a direct application of **0–1 BFS**.

- Ordinary BFS minimizes the number of moves when every move has equal cost. That is not our objective here.
- Dijkstra also works, but its heap should prioritize the **total cost from `S`**, not just whether the next cell is a wall.
- A deque lets 0–1 BFS maintain the required distance order in linear time.

Maintain `dist[x][y]`, the smallest number of wall breaks found so far to reach `(x, y)`.

For a neighbour `(nx, ny)`, try:

$$
\text{candidate} = \operatorname{dist}[x][y] + w.
$$

Only if this candidate is strictly smaller than `dist[nx][ny]`, update the distance and enqueue the neighbour:

| Cost of the move | Deque operation | Reason |
| --- | --- | --- |
| `0` | `push_front` | The candidate stays at the current distance level |
| `1` | `push_back` | The candidate belongs to the next distance level |

The front/back rule depends on the **edge weight**, while the distances represent **cumulative wall breaks**. An empty cell can still have distance 2 if reaching it requires crossing two walls first.

### Processing Steps

1. Set all distances to `INF` and all settled flags to false.
2. Set the source distance to zero and put `S` at the front of the deque.
3. Pop a cell from the front. Skip it if already settled; otherwise settle it.
4. Inspect its four possible neighbours, checking boundaries.
5. Compute each move's cost from the destination cell and relax its distance.
6. Push improved candidates to the front for cost 0, or the back for cost 1.
7. The answer is `dist[E]`.

We use the standard 0–1 BFS rule of settling a cell on its first **removal**, not on insertion. The deque prioritizes the smallest unsettled distance, so that distance is final when the cell is settled. Later duplicate entries are skipped before scanning neighbours.

The implementation computes the whole distance matrix to match the diagram. If only the answer is needed, it can stop when `E` is settled—not merely when `E` is first inserted as a candidate under the general 0–1 BFS framework.

## 5. Dry Run on the Illustrated Grid

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/8ba414da-9edb-4ce6-b84b-350fe46c5940.png" alt="Six-by-five grid with S in row 2 column 2 and E in row 6 column 2, followed by the minimum-wall-break distance matrix showing answer 2; AlgoZenith logo and rounded border" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The top grid is:

```text
####.
.S#..
#...#
#####
#####
#E..#
```

Use **1-based coordinates** in this explanation: `S = (2, 2)` and `E = (6, 2)`. The code uses zero-based coordinates.

### First Expansion from `S`

With neighbour order down, up, right, left:

| Neighbour | Cell | Candidate distance | Operation |
| --- | --- | --- | --- |
| `(3, 2)` | `.` | 0 | Push to front |
| `(1, 2)` | `#` | 1 | Push to back |
| `(2, 3)` | `#` | 1 | Push to back |
| `(2, 1)` | `.` | 0 | Push to front |

After expanding `S`, the deque is:

```text
Front -> (2,1):0, (3,2):0, (1,2):1, (2,3):1 <- Back
```

The numbers after `:` are current wall-breaking distances. Free moves continue to be explored before any candidate requiring one wall break.

### Follow One Optimal Route

The following table shows one route's costs, not the complete deque-processing order:

| Move | Destination | Additional walls | Total walls |
| --- | --- | --- | --- |
| Start | `(2, 2)` = `S` | 0 | 0 |
| Down | `(3, 2)` = `.` | 0 | 0 |
| Down | `(4, 2)` = `#` | 1 | 1 |
| Down | `(5, 2)` = `#` | 1 | 2 |
| Down | `(6, 2)` = `E` | 0 | 2 |

This shows that two breaks are sufficient. They are also necessary: rows 4 and 5 consist entirely of walls, and any route from row 2 to row 6 must enter at least one cell in each of those rows. Thus, the optimum is **2**.

### Final Distance Matrix

```text
1 1 2 1 0
0 0 1 0 0
1 0 0 0 1
2 1 1 1 2
3 2 2 2 3
3 2 2 2 3
```

This matches all 30 entries in the image's lower grid. Each number counts walls broken, **not moves taken**. For example, the top-right cell has distance 0 because it is reachable through empty cells, even though it is not adjacent to `S`.

## 6. Complete C++17 Implementation

### Input and Output Used Here

Input contains `n m`, followed by `n` strings of length `m`. Assume a nonempty rectangular grid with exactly one `S` and one `E` and only the four allowed symbols.

Print one integer: the minimum number of walls to break.

Distances use `int`; the implementation assumes `n × m < INT_MAX`. A simple route visits at most `n × m` cells, so its wall count fits this bound. No arithmetic is performed on `INF`, because only cells with finite distances enter the deque.

```cpp
#include <deque>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int INF = numeric_limits<int>::max();
const int dx[4] = {1, -1, 0, 0};
const int dy[4] = {0, 0, 1, -1};

vector<vector<int>> zeroOneBfs(
    const vector<string>& grid, pair<int, int> source
) {
    int n = static_cast<int>(grid.size());
    int m = static_cast<int>(grid[0].size());

    vector<vector<int>> dist(n, vector<int>(m, INF));
    vector<vector<char>> settled(n, vector<char>(m, false));
    deque<pair<int, int>> dq;

    auto [sx, sy] = source;
    dist[sx][sy] = 0;
    dq.push_front({sx, sy});

    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();

        if (settled[x][y]) continue;
        settled[x][y] = true;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (settled[nx][ny]) continue;

            // Walls are valid destinations, but entering them costs 1.
            int cost = (grid[nx][ny] == '#') ? 1 : 0;
            int candidate = dist[x][y] + cost;

            if (candidate < dist[nx][ny]) {
                dist[nx][ny] = candidate;
                if (cost == 0) dq.push_front({nx, ny});
                else dq.push_back({nx, ny});
            }
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    pair<int, int> source = {-1, -1};
    pair<int, int> target = {-1, -1};

    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'S') source = {i, j};
            if (grid[i][j] == 'E') target = {i, j};
        }
    }

    vector<vector<int>> dist = zeroOneBfs(grid, source);
    cout << dist[target.first][target.second] << '\n';
}
```

### Sample 1: The Illustrated Grid

Input:

```text
6 5
####.
.S#..
#...#
#####
#####
#E..#
```

Output:

```text
2
```

### Sample 2: More Moves Can Mean Fewer Wall Breaks

Input:

```text
2 5
S###E
.....
```

Output:

```text
0
```

Going straight along the top row takes 4 moves but breaks 3 walls. Going down, across the bottom row, and back up takes 6 moves and breaks none. The second route is optimal for this objective.

### Sample 3: Every Intermediate Cell Is a Wall

Input:

```text
1 5
S###E
```

Output:

```text
3
```

All three walls must be crossed. Entering `E` does not add another unit.

## 7. Complexity

The implicit graph has `V = n × m` vertices and at most `4nm` directed movement edges.

- **Time: `O(V + E) = O(nm)`**. Each cell is settled once and its at most four neighbours are scanned once. Strict improvements generate at most `O(E)` deque entries, including any duplicates.
- **Auxiliary space: `O(nm)`** for distances, settled flags, and the deque. The grid itself also occupies `O(nm)` space.

## 8. Common Mistakes

- **Treating `#` as impassable:** walls are allowed destinations with cost 1.
- **Charging for the current cell:** inspect the cell being entered.
- **Charging for `S` or `E`:** only `#` has cost 1.
- **Using ordinary BFS to minimize moves:** it does not minimize a mixture of zero-cost and one-cost moves.
- **Prioritizing only the next cell's type in a heap:** Dijkstra would need the cumulative distance as its priority.
- **Enqueuing without a strict improvement:** zero-cost cycles can cause repeated useless work.
- **Changing a wall to `.` during exploration:** this incorrectly shares one candidate route's wall break with other candidates.

The formulation to remember is: **cell = vertex, move = edge, wall entered = cost 1; all other moves = cost 0.** Once these costs are defined, 0–1 BFS solves the problem directly.

</READING_WIDGET>
