<VIDEO_WIDGET>

<VIDEO_ID>3523</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Implementing a Queue Using a Linked List

A linked list provides a far superior and simpler approach to building a basic queue. Because a queue modifies both ends of the data (inserting at the back, deleting from the front), we just need to maintain **two pointers** on our linked list:

1. `front`: Points to the head of the linked list (used for Dequeue).
2. `rear`: Points to the tail of the linked list (used for Enqueue).

### Why use a Linked List?

- **No shifting required**: We just rewire a pointer to remove the front element, leaving the rest of the queue untouched!
- **Fast operations**: Both Enqueue and Dequeue are strictly `O(1)` time complexity.
- **Dynamic Size**: No need to define a maximum `capacity` like we do in arrays!

### Code Implementation (Linked List Queue)

```cpp
#include <iostream>
using namespace std;

// Defining the Linked List Node
class Node {
public:
    int data;
    Node* next;

    Node(int new_data) {
        data = new_data;
        next = nullptr;
    }
};

class LinkedListQueue {
private:
    Node* front;  // Points to the first element
    Node* rear;   // Points to the last element
    int currSize; // Tracks the number of elements

public:
    LinkedListQueue() {
        front = nullptr;
        rear = nullptr;
        currSize = 0;
    }

    bool isEmpty() {
        return front == nullptr;
    }

    // Enqueue: Add to the rear (O(1))
    void enqueue(int new_data) {
        Node* newNode = new Node(new_data);

        // If queue is empty, the new node is both front and rear
        if (isEmpty()) {
            front = rear = newNode;
        } else {
            // Add the new node to the end and update the rear pointer
            rear->next = newNode;
            rear = newNode;
        }
        currSize++;
    }

    // Dequeue: Remove from the front (O(1))
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow!\n";
            return -1;
        }

        Node* temp = front;
        int removedData = temp->data;

        // Move front to the next node
        front = front->next;

        // If the queue becomes empty after dequeue, rear must also become nullptr
        if (front == nullptr) {
            rear = nullptr;
        }

        delete temp; // Free memory!
        currSize--;

        return removedData;
    }

    // Get Front (O(1))
    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty!\n";
            return -1;
        }
        return front->data;
    }

    // Get Size
    int size() {
       return currSize;
    }
};
```

> 💡 **Core Insight:** A Linked List is the most natural and efficient way to implement a basic Queue. By managing both ends (`front` and `rear`) with simple pointers, it entirely eliminates the disastrous `O(N)` array shifting problem and ensures blazing-fast `O(1)` operations across the board!

---

> 🚀 **Up Next:** Incredible work! You have successfully mastered the theory and implementation of Stacks, Queues, and Linked Lists. It's time to cement these skills. Dive into the final **Practice Problems** and prove your mastery!

</READING_WIDGET>
