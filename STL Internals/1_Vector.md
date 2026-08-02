<VIDEO_WIDGET>

<VIDEO_ID>3574</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# How `std::vector` Actually Works

> *In C++, a standard array (`int arr[10]`) has a fixed size. If you try to add an 11th element, your program crashes. Yet, `std::vector` seems to magically grow infinitely as you `push_back` elements. How does it do this without destroying performance?*

---

## 1. The Illusion of Infinite Memory

A `std::vector` does not actually possess "infinite" memory. Under the hood, a vector is just a standard, fixed-size C-style array allocated on the **heap** (dynamic memory).

To maintain the illusion of infinite growth, the vector keeps track of three internal pointers (or integers):
1. **Size:** The number of elements actually stored right now.
2. **Capacity:** The total number of memory slots currently allocated.
3. **Data Pointer:** A pointer to the underlying raw array in memory.

As long as `Size < Capacity`, `push_back` is an instant, $O(1)$ operation. The vector just places the new element in the next available slot and increments `Size`.

---

## 2. The Reallocation Penalty (When Size == Capacity)

What happens when the vector is completely full, and you call `push_back` one more time?
Because memory must be perfectly **contiguous** (continuous in RAM), the vector cannot just "borrow" the next slot in memory (another program might be using it!). 

Instead, it must undergo a massive internal operation called **Reallocation**:
1. It asks the OS to allocate a brand new, significantly larger chunk of memory somewhere else.
2. It copies every single element from the old array into the new array.
3. It deletes the old array to free up the memory.
4. It finally inserts your new element.

This reallocation step takes **$O(N)$ time** because it has to copy $N$ elements. If this happened on every single `push_back`, the vector would run in $O(N^2)$ time overall and be utterly useless!

> 🚨 **The CP Trap: Iterator Invalidation**
> When a vector undergoes Reallocation, it deletes the old array. This means all existing pointers, references, and iterators to the vector's elements are instantly invalidated!
> If you store a reference to an element (`int& x = v[0];`), and then call `push_back()` which triggers a reallocation, trying to read `x` later will cause a massive memory corruption bug!

---

## 3. Amortized $O(1)$ and The Growth Factor

To prevent constant reallocations, vectors don't just grow by 1 slot. They multiply their capacity using a **Growth Factor**. 

> 💡 **CP / Interview Insight: GCC vs MSVC**
> When a vector fills up, how much bigger is the new array? 
> - On **GCC** (used by Codeforces, LeetCode, and Linux), the growth factor is **2.0x**. If capacity is 16, it jumps to 32.
> - On **MSVC** (Visual Studio / Windows), the growth factor is **1.5x**. If capacity is 16, it jumps to 24. 

Because the vector doubles its size, reallocations happen exponentially less often. 
- The 1st reallocation copies 1 element.
- The 2nd copies 2 elements.
- The 3rd copies 4 elements...
- The 10th copies 1024 elements...

Mathematically, the sum of this geometric series is bounded by $2N$. So, inserting $N$ elements takes $2N$ operations total. When we divide $2N$ total operations by $N$ insertions, we find that the average cost of a `push_back` is exactly **$O(1)$ Amortized Time**.

---

## 4. Under the Hood: The Code (Simplified)

To truly understand it, let's write our own mini-vector from scratch! This is a very common FAANG interview question.

> 💡 **C++ Insight: What is `template <typename T>`?**
> You will see this placed directly above all our internal class implementations. `T` stands for "Type". It allows a single data structure or function to accept *any* data type (`int`, `string`, `double`) without having to copy-paste and rewrite the code for each type! 
> 
> **Placement Rules:**
> 1. You must write `template <typename T>` strictly on the line directly above the `class` or `function` definition.
> 2. It is not permanently turned on for the whole file. If you write a second template function or class below the first one, you must declare `template <typename T>` again directly above it!

```cpp
template <typename T>
class MyVector {
private:
    T* data;           // Pointer to the raw dynamic array
    int current_size;  // How many elements are actually inside
    int capacity;      // How much memory is currently allocated

public:
    // Constructor: Start with capacity of 1
    MyVector() {
        capacity = 1;
        current_size = 0;
        data = new T[capacity]; 
    }

    // The Magic push_back function
    void push_back(T value) {
        // If we are out of space, trigger a Reallocation!
        if (current_size == capacity) {
            
            // 1. Double the capacity (Growth Factor = 2)
            capacity *= 2;
            
            // 2. Allocate a brand new, larger array
            T* new_data = new T[capacity];
            
            // 3. Move old elements over (Avoids expensive deep copies!)
            for (int i = 0; i < current_size; i++) {
                new_data[i] = std::move(data[i]);
            }
            
            // 4. Delete the old array to prevent memory leaks
            delete[] data;
            
            // 5. Point to the new array
            data = new_data;
        }

        // Fast O(1) insertion
        data[current_size] = value;
        current_size++;
    }

    // O(1) Random Access
    T operator[](int index) {
        return data[index];
    }
};
```

> 🚨 **The CP Trap: `v.reserve()`**
> If you know in advance that your vector will hold exactly $10^6$ elements, allowing the vector to automatically double its capacity over and over again will trigger 20 massive reallocations, wasting time and memory. 
> **The Fix:** Always call `v.reserve(1000000);` right after creating the vector. This forces the vector to immediately allocate space for 1 million elements, completely bypassing all future reallocations!

> 💡 **CP / Systems Insight: Freeing Memory**
> Calling `v.clear()` does NOT free memory—it only changes the size to 0. If you have a massive vector and need to give that RAM back to the operating system, you must call `v.shrink_to_fit();`. This forces the vector to reallocate its capacity to perfectly match its current size.

---

## 5. Summary of STL `std::vector` Internals

- **Data Structure:** Dynamic Array (Contiguous Memory)
- **`push_back()` Time:** $O(1)$ Amortized, $O(N)$ Worst-Case (Reallocation)
- **Random Access `v[i]`:** $O(1)$ Guaranteed
- **Growth Factor:** 2.0x (GCC) or 1.5x (MSVC)

> 🚀 **Next Up:** Vectors are amazing, but sometimes we need strict LIFO (Last-In, First-Out) control. Let's see how C++ implements Stacks!

</READING_WIDGET>
