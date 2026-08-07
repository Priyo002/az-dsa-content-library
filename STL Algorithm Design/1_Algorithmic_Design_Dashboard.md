<VIDEO_WIDGET>

<VIDEO_ID>3593</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Structuring State

> _Algorithmic design is the systematic creation and optimization of data structures to solve specific computational problems. A well-designed algorithm encapsulates logic to handle massive streams of queries efficiently, ensuring simplicity and maintainability. Let's master the art of designing custom structs!_

---

## 1. The Dashboard Database

Imagine managing a server dashboard where you must dynamically process the following operations:

1. `Insert(x)`: Add a new user with value `x`.
2. `Remove(x)`: Remove a user with value `x`.
3. `Sum()`: Get the sum of all users in $O(1)$ time.
4. `GetMax()`: Retrieve the maximum user value in $O(1)$ time.
5. `GetDistinct()`: Get the number of _distinct_ values in $O(1)$ time.

### The Ultimate Weapon: `std::map`

To maintain $O(1)$ queries while supporting $O(\log N)$ dynamic insertions and deletions, we can wrap a `std::map` inside a custom `struct`.

- We maintain a global `cur_sum` variable that we update mathematically during insertion/removal.
- The `std::map` acts as a Frequency Map. Because it is backed by a Red-Black Tree, its keys are always perfectly sorted!

```cpp
#include <iostream>
#include <map>
using namespace std;

struct Dashboard {
    long long cur_sum = 0;
    map<int, int> mp; // Frequency Map: {value -> count}

    // Time: O(log N)
    void insert(int x) {
        cur_sum += x;
        mp[x]++;
    }

    // Time: O(log N)
    void remove(int x) {
        cur_sum -= x;
        mp[x]--;

        // Critical: Erase the key completely if frequency hits 0!
        if (mp[x] == 0) {
            mp.erase(x);
        }
    }

    // Time: O(1)
    long long sum() {
        return cur_sum;
    }

    // Time: O(1) Amortized
    int getmax() {
        // The map is sorted ascending. The last element is the maximum!
        auto it = mp.end();
        it--;
        return it->first;
    }

    // Time: O(1)
    int getdistinct() {
        // Because we erase keys when they hit 0, the size is exactly the distinct count!
        return mp.size();
    }
};
```

> 🚨 **The CP Trap: Map Zero-Frequency Ghosts**
> Notice the crucial `if (mp[x] == 0) { mp.erase(x); }` in the `remove` function.
> Beginners often just write `mp[x]--`. But in C++, if a key exists in a map with a value of `0`, the node still physically exists in the Red-Black tree! If you don't erase it, `getmax()` might return a deleted "ghost" value, and `getdistinct()` will return an artificially inflated size! You must explicitly erase empty keys.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/ed4c8c56-e0ed-4c56-b547-0710d4593592.jpg" alt="Map Ghost Node Trap" style="max-width: 100%; height: auto;" identifier="az-img-upload">

</READING_WIDGET>
