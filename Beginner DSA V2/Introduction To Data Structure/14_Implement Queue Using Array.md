<VIDEO_WIDGET>

<VIDEO_ID>3522</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Implementing a Queue Using an Array

Imagine waiting in line to buy tickets for a blockbuster movie. The person who arrived first gets to buy their ticket first. If you arrive last, you have to stand at the very back of the line and wait for everyone in front of you to finish.

This is exactly how a **Queue** data structure works! It follows the **FIFO** (First-In, First-Out) principle. You enter at the **rear** (Enqueue) and leave from the **front** (Dequeue).

Just like stacks, we can build queues using either **Arrays** or **Linked Lists**. However, as we'll see, using an array for a queue introduces some tricky and expensive problems! Let's explore both approaches.

---

To implement a queue using a standard fixed-size array, we need to keep track of a few things:

1. An integer array (`arr`) to store the elements.
2. A `capacity` variable to track the maximum number of elements the queue can hold.
3. A `size` variable to track the current number of elements inside the queue.

### Core Operations

- **Enqueue (Insert)**: Add an element to the back of the queue (at index `size`). If `size == capacity`, the queue is full (**Queue Overflow**).
  - _Time Complexity_: `O(1)`
- **Dequeue (Remove)**: Remove the element at the front of the queue (at index `0`). However, because it's an array, removing index `0` leaves an empty gap at the beginning! To fix this, we must **shift every single remaining element one position to the left**. If `size == 0`, the queue is empty (**Queue Underflow**).
  - _Time Complexity_: `O(N)` 🚨 _(Due to shifting)_
- **getFront / getRear**: Return the elements at index `0` and index `size - 1` respectively.
  - _Time Complexity_: `O(1)`

### Code Implementation (Simple Array Queue)

```cpp
#include <iostream>
using namespace std;

class ArrayQueue {
    int* arr;
    int capacity;
    int size;

public:
    ArrayQueue(int c) {
        capacity = c;
        arr = new int[capacity];
        size = 0;
    }

    // Enqueue: Adds an element to the rear
    void enqueue(int x) {
        if (size == capacity) {
            cout << "Queue Overflow!\n";
            return;
        }
        arr[size] = x;
        size++;
    }

    // Dequeue: Removes the front element (Requires shifting!)
    void dequeue() {
        if (size == 0) {
            cout << "Queue Underflow!\n";
            return;
        }
        // Shift all elements one step to the left
        for (int i = 1; i < size; i++) {
            arr[i - 1] = arr[i];
        }
        size--;
    }

    // Get Front
    int getFront() {
        if (size == 0) {
            cout << "Queue is empty!\n";
            return -1;
        }
        return arr[0];
    }

    // Get Rear
    int getRear() {
        if (size == 0) {
            cout << "Queue is empty!\n";
            return -1;
        }
        return arr[size - 1];
    }
};
```

> 🚨 **The Terrible `O(N)` Limitation:** Did you notice that `dequeue()` uses a `for` loop? Shifting every element in an array takes `O(N)` time. This is painfully slow! In the real world, if we _must_ use an array for a queue (to take advantage of CPU caching), we use a clever technique called a **Circular Queue** to ensure both enqueue and dequeue are `O(1)`. But for now, let's look at a much simpler way to get `O(1)` speed!

---

> 🚀 **Next Up:** The simple array-based Queue works, but that $O(N)$ shifting time is a massive bottleneck. Let's eliminate that inefficiency completely by **Implementing a Queue using a Linked List**!

</READING_WIDGET>
