<VIDEO_WIDGET>

<VIDEO_ID>3554</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Deque (Double-Ended Queue) Data Structure

> *Welcome to the STL! Instead of manually shifting arrays, the C++ Standard Template Library provides the Deque to instantly handle data at both ends.*

Think about waiting in a normal queue: you enter at the back and exit at the front. But what if you wanted a more flexible line? Imagine a ticket counter where VIPs can cut straight to the front of the line, or where someone at the absolute back of the line can change their mind and leave without waiting. 

In Computer Science, this flexible, two-way line is exactly what we call a **Deque** (pronounced "deck"), which stands for **Double-Ended Queue**.

---

## 1. The Best of Both Worlds

A Deque is effectively a hybrid between a Stack and a Queue. It allows you to perform operations at **both** the Front and the Back of the container. 

You can push to the front, push to the back, pop from the front, and pop from the back.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/6abe26e5-50ec-44a5-bd5f-31fbf2c95525.jpg" alt="Deque Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Core Operations

Just like Stacks and Queues, restricting how we access the data makes a Deque incredibly fast.

1. **Push Back (`push_back(x)`):** Adds element `x` to the back of the deque in **$O(1)$ time**.
2. **Push Front (`push_front(x)`):** Adds element `x` to the front of the deque in **$O(1)$ time**.
3. **Pop Back (`pop_back()`):** Removes the element from the back of the deque in **$O(1)$ time**.
4. **Pop Front (`pop_front()`):** Removes the element from the front of the deque in **$O(1)$ time**.
5. **Front (`front()`):** Returns the value of the first element in **$O(1)$ time**.
6. **Back (`back()`):** Returns the value of the last element in **$O(1)$ time**.
7. **Size (`size()`):** Returns the total number of elements in **$O(1)$ time**.
8. **IsEmpty (`empty()`):** Checks if the deque has zero elements in **$O(1)$ time**.
9. **Random Access (`dq[i]`):** Unlike standard Queues or Stacks, a C++ Deque allows you to instantly read or modify any element at any index in **$O(1)$ time**!

> 🚨 **The CP Trap: Popping an Empty Deque**
> Exactly like a Stack or Queue, calling `.pop_front()`, `.pop_back()`, `.front()`, or `.back()` on an empty Deque will cause a fatal **Segmentation Fault** and instantly crash your program! Always verify the deque isn't empty first.

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;

    dq.push_back(10);  // Deque: [10]
    dq.push_back(20);  // Deque: [10, 20]
    dq.push_front(5);  // Deque: [5, 10, 20]
    dq.push_front(1);  // Deque: [1, 5, 10, 20]

    cout << "Front element is: " << dq.front() << "\n"; // Prints 1
    cout << "Back element is: " << dq.back() << "\n";   // Prints 20

    dq.pop_front(); // Removes 1 from the front. Deque: [5, 10, 20]
    dq.pop_back();  // Removes 20 from the back. Deque: [5, 10]

    cout << "Size of Deque is: " << dq.size() << "\n"; // Prints 2

    // Secure pop
    if (!dq.empty()) {
        cout << "New Front element is: " << dq.front() << "\n"; // Prints 5
    }

    return 0;
}
```

---

## 3. Why Do We Need Deques?

If a Stack is LIFO and a Queue is FIFO, a Deque is the ultimate flexible buffer. It is used when you need constant time $O(1)$ insertions and deletions at **both** ends of your data.

> 💡 **CP Insight:** The absolute most important use case for a Deque in Competitive Programming is the **Sliding Window Maximum** (or Minimum) problem. By maintaining a monotonic order of elements in the Deque, you can find the maximum value in a moving window in $O(1)$ time per step!

---

## 4. Practice Problem: Palindrome Checker (Easy)

**The Problem:** Given a string, determine if it is a palindrome (reads the same forwards and backwards).
**The Direct Application:** A Deque perfectly models this! We can push all characters into the Deque, and then simultaneously `.pop_front()` and `.pop_back()` to compare the ends. If they ever mismatch, it's not a palindrome.

### The Code (C++)

```cpp
#include <iostream>
#include <deque>
#include <string>
using namespace std;

bool isPalindrome(string s) {
    deque<char> dq;
    
    // Push all characters into the Deque
    for (char c : s) {
        dq.push_back(c);
    }
    
    // Compare front and back until 0 or 1 character remains
    while (dq.size() > 1) {
        if (dq.front() != dq.back()) {
            return false; // Mismatch found!
        }
        dq.pop_front();
        dq.pop_back();
    }
    
    return true; // It's a palindrome!
}
```

---

> 🚀 **Next Up:** Now that you've mastered Stacks, Queues, and Deques, it's time to explore data structures that automatically sort data for you. Let's dive into the **Priority Queue**!

</READING_WIDGET>