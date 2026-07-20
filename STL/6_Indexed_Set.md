<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Indexed Set (Policy-Based Data Structure)

> *When the standard STL containers aren't enough, C++ hides a secret weapon. Policy-Based Data Structures (PBDS) give you the sorting power of a Set, combined with the index access of an Array.*

In competitive programming, there are times when the standard C++ STL falls short. What happens when you have a constantly changing collection of numbers, and you need to rapidly find:
1. The K-th smallest element?
2. How many elements are strictly smaller than X?

We have learned that `std::set` is fantastic at keeping elements sorted and finding them in $O(\log N)$ time. However, it has one fatal flaw in C++: **You cannot access elements by their index.**

If you have a set of `[10, 20, 30, 40]`, you cannot simply ask C++ for `set[2]` to get `30`. You would have to iterate through the set one by one, which takes massive $O(N)$ time.

What if you needed to find the median element of a massive, constantly changing list? Or find exactly how many numbers are strictly smaller than $X$?

Enter the "secret weapon" of C++ Competitive Programmers: the **Policy-Based Data Structure (PBDS)**, commonly referred to as the **Indexed Set**.

---

## 1. What is an Indexed Set?

An Indexed Set is not part of the standard C++ `<set>` library. It is a GNU C++ extension that provides a highly augmented Binary Search Tree. 

It does everything a normal `std::set` does (insert, delete, find in $O(\log N)$), but it tracks the subtree sizes internally. This grants it **two literal superpowers** that standard sets do not possess.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/fed5192f-883c-458f-b0c3-f4e3277f0aaf.jpg" alt="Indexed Set Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Superpower 1: `find_by_order(k)`
This function returns an iterator to the $k^{th}$ smallest element in the set (using 0-based indexing) in **$O(\log N)$ time**.
* *Example: If the set is `[5, 10, 15, 20]`, `find_by_order(2)` returns an iterator pointing to `15`.*

### Superpower 2: `order_of_key(x)`
This function returns the exact integer count of elements that are strictly smaller than `x` in **$O(\log N)$ time**.
* *Example: If the set is `[5, 10, 15, 20]`, `order_of_key(12)` returns `2` (because only 5 and 10 are smaller).*

---

## 2. The (Ugly) Syntax

Because it is a compiler extension and not part of standard C++, the syntax to import and define an Indexed Set is notoriously ugly and long. Most Competitive Programmers simply memorize it or keep it in their template file.

> 🚨 **CP Trap: The Headers**
> You MUST include the `<ext/pb_ds/...>` headers and the `using namespace __gnu_pbds;` directive, otherwise the compiler will have absolutely no idea what you are doing!

### The Code (C++)

```cpp
#include <iostream>
// 1. Mandatory PBDS Headers
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

// 2. The massive Macro definition (memorize this!)
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;

int main() {
    indexed_set s;
    
    // Inserts elements exactly like a normal set
    s.insert(10);
    s.insert(20);
    s.insert(30);
    s.insert(40);
    s.insert(50);
    // Set is now: [10, 20, 30, 40, 50]

    // === SUPERPOWER 1: find_by_order ===
    // Find the 2nd index (0-based)
    auto it = s.find_by_order(2); 
    cout << "The element at index 2 is: " << *it << "\n"; // Prints 30

    // 🚨 Safe querying (Preventing Segmentation Faults)
    auto out_of_bounds = s.find_by_order(100); 
    if (out_of_bounds != s.end()) {
        cout << *out_of_bounds << "\n";
    } else {
        cout << "Out of bounds!\n";
    }

    // === SUPERPOWER 2: order_of_key ===
    // Count how many elements are strictly smaller than 35
    int count = s.order_of_key(35);
    cout << "Elements strictly smaller than 35: " << count << "\n"; // Prints 3 (10, 20, 30)

    // It works even if the number isn't in the set!
    cout << "Elements strictly smaller than 100: " << s.order_of_key(100) << "\n"; // Prints 5

    return 0;
}
```

---

## 3. Creating an Indexed *Multiset*

Just like a normal set, the standard `indexed_set` strictly rejects duplicates. But what if you want to allow duplicates (like a `std::multiset`) while keeping the superpowers?

You might think you can just change `less<int>` to `less_equal<int>`. **Do not do this!** It fundamentally breaks the `erase()` function in PBDS.

Instead, the universally accepted CP trick to create an Indexed Multiset is to use a `pair<int, int>` as the data type!
The first integer is your actual value, and the second integer is a unique ID (usually the current time or a rising counter) to force every pair to be mathematically unique.

```cpp
// 1. Define the PBDS using a pair
typedef tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update> indexed_multiset;

int main() {
    indexed_multiset ms;
    int timer = 0; // Unique ID generator

    // Insert two 10s using unique IDs
    ms.insert({10, timer++});
    ms.insert({10, timer++});

    // Both 10s are successfully stored!
    cout << "Size: " << ms.size() << "\n"; // Prints 2
    
    // How to query the Multiset:
    // To find how many numbers are strictly less than 10, 
    // we use a dummy ID of 0 (the absolute lowest possible ID).
    int count = ms.order_of_key({10, 0}); 
    cout << "Elements strictly smaller than 10: " << count << "\n";
    
    return 0;
}
```

---

## 4. Practice Problem: Count Inversions (Medium)

**The Problem:** Given an array, find how many pairs of indices $(i, j)$ exist such that $i < j$ and $nums[i] > nums[j]$. In simpler terms: how many numbers to the right are strictly smaller than the current number?
**The Direct Application:** This is the quintessential PBDS problem! We iterate through the array backwards. For each number, we use `.order_of_key(num)` to instantly count how many numbers currently in the tree are strictly smaller than `num`. Then, we `.insert(num)` into the tree. 

### The Code (C++)

```cpp
#include <iostream>
#include <vector>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;

int countInversions(vector<int>& nums) {
    indexed_set pbds;
    int inversions = 0;
    
    // Iterate backwards
    for (int i = nums.size() - 1; i >= 0; i--) {
        // Count how many elements currently in the PBDS are smaller
        inversions += pbds.order_of_key(nums[i]);
        
        // Insert current element for the next iterations
        pbds.insert(nums[i]);
    }
    
    return inversions;
}
```

</READING_WIDGET>
