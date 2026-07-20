<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Priority Queue (Heap) Data Structure

> *In competitive programming, time is everything. The STL Priority Queue is your ultimate shortcut for automatically keeping data sorted without having to constantly call `sort()`.*

Imagine you are a doctor in an Emergency Room. Patients are constantly arriving. Do you treat them in the exact order they arrived (FIFO, like a normal Queue)? No! You treat the patient with the most severe injury first, regardless of when they walked through the door.

In Computer Science, a queue that automatically brings the "most important" element to the absolute front is called a **Priority Queue**. 

Behind the scenes, a Priority Queue is powered by a tree-like data structure called a **Heap**.

---

## 1. Max-Heap vs Min-Heap

By default, in C++, a Priority Queue acts as a **Max-Heap**. This means the largest numerical value automatically floats to the very top (the front). 

If you want the smallest element to be at the top instead, you can declare it as a **Min-Heap**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/da41ad92-5acd-4512-8d45-1521b15a1875.jpg" alt="Priority Queue Max Heap Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

Unlike Arrays or standard Queues, inserting an element into a Priority Queue isn't instantaneous ($O(1)$). Because it must maintain its internal sorted structure (the Heap), inserting or removing an element takes **$O(\log N)$ Time Complexity**.

---

## 2. Core Operations

1. **Push (`push(x)`):** Adds element `x` into the queue and internally shifts it to its correct sorted position in **$O(\log N)$** time.
2. **Pop (`pop()`):** Removes the absolute top element (the highest priority) from the queue and re-balances the remaining elements in **$O(\log N)$** time.
3. **Top (`top()`):** Returns the value of the highest priority element in **$O(1)$** time without removing it. Note: Unlike a standard queue, it is called `top()`, not `front()`.
4. **Size (`size()`):** Returns the total number of elements in **$O(1)$ time**.
5. **IsEmpty (`empty()`):** Checks if the queue has zero elements in **$O(1)$ time**.

> 🚨 **The CP Trap: Forgetting it's a Max-Heap by default**
> Beginners often forget that `priority_queue<int>` automatically sorts descending (Max-Heap). To make a Min-Heap (sorting ascending), you must use the slightly verbose syntax: `priority_queue<int, vector<int>, greater<int>>`.

### The Code (C++)

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // 1. Default Max-Heap (Largest at the top)
    priority_queue<int> maxHeap;
    
    maxHeap.push(10);
    maxHeap.push(50);
    maxHeap.push(5);
    maxHeap.push(100);

    cout << "Max-Heap Top: " << maxHeap.top() << "\n"; // Prints 100
    maxHeap.pop(); // Removes 100. The new top becomes 50!


    // 2. Min-Heap (Smallest at the top)
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    minHeap.push(10);
    minHeap.push(50);
    minHeap.push(5);
    minHeap.push(100);

    cout << "Min-Heap Top: " << minHeap.top() << "\n"; // Prints 5
    minHeap.pop(); // Removes 5. The new top becomes 10!

    return 0;
}
```

> 💡 **CP Optimization: $O(N)$ Heapify**
> If you already have a `vector<int> v` filled with numbers, do not use a for loop to push them into a Priority Queue one by one ($O(N \log N)$). Instead, pass the vector's iterators directly into the constructor! This builds the heap in strict $O(N)$ time:
> ```cpp
> vector<int> v = {10, 50, 5, 100};
> priority_queue<int> maxHeap(v.begin(), v.end()); // O(N) time!
> ```

> ⚙️ **Storing Pairs:** 
> In competitive programming, you will often store pairs (e.g., `priority_queue<pair<int, int>>`). By default, C++ will prioritize based on the **first** element of the pair. If there is a tie, it breaks the tie using the **second** element!

---

## 3. Why Do We Need Priority Queues?

Why not just use an Array and call `sort()` every time?
Calling `sort()` takes $O(N \log N)$ time. If you insert $N$ items one by one and sort after every single insertion, it takes $O(N^2 \log N)$ overall. 
A Priority Queue handles $N$ insertions dynamically in just **$O(N \log N)$** total time!

> 💡 **CP Insight:** If a problem requires you to repeatedly find the "minimum", "maximum", "cheapest", or "closest" element amidst a constantly changing stream of data, a Priority Queue is almost always the answer.

---

## 4. Practice Problem: Last Stone Weight (Easy)

**The Problem:** You are given an array of stone weights. Every turn, you smash the two heaviest stones together. If they have the same weight, both are destroyed. If one is heavier, the remaining weight goes back into the pile. What is the weight of the last remaining stone?
**The Direct Application:** A pure Max-Heap simulation! We load all stones into a Priority Queue, `.pop()` the top two to smash them, and `.push()` the remainder back in until the queue is empty or has 1 stone.

### The Code (C++)

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int lastStoneWeight(vector<int>& stones) {
    // 1. Build a Max-Heap from the array in O(N) time!
    priority_queue<int> maxHeap(stones.begin(), stones.end());
    
    // 2. Simulate the smashing process
    while (maxHeap.size() > 1) {
        int y = maxHeap.top(); // Heaviest
        maxHeap.pop();
        int x = maxHeap.top(); // Second Heaviest
        maxHeap.pop();
        
        if (y > x) {
            maxHeap.push(y - x); // Push the remainder back
        }
    }
    
    // 3. Return the last stone (or 0 if none remain)
    return maxHeap.empty() ? 0 : maxHeap.top();
}
```

---

> 🚀 **Next Up:** Priority Queues are incredibly fast for fetching the absolute maximum or minimum, but what if you need to search for a specific value anywhere in the middle? Let's explore the power of the **Set** data structure!

</READING_WIDGET>
