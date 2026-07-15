<VIDEO_WIDGET>

<VIDEO_ID>3517</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# The Queue Data Structure

Think about the last time you waited in line to buy a movie ticket. The rules were simple and fair: the first person to arrive in the line is the absolute first person to get a ticket and leave the line. If someone new arrives, they must go to the very back of the line and wait their turn.

In Computer Science, this "fair waiting line" is exactly what we call a **Queue**.

---

## 1. The FIFO Principle

While a Stack strictly uses LIFO (Last-In-First-Out), a Queue strictly uses the **FIFO** principle:
**First In, First Out**

A Queue requires two separate access points. You insert new elements exclusively at the **Back** (or "Rear") of the queue, and you remove elements exclusively from the **Front** of the queue.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d4e5c437-55ac-49e0-8118-229d189ca89b.png" alt="Queue Fifo Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Core Operations

Just like the Stack, restricting how we access the data makes a Queue incredibly fast. Every fundamental operation operates in exactly **$O(1)$ Time Complexity**.

1. **Push / Enqueue (`push(x)`):** Adds element `x` to the absolute Back of the queue.
2. **Pop / Dequeue (`pop()`):** Removes the element currently sitting at the Front of the queue.
3. **Front (`front()`):** Returns the value of the first element waiting in line _without_ removing it.
4. **Back (`back()`):** Returns the value of the last element that just joined the line.
5. **Size (`size()`):** Returns the total number of elements currently waiting in the queue.
6. **IsEmpty (`empty()`):** Checks if the queue has zero elements.

> 🚨 **The CP Trap: Popping an Empty Queue**
> Exactly like a Stack, calling `.pop()`, `.front()`, or `.back()` on an empty Queue will cause a fatal **Segmentation Fault** and instantly crash your program! Always verify the queue isn't empty first.

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;

    q.push(10); // Queue: [Front -> 10 <- Back]
    q.push(20); // Queue: [Front -> 10, 20 <- Back]
    q.push(30); // Queue: [Front -> 10, 20, 30 <- Back]

    cout << "Front element is: " << q.front() << "\n"; // Prints 10
    cout << "Back element is: " << q.back() << "\n";   // Prints 30

    q.pop(); // Removes 10 from the front. Queue: [20, 30]

    cout << "Size of Queue is: " << q.size() << "\n"; // Prints 2

    // Secure pop
    if (!q.empty()) {
        cout << "New Front element is: " << q.front() << "\n"; // Prints 20
    }

    return 0;
}
```

---

## 3. Why Do We Need Queues?

If a Stack is used for "undoing" recent actions, what is a Queue used for?
**Fairness, Scheduling, and Level-by-Level processing.**

When data is coming in faster than you can process it, you store it in a Queue so that the oldest, most urgent data gets handled first.

> 💡 **CP Insight:** The absolute most important use case for a Queue in Competitive Programming is **Breadth-First Search (BFS)**. If you need to search a maze or a graph level-by-level (exploring all immediate neighbors before moving further away), a Queue is the mandatory data structure.

### Famous Queue Applications:

1. **Printer Spooling:** If 5 people in an office hit "Print" at the same time, the printer puts the documents in a Queue and prints them in the exact order they were received.
2. **CPU Task Scheduling:** Your computer's processor uses Queues to decide which background app gets access to the CPU next.
3. **Customer Support Hotlines:** "Your call is important to us. You are currently 3rd in line."

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d96dd8f1-719d-45e0-834d-167c321a4a24.png" alt="Cpu Task Queue" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Solving "Number of Recent Calls"

Let's look at the absolute quintessential beginner Queue problem: **Number of Recent Calls**.

**The Problem:** You are tasked with building a system that counts how many requests have happened in the past 3000 milliseconds.
You have a function `ping(int t)` that receives a ping at time `t`. You need to return the number of pings that have occurred exactly within the time frame `[t - 3000, t]`.

**Examples:**

- `ping(1)` $\rightarrow$ Returns `1` (Ping at `t=1` is inside `[-2999, 1]`)
- `ping(100)` $\rightarrow$ Returns `2` (Pings at `1, 100` are inside `[-2900, 100]`)
- `ping(3001)` $\rightarrow$ Returns `3` (Pings at `1, 100, 3001` are inside `[1, 3001]`)
- `ping(3002)` $\rightarrow$ Returns `3` (Pings at `100, 3001, 3002`. The ping at `t=1` is completely outside the `[2, 3002]` window and is discarded!)

### The Intuition

Why is a Queue the perfect data structure here? Because of the **"Oldest Data Expires First"** rule.
As time moves forward, the oldest pings expire and need to be thrown away.
"Oldest element in, is the first element out" is the exact definition of **First-In-First-Out (FIFO)**!

### The Algorithm

1. Every time a `ping(t)` arrives, `push` it to the Back of the queue.
2. The current valid time window is `[t - 3000, t]`.
3. Check the `front()` of the queue (which holds the absolute oldest ping). If that oldest ping happened _before_ `t - 3000`, it has expired!
4. `pop()` the expired ping from the front. Repeat this until the `front()` ping is safely inside the 3000ms window.
5. Finally, the queue now strictly contains only valid pings. Simply return the `size()` of the queue!

### The Code (C++)

```cpp
#include <queue>
using namespace std;

class RecentCounter {
private:
    queue<int> q; // Our FIFO time tracker

public:
    RecentCounter() {
        // Queue starts empty
    }

    int ping(int t) {
        // 1. Add the new ping to the back of the line
        q.push(t);

        // 2. Remove all expired pings from the front of the line
        // We use a while loop because multiple old pings might have expired!
        while (!q.empty() && q.front() < t - 3000) {
            q.pop();
        }

        // 3. The queue size now represents the number of valid recent calls
        return q.size();
    }
};
```

---

> 🚀 **Next Up:** Stacks and Queues are amazing, but they often rely on strict, contiguous memory. What if we want to scatter our data across memory and connect them like a chain? Let's unlock the power of the **Singly Linked List**!

</READING_WIDGET>
