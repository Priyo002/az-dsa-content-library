<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Top K Elements

> *In FAANG interviews, Algorithmic Design questions often require you to build a custom data structure that maintains complex state dynamically. Let's master the architecture required to track the Top K elements in a live data stream!*

---

## 1. The Running Top-K Sum

What if a system asks you to: **Maintain the sum of ONLY the Top $K$ elements dynamically.**

If your system only receives new data (Insertions) and never deletes old data, we can design a struct using a single **Min-Heap**.

```cpp
#include <iostream>
#include <queue>
using namespace std;

struct RunningTopK {
    int K;
    priority_queue<int, vector<int>, greater<int>> min_pq;
    long long sumK;

    void init(int _K) {
        K = _K;
        sumK = 0;
    }

    // Time Complexity: O(log K)
    void insert(int x) { 
        min_pq.push(x);
        sumK += x; // Optimistically add it to our running sum

        // If we exceed K, throw away the smallest element!
        if (min_pq.size() > K) {
            int smallest = min_pq.top();
            min_pq.pop();
            sumK -= smallest; // Correct the sum
        }
    }

    // Time Complexity: O(1) Instant Query!
    long long getSum() { 
        return sumK;
    }
};
```

---

## 2. The Deletion Problem & The Two-Multiset Pattern

The Min-Heap architecture is flawless for $O(\log K)$ insertions. **But what if a user deletes their data?** 
A `std::priority_queue` does not support random deletion (`pq.erase(val)` does not exist). To support both Insertions and Deletions, we must abandon the Priority Queue and design a complex **Two-Multiset Architecture**.

1. **`mt1` (The Winners):** Contains exactly the Top $K$ elements.
2. **`mt2` (The Bench):** Contains all the remaining "smaller" elements.

Because Multisets are built on Red-Black Trees, they perfectly maintain sorted order and support $O(\log N)$ deletion of *any* element!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/f354b218-359c-44bc-8802-c39130b91abf.jpg" alt="Two-Multiset Pattern" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### The Algorithm Logic:
- **Insertion:** Always insert the new element into `mt1` and add to `sumK`. If `mt1` now has $K+1$ elements, find the absolute smallest element in `mt1` (`mt1.begin()`), subtract it from `sumK`, and demote it to `mt2`.
- **Deletion:** If the element is in `mt1`, erase it and subtract from `sumK`. If it's in `mt2`, just erase it.
- **Rebalancing:** If an element was deleted from `mt1`, we now only have $K-1$ winners! We must promote the largest element from `mt2` (`--mt2.end()`) up into `mt1` to restore the balance.

### The Code Implementation
```cpp
#include <iostream>
#include <set>
using namespace std;

struct DynamicTopK {
    int K;
    multiset<int> mt1; // The Top K elements
    multiset<int> mt2; // The remaining elements
    long long sumK;

    void init(int _K) {
        K = _K;
        sumK = 0;
        mt1.clear();
        mt2.clear();
    }

    // Time Complexity: O(log N)
    void insert(int x) { 
        mt1.insert(x);
        sumK += x;

        // If we have too many winners, demote the smallest one
        if (mt1.size() > K) {
            auto it = mt1.begin(); // Smallest in mt1
            sumK -= *it;
            mt2.insert(*it);       // Demote to mt2
            mt1.erase(it);         // Remove from mt1
        }
    }

    // Time Complexity: O(log N)
    void remove(int x) { 
        // 1. Is it a Winner?
        if (mt1.find(x) != mt1.end()) {
            mt1.erase(mt1.find(x));
            sumK -= x;
        } 
        // 2. Or is it on the Bench?
        else if (mt2.find(x) != mt2.end()) {
            mt2.erase(mt2.find(x));
        }

        // 3. Rebalance! If mt1 lost a member, promote the best from mt2
        if (mt1.size() < K && !mt2.empty()) {
            auto it = mt2.end();
            it--; // Largest element in mt2
            
            int val = *it;
            mt1.insert(val); // Promote to mt1
            sumK += val;
            
            mt2.erase(it);   // Remove from mt2
        }
    }

    // Time Complexity: O(1)
    long long getSum() { 
        return sumK;
    }
};
```

> 🚨 **The CP Trap: Multiset Erase by Value vs Iterator**
> Notice how the deletion code strictly uses `mt1.erase(mt1.find(x))` instead of `mt1.erase(x)`. 
> **This is critical!** If you write `mt1.erase(5)`, C++ will find and destroy **EVERY SINGLE INSTANCE** of the number 5 in the multiset! If there were three 5s, all three are deleted, permanently corrupting your size logic and `sumK` math. By passing the exact *iterator* returned by `find(x)`, C++ guarantees it only deletes a single instance.

</READING_WIDGET>
