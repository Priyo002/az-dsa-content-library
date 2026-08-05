<VIDEO_WIDGET>

<VIDEO_ID>363</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Min Stack

> *Data structures rarely exist in isolation. Real-world systems often require hybrid data structures that maintain a "running state" across time. The Min Stack is the foundational problem that tests your ability to synchronize current data with historical states.*

---

## 1. The Challenge

A standard Stack follows the Last-In-First-Out (LIFO) principle and supports `push`, `pop`, and `top` in $O(1)$ time. 
Your challenge is to upgrade the standard stack to support an additional operation: **`getMin()`**, which returns the absolute minimum element currently present in the stack, also in strict **$O(1)$ time**.

**Operations to Support:**
1. `push(val)`: Pushes the element `val` onto the stack.
2. `pop()`: Removes the element on the top of the stack.
3. `top()`: Gets the top element of the stack.
4. `getMin()`: Retrieves the minimum element in the stack.

---

## 2. Why a Simple Variable Fails

A common beginner mistake is to simply declare an integer variable `current_min` in the class. When a new element arrives, they do `current_min = min(current_min, val)`.

**Why does this fail?**
It works perfectly for `push()`! But what happens during a `pop()`?
If the element you just popped happens to be the `current_min`, you now have to update `current_min` to whatever the *second smallest* element in the stack was. Finding the second smallest element requires traversing the entire stack, which is $O(N)$ time, violating the $O(1)$ requirement!

To achieve $O(1)$ pops, we must remember the historical minimum state at every single level of the stack.

---

## 3. The "State Synchronization" Architecture

Instead of storing just a single value at each level of the stack, we store a **Pair** of values:
`{ the_actual_value, the_minimum_value_at_this_exact_level }`

When you push a new value, you look at the `min` of the previous level, compare it with your new value, and store the result as *your* level's `min`.

### Walkthrough:
Let's push `[5, 7, 3, 8]` into an empty Min Stack.

1. **Push 5:** Stack is empty. `min` is `5`. Store `{5, 5}`.
2. **Push 7:** Compare `7` with previous `min` (which is `5`). New `min` is `5`. Store `{7, 5}`.
3. **Push 3:** Compare `3` with previous `min` (which is `5`). New `min` is `3`. Store `{3, 3}`.
4. **Push 8:** Compare `8` with previous `min` (which is `3`). New `min` is `3`. Store `{8, 3}`.

If we call `getMin()` now, we simply look at the top pair `{8, 3}` and return the second value: `3`.
If we call `pop()`, we remove `{8, 3}`. The new top is `{3, 3}`. The historical minimum is perfectly preserved!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/4a51ff7d-dac1-4543-ac99-776ebb23fcf7.jpg" alt="Min Stack Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. The Code Implementation

> 💡 **The Elite STL Trick: Vector over Stack**
> While you could use `std::stack<pair<int, int>>`, seasoned competitive programmers prefer using `std::vector<pair<int, int>>`. A vector allows for faster continuous memory allocation, avoids the overhead of the stack adapter, and lets us use `back()` and `pop_back()` cleanly.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class MinStack {
private:
    // Stores {actual_value, minimum_value_at_this_level}
    vector<pair<int, int>> st;

public:
    MinStack() {
        // Initialize an empty vector
    }
    
    // Time Complexity: O(1)
    void push(int val) {
        if (st.empty()) {
            st.push_back({val, val});
        } else {
            // The new minimum is the min between the new value and the previous level's minimum
            int current_min = min(val, st.back().second);
            st.push_back({val, current_min});
        }
    }
    
    // Time Complexity: O(1)
    void pop() {
        if (!st.empty()) {
            st.pop_back();
        }
    }
    
    // Time Complexity: O(1)
    int top() {
        // Production Guard against Undefined Behavior (Segmentation Fault)
        if (st.empty()) return -1; // Or throw an exception
        return st.back().first;
    }
    
    // Time Complexity: O(1)
    int getMin() {
        // Production Guard against Undefined Behavior (Segmentation Fault)
        if (st.empty()) return -1; // Or throw an exception
        return st.back().second;
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`). We are simply looking at or modifying the back of a vector.
*   **Space Complexity:** $O(N)$. We require extra space to store the historical minimum alongside every single element. 

> 🚨 **Systems Insight: The $O(1)$ Space Flex**
> Can this be done in strict $O(1)$ auxiliary space? Yes! There is an elite mathematical trick where you store an encoded value `(2 * val - min)` in the stack instead of pairs. While mathematically brilliant, it is highly susceptible to **Integer Overflow** in production systems and is generally reserved only as an interview discussion point, not actual production code. 

> **The FAANG Memory Optimization: Two Stacks**
> Using `std::vector<pair<int, int>>` is the easiest way to code this, but if you push 1 million elements into the stack, you are copying the minimum value 1 million times, even if the minimum hasn't changed!
> The elite memory optimization is to use **Two Separate Stacks (Vectors)**: one for the actual data (`vector<int> st`), and a second `vector<int> min_stack`. When you `push(val)`, you only push it into `min_stack` if `val <= min_stack.back()`. When you `pop()`, you only pop from `min_stack` if the popped value equals `min_stack.back()`. This drastically reduces the memory footprint in the average case.

## 5. Module Summary
- A single `min` variable fails because `pop()` operations destroy historical state.
- By synchronizing the current value with the running minimum inside a `pair`, we achieve $O(1)$ time complexity for all operations.
- `std::vector` is often preferred over `std::stack` for cleaner memory alignment and performance.

</READING_WIDGET>
