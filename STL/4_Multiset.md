<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Multiset Data Structure

> *Sometimes you need the strict sorting of a Set, but you can't afford to lose duplicate data. The STL Multiset bridges this gap, giving you the best of both worlds!*

In the previous lesson, we learned that a `std::set` is incredibly powerful because it automatically sorts everything in $O(\log N)$ time. But there was one major limitation: **it strictly rejects duplicates.**

What if you are tracking the high scores of a video game? If two players both score `10,000` points, you can't just delete one of them! You need a data structure that maintains the perfect sorted order of a Binary Search Tree, but *allows* duplicate values to coexist peacefully.

Enter the **Multiset**.

---

## 1. What is a Multiset?

A `std::multiset` is essentially identical to a `std::set`, with one defining difference: **Multiple elements can have the exact same value.**

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/a5ae58f5-f322-4d92-b19a-90ab86b6f32e.jpg" alt="Multiset Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Because it is still powered by a balanced Binary Search Tree under the hood, all core operations (Insert, Delete, Find) still run in **$O(\log N)$ Time**.

---

## 2. The Dangerous `erase()` Trap

While the operations in a multiset are identical to a set, there is one massive, hidden trap that catches almost every beginner in Competitive Programming when using `.erase()`.

When you tell a multiset to erase a specific value, e.g., `ms.erase(10)`, **it deletes ALL copies of that value.**

If your multiset is `[5, 10, 10, 10, 20]`, calling `ms.erase(10)` instantly deletes all three `10`s, leaving `[5, 20]`.

> 🚨 **CP Insight: How to erase just ONE copy?**
> If you only want to delete a single instance of `10`, you must find its iterator first, and then erase the iterator!
> 
> **Wrong way (Deletes all 10s):**
> `ms.erase(10);`
>
> **Right way (Deletes only one 10):**
> `ms.erase(ms.find(10));`

> 🚨 **The CP Trap: The `.count()` Time Limit Exceeded**
> In a multiset, `.count(x)` takes $O(\log N + K)$ time, where $K$ is the number of copies. If you have 100,000 copies of a number, `count()` will manually iterate through every single one of them, causing an $O(N)$ TLE!
> If you just want to check if an element exists, NEVER use `ms.count(x) > 0`. Always use `ms.find(x) != ms.end()` which is strictly $O(\log N)$.

### The Code (C++)

```cpp
#include <iostream>
#include <set> // multiset is included in the <set> header
using namespace std;

int main() {
    multiset<int> ms;
    
    ms.insert(10);
    ms.insert(20);
    ms.insert(10); // Duplicate allowed!
    ms.insert(10); // Duplicate allowed!

    cout << "Initial Multiset: ";
    for (int x : ms) cout << x << " "; // Prints: 10 10 10 20
    cout << "\n";

    // 1. Counting duplicates
    cout << "Count of 10s: " << ms.count(10) << "\n"; // Prints 3

    // 2. Erasing a single copy (SAFE method)
    ms.erase(ms.find(10));
    cout << "After erasing ONE 10: ";
    for (int x : ms) cout << x << " "; // Prints: 10 10 20
    cout << "\n";

    // 3. Erasing all copies (DANGEROUS method)
    ms.erase(10);
    cout << "After erasing ALL 10s: ";
    for (int x : ms) cout << x << " "; // Prints: 20
    cout << "\n";

    return 0;
}
```

---

## 3. Why Do We Need Multisets?

If you just want to count duplicates, a `std::map` (which we will learn next) is often better. However, a Multiset shines in one highly specific scenario: **Sliding Windows with changing minimums/maximums.**

In a previous lesson, we used a `Deque` to find the maximum in a sliding window in $O(N)$ time. However, that only worked because we *only* cared about the absolute maximum. 

If a problem requires you to find the **Median**, or query the exact sorted order of a dynamically changing window of numbers, a Deque fails. You MUST use a Multiset!

### Famous Multiset Applications:

1. **Dynamic Median Finding:** As numbers continuously arrive and leave, a multiset naturally keeps them sorted, making it easy to fetch the middle element.
2. **Event Scheduling overlaps:** If multiple events have the exact same start time, a multiset can store and sort all of them without overwriting data.
3. **Sliding Window Minimum/Maximum (Alternative):** If you struggle to implement the complex $O(N)$ Deque logic, a Multiset offers a simple $O(N \log K)$ alternative. Just insert the new element, erase the outgoing element's iterator, and the maximum is always `*ms.rbegin()`!

### Fetching the Min and Max in $O(1)$ Time:
Since the multiset is always sorted, the minimum is always at the front, and the maximum is always at the back.
```cpp
int min_val = *ms.begin();   // Smallest element
int max_val = *ms.rbegin();  // Largest element (Reverse Begin)
```

---

## 4. Practice Problem: Closest Number in a Data Stream (Medium)

**The Problem:** You are receiving a continuous stream of numbers. At any point, given a query number `X`, you must find the smallest number currently in your stream that is greater than or equal to `X`. (Duplicates are possible in the stream).
**The Direct Application:** This is the absolute bread-and-butter of a Multiset! Because a multiset automatically sorts the stream and handles duplicates, we can simply call `ms.lower_bound(X)` to find the closest valid number in exactly $O(\log N)$ time.

### The Code (C++)

```cpp
#include <iostream>
#include <set>
using namespace std;

class StreamQueries {
    multiset<int> ms;
    
public:
    // 1. Add a number to the stream in O(log N)
    void addNumber(int num) {
        ms.insert(num);
    }
    
    // 2. Find closest number >= X in O(log N)
    int getClosest(int x) {
        auto it = ms.lower_bound(x);
        
        if (it != ms.end()) {
            return *it; // Found a valid number!
        } else {
            return -1;  // No number is >= X
        }
    }
};
```

---

> 🚀 **Next Up:** You've mastered how to store and sort raw values. Now, what if you want to create a dictionary that links a unique "Name" to a "Score"? Let's dive into the **Map** data structure!

</READING_WIDGET>
