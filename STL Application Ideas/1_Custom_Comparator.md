<VIDEO_WIDGET>

<VIDEO_ID>3587</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Custom Comparators in C++

> *By default, C++ sorts numbers from smallest to largest. But what if you want to sort them largest to smallest? Or what if you want to sort a list of Students by their grades, and then by their names alphabetically if their grades tie? Let's master the art of Custom Comparators.*

---

## 1. The Anatomy of a Comparator

A comparator is simply a custom rule that answers one question for the C++ STL: **"Given two elements `A` and `B`, should `A` be placed strictly before `B`?"**

- If your rule returns `true`, the STL will put `A` before `B`.
- If your rule returns `false`, the STL will put `B` before `A` (or treat them as equivalent).

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/b5f947f1-66dc-42b8-b293-c3be542e2317.jpg" alt="Comparator Logic" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Using Functions for `std::sort`

The `std::sort` algorithm is incredibly flexible. It accepts a standard boolean function as its third argument.

### Example: Sorting in Descending Order
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// The rule: Should 'a' come before 'b'?
bool compareDescending(const int& a, const int& b) {
    return a > b; // Put 'a' first if it is strictly greater than 'b'
}

int main() {
    vector<int> v = {1, 5, 2, 9, 3};
    sort(v.begin(), v.end(), compareDescending);
    
    // Result: [9, 5, 3, 2, 1]
}
```

### Example: Complex Multi-Level Sorting
Imagine you are sorting a leaderboard of players. You want to sort by Score (Descending). But if two players have the exact same score, you want to sort by their Name (Ascending alphabetically).

```cpp
struct Player {
    string name;
    int score;
};

bool comparePlayers(const Player& a, const Player& b) {
    if (a.score != b.score) {
        return a.score > b.score; // 1st Priority: Sort by score descending
    }
    return a.name < b.name;       // 2nd Priority: If scores tie, sort by name ascending
}

int main() {
    vector<Player> v = {{"Alice", 50}, {"Bob", 100}, {"Charlie", 50}};
    sort(v.begin(), v.end(), comparePlayers);
    
// Result: Bob (100), Alice (50), Charlie (50)
}
```

> 🚨 **The CP Trap: The `const&` Performance Killer (TLE)**
> Notice how we pass parameters as `const T& a, const T& b` instead of just `T a, T b` (pass-by-value). 
> If you pass a massive `std::string` or nested `std::vector` by value, the comparator will trigger a deep copy of the entire object every single time it compares two elements! Since a sorting algorithm compares elements $O(N \log N)$ times, this will instantly trigger a Time Limit Exceeded (TLE) error in contests and cause massive lag in production systems. **Always pass comparator arguments by `const reference`!**

> 🚨 **The CP Trap: The Strict Weak Ordering Rule**
> The absolute most common cause of mysterious `Segmentation Faults` in C++ sorting is writing `a >= b` instead of `a > b`. 
> 
> The C++ STL strictly requires a mathematical property called **Strict Weak Ordering**. This means if two elements are mathematically equal, your comparator **MUST** return `false`. If you return `true` for equal elements, the underlying QuickSort pointers inside `std::sort` will cross bounds and infinitely loop, crashing your entire program!

---

## 3. The Modern Engine: Lambda Expressions

While writing separate functions outside of `main()` works, it costs precious seconds during a contest. Furthermore, in modern software engineering environments, scattering loose comparator functions across a massive codebase pollutes the global namespace and makes code hard to read.

Since **C++11**, the modern, default way to write a custom comparator for `std::sort` is using an inline **Lambda Expression**.

```cpp
int main() {
    vector<Player> v = {{"Alice", 50}, {"Bob", 100}, {"Charlie", 50}};
    
    // The Lambda is defined directly inside the sort function!
    sort(v.begin(), v.end(), [](const Player& a, const Player& b) {
        if (a.score != b.score) return a.score > b.score;
        return a.name < b.name;
    });
}
```
This is significantly faster to type and keeps your logic perfectly encapsulated where it is actually used.

---

## 4. Using Structs (Functors) for Data Structures

While `std::sort` is happy to accept standard functions (and Lambdas!), complex data structures like `std::priority_queue`, `std::set`, and `std::map` are built using **C++ Templates**. They require a C++ *Type*, not a function pointer.

To pass a custom rule to a data structure, you must create a `struct` (or class) and overload the function call operator `operator()`. This object is known as a **Functor**.

### Custom Priority Queue
By default, `std::priority_queue` is a Max-Heap. Here is how you use a Functor to flip it into a Min-Heap.

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// The Functor
struct CompareMin {
    bool operator()(const int& a, const int& b) {
        // Priority Queues evaluate "Should 'a' have LOWER priority than 'b'?"
        return a > b; 
    }
};

int main() {
    // 1. Data Type
    // 2. Underlying Container
    // 3. Custom Comparator Functor Type
    priority_queue<int, vector<int>, CompareMin> pq;
    
    pq.push(10);
    pq.push(2);
    pq.push(5);
    
    cout << pq.top(); // Prints 2!
}
```

> 💡 **CP Insight: The Priority Queue Flipper**
> Notice that for a `std::priority_queue`, the logic feels "backwards". To make a Min-Heap, our comparator returns `a > b`! 
> 
> This is because the STL Priority Queue uses the comparator to determine if element `a` should be pushed *down* the heap (lower priority). If `a > b`, `a` has lower priority than `b` and sinks. Therefore, the smallest elements float up to the `.top()`!
>
> *(Note: For simple Min-Heaps of primitives, C++ provides a built-in functor in the `<functional>` library: `priority_queue<int, vector<int>, greater<int>> pq;`)*

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/120d9605-8fcf-4ccd-a137-ed66e26f0a5a.jpg" alt="Priority Queue Min-Heap Functor" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 5. Custom Sets, Maps, and Multisets

Because `std::set`, `std::map`, `std::multiset`, and `std::multimap` are all implemented using Red-Black Trees, they rely heavily on comparisons to balance the tree branches. You can pass a Functor to them exactly like a Priority Queue!

```cpp
// Sort a set in descending order
struct CompareSet {
    // Important: Sets and Maps require the operator to be 'const'!
    bool operator()(const int& a, const int& b) const {
        return a > b;
    }
};

int main() {
    // Pass the functor TYPE as the second template argument
    set<int, CompareSet> s;
    s.insert(1);
    s.insert(10);
    s.insert(5);
    
    for (int x : s) {
        cout << x << " "; // Prints: 10 5 1
    }
}
```
*(Notice the `const` keyword on the operator! The internal Red-Black tree demands read-only safety when navigating nodes, so your Functor must promise not to modify any variables).*

---

## 6. Where Can You NOT Use Custom Comparators?

Custom comparators are strictly for algorithms and data structures that rely on **Sorting** (like `std::sort`, Red-Black Trees, and Heaps). 

You **cannot** pass a Custom Comparator to an `std::unordered_set` or `std::unordered_map`! 
Because these data structures use Hash Tables instead of trees, they do not care if `A` is "greater than" `B`. They only care about two things:
1. **Hash Function:** Which mathematical bucket should this element go into?
2. **Equality (`==`):** Is this element exactly identical to another element in the bucket?

To customize an unordered container, you have to write a Custom Hash Function, which is an entirely different (and much more complex) mathematical process!

---

## 7. Summary

- **`std::sort`:** Accepts standard boolean functions and **Lambdas**.
- **Data Structures (`priority_queue`, `set`, `map`):** Require a `struct` Functor that overloads `operator()`.
- **Pass By Reference:** Always use `const T&` to prevent massive $O(N \log N)$ deep-copy penalties (TLE).
- **The Golden Rule:** Always return `false` for equality to prevent `Segmentation Faults` (Strict Weak Ordering).

</READING_WIDGET>
