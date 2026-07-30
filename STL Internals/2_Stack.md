<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# How `std::stack` Actually Works

> *When you create a Stack in C++, what is actually being created in memory? If you look closely at the C++ STL documentation, you'll realize that a Stack does not technically exist as a standalone data structure! Let's explore the concept of "Container Adaptors."*

---

## 1. The Container Adaptor Secret

In C++, a `std::stack` is **not** an independent data structure. It does not have its own unique memory management, pointers, or node systems. 

Instead, it is a **Container Adaptor**. This means it is simply a lightweight "wrapper" placed over an existing STL container (like a Vector, Deque, or List). The wrapper simply restricts your access to the underlying container, hiding everything except the Last-In, First-Out (LIFO) operations.

For example, a Stack restricts you to only using the back of the array. It renames `push_back()` to `push()`, `back()` to `top()`, and `pop_back()` to `pop()`.

> 🚨 **The CP Trap: You Cannot Iterate!**
> Because a Stack is a strict LIFO wrapper, it intentionally hides the `.begin()` and `.end()` iterators of the underlying container. You cannot use a for loop to print a stack! The only way to view elements is to repeatedly call `top()` and then `pop()`, destroying the stack in the process.

---

## 2. What is the Default Underlying Container?

If you declare `stack<int> st;`, what container is it wrapping?
By default, the C++ STL builds a Stack on top of a **`std::deque`**! (We will explore exactly how Deques work internally in a later module, but for now, know that they allocate memory in smaller chunks to avoid the massive $O(N)$ reallocation penalty of Vectors).

Why not a Vector?
Imagine you are using a `std::stack` backed by a `std::vector`. You push 1 million elements, and the vector fills its capacity. When you push the 1,000,001st element, the vector must halt your program, allocate a massive new array, and copy 1 million elements over. This single `push()` suddenly took $O(N)$ time instead of $O(1)$. 
In systems programming, this sudden latency spike is unacceptable.

Because a `std::deque` allocates memory in smaller chunks, it **never** copies old elements when expanding. Every single `push()` is strictly $O(1)$, making it the perfect, lag-free backing for a Stack.

---

## 3. Customizing the Backing Container

Because a Stack is just a wrapper, the C++ STL allows you to completely swap out the underlying engine! You just pass the desired container as the second template argument.

```cpp
#include <iostream>
#include <stack>
#include <vector>
#include <list>
using namespace std;

int main() {
    // 1. A Stack backed by a Deque (The Default)
    stack<int> default_stack; 
    
    // 2. A Stack backed by a Vector (Better cache locality!)
    stack<int, vector<int>> vector_stack;
    
    // 3. A Stack backed by a Doubly Linked List (True O(1) guaranteed, bad cache)
    stack<int, list<int>> list_stack;
    
    return 0;
}
```

> 💡 **CP Insight: When to swap the engine?**
> In competitive programming, a `std::deque` is slightly slower than a `std::vector` because it is broken into chunks (Cache Misses). Since a Stack only adds and removes from the *back*, it never needs `push_front()`. Therefore, defining your stack as `stack<int, vector<int>>` will often run **faster** than the default stack!

---

## 4. Under the Hood: The Code (Simplified)

To prove that a Stack is just a wrapper, here is what the actual STL implementation looks like conceptually. Notice how the class doesn't manage any pointers or memory itself—it just forwards all the work to the underlying container!

```cpp
// The template accepts the element type, and defaults the container to a deque!
template <typename T, typename Container = std::deque<T>>
class MyStack {
private:
    // The actual data structure doing the heavy lifting
    Container c; 

public:
    // Is the stack empty? Just ask the container!
    bool empty() {
        return c.empty();
    }

    // Push an element? Just call push_back on the container!
    void push(T value) {
        c.push_back(value);
    }

    // Pop an element? Just call pop_back on the container!
    void pop() {
        c.pop_back();
    }

    // Look at the top? Just look at the back of the container!
    T top() {
        return c.back();
    }
};
```

> 💡 **Systems Insight: Why does `pop()` return `void`?**
> If `pop()` removed the element and returned it by value, it would have to invoke a Copy Constructor. If your system is low on memory and that copy throws an exception, the element was already deleted from the stack, but you never received it—the data is permanently lost! By forcing you to read the data via `top()` (which returns a safe reference) before destroying it with a `void pop()`, C++ guarantees Strong Exception Safety.

---

## 5. Summary of STL `std::stack`

- **Data Structure Type:** Container Adaptor (Wrapper)
- **Default Underlying Container:** `std::deque`
- **Time Complexity:** $O(1)$ for push, pop, top
- **Memory Management:** None (Handled entirely by the underlying container)

> 🚀 **Next Up:** A Stack uses LIFO logic (Last-In, First-Out). What about a Queue, which uses FIFO logic (First-In, First-Out)? Let's see how `std::queue` is built under the hood!

</READING_WIDGET>
