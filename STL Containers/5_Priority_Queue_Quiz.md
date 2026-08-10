<READING_WIDGET>
# Priority Queue Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, what is the exact syntax to declare a Priority Queue of integers that behaves as a Min-Heap (smallest element at the top)?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        By default, `priority_queue<int>` is a Max-Heap. You need to provide the underlying container and a custom comparator to reverse this.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        To declare a Min-Heap in C++, you must explicitly define the underlying container (`std::vector<int>`) and pass the `std::greater<int>` comparator. The correct syntax is `priority_queue<int, vector<int>, greater<int>> minHeap;`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `priority_queue<int, less<int>> minHeap;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `priority_queue<int> minHeap;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `priority_queue<int, vector<int>, greater<int>> minHeap;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `min_priority_queue<int> minHeap;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Priority Queue, Min-Heap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You have a `vector<int> v` of size $N$ filled with unsorted integers. What is the most time-efficient way to load all these elements into a `priority_queue`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the CP Optimization discussed in the module. Looping and pushing takes $O(N \log N)$. Can we do better?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Passing the vector's iterators directly into the constructor (e.g., `priority_queue<int> pq(v.begin(), v.end());`) invokes the $O(N)$ Heapify algorithm. Using a `for` loop to push elements one by one takes $O(N \log N)$ time, which is strictly slower.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Looping through the vector and calling `.push()` on each element
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Passing the vector's iterators directly into the Priority Queue constructor
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Sorting the vector first with `sort()`, then using a `for` loop to `.push()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They all take the exact same time complexity of $O(N^2)$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Priority Queue, Heapify, Time Complexity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following code snippet:**
```cpp
priority_queue<pair<int, int>> pq;
pq.push({10, 50});
pq.push({20, 10});
pq.push({10, 100});
cout << pq.top().second;
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How does a C++ Priority Queue handle comparisons for `pair` data structures by default?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By default, a Max-Heap compares pairs by their **first** element. The pairs `{20, 10}` has the largest first element (`20`), so it becomes the top of the heap. Thus, `pq.top().second` will output `10`. (If the first elements were tied, it would break the tie using the second element).
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
                `50`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `100`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Priority Queue, Pairs, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why does inserting an element into a `std::priority_queue` take $O(\log N)$ time, instead of the $O(1)$ time seen in a standard `std::queue`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what physical data structure powers a Priority Queue under the hood.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Priority Queue is physically implemented as a binary tree (a Heap). When you insert a new element, it must bubble up or sift down through the tree levels to maintain the strictly sorted heap property. Traversing the height of this tree takes $O(\log N)$ time.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it has to copy the entire array to a new memory block on every insertion
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it must maintain its internal tree-like Heap structure to keep elements sorted
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it calls `std::sort()` internally on every insertion
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it is a Doubly Linked List
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Priority Queue, Time Complexity, Heap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following code snippet:**
```cpp
priority_queue<int> maxHeap;
maxHeap.push(15);
maxHeap.push(30);
maxHeap.push(10);
maxHeap.pop();
maxHeap.push(20);
cout << maxHeap.top();
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Trace the internal state of the Max-Heap after each operation. Which number is floating at the top?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        1. Push 15, 30, 10 $\rightarrow$ Heap top is `30`.
        2. `pop()` $\rightarrow$ Removes `30`. The new highest element `15` becomes the top.
        3. Push 20 $\rightarrow$ `20` is greater than `15`, so `20` bubbles up to become the new top.
        4. `top()` $\rightarrow$ Returns `20`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `10`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `15`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `20`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `30`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Priority Queue, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
