<VIDEO_WIDGET>

<VIDEO_ID>3567</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Lower & Upper Bound

> _Welcome back! Now that you know how to perfectly sort your data, it's time to learn how to rapidly search through it. The C++ STL provides built-in bound functions that can find elements incredibly fast in $O(\log N)$ time!_

**Wait, how do they search so fast?**
These functions are actually highly optimized C++ implementations of **Binary Search**! (Don't worry, we will learn how to write custom Binary Search algorithms in detail later in the course). Because they use binary search under the hood, there is one unbreakable Golden Rule: **The array MUST be completely sorted first!** If you attempt to use any of these bound functions on an unsorted array, they will return completely random, garbage results without throwing any errors!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d3ddf805-24a4-43db-95af-57e63e0a5f27.jpg" alt="lower_bound and upper_bound Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. `std::lower_bound` ($\ge X$)

In Competitive Programming, we often need to know exactly _where_ an element (or the next best element) is located.
`std::lower_bound` finds the **first element that is greater than or equal to $X$**.

**When to apply it:** Use this when you need to find the exact starting position of a number, or when you want to find the smallest number that meets a certain minimum threshold.

> 🚨 **The Iterator Trap:** `lower_bound` does NOT return an integer index. It returns an _iterator_ pointing to the element in memory. To convert this iterator into a usable, zero-based integer index, you **must subtract the beginning iterator `v.begin()`** from it!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Indices:      0   1   2   3   4   5
    vector<int> v = {10, 20, 30, 30, 30, 40};

    // Find the first element >= 30
    auto it = lower_bound(v.begin(), v.end(), 30);

    // Convert iterator to index!
    int index = it - v.begin();

    cout << "First element >= 30 is at index: " << index << "\n"; // Output: 2

    return 0;
}
```

If the number is larger than every element in the array (e.g., searching for 100), `lower_bound` will safely return `v.end()`, which converts to an index exactly equal to `v.size()`.

> 🚨 **The CP Trap: Descending Arrays**
> If your array is sorted in **descending** order (e.g., `[50, 40, 30, 20]`), calling standard `lower_bound(30)` will fail completely or return garbage. Because the array isn't ascending, the internal binary search breaks. You MUST pass `greater<int>()` as a third argument so the binary search knows the rules have reversed!
> `auto it = lower_bound(v.begin(), v.end(), 30, greater<int>());`

---

## 2. `std::upper_bound` ($> X$)

`std::upper_bound` is the twin sibling of `lower_bound`. Instead of greater than or equal to, it finds the **first element that is STRICTLY greater than $X$**.

**When to apply it:** Use this when you need to find the element that comes immediately _after_ your target, or to find the end boundary of a sequence of duplicate numbers.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Indices:      0   1   2   3   4   5
    vector<int> v = {10, 20, 30, 30, 30, 40};

    // Find the first element STRICTLY > 30
    auto it = upper_bound(v.begin(), v.end(), 30);

    int index = it - v.begin();

    cout << "First element > 30 is at index: " << index << "\n"; // Output: 5

    return 0;
}
```

---

## 3. The "Step Back" Trick (Finding $< X$ and $\le X$)

The STL gives us $\ge X$ (`lower_bound`) and $> X$ (`upper_bound`). But in CP, we frequently need to find the largest element that is **strictly less than** $X$ ($< X$) or **less than or equal to** $X$ ($\le X$).
Beginners often try to write custom binary searches for this, wasting valuable contest time. Instead, use the "Step Back" trick!

- To find the largest element **strictly $< X$**: find `lower_bound(X)` and step the iterator back by one (`--it`)!
- To find the largest element **$\le X$**: find `upper_bound(X)` and step back by one (`--it`).

_(Just remember to verify the iterator isn't already at `v.begin()` before stepping back, otherwise you will Segmentation Fault!)_

---

## 4. Counting Occurrences in $O(\log N)$ Time

By combining `lower_bound` and `upper_bound`, we unlock a powerful CP trick!
Because `lower_bound` gives us the exact index where a run of duplicates _starts_, and `upper_bound` gives us the exact index where that run _ends_, subtracting them gives us the exact count of how many times a number appears!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Indices:      0   1   2   3   4   5
    vector<int> v = {10, 20, 30, 30, 30, 40};

    // How many times does 30 appear?
    auto low = lower_bound(v.begin(), v.end(), 30);
    auto up = upper_bound(v.begin(), v.end(), 30);

    int count = up - low;

    cout << "The number 30 appears " << count << " times.\n"; // Output: 3

    return 0;
}
```

---

## 5. The Set/Map Speed Trap

In earlier modules, you learned about `std::set` and `std::map`. Since they are inherently sorted, you might be tempted to use the STL `std::lower_bound` function on them. **Do not do this!**

> 💡 **CP Insight: The Member Function Rule**
> Sets and Maps do not have random-access iterators (they are built using trees, not contiguous arrays). If you pass a `std::set` into `std::lower_bound(s.begin(), s.end(), val)`, the compiler will painstakingly traverse the tree node by node. Your $O(\log N)$ optimized search instantly degrades into an $O(N)$ linear search, resulting in a **Time Limit Exceeded (TLE)**!
>
> **The Fix:** Always use their built-in member functions! Call `s.lower_bound(val)` instead, which uses the internal tree structure to guarantee $O(\log N)$ speed.

---

> 🚀 **Next Up:** Now that you have mastered searching arrays efficiently, it's time to learn how to manipulate the array's raw contents. Let's move on to powerful permutation algorithms!

</READING_WIDGET>
