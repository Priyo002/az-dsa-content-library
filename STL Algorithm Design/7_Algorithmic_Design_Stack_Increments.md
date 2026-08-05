<VIDEO_WIDGET>

<VIDEO_ID>364</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Stack with Lazy Increments

> *Modifying multiple elements inside a data structure simultaneously is notoriously slow. In this module, we'll design a Custom Stack that can instantly increment its bottom $k$ elements in strict $O(1)$ time using a legendary technique: **Lazy Propagation**.*

---

## 1. The Challenge

We need to design a stack with a maximum capacity that supports three operations:
1. `push(x)`: Adds `x` to the top of the stack if it hasn't reached `maxSize`.
2. `pop()`: Pops and returns the top of the stack (or `-1` if empty).
3. `inc(k, val)`: Increments the bottom $k$ elements of the stack by `val`. (If there are fewer than $k$ elements, increment all of them).

### The Naive $O(K)$ Approach
The most obvious way to implement `inc(k, val)` is to just use a `for` loop, iterating from index `0` up to `k-1`, and adding `val` to each element.
While this works, it takes $O(K)$ time. If $K$ is massive, and we call `inc` millions of times, our system will lag heavily. We need an $O(1)$ solution.

---

## 2. The $O(1)$ Architecture: Lazy Propagation

To achieve strict $O(1)$ time, we must **delay** the actual addition until the absolute last possible moment. This is called *Lazy Propagation*.

Instead of updating $k$ elements immediately, we maintain a secondary array: the `incArray`.
When we are told to add `val` to the bottom $k$ elements, we simply go to the index `k - 1` in our `incArray` and add `val` to it. We don't touch any other elements!

`incArray[k - 1] += val`

This single operation serves as a "bookmark" that says: *"Everything from this index and below needs to be incremented by `val`."*

### The Trickle-Down Effect (`pop()`)
When do we actually apply this delayed addition? Only when an element is leaving the stack!
During a `pop()` operation at index `i`:
1. We look at the actual value in our stack at index `i`.
2. We look at the `incArray[i]`. We add this increment value to our actual value before returning it.
3. **The Magic Step:** Before we delete index `i`, we take its increment value and pass it downwards to the element right below it!
   `incArray[i - 1] += incArray[i]`
4. Finally, we reset `incArray[i] = 0` so it's clean for future pushes.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/3971271b-15ce-4e20-ae9f-499de07e2c57.jpg" alt="Stack Lazy Increments Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class CustomStack {
private:
    vector<int> stack;
    // Use long long to prevent silent Integer Overflow from lazy accumulations
    vector<long long> incArray; 
    int maxSize;

public:
    CustomStack(int maxSize) {
        this->maxSize = maxSize;
        // Only reserve capacity. 
        // Do NOT pre-allocate with .assign() or you will waste O(maxSize) RAM and Time!
        stack.reserve(maxSize);
        incArray.reserve(maxSize);
    }
    
    // Time Complexity: O(1)
    void push(int x) {
        if (stack.size() < maxSize) {
            stack.push_back(x);
            // Synchronize the lazy array dynamically!
            incArray.push_back(0); 
        }
    }
    
    // Time Complexity: O(1)
    int pop() {
        if (stack.empty()) return -1;
        
        int i = stack.size() - 1; // Current top index
        
        // Calculate the true value including any pending increments
        long long res = stack[i] + incArray[i];
        
        // Lazy Propagation: Pass the increment down to the element below
        if (i > 0) {
            incArray[i - 1] += incArray[i];
        }
        
        // Cleanly pop from both arrays to ensure memory footprint stays minimal
        stack.pop_back();
        incArray.pop_back();
        
        return (int)res; // Safely cast back to int for return
    }
    
    // Time Complexity: O(1)
    void inc(int k, int val) {
        if (stack.empty()) return;
        
        // Find the highest valid index we can apply this to
        int i = min((int)stack.size(), k) - 1;
        
        // Drop the "lazy bookmark"
        incArray[i] += val;
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** $O(1)$ for ALL operations (`push`, `pop`, `inc`). There are absolutely zero loops in our code!
*   **Space Complexity:** $O(E)$ where $E$ is the number of elements *currently* in the stack. By dynamically using `push_back(0)` and `pop_back()`, we ensure our memory footprint perfectly mirrors active usage, avoiding massive RAM waste if `maxSize` is excessively large.

> 🚨 **Systems Insight: The Integer Overflow Trap**
> Lazy Propagation means numbers *accumulate*. If a system calls `inc(k, 1000000)` a thousand times before anyone calls `pop()`, the value inside `incArray[i]` will easily exceed the 32-bit limit of a standard `int`. This wraps around into negative numbers, silently destroying data integrity. Always track cumulative lazy states using `long long`!

> 💎 **Systems Insight: The Power of Laziness**
> Lazy Propagation is not just a trick for this specific stack problem; it is the cornerstone of advanced Range Query data structures like **Segment Trees**. In enterprise databases, modifying millions of records simultaneously locks the entire database table. Using "lazy updates" allows the system to remain highly responsive, only calculating the final values precisely when a user actually queries them!

## 4. Module Summary
- The naive $O(K)$ looping approach is completely unscalable for massive systems.
- By using a secondary array, we can drop "bookmarks" that represent pending additions in strict $O(1)$ time.
- These pending additions are applied and "trickled down" to lower elements during the `pop()` operation.
- This technique (Lazy Propagation) is a critical optimization strategy used in advanced tree structures and database architectures.

</READING_WIDGET>
