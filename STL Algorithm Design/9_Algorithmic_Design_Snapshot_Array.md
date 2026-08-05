<VIDEO_WIDGET>

<VIDEO_ID>366</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Snapshot Array

> *Designing a Snapshot Array tests your ability to manage system state over time. This architecture is heavily used in real-world applications like Database transactions, Git version control, and text editor "Undo" histories.*

---

## 1. The Challenge

You must implement a `SnapshotArray` that supports the following interface:
1. `SnapshotArray(int length)`: Initializes an array of a given length. Every element starts at `0`.
2. `set(index, val)`: Sets the element at the given `index` to be `val`.
3. `snap()`: Takes a snapshot of the array and returns the `snap_id` (the total number of times `snap()` was called minus 1).
4. `get(index, snap_id)`: Returns the value at the given `index`, exactly as it was when the snapshot with `snap_id` was taken.

### The Naive Memory Trap
The beginner approach is to create a massive `vector<vector<int>>` and actually copy the *entire* array every single time `snap()` is called. 
If the array has $100,000$ elements, and you call `snap()` $100,000$ times, you just copied $10$ Billion elements! This guarantees a massive **Memory Limit Exceeded (MLE)** crash. 

We need a system that only stores *changes*, not full copies.

---

## 2. The Golden Architecture: Vertical Timelines

Instead of taking horizontal snapshots of the entire array, we turn the array sideways! 
Each individual index will maintain its own personal "History Stack" (a vertical timeline).

We define the architecture as: `vector<vector<pair<int, int>>>`
Where `arr[i]` holds a list of pairs: `{snap_id, value}`.

*   When `set(index, val)` is called, we append `{current_snap_id, val}` to the history stack of `arr[index]`.
*   When `snap()` is called, we simply increment `current_snap_id++`. That's it! Strict $O(1)$ time and $O(1)$ memory!

### The Binary Search Retrieval
How do we `get(index, target_snap_id)`?
We go to `arr[index]` and look at its history stack. The history stack is inherently sorted by `snap_id` because time only moves forward. 
Therefore, we can use **Binary Search** to find the exact `snap_id` we want! 
Since a specific `target_snap_id` might not exist in the history (maybe that index wasn't modified during that snapshot), we use `std::upper_bound` to find the first snapshot *greater* than our target, and step one index backwards to get the most recent valid value!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/dd39efae-7e18-4869-89fd-f644736f33c0.jpg" alt="Snapshot Array Binary Search Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Code Implementation

> 💎 **The FAANG Memory Optimization**
> What if a user calls `set(index, 5)` and then `set(index, 10)` *before* calling `snap()`? Both edits happen in the exact same `snap_id`! Instead of storing both, we should overwrite the previous value. This saves massive amounts of memory in high-frequency update systems.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class SnapshotArray {
private:
    int current_snap_id;
    // The Array: Index -> List of {snap_id, value}
    vector<vector<pair<int, int>>> history;

public:
    SnapshotArray(int length) {
        current_snap_id = 0;
        // 💡 Constructor Initialization Speed: Allocate the entire 2D array and default {0, 0}
        // pairs in one contiguous memory block instead of a slow loop!
        history.assign(length, vector<pair<int, int>>{{0, 0}});
    }
    
    // Time Complexity: O(1) Amortized
    void set(int index, int val) {
        // Elite Optimization: If the last edit was in the exact same snap_id, overwrite it!
        if (!history[index].empty() && history[index].back().first == current_snap_id) {
            history[index].back().second = val;
        } else {
            // Otherwise, append a new historical record
            history[index].push_back({current_snap_id, val});
        }
    }
    
    // Time Complexity: O(1)
    int snap() {
        return current_snap_id++;
    }
    
    // Time Complexity: O(log H) where H is the number of edits made to this specific index
    int get(int index, int snap_id) {
        // Binary search to find the first record whose snap_id is GREATER than our target
        auto it = upper_bound(history[index].begin(), history[index].end(), make_pair(snap_id, INT_MAX));
        
        // Step exactly one position backward to get the active value at our target time
        it--;
        
        return it->second;
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   `set()`: $O(1)$ amortized (vector push_back).
    *   `snap()`: $O(1)$. We just increment an integer.
    *   `get()`: $O(\log H)$ where $H$ is the number of historical edits made to that specific index.
*   **Space Complexity:** $O(S)$ where $S$ is the total number of `set()` operations performed. We strictly store changes, ensuring optimal memory efficiency compared to the naive full-array copying.

> 🚨 **The Elite CP Insight: Why `INT_MAX`?**
> In the `get` method, we used: `upper_bound(..., make_pair(snap_id, INT_MAX))`. Why `INT_MAX`? 
> When C++ compares two `std::pair` objects, it checks the `first` element. *If they are equal*, it compares the `second` element!
> If our array had `{snap_id, 5}` and we searched for `make_pair(snap_id, 0)`, C++ would evaluate `{snap_id, 5} > {snap_id, 0}`. `upper_bound` would instantly stop and return `{snap_id, 5}`, which means stepping backward would yield the *previous* `snap_id`'s value—the completely wrong answer! By aggressively using `INT_MAX`, we mathematically force C++ to look past *every possible value* within the current `snap_id`, guaranteeing it safely lands on `snap_id + 1`.

## 4. Module Summary
- Taking full-array snapshots guarantees a massive Memory Limit Exceeded (MLE) crash in production systems.
- Optimal state management uses "Vertical Timelines," where each index tracks its own modification history.
- `snap()` becomes a mathematically free operation ($O(1)$), simply incrementing a master clock ID.
- Retrieving historical data requires an $O(\log H)$ Binary Search (`upper_bound`) across the specific index's timeline.

</READING_WIDGET>
