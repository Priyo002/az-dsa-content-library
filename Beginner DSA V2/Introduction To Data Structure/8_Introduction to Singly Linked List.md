<VIDEO_WIDGET>

<VIDEO_ID>3518</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to Singly Linked List

Imagine you're playing a massive treasure hunt game. You find a clue, and it doesn't just give you the prize—it gives you a piece of information and the exact coordinates of where to find the _next_ clue. You follow the chain, clue by clue, until you reach the end.

This is exactly how a **Linked List** works in computer science! Instead of storing everything in one massive, perfectly aligned row (like an Array), a Linked List scatters its data across memory. Each piece of data simply holds a "clue"—a pointer—telling the computer exactly where to find the next piece.

## Connection to Linear Data Structures

Like Arrays, Stacks, and Queues, a Linked List is a **Linear Data Structure**. This means the data is organized in a strict sequence. However, while arrays demand a single, continuous block of memory (which can be hard to find if your memory is highly fragmented), linked lists are incredibly flexible. They grab available memory blocks wherever they exist and magically link them all together.

> 💡 **Core Insight:** Arrays are rigid but allow instant access (like houses on a perfectly numbered street). Linked Lists are flexible but require sequential access (like following a treasure map). If you need to constantly add and remove elements without shifting everything else around, Linked Lists are your best friend!

---

In a **Singly Linked List**, each element is called a **Node**. A node contains two things:

1. The **Data** (the actual value you want to store).
2. The **Next Pointer** (the exact memory address of the next node in the chain).

The very first node is universally known as the **Head**, and the very last node points to `NULL` to signify the absolute end of the chain.

<img src="https://d3pdqc0wehtytt.cloudfront.net/academy-media/62/a7b10c0d-de88-446c-9e15-85d9b4a11b8e.png" alt="Singly Linked List Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Creating a Singly Linked List

Here is how you define and create a simple singly linked list in C++:

```cpp
#include <iostream>
using namespace std;

// Defining the Node structure
struct Node {
    int data;       // The value
    Node* next;     // Pointer to the next node

    // Constructor to easily create a new node
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

int main() {
    // 1. Create the standalone nodes
    Node* head = new Node(10);
    Node* second = new Node(20);
    Node* third = new Node(30);

    // 2. Link them together
    head->next = second;
    second->next = third;

    return 0;
}
```

### Operations on a Singly Linked List

Let's dive into how we manipulate a Singly Linked List.

#### Traversal

Traversal is the act of visiting every single node in the list. Start at the `head` and hop to the `next` pointer until you hit `NULL`.

- _Time Complexity_: `O(N)` (You have to visit $N$ elements).

```cpp
// Traverse and print the list
void traverseList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next; // Move to the next node
    }
    cout << "NULL" << endl;
}
```

#### Insertion

**At the Front (Head)**
Make the new node's `next` point to the current `head`, and then update the `head` to be the new node.

- _Time Complexity_: `O(1)` (Instant! No shifting needed).

```cpp
void insertAtFront(Node*& head, int val) {
    Node* newNode = new Node(val);
    newNode->next = head;
    head = newNode;
}
```

**At the Back (Tail)**
Traverse the list to find the very last node, and make its `next` point to the new node.

- _Time Complexity_: `O(N)` (Because you have to traverse to find the tail).

```cpp
void insertAtBack(Node*& head, int val) {
    Node* newNode = new Node(val);
    if (head == nullptr) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
}
```

**At Any Specific Position (0-indexed)**
Traverse the list to the node _just before_ the desired position. Rewire the previous node's `next` to point to the new node, and the new node's `next` to point to the rest of the chain.

- _Time Complexity_: `O(N)` (Due to traversal).

```cpp
void insertAtPosition(Node*& head, int val, int pos) {
    if (pos == 0) {
        insertAtFront(head, val);
        return;
    }
    Node* newNode = new Node(val);
    Node* temp = head;
    for (int i = 0; temp != nullptr && i < pos - 1; i++) {
        temp = temp->next;
    }
    if (temp == nullptr) return; // Position out of bounds

    newNode->next = temp->next;
    temp->next = newNode;
}
```

#### Deletion

**At the Front (Head)**
Simply move the `head` pointer to `head->next` and delete the old head.

- _Time Complexity_: `O(1)`

```cpp
void deleteFront(Node*& head) {
    if (head == nullptr) return;
    Node* toDelete = head;
    head = head->next;
    delete toDelete;
}
```

**At the Back (Tail)**
You must traverse the entire list to find the _second to last_ node, change its `next` to `nullptr`, and delete the last node.

- _Time Complexity_: `O(N)`

```cpp
void deleteBack(Node*& head) {
    if (head == nullptr) return;
    if (head->next == nullptr) {
        delete head;
        head = nullptr;
        return;
    }
    Node* temp = head;
    while (temp->next->next != nullptr) {
        temp = temp->next;
    }
    delete temp->next;
    temp->next = nullptr;
}
```

**At Any Specific Position**
Traverse to the node _just before_ the one you want to delete. Change its `next` pointer to skip over the target node.

- _Time Complexity_: `O(N)`

```cpp
void deleteAtPosition(Node*& head, int pos) {
    if (head == nullptr) return;
    if (pos == 0) {
        deleteFront(head);
        return;
    }
    Node* temp = head;
    for (int i = 0; temp != nullptr && i < pos - 1; i++) {
        temp = temp->next;
    }
    if (temp == nullptr || temp->next == nullptr) return; // Out of bounds

    Node* toDelete = temp->next;
    temp->next = temp->next->next;
    delete toDelete;
}
```

---

> 🚀 **Next Up:** A Singly Linked List is great, but its one-way street design makes moving backward impossible. Let's upgrade our nodes with a 'previous' pointer and explore the incredibly flexible **Doubly Linked List**!

</READING_WIDGET>
