<VIDEO_WIDGET>

<VIDEO_ID>3520</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Implementing a Stack Using an Array

Imagine a stack of heavy cafeteria trays. You can only add a new tray to the **top** of the stack, and you can only take a tray off from the **top**. You can't just magically pull out the third tray from the bottom without causing a massive crash!

This is exactly how a **Stack** data structure operates. It follows the **LIFO** (Last-In, First-Out) principle. The last element you push onto the stack is the very first one you pop off.

While the *concept* of a stack is universal, we can build it under the hood using two different foundational data structures: **Arrays** and **Linked Lists**. Let's dive into both!

---


The easiest way to build a stack is by using a standard Array. We just need to keep track of a `top` variable that points to the index of the highest element.

To implement this, we need:
1. An integer array (`arr`) to store the actual elements.
2. A `capacity` variable to define the absolute maximum size of the stack.
3. A `top` variable to track the current top element. (Initially set to `-1` to indicate the stack is completely empty).

### Core Operations

- **Push (`O(1)`)**: Adds an item. If `top == capacity - 1`, the stack is full (**Stack Overflow**). Otherwise, increment `top` and add the element.
- **Pop (`O(1)`)**: Removes an item. If `top == -1`, the stack is empty (**Stack Underflow**). Otherwise, return the element at `top` and decrement `top`.
- **Peek (`O(1)`)**: Returns the element at `top` without removing it.
- **isEmpty / isFull (`O(1)`)**: Simply checks if `top == -1` or `top == capacity - 1`.

### Code Implementation (Fixed-Size Array)

```cpp
#include <iostream>
using namespace std;

class ArrayStack {
    int* arr;       // Array to store elements
    int capacity;   // Maximum size
    int top;        // Index of top element

public:
    // Constructor
    ArrayStack(int cap) {
        capacity = cap;
        arr = new int[capacity];
        top = -1;
    }

    void push(int x) {
        if (top == capacity - 1) {
            cout << "Stack Overflow!\n";
            return;
        }
        arr[++top] = x;
    }

    int pop() {
        if (top == -1) {
            cout << "Stack Underflow!\n";
            return -1;
        }
        return arr[top--]; // Return element, then decrement top
    }

    int peek() {
        if (top == -1) {
            cout << "Stack is Empty\n";
            return -1;
        }
        return arr[top];
    }

    bool isEmpty() {
        return top == -1;
    }
    
    bool isFull() {
        return top == capacity - 1;
    }
};
```

> 🚨 **The Limitation:** A fixed-size array stack can completely run out of space! If you try to push elements beyond its `capacity`, you hit a `Stack Overflow`. In modern C++, you can seamlessly fix this by using a `std::vector` instead of a raw pointer array, creating a **Dynamic Size Stack** that automatically scales behind the scenes!

---

> 🚀 **Next Up:** Our Array-based Stack is incredibly fast, but its fixed capacity makes it dangerously rigid. Let's solve the dreaded "Stack Overflow" by **Implementing a Stack using a Dynamic Linked List**!

</READING_WIDGET>
