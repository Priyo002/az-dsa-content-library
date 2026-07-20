<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Set Data Structure

> *Tired of writing loops to check for duplicate numbers? The C++ STL provides the Set to instantly deduplicate your data and answer existence queries in milliseconds.*

Imagine you have a magic bag. No matter how many identical red balls you throw into it, when you open the bag, there is always exactly one red ball inside. Furthermore, the bag somehow automatically organizes everything inside it from smallest to largest.

In Computer Science, this unique, auto-organizing container is called a **Set**. 

A Set is a mathematical concept translated into code: it is a collection of distinct elements. 

---

## 1. Set vs Unordered Set

In C++, you actually have two different types of Sets at your disposal. Choosing the correct one is absolutely critical for Competitive Programming because they operate entirely differently under the hood!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/975d792a-f8d4-495d-ac36-b7dab69b698f.jpg" alt="Set vs Unordered Set Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### `std::set` (Ordered Set)
- **The Engine:** Powered by a balanced Binary Search Tree (usually a Red-Black Tree).
- **The Guarantee:** Elements are ALWAYS kept in strictly sorted (ascending) order.
- **The Cost:** Because it has to maintain a complex tree structure, inserting, deleting, or finding an element takes **$O(\log N)$ Time**.

### `std::unordered_set` (Unordered Set)
- **The Engine:** Powered by a Hash Table.
- **The Guarantee:** Elements are scattered randomly in buckets. There is absolutely no order.
- **The Cost:** Because it relies on direct mathematical hashing, inserting, deleting, or finding an element takes blazing fast **$O(1)$ Average Time**.

> 💡 **CP Insight: Which one should you use?**
> If you just need to check "Have I seen this number before?" or "Remove all duplicates," ALWAYS use `unordered_set` for that lightning-fast $O(1)$ time. 
> Only use `set` if you explicitly need the data to be retrieved in **sorted order**, or if you need to perform binary-search style queries like `lower_bound()`.

> 🚨 **The CP Trap: Anti-Hash Tests**
> While `unordered_set` is $O(1)$ on average, its worst-case time complexity is $O(N)$. In competitive programming, platforms often have anti-hash test cases designed to force collisions and TLE your code. If you must use an `unordered_set` to avoid $O(\log N)$ overhead, you should implement a custom hash function. Otherwise, play it safe and use `std::set`!

---

## 2. Core Operations

Both sets share the exact same syntax for their core operations. The only difference is the underlying time complexity.

1. **Insert (`insert(x)`):** Adds element `x` into the set in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered). If `x` already exists, the set simply ignores the command.
2. **Erase (`erase(x)`):** Removes element `x` from the set in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
3. **Count (`count(x)`):** Returns `1` if `x` is in the set, and `0` if it is not in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
4. **Find (`find(x)`):** Returns an iterator to `x` if it exists, or `set.end()` if it doesn't in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
5. **Size (`size()`):** Returns the total number of unique elements in **$O(1)$ time** for both.

### The Code (C++)

```cpp
#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

int main() {
    // === 1. Ordered Set ===
    set<int> orderedSet;
    orderedSet.insert(50);
    orderedSet.insert(10);
    orderedSet.insert(30);
    orderedSet.insert(10); // Duplicate! Will be silently ignored.

    cout << "Ordered Set: ";
    for (int x : orderedSet) {
        cout << x << " "; // Guaranteed to print: 10 30 50
    }
    cout << "\n";

    // === 2. Unordered Set ===
    unordered_set<int> hashSet;
    hashSet.insert(50);
    hashSet.insert(10);
    hashSet.insert(30);
    hashSet.insert(10); // Duplicate! Will be silently ignored.

    cout << "Unordered Set: ";
    for (int x : hashSet) {
        cout << x << " "; // Might print: 30 50 10 (Order is completely random!)
    }
    cout << "\n";

    // === 3. Fast Lookups ===
    if (hashSet.count(30)) {
        cout << "30 is in the set!\n"; // O(1) time
    }

    return 0;
}
```

---

## 3. Advanced Ordered Set Operations

Because `std::set` is sorted, it unlocks powerful Binary Search capabilities that an `unordered_set` simply cannot do.

1. **`lower_bound(x)`:** Returns an iterator to the *first element that is $\ge x$*.
2. **`upper_bound(x)`:** Returns an iterator to the *first element that is strictly $> x$*.

This allows you to find the "next largest available number" in exactly $O(\log N)$ time, which is heavily tested in advanced Competitive Programming rounds!

> ⚠️ **Syntax Warning:** 
> Always use the member function `orderedSet.lower_bound(x)` which runs in $O(\log N)$. NEVER use the global algorithm `std::lower_bound(orderedSet.begin(), orderedSet.end(), x)`. Because a set does not have random access iterators, the global algorithm will quietly degrade to $O(N)$ time and TLE your solution!

---

## 5. Practice Problem: Intersection of Two Arrays (Easy)

**The Problem:** Given two integer arrays, return an array of their intersection (the numbers that exist in both arrays). Each element in the result must be unique.
**The Direct Application:** The perfect job for a Set! We can instantly deduplicate the first array by tossing it into an `unordered_set`. Then, we loop through the second array and use `.count()` to check for matches in $O(1)$ time!

### The Code (C++)

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    // 1. Deduplicate nums1 into a set
    unordered_set<int> set1(nums1.begin(), nums1.end());
    vector<int> result;
    
    // 2. Check each element of nums2
    for (int num : nums2) {
        if (set1.count(num)) {
            result.push_back(num);
            
            // 3. Erase it so we don't push duplicates into the result!
            set1.erase(num);
        }
    }
    
    return result;
}
```

---

> 🚀 **Next Up:** You've learned how to store single values uniquely in a Set. But what if you need the sorted power of a Set, but also need to store duplicate values (like video game high scores)? Let's master the **Multiset** data structure!

</READING_WIDGET>
