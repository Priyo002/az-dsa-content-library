<VIDEO_WIDGET>

<VIDEO_ID>3521</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Implementing a Stack Using a Linked List

What if you don't know exactly how big your stack needs to be, and you don't want to use an array? You can implement a stack using a **Singly Linked List**!

In this approach, the `head` of the linked list acts as the `top` of the stack. Every time you push an element, you simply insert a new node at the _front_ of the list. Every time you pop, you delete the node at the _front_.

### Why use a Linked List?

- **No strict capacity limits**: It grows dynamically as long as your computer has free memory. You never have to worry about a "Stack Overflow" due to an arbitrary fixed capacity limit!
- **Fast operations**: Because we only ever add or remove from the `head` (the top), every operation is strictly `O(1)` time complexity.

### Code Implementation (Linked List)

```cpp
#include <iostream>
using namespace std;

// Defining the Linked List Node
class Node {
public:
    int data;
    Node* next;

    Node(int x) {
        data = x;
        next = nullptr;
    }
};

class LinkedListStack {
    Node* top;  // Pointer to the top of the stack (the head of the list)
    int count;  // To keep track of the current size

public:
    LinkedListStack() {
        top = nullptr;
        count = 0;
    }

    // Push: Insert at the front of the linked list
    void push(int x) {
        Node* temp = new Node(x);
        temp->next = top;
        top = temp;
        count++;
    }

    // Pop: Remove from the front of the linked list
    int pop() {
        if (top == nullptr) {
            cout << "Stack Underflow!\n";
            return -1;
        }
        Node* temp = top;
        top = top->next;
        int val = temp->data;

        delete temp; // Free memory!
        count--;
        return val;
    }

    // Peek: Look at the front element
    int peek() {
        if (top == nullptr) {
            cout << "Stack is Empty\n";
            return -1;
        }
        return top->data;
    }

    bool isEmpty() {
        return top == nullptr;
    }

    int size() {
        return count;
    }
};
```

> 💡 **Core Insight:** If you just need a simple, incredibly fast stack and know the maximum size in advance, an **Array Stack** is incredibly CPU cache-friendly and performant. But if your data size is unpredictable and highly volatile, a **Linked List Stack** provides perfect dynamic memory management without any resizing overhead!

---

> 🚀 **Next Up:** You've built a robust, dynamic Stack. Now it's time to shift gears. Let's see how we can apply these exact same foundational concepts to **Implement a Queue using an Array**!

</READING_WIDGET>
