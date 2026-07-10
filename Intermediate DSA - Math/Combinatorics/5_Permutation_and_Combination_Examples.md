<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Permutations and Combinations Examples

Now that you have learned the mathematical foundations of both Permutations ($^nP_r$) and Combinations ($^nC_r$), it's time to see how these concepts are applied to solve complex counting problems in geometry and arrays. 

These patterns appear constantly in Competitive Programming!

---

## 1. Maximum Intersection Points (8 Lines and 4 Circles)

**Problem:** What is the maximum possible number of intersection points if we draw exactly 8 straight lines and 4 circles on a 2D plane?

To maximize intersections, we must assume no lines are parallel, no circles are perfectly concentric, and no three shapes intersect at the exact same point. We break this down into three mutually exclusive cases:

### Case 1: Line-Line Intersections
Two distinct straight lines can intersect at most **once**.
The number of ways to choose exactly 2 lines from the pool of 8 is a combination problem (since line $A$ crossing line $B$ is the same intersection as $B$ crossing $A$):
$$C(8, 2) = \frac{8!}{2! \times (8 - 2)!} = \frac{8 \times 7}{2} = 28 \text{ points}$$

### Case 2: Circle-Circle Intersections
Two distinct circles can intersect at most **twice**.
The number of ways to choose exactly 2 circles from the pool of 4 is $C(4, 2)$:
$$C(4, 2) = \frac{4!}{2! \times (4 - 2)!} = \frac{4 \times 3}{2} = 6 \text{ pairs}$$
Since each pair intersects twice, the maximum points are:
$$6 \times 2 = 12 \text{ points}$$

### Case 3: Line-Circle Intersections
A single straight line can intersect a single circle at most **twice**.
Since there are 8 lines and 4 circles, there are $8 \times 4 = 32$ unique line-circle pairings (Multiplication Principle!). 
Since each pairing yields up to 2 points:
$$32 \times 2 = 64 \text{ points}$$

**Final Calculation:**
By the Addition Principle, we sum all mutually exclusive cases:
$$28 + 12 + 64 = 104 \text{ maximum intersection points.}$$

---

## 2. Total Number of Subarrays in an Array of Size N

**Problem:** How many contiguous subarrays exist in an array of size $N$?

A subarray is a contiguous segment of an array. A brilliant combinatorial way to think about a subarray is to visualize **dividers** sitting between the array elements. 

If an array has $N$ elements, there are exactly $N+1$ possible positions to place a divider (including the far left and far right ends). 

To form a contiguous subarray, you simply need to **select exactly 2 distinct dividers**—one to mark the start of the subarray, and one to mark the end!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/3b35e3ea-fe11-4ab6-a968-f0b593f561d1.jpg" alt="Counting Subarrays With Dividers" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Since the order of selecting the two dividers doesn't matter (choosing divider 2 then 4 forms the exact same subarray as choosing 4 then 2), the total number of subarrays is simply:
$$C(N+1, 2) = \frac{(N+1)N}{2}$$

### Example for $N = 4$:
For an array like `[1, 2, 3, 4]`, $N=4$. Total subarrays:
$$\frac{5 \times 4}{2} = 10$$
*(These 10 subarrays are: `(1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4), (1,2,3,4)`)*

*(Note: This formula counts all strictly non-empty subarrays. If a specific CP problem allows an "empty" subarray `[]` as a valid selection, simply add $+1$ to your final answer!)*

---

## 3. Total Number of Rectangles on an $N \times N$ Chessboard

**Problem:** How many unique rectangles can be formed on an $N \times N$ grid?

Think about how a rectangle is structurally formed on a grid. A rectangle is perfectly bounded by exactly **2 horizontal lines** and **2 vertical lines**. 

An $N \times N$ grid is made up of $N+1$ horizontal lines and $N+1$ vertical lines.

To form any unique rectangle, we must:
1. Select exactly 2 horizontal lines from the $N+1$ available lines.
2. Select exactly 2 vertical lines from the $N+1$ available lines.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/dfa8bb96-e541-45ae-a8d3-a517ef59fe9f.jpg" alt="Rectangles on a Grid" style="max-width: 100%; height: auto;" identifier="az-img-upload">

By the Multiplication Principle, the total number of rectangles is:
$$C(N+1, 2) \times C(N+1, 2) = \left( \frac{(N+1)N}{2} \right)^2$$

### Example for $N = 3$:
For a $3 \times 3$ grid, there are 4 horizontal and 4 vertical lines:
$$C(4, 2) \times C(4, 2) = \left( \frac{4 \times 3}{2} \right)^2 = 6 \times 6 = 36 \text{ rectangles}$$

---

## 4. Total Number of Squares on an $N \times N$ Chessboard

**Problem:** How many *squares* exist on an $N \times N$ chessboard?

A square is a highly restricted rectangle where the width must exactly equal the height. We can no longer just pick random lines; we must carefully count the squares by their physical sizes: $1 \times 1, 2 \times 2, ... , N \times N$.

### Counting $k \times k$ Squares
For a square of size $k \times k$, think about where its top-left corner can physically be placed without the square spilling off the edge of the board. 

The top-left corner has exactly $(N - k + 1)$ valid horizontal positions and $(N - k + 1)$ valid vertical positions.
Thus, the total number of $k \times k$ squares is:
$$(N - k + 1)^2$$

To get the absolute total number of squares of *all* sizes, we must sum this up for all valid sizes of $k$ (from $1$ to $N$):
$$\sum_{k=1}^{N} (N - k + 1)^2 = N^2 + (N-1)^2 + ... + 1^2$$

This is just the sum of the first $N$ perfect squares! Using standard mathematical formulas, this simplifies beautifully to:
$$\frac{N(N+1)(2N+1)}{6}$$

> 💡 **CP Insight:** The formulas for subarrays $\left( \frac{N(N+1)}{2} \right)$ and squares $\left( \frac{N(N+1)(2N+1)}{6} \right)$ should be memorized. In CP, whenever you see an $O(N^2)$ brute-force solution trying to count subarrays, you can almost always reduce it to $O(1)$ math using combinatorics!

</READING_WIDGET>
