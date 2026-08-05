<VIDEO_WIDGET>

<VIDEO_ID>361</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: LRU Cache

> *The LRU Cache is arguably the single most famous Algorithmic Design question in FAANG interviews. It requires you to seamlessly combine two foundational data structures to overcome the physical limitations of both.*

---

## 1. What is an LRU Cache?

A **Cache** is a small, ultra-fast memory storage used to hold frequently accessed data. Because cache memory is physically small, it has a strict `capacity` limit. When the cache is completely full and a new piece of data needs to be stored, we must **evict** (delete) an existing piece of data to make room.

The **Least Recently Used (LRU)** eviction policy states: *The piece of data that has gone the longest time without being accessed should be the one evicted.*

**Operations we must support:**
1. `get(key)`: Return the value associated with the key. (This counts as "using" the key).
2. `put(key, value)`: Insert the key-value pair. If it already exists, update its value. If capacity is exceeded, evict the LRU key. (This counts as "using" the key).

**The massive constraint:** Both `get` and `put` must run in strict **$O(1)$ Time Complexity**.

---

## 2. Why Single Data Structures Fail

If we just use an **Array / Vector**:
- We can maintain order (newest at the back, oldest at the front).
- But searching for a key takes $O(N)$. Shifting elements after eviction takes $O(N)$. This is too slow.

If we just use a **Hash Map (`std::unordered_map`)**:
- We get $O(1)$ key lookups and insertions!
- But Hash Maps are entirely *unordered*. We have absolutely no way to know which key is the oldest or newest!

We must combine them.

---

## 3. The Golden Architecture: Hash Map + Doubly Linked List

To achieve $O(1)$ across the board, we build a hybrid structure.

1. **A Doubly Linked List (DLL):** We use a DLL to physically maintain the order of usage. The `Head` of the DLL represents the Most Recently Used data. The `Tail` of the DLL represents the Least Recently Used data.
    - *Why Doubly Linked?* Because if we want to extract a node from the middle of the list and move it to the Head in $O(1)$ time, we must have pointers to both its `prev` and `next` nodes to stitch the gap back together!

2. **A Hash Map:** We use a Hash Map that stores `Key -> Node*`.
    - This allows us to instantly jump to any physical node in the DLL in $O(1)$ time without having to traverse the list!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7faf210d-aabe-4180-83e8-e20ace7bc477.jpg" alt="LRU Cache Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### The Core Mechanics:
*   **When a node is accessed (`get` or `put`):** We use the Hash Map to instantly find the node in $O(1)$. We then extract it from the DLL, and append it to the Head. It is now the Most Recently Used.
*   **When capacity is exceeded (`put`):** We look at the Tail of the DLL. That is our Least Recently Used node. We delete it from the DLL, delete its key from the Hash Map, and insert our new node at the Head.

---

## 4. The Code Implementation

> 🚨 **The CP Trap: Edge Case Nightmares**
> Extracting a node from a DLL requires updating `node->prev->next` and `node->next->prev`. If the node happens to be exactly at the Head or exactly at the Tail, these pointers might be `nullptr`, causing a massive **Segmentation Fault**.
> **The Pro Move:** Always initialize two "Dummy" nodes: a permanent `head` and a permanent `tail`. Real data is inserted strictly *between* them. This mathematically guarantees that no real node will ever have a `nullptr` neighbor, completely eliminating edge cases!

```cpp
#include <unordered_map>
using namespace std;

// The DLL Node
struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> cache; // Key -> Node pointer
    Node* head; // Dummy Head
    Node* tail; // Dummy Tail

    // Helper: Remove an existing node from the DLL
    void removeNode(Node* node) {
        Node* prevNode = node->prev;
        Node* nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }

    // Helper: Insert a node right after the Dummy Head (Most Recently Used)
    void insertNodeAtHead(Node* node) {
        Node* headNext = head->next;
        head->next = node;
        node->prev = head;
        node->next = headNext;
        headNext->prev = node;
    }

    // Helper: Move an accessed node to the front
    void moveToHead(Node* node) {
        removeNode(node);
        insertNodeAtHead(node);
    }

public:
    LRUCache(int cap) {
        capacity = cap;
        // Initialize Dummy Nodes
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }
    
    // 🚨 Production Trap: Prevent Memory Leaks!
    ~LRUCache() {
        Node* curr = head;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1; // Cache Miss
        }
        
        // Cache Hit: Move to Most Recently Used position
        Node* node = cache[key];
        moveToHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // Key exists: Update value and mark as recently used
            Node* node = cache[key];
            node->val = value;
            moveToHead(node);
        } else {
            // Key doesn't exist: Create new node
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            insertNodeAtHead(newNode);
            
            // Check Capacity
            if (cache.size() > capacity) {
                // Evict the LRU node (the one right before Dummy Tail)
                Node* lruNode = tail->prev;
                removeNode(lruNode);
                cache.erase(lruNode->key); // Delete from Hash Map
                delete lruNode; // Prevent Memory Leak
            }
        }
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** $O(1)$ for both `get` and `put`. Hash Map lookups are $O(1)$, and pointer manipulation in a DLL is strict $O(1)$.
*   **Space Complexity:** $O(C)$ where $C$ is the `capacity`. The Hash Map and the DLL both store exactly $C$ elements.

---

## 5. The Elite STL Trick: `std::list::splice`

> 💡 **The Interview Flex**
> FAANG interviewers love to ask: *"Can you implement this using only standard STL containers instead of raw pointers?"* 
> Many candidates don't realize that C++ already has a Doubly Linked List built-in: `std::list`. More importantly, `std::list` has a magical function called `splice()`, which extracts a node from the middle of a list and moves it to the front in strict $O(1)$ time, manipulating the internal pointers perfectly for you!

Here is how you write a production-ready LRU Cache in under 30 lines of code:

```cpp
#include <unordered_map>
#include <list>
using namespace std;

class LRUCacheSTL {
private:
    int capacity;
    list<pair<int, int>> dll; // Store {key, value}
    
    // Hash Map: Key -> Iterator pointing to the DLL Node
    unordered_map<int, list<pair<int, int>>::iterator> cache;

public:
    LRUCacheSTL(int cap) : capacity(cap) {}

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        
        // splice(destination_iterator, list_to_move_from, node_iterator_to_move)
        // Moves the node to the front in O(1) time!
        dll.splice(dll.begin(), dll, cache[key]);
        return cache[key]->second;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            cache[key]->second = value;
            dll.splice(dll.begin(), dll, cache[key]); // Move to front
        } else {
            dll.push_front({key, value});
            cache[key] = dll.begin();
            
            if (cache.size() > capacity) {
                // Evict the back (oldest) element
                cache.erase(dll.back().first);
                dll.pop_back();
            }
        }
    }
};
```

</READING_WIDGET>
