<VIDEO_WIDGET>

<VIDEO_ID>362</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: LFU Cache

> *If the LRU Cache is the golden standard of interviews, the LFU (Least Frequently Used) Cache is the final boss. It tests your ability to maintain multiple simultaneous state architectures while forcing strict $O(1)$ time complexity.*

---

## 1. What is an LFU Cache?

While an LRU cache evicts data based purely on *Time* (oldest out), an **LFU Cache** evicts data based on *Popularity* (least accessed out).

**Operations we must support:**
1. `get(key)`: Return the value associated with the key. Using the key increases its frequency by 1.
2. `put(key, value)`: Insert the key-value pair. If it already exists, update its value. (Using the key increases its frequency by 1). 
3. **The Tie-Breaker:** If the cache is full and we need to evict, we delete the key with the lowest frequency. *If multiple keys share the exact same lowest frequency, we evict the one that is the Least Recently Used (LRU) among them!*

**The massive constraint:** Both `get` and `put` must run in strict **$O(1)$ Time Complexity**.

---

## 2. The $O(1)$ LFU Architecture

To achieve $O(1)$ across the board, we cannot just use a single Priority Queue (which would take $O(\log N)$ to sort by frequency). We need a multi-layered Hash Map architecture!

We need exactly **three structural components:**

1. **The Key Map:** `unordered_map<int, Node>`
   - Allows us to instantly jump to a key to get its value and its current frequency.
2. **The Frequency Map:** `unordered_map<int, std::list<int>>`
   - This maps a `frequency` integer to a **Doubly Linked List** of keys!
   - All keys that have been accessed exactly $F$ times live in the list at `freqMap[F]`.
   - Because it's a Doubly Linked List, it acts as a mini LRU Cache for that specific frequency! (Newest at the front, oldest at the back).
3. **The `min_freq` Variable:**
   - An integer that tracks the absolute lowest frequency currently in the cache. 
   - When it's time to evict, we instantly know to look at `freqMap[min_freq]` and delete the element at the back of its list!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/4fa046e4-9feb-46e6-ae0b-332ab12363b9.jpg" alt="LFU Cache Architecture Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### The Core Mechanics:
*   **When a node is accessed:** We find it in the Key Map, extract it from its current list in the Frequency Map (e.g., `freqMap[2]`), increment its frequency, and push it to the front of the next list (`freqMap[3]`).
*   **When `min_freq` updates:** If we extract the very last node from `freqMap[min_freq]`, and that list is now empty, it means the lowest frequency just leveled up! We must increment `min_freq++`.

---

## 3. The Code Implementation

> 💡 **The Elite STL Trick Returns**
> Just like we saw in the LRU Cache, implementing raw Doubly Linked List pointers here is a nightmare. By using `std::list` inside our Frequency Map, we can leverage STL iterators to erase nodes in strict $O(1)$ time!

```cpp
#include <unordered_map>
#include <list>
using namespace std;

// The core data wrapper
struct Node {
    int key;
    int value;
    int freq;
    list<int>::iterator list_it; // Pointer to where this key lives in the DLL
};

class LFUCache {
private:
    int capacity;
    int min_freq;
    
    // Key -> Node Data
    unordered_map<int, Node> keyMap; 
    
    // Frequency -> Doubly Linked List of Keys (Maintains LRU order per frequency)
    unordered_map<int, list<int>> freqMap; 

    // Helper: Upgrades a key's frequency in O(1)
    void updateFrequency(int key) {
        // 1. Get the node
        Node& node = keyMap[key];
        int current_freq = node.freq;
        
        // 2. Erase the key from its current frequency list
        freqMap[current_freq].erase(node.list_it);
        
        // 3. Check if the list we just erased from is completely empty
        if (freqMap[current_freq].empty()) {
            // If it was the minimum frequency, level it up!
            if (current_freq == min_freq) {
                min_freq++; 
            }
            // Delete the empty list from the hash map to prevent Memory Leaks!
            freqMap.erase(current_freq); 
        }
        
        // 4. Increment the node's frequency and move it to the new list
        node.freq++;
        freqMap[node.freq].push_front(key); // Push to front (Most Recently Used)
        
        // 5. Update the iterator pointer
        node.list_it = freqMap[node.freq].begin();
    }

public:
    LFUCache(int cap) {
        capacity = cap;
        min_freq = 0;
    }
    
    int get(int key) {
        if (keyMap.find(key) == keyMap.end()) {
            return -1; // Cache Miss
        }
        
        // Cache Hit: Update frequency and return value
        updateFrequency(key);
        return keyMap[key].value;
    }
    
    void put(int key, int value) {
        if (capacity == 0) return; // Edge case
        
        if (keyMap.find(key) != keyMap.end()) {
            // Key exists: Update value and increment frequency
            keyMap[key].value = value;
            updateFrequency(key);
        } else {
            // Check Capacity Eviction
            if (keyMap.size() >= capacity) {
                // Evict the Least Recently Used element from the min_freq list
                int evict_key = freqMap[min_freq].back(); // Oldest is at the back
                freqMap[min_freq].pop_back();
                keyMap.erase(evict_key);
            }
            
            // Insert New Key
            min_freq = 1; // A new key ALWAYS starts at frequency 1
            freqMap[1].push_front(key);
            
            // Save to Key Map
            keyMap[key] = {key, value, 1, freqMap[1].begin()};
        }
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** $O(1)$ for both `get` and `put`. Erasing from a `std::list` using an iterator is $O(1)$, and Hash Map access is $O(1)$.
*   **Space Complexity:** $O(C)$ where $C$ is the `capacity`. The Key Map stores exactly $C$ elements, and the collective size of all Doubly Linked Lists in the Frequency Map combined will also be exactly $C$.

> 💡 **Systems Insight: Iterator Invalidation**
> You might wonder: *"Why can't we use a `std::vector` or `std::deque` inside the Frequency Map to save cache locality?"*
> The answer lies in **Iterator Invalidation**. If we used a `std::vector`, pushing a new key might trigger a memory reallocation to a new location, which instantly invalidates all the `list_it` pointers stored in our Key Map! Because a `std::list` relies on individually allocated nodes, iterators to existing nodes remain mathematically stable forever, no matter how many other elements you add or remove.

## 4. Module Summary
- The LFU Cache evicts based on absolute lowest popularity.
- We must break ties using the LRU rule (Least Recently Used among the least frequently used).
- Achieving $O(1)$ operations requires three components: a Key Map, a Frequency Map mapped to Doubly Linked Lists, and a `min_freq` integer.
- Empty frequency buckets must be meticulously erased from memory to prevent long-term server memory leaks.

</READING_WIDGET>
