<READING_WIDGET>
# Deque (Double-Ended Queue) Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, which of the following operations is possible in $O(1)$ time on a `std::deque` but requires $O(N)$ time on a standard `std::vector`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what "Double-Ended" implies for efficient insertions.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::deque` allows for $O(1)$ insertions and deletions at *both* the front and the back. In a `std::vector`, adding an element to the front (e.g., using `insert()`) requires shifting all existing elements one position to the right, which takes $O(N)$ time.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Accessing an element at a specific index using `dq[i]`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Adding an element to the front using `push_front()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Adding an element to the back using `push_back()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Getting the total number of elements using `size()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following C++ code snippet:**
```cpp
deque<int> dq;
dq.push_back(10);
dq.push_front(20);
dq.push_back(30);
dq.pop_front();
cout << dq.front();
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Trace the state of the deque carefully after every push and pop operation.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        1. `push_back(10)` -> `[10]`
        2. `push_front(20)` -> `[20, 10]`
        3. `push_back(30)` -> `[20, 10, 30]`
        4. `pop_front()` removes the first element (20) -> `[10, 30]`
        5. `dq.front()` returns the new first element, which is `10`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `10`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `20`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `30`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `Segmentation Fault`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **What happens if you execute `dq.pop_back()` on a completely empty `std::deque` in C++?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what happens when you try to remove an item that doesn't exist. Does C++ fail safely or fatally?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Calling `.pop_front()`, `.pop_back()`, `.front()`, or `.back()` on an empty Deque leads to Undefined Behavior, which typically causes a fatal **Segmentation Fault** crashing your program. You must always verify `!dq.empty()` before attempting to access or remove elements.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The deque safely ignores the command and continues execution
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The compiler throws a syntax error during compilation
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It causes a Segmentation Fault and crashes the program
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It returns `0` or `null` by default
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Edge Cases, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Unlike standard Queues (`std::queue`) and Stacks (`std::stack`), which operation is uniquely supported in $O(1)$ time by a C++ `std::deque`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Queues and Stacks only allow access to the very ends of the data structure. What else can a Deque do?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A C++ `std::deque` supports Random Access! This means you can instantly read or modify any element at any index (e.g., `dq[i]`) in $O(1)$ time, which is completely impossible in standard Queues or Stacks.
        
        > While `dq[i]` is $O(1)$, a FAANG interviewer will note it is structurally heavier than a `std::vector`. A vector is one continuous block of memory (1 pointer dereference). A deque is a map of memory chunks (2 pointer dereferences), which incurs overhead and reduces L1 CPU cache locality!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Popping from the front
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Random Access (e.g., `dq[i]`)
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Checking if the container is empty
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Pushing to the back
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In Competitive Programming, a `std::deque` is most famously used to optimize which of the following algorithmic problems to $O(N)$ time?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about moving a fixed-size frame across an array and keeping track of the best value inside it.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The absolute most important use case for a Deque in CP is the **Sliding Window Maximum (or Minimum)** problem. By maintaining a monotonically decreasing (or increasing) order of elements inside the Deque, you can instantly find the max/min value in a moving window in amortized $O(1)$ time per step.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Finding the Shortest Path in a Weighted Graph
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Sliding Window Maximum
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Binary Search on an Unsorted Array
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Generating all Permutations of a String
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How is a C++ `std::deque` internally structured to allow for both $O(1)$ front/back insertions and $O(1)$ random access?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Beginners often assume it's just a Doubly Linked List, but a DLL cannot achieve $O(1)$ random access (`dq[i]`).
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A C++ `std::deque` is implemented as an **Array of Arrays** (or a chunked map). It allocates fixed-size arrays (chunks) and keeps a central map of pointers to these chunks. This allows it to instantly calculate which chunk an index falls into ($O(1)$ random access) while only needing to allocate a new chunk when the absolute front or back chunk becomes completely full ($O(1)$ insertions).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is a standard Doubly Linked List
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is a standard Singly Linked List
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is a single, massive continuous block of memory like a `std::vector`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is a map of fixed-size arrays (an Array of Arrays / chunked map)
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Internal Architecture, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How does a `std::deque` handle pointer and reference invalidation when adding new elements to the front or back, compared to a `std::vector`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the "chunked map" architecture from the previous question. Does a deque need to physically move existing elements when expanding?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        When a `std::vector` runs out of capacity, it reallocates a larger contiguous block of memory, physically moving every element and instantly invalidating all existing pointers and references. Because a `std::deque` uses a chunked map, it never physically moves existing elements; it simply allocates a new chunk. Therefore, pushing to either end of a deque safely preserves all references and pointers to existing elements!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Both vector and deque invalidate all references when they expand.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A vector preserves references, while a deque invalidates them because it is chunked.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A deque preserves references to existing elements when pushing to either end, whereas a vector invalidates them upon reallocation.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Neither vector nor deque ever invalidates references.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Memory Safety, Reference Invalidation, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
