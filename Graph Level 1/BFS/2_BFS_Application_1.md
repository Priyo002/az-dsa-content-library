<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# BFS Application: Pathfinding in a Grid with Obstacles

In the previous lesson, BFS found shortest distances in an unweighted graph. A grid with movement rules is another way to describe such a graph—even when the input does not contain an explicit edge list.

We will use BFS to determine whether a destination is reachable, find the minimum number of moves, and reconstruct one shortest path.

## 1. Problem Statement

You are given a grid with \(n\) rows and \(m\) columns. Each cell contains one of these characters:

| Character | Meaning |
| --- | --- |
| `#` | Wall: movement into this cell is not allowed. |
| `.` | Open cell. |
| `S` | Starting cell. |
| `E` | Destination cell. |

Assume the grid is nonempty and rectangular, with exactly one `S` and one `E`.

From a cell, you may move **down, up, right, or left** if the destination is inside the grid and is not a wall. Diagonal moves are not allowed. Every move costs one step.

Find:

1. Whether a path exists from `S` to `E`.
2. The minimum number of steps if it exists.
3. One shortest path, written as a sequence of cell coordinates.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/aa120a82-91e8-4546-b645-5b29956a8dde.png" alt="Six-row, five-column obstacle grid with S at zero-based coordinate (1,1) and E at (5,0)" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The illustrated grid is:

```text
##.#.
.S.#.
.#...
##.#.
.##..
E....
```

We use **zero-based coordinates** `(row, column)`, with rows increasing downward and columns increasing to the right. Thus, `S` is at `(1, 1)` and `E` is at `(5, 0)`.

Here, \(m\) means the number of **columns**, not the number of edges as in the previous graph examples.

## 2. Representing the Grid as a Graph

Think of each traversable cell—`.`, `S`, or `E`—as a vertex. Two vertices share an edge when a legal move takes us between their cells.

Walls are **not traversable vertices** in this model. They remain in the input matrix so that we can reject moves into them.

There is no need to build an adjacency list for every cell. We can generate neighbours directly from the movement rules whenever BFS processes a cell. This is an **implicit graph**: the edges are determined by the grid rather than stored separately.

### Four Direction Vectors

For a current cell `(x, y)`, pair corresponding entries of these arrays:

```cpp
const vector<int> dx = {1, -1, 0, 0};
const vector<int> dy = {0, 0, 1, -1};
```

| Direction | Change in row | Change in column | Candidate cell |
| --- | --- | --- | --- |
| Down | +1 | 0 | `(x + 1, y)` |
| Up | -1 | 0 | `(x - 1, y)` |
| Right | 0 | +1 | `(x, y + 1)` |
| Left | 0 | -1 | `(x, y - 1)` |

A candidate `(xx, yy)` is a valid neighbour only if:

$$
0 \leq xx < n,\qquad 0 \leq yy < m,
\qquad \text{arr}[xx][yy] \ne \texttt{'#'}
$$

Check the boundaries **before** accessing `arr[xx][yy]`. Both `S` and `E` are traversable, so checking only for `'.'` would be incorrect.

Also distinguish two questions: **Is the move legal?** checks boundaries and walls; **has the destination already been discovered?** checks the visited matrix.

## 3. Applying BFS

All legal moves cost one step, so BFS explores cells in increasing shortest distance from `S`.

Maintain three matrices:

- `vis[x][y]`: whether the cell has been discovered; initially 0.
- `dis[x][y]`: its shortest distance from `S`; initially -1.
- `par[x][y]`: the cell from which it was first discovered; initially `(-1, -1)`.

The queue stores **coordinates only**. Distances are already available in `dis`, so they do not need to be stored again in each queue entry.

### Initialize

Find `S` and `E` while reading the grid. Mark `S` as visited, assign distance 0, and add it to the queue.

### Expand a Cell

After removing `(x, y)` from the queue, generate its valid neighbours. For each unvisited neighbour `(xx, yy)`:

```cpp
vis[xx][yy] = 1;
dis[xx][yy] = dis[x][y] + 1;
par[xx][yy] = {x, y};
q.push({xx, yy});
```

Mark the cell **when adding it to the queue**, not when removing it. Multiple nearby cells may otherwise add the same destination more than once.

Record the parent only on first discovery. BFS's first route to a cell is already shortest, and the parent records the preceding cell on that route.

### Finish

The implementation below processes all cells reachable from `S`:

- If `dis[E] == -1`, no path exists.
- Otherwise, `dis[E]` is the minimum number of moves, and we can follow parents to reconstruct a shortest path.

## 4. Dry Run on the Illustrated Grid

Use the direction order **down, up, right, left**, as defined above.

At `S = (1, 1)`, the downward and upward cells are walls. BFS therefore discovers `(1, 2)` first and `(1, 0)` second, both at distance 1.

The next layer contains `(2, 2)`, `(0, 2)`, and `(2, 0)`. Some branches end at walls, but BFS continues with the other cells already waiting in the queue.

The following table groups first discoveries by distance. Coordinates within a row follow this implementation's discovery order.

| Distance | Newly discovered cells |
| --- | --- |
| 0 | `(1, 1)` |
| 1 | `(1, 2)`, `(1, 0)` |
| 2 | `(2, 2)`, `(0, 2)`, `(2, 0)` |
| 3 | `(3, 2)`, `(2, 3)` |
| 4 | `(2, 4)` |
| 5 | `(3, 4)`, `(1, 4)` |
| 6 | `(4, 4)`, `(0, 4)` |
| 7 | `(5, 4)`, `(4, 3)` |
| 8 | `(5, 3)` |
| 9 | `(5, 2)` |
| 10 | `(5, 1)` |
| 11 | `(5, 0)` — the destination `E` |
| 12 | `(4, 0)` |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/90ec1e8d-6215-49c3-a7ee-f83858931782.png" alt="Shortest-distance matrix for the six-by-five grid, with source distance 0 at (1,1), destination distance 11 at (5,0), and distance 12 at (4,0); walls remain marked with #" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The destination is first reached at distance **11**. The distance 12 at `(4, 0)` is also valid: that cell is reached by continuing upward from `E`. In this problem, `E` is a traversable cell, and this BFS continues until the queue is empty.

In the displayed matrix, `#` identifies a wall. In the code's integer distance matrix, walls keep their initial value -1 because they are never visited; an unreachable open cell would also retain -1.

## 5. Reconstructing One Shortest Path

For each discovered cell, `par` remembers the previous cell on a shortest route from `S`.

For example, when `(5, 1)` discovers `E = (5, 0)`, we set:

```text
par[5][0] = (5, 1)
dis[5][0] = dis[5][1] + 1 = 11
```

To reconstruct the route:

1. Start at `E`.
2. Append the current cell to a path vector.
3. Move to its parent until reaching `S`.
4. Append `S` and reverse the vector, because the collected route runs from end to start.

For the dry run, the parent chain is:

```text
(5,0) <- (5,1) <- (5,2) <- (5,3) <- (5,4) <- (4,4)
      <- (3,4) <- (2,4) <- (2,3) <- (2,2) <- (1,2) <- (1,1)
```

Each arrow above points from a parent toward its child. To backtrack, begin at `(5,0)` and read the chain toward the right.

Reversing the collected cells gives one shortest path from `S` to `E`:

```text
(1,1) -> (1,2) -> (2,2) -> (2,3) -> (2,4) -> (3,4)
      -> (4,4) -> (5,4) -> (5,3) -> (5,2) -> (5,1) -> (5,0)
```

It contains **12 cells and 11 moves**. In general:

$$
\text{Number of moves} = \text{Number of cells in the path} - 1
$$

Do not follow parents when `E` is unreachable: it has no valid parent chain. Also, stop at `S` rather than following its initial `(-1, -1)` parent.

The reconstructed route need not be unique. For example, at distance 7, either `(5, 4)` or `(4, 3)` could lead to `(5, 3)`. Our direction order causes `(5, 4)` to discover it first. Another neighbour order could choose a different shortest route without changing the minimum distance.

## 6. Complete C++ Implementation

### Input

- First line: `n m`, the numbers of rows and columns.
- Next `n` lines: strings of length `m` containing the grid.
- There is exactly one `S` and one `E`.

### Output for This Example

- If no path exists, print `Not Possible`.
- Otherwise, print `Possible`, the minimum number of steps, and one shortest path as zero-based coordinates.

```cpp
#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <utility>
#include <vector>
using namespace std;

using Cell = pair<int, int>;

int n, m;
vector<string> arr;
vector<vector<int>> vis, dis;
vector<vector<Cell>> par;

const vector<int> dx = {1, -1, 0, 0};
const vector<int> dy = {0, 0, 1, -1};

bool is_valid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && arr[x][y] != '#';
}

vector<Cell> neigh(int x, int y) {
    vector<Cell> neighbours;

    for (size_t dir = 0; dir < dx.size(); ++dir) {
        int xx = x + dx[dir];
        int yy = y + dy[dir];
        if (is_valid(xx, yy)) {
            neighbours.push_back({xx, yy});
        }
    }

    return neighbours;
}

void bfs(int x, int y) {
    queue<Cell> q;
    vis[x][y] = 1;
    dis[x][y] = 0;
    q.push({x, y});

    while (!q.empty()) {
        auto [a, b] = q.front();
        q.pop();

        for (auto [xx, yy] : neigh(a, b)) {
            if (!vis[xx][yy]) {
                vis[xx][yy] = 1;
                dis[xx][yy] = dis[a][b] + 1;
                par[xx][yy] = {a, b};
                q.push({xx, yy});
            }
        }
    }
}

void solve() {
    cin >> n >> m;
    arr.resize(n);

    Cell start = {-1, -1};
    Cell finish = {-1, -1};

    for (int row = 0; row < n; ++row) {
        cin >> arr[row];
        for (int col = 0; col < m; ++col) {
            if (arr[row][col] == 'S') start = {row, col};
            if (arr[row][col] == 'E') finish = {row, col};
        }
    }

    // The input guarantees that the scan finds exactly one S and one E.
    vis.assign(n, vector<int>(m, 0));
    dis.assign(n, vector<int>(m, -1));
    par.assign(n, vector<Cell>(m, {-1, -1}));

    bfs(start.first, start.second);

    if (dis[finish.first][finish.second] == -1) {
        cout << "Not Possible\n";
        return;
    }

    vector<Cell> path;
    Cell current = finish;

    while (current != start) {
        path.push_back(current);
        current = par[current.first][current.second];
    }
    path.push_back(start);
    reverse(path.begin(), path.end());

    cout << "Possible\n";
    cout << "Minimum steps: " << dis[finish.first][finish.second] << '\n';
    cout << "Path from start to end:\n";
    for (size_t i = 0; i < path.size(); ++i) {
        if (i > 0) cout << ' ';
        cout << '(' << path[i].first << ", " << path[i].second << ')';
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
```

`Cell` is simply a shorter name for `pair<int, int>`. The structured bindings, such as `auto [a, b]`, use C++17 to unpack a coordinate pair.

The `&&` conditions in `is_valid` are evaluated left to right with short-circuiting. Consequently, the code never reads `arr[x][y]` if a boundary check fails.

The reconstruction condition `current != start` means that **either coordinate still differs**. Written with separate coordinates, it would be `curx != stx || cury != sty`, not `&&`.

### Sample 1: The Illustrated Grid

Input:

```text
6 5
##.#.
.S.#.
.#...
##.#.
.##..
E....
```

Output:

```text
Possible
Minimum steps: 11
Path from start to end:
(1, 1) (1, 2) (2, 2) (2, 3) (2, 4) (3, 4) (4, 4) (5, 4) (5, 3) (5, 2) (5, 1) (5, 0)
```

### Sample 2: No Path Exists

Input:

```text
3 3
S..
###
..E
```

Output:

```text
Not Possible
```

The wall row separates `S` and `E`. BFS explores the top row, leaves `E` at distance -1, and does not attempt reconstruction.

## 7. Why Is the Reconstructed Path Shortest?

Every legal grid move is an edge of cost 1. Therefore, the shortest-distance argument from ordinary BFS applies unchanged: cells are discovered in increasing distance from `S`.

When a cell is first discovered, its parent is an adjacent cell whose distance is exactly one less:

$$
\text{dis}[\text{child}] = \text{dis}[\text{parent}] + 1
$$

Following parents decreases the distance by 1 at every step. The chain cannot cycle and must terminate at the source, whose distance is 0. Starting at `E`, it takes exactly `dis[E]` parent steps to reach `S`.

After reversal, the route is legal and has the minimum number of moves.

## 8. KWALK: Changing the Movement Rules

For the **knight-movement variant** discussed here, a move changes one coordinate by 2 and the other by 1, like a chess knight. Every jump still costs one move.

The BFS framework stays the same. What changes is the function that generates neighbouring cells.

Replace the four-direction arrays with these eight paired offsets:

```cpp
const vector<int> dx = {2, 1, -1, -2, -2, -1, 1, 2};
const vector<int> dy = {-1, -2, -2, -1, 1, 2, 2, 1};
```

They represent:

$$
(2,-1),\ (1,-2),\ (-1,-2),\ (-2,-1),\
(-2,1),\ (-1,2),\ (1,2),\ (2,1)
$$

The neighbour loop already uses `dx.size()`, so it automatically considers all eight moves. Do not leave a hard-coded four-iteration loop when making this change.

### What Stays the Same?

- Check that the **landing cell** is within the grid and is not a wall.
- Mark a landing cell on first discovery.
- Increase distance by 1 for each jump.
- Record the previous cell as its parent.
- Reconstruct the route using the same parent-following logic.

Under these knight rules, the piece **jumps over intervening cells**. Their contents do not block a move; only the landing cell is checked. A jump changes coordinates by a total of three units, but still counts as **one move**, not three.

For example:

```text
S##
##E
###
```

With four-direction movement, `S = (0,0)` cannot leave its cell. With knight movement, the offset `(1,2)` lands directly on `E = (1,2)`, so the answer is one move:

```text
(0,0) -> (1,2)
```

The complete program above uses four-direction movement unless its two direction arrays are replaced. The knight variant is a different graph on the same grid, so its reachability and shortest distances can differ.

## 9. Complexity

There are at most \(nm\) traversable cells. Each reachable cell is enqueued once, and processing it considers four candidate moves—or eight in the knight variant.

Since the number of candidate moves per cell is constant:

- **Time:** \(O(nm)\), including input, matrix initialization, BFS, and path reconstruction.
- **Space:** \(O(nm)\) for the grid, visited matrix, distances, parents, queue, and reconstructed path.

Although the parent matrix stores coordinate pairs, that is only a constant amount of information per cell. We do not copy an entire path into each queue entry.

## 10. Common Mistakes and Quick Checks

- **Using start/end coordinates before locating them:** scan the input for `S` and `E` before calling BFS.
- **Reading outside the grid:** check row and column bounds before accessing a cell.
- **Treating only `.` as open:** `S` and `E` are traversable too.
- **Marking on removal from the queue:** mark on insertion to avoid repeated discoveries.
- **Overwriting a visited cell's parent:** keep the parent chosen on first discovery.
- **Reconstructing an unreachable destination:** check its distance first.
- **Forgetting to reverse the parent chain:** following parents produces the route from `E` back to `S`.
- **Counting cells instead of moves:** a path with \(k\) cells has \(k-1\) moves.
- **Using the wrong movement rules:** four-direction moves cannot pass through walls; knight jumps ignore intervening cells but cannot land on a wall.

To verify a reported path, check its endpoints, ensure every listed cell is inside the grid and not a wall, verify each consecutive move is allowed, and confirm that its number of moves equals the recorded shortest distance.

## Quick Recap

- Model traversable cells as vertices and legal moves as edges; generate neighbours on demand.
- Use BFS because every move has equal cost.
- Store one distance and one parent per discovered cell.
- If `E` is reachable, follow parents back to `S` and reverse the result.
- Different movement offsets, such as knight jumps, change the graph without changing the BFS framework.

</READING_WIDGET>
