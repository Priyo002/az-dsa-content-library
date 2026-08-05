
<READING_WIDGET>
# Logic
</READING_WIDGET>

<VIDEO_WIDGET>

<VIDEO_ID>470</VIDEO_ID>

</VIDEO_WIDGET>


<READING_WIDGET>
# Code
</READING_WIDGET>

<VIDEO_WIDGET>

<VIDEO_ID>471</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Running Mean, Median, and Mode

> *The ability to process live data streams and instantly extract statistical metrics is the absolute core of Data Engineering, Analytics, and High-Frequency Trading. This module combines three distinct data architectures into a single, cohesive engine.*

---

## 1. The Challenge

You are given a dynamically changing array that starts empty. You must process a stream of up to $10^5$ queries supporting:
1. `insert x`: Add an element to the array.
2. `remove x`: Remove an element from the array (guaranteed to exist).
3. `getMean`: Return the average of all current elements.
4. `getMedian`: Return the middle element (or average of the two middle elements if the count is even).
5. `getMode`: Return the most frequent element (if tied, return the smallest).

**The Modulo Constraint:** If the array is empty, return `-1`. If an answer is a fraction $\frac{P}{Q}$, you must return $(P \times Q^{-1}) \pmod{10^9+7}$, where $Q^{-1}$ is the Modular Multiplicative Inverse of $Q$.

---

## 2. Breaking Down the Three Engines

To achieve high performance, we cannot re-calculate these metrics from scratch on every query. We must use **Running States**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/6a1c7e35-3751-4791-87fc-c66c0180f122.jpg" alt="Running Metrics Data Analytics Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Engine 1: The Running Mean
The mean is simply `Sum / Count`. 
- **State variables:** A `long long sum` and an `int count`.
- **Insert `x`:** `sum = (sum + x) % MOD`, `count++`
- **Remove `x`:** `sum = (sum - x + MOD) % MOD`, `count--`
- **getMean:** We apply Fermat's Little Theorem to divide under a modulo: `(sum * modInverse(count, MOD)) % MOD`.

### Engine 2: The Running Median (Two Multisets)
To find the middle element dynamically, we split the data into two halves.
We use two `std::multiset<int>`:
- `left_set`: Stores the smaller half of the numbers (acts as a Max-Heap).
- `right_set`: Stores the larger half of the numbers (acts as a Min-Heap).

**The Balancing Rule:** `left_set` must either be equal in size to `right_set`, or exactly $1$ element larger. 
- If total elements are odd, the median is the largest element in the `left_set` (which is `*left_set.rbegin()`).
- If even, the median is the average of the largest in `left_set` and the smallest in `right_set`.

> 🚨 **The C++ `multiset::erase` Trap**
> If you call `left_set.erase(x)`, C++ will brutally delete **every single instance** of `x` in the multiset! Since we only want to remove one instance, we must pass an *iterator*: `left_set.erase(left_set.find(x))`.

### Engine 3: The Running Mode (Frequency Sets)
We need to know the highest frequency, and break ties by choosing the smallest element.
We use two structures:
1. `map<int, int> freq`: Tracks the frequency of each element.
2. `set<pair<int, int>> mode_tracker`: Stores `{-frequency, element}`.

**Why negative frequency?** A `std::set` sorts ascending by default. By negating the frequency, the highest frequency becomes the most negative number, forcing it to the absolute front of the set (`set.begin()`). If frequencies tie, it naturally falls back to sorting the element ascending!
- **Insert `x`:** Find `x` in the set, erase it, increment its frequency in the map, and re-insert it with its new `{-freq, x}`.
- **getMode:** Simply return `mode_tracker.begin()->second`.

---

## 3. The Code Implementation

```cpp
#include <iostream>
#include <set>
#include <map>
using namespace std;

const int MOD = 1000000007;

// Modular Exponentiation to find (base^exp) % mod
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

// Modular Multiplicative Inverse using Fermat's Little Theorem
long long modInverse(long long n) {
    return power(n, MOD - 2);
}

class MetricsEngine {
private:
    // Mean State
    long long total_sum = 0;
    int count = 0;
    
    // Median State
    multiset<int> left_set;  // Smaller half
    multiset<int> right_set; // Larger half
    
    // Mode State
    map<int, int> freq;
    set<pair<int, int>> mode_tracker; // {-frequency, element}

    // Helper to balance the Median multisets
    void balance() {
        // Left can have at most 1 more element than Right
        while (left_set.size() > right_set.size() + 1) {
            auto it = prev(left_set.end()); // Largest in left
            right_set.insert(*it);
            left_set.erase(it);
        }
        while (right_set.size() > left_set.size()) {
            auto it = right_set.begin(); // Smallest in right
            left_set.insert(*it);
            right_set.erase(it);
        }
    }

public:
    void insert(int x) {
        // 1. Update Mean
        total_sum = (total_sum + (x % MOD)) % MOD;
        count++;
        
        // 2. Update Median
        if (left_set.empty() || x <= *left_set.rbegin()) {
            left_set.insert(x);
        } else {
            right_set.insert(x);
        }
        balance();
        
        // 3. Update Mode
        if (freq[x] > 0) {
            mode_tracker.erase({-freq[x], x});
        }
        freq[x]++;
        mode_tracker.insert({-freq[x], x});
    }
    
    void remove(int x) {
        // 1. Update Mean
        // The Negative Modulo Trap
        // Safely modulo x first, as C++ preserves negative signs on modulo!
        total_sum = (total_sum - (x % MOD) + MOD) % MOD;
        count--;
        
        // 2. Update Median
        auto it_left = left_set.find(x);
        if (it_left != left_set.end()) {
            left_set.erase(it_left); // Erase by iterator!
        } else {
            right_set.erase(right_set.find(x));
        }
        balance();
        
        // 3. Update Mode
        mode_tracker.erase({-freq[x], x});
        freq[x]--;
        if (freq[x] > 0) {
            mode_tracker.insert({-freq[x], x});
        } else {
            // The Ghost Frequency Memory Leak
            // Actively erase keys that hit 0 to prevent infinite RAM bloat!
            freq.erase(x);
        }
    }
    
    long long getMean() {
        if (count == 0) return -1;
        return (total_sum * modInverse(count)) % MOD;
    }
    
    long long getMedian() {
        if (count == 0) return -1;
        
        if (left_set.size() > right_set.size()) {
            return *left_set.rbegin() % MOD;
        } else {
            // Even count: Average of the two middle elements
            long long a = *left_set.rbegin();
            long long b = *right_set.begin();
            long long mid_sum = (a + b) % MOD;
            return (mid_sum * modInverse(2)) % MOD;
        }
    }
    
    int getMode() {
        if (count == 0) return -1;
        return mode_tracker.begin()->second;
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** 
    *   `insert / remove`: $O(\log N)$ due to maintaining the elements in the `multiset` (Median) and `set` (Mode). 
    *   `getMean`: $O(\log \text{MOD})$ because of the `modInverse` exponentiation.
    *   `getMedian / getMode`: $O(1)$. We just look at the `rbegin()` / `begin()` iterators of our sets!
*   **Space Complexity:** $O(N)$. We store each unique frequency state and every element in our sets.

## 4. Module Summary
- True Data Analytics engines cannot recompute metrics from scratch; they maintain highly optimized **Running States**.
- The **Running Median** relies on balancing a pair of `std::multiset` containers to ensure the middle elements are always instantly accessible at the boundaries.
- The **Running Mode** brilliantly exploits C++ sorting mechanics by storing `{-freq, element}` inside a `std::set`, pushing the highest frequency (and lowest tied value) to the absolute front in $O(\log N)$ time.
- Fractions in CP output must be converted using the Modular Multiplicative Inverse ($P \times Q^{-1} \pmod M$).

</READING_WIDGET>
