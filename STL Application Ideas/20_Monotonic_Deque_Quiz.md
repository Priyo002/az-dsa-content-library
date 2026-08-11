<READING_WIDGET>
# Monotonic Deque Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **To solve the "Sliding Window Maximum" problem in strict $O(N)$ time, elite competitive programmers use a `std::deque` (Double-Ended Queue) rather than a standard `std::stack` or `std::queue`. Why is a Deque the only data structure capable of solving this?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the two separate actions happening: old numbers expire as the window slides, and weak numbers are destroyed when large numbers arrive.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        We must perform $O(1)$ operations on both ends of the container simultaneously! We need to `pop_front()` to evict old numbers that have fallen out of the left side of the window, while simultaneously executing `pop_back()` to purge weak numbers from the right side when a new massive number arrives. Only a `std::deque` supports fast modifications at both ends.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because standard Stacks and Queues are built using dynamic arrays, which cause memory lag during reallocation.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because we require $O(1)$ modifications at both ends simultaneously: evicting old expired numbers from the front, and purging weak numbers from the back.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Deque automatically sorts the elements in $O(\log N)$ time natively.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::deque` allows random access via pointers, while a `std::stack` does not.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window Maximum, Double Ended Queue, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A candidate attempts to solve Sliding Window Maximum by pushing the actual integer values into the Monotonic Deque. Why is this a fatal architectural trap?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If the number `75` is at the front of your Deque, how do you know if it belongs in the current window or if the window slid past it 10 steps ago?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        You must strictly store the **Array Indices**! If you store the raw integer values, you have absolutely no mathematical way to know when a number at the front of the deque has expired and fallen out of the sliding window. By storing the index `i`, checking expiration is a simple $O(1)$ math equation: `dq.front() <= i - k`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Storing raw values triggers a runtime warning in modern C++ compilers.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because without the indices, it is mathematically impossible to know if the element at the front of the deque has expired and fallen out of the sliding window.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `nums[dq.back()]` executes faster in CPU cache than accessing raw integers directly.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Values consume 4 bytes of memory, while indices only consume 2 bytes.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window Maximum, Storing Indices, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When purging weak numbers from the back of the Deque, elite programmers use the condition `nums[dq.back()] <= nums[i]`. Why is it critical to use `<=` instead of strictly `<`? What happens to duplicate values?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If you have two identical numbers, which one will survive longer in a window moving to the right?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If the current number is exactly equal to the older number at the back of the deque, the older number is mathematically useless! Because the newer number arrived later, it is guaranteed to survive in the sliding window longer. Purging duplicates keeps the deque perfectly minimal and optimized.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                If the newer number is equal to the older number, the older one is useless because the newer one will survive in the sliding window longer. Purging duplicates keeps the deque minimal.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Using `<` will cause the Monotonic Deque to accidentally act as a Sliding Window Minimum instead.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Duplicate values violate the Strict Weak Ordering rules of C++, causing a Compilation Error.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is actually a mistake. Elite programmers strictly use `<` to preserve duplicate data in case the window moves backwards.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window Maximum, Duplicates, Lifespan, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A junior developer reviews your code and states: "There is a `while` loop nested inside a `for` loop. This algorithm is $O(N \times K)$, not $O(N)$." Why is this a classic CP illusion?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How many times can a single index be inserted into the Deque, and how many times can it be removed?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Every single array index is `push_back()` into the deque exactly **once**. Therefore, an index can be popped (either from the front or the back) at most **once**. Because an element cannot be deleted twice, the nested `while` loops will run a combined total of at most $N$ times across the *entire program*, guaranteeing flawless amortized $O(N)$ time complexity.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the compiler unrolls nested `while` loops natively in C++14.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because every element is pushed exactly once and popped at most once. The `while` loop runs at most $N$ times total across the entire execution.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the `std::deque` relies on a Hash Table internally, mapping searches to $O(1)$ regardless of loop nesting.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They are correct. The algorithm is $O(N \times K)$, but it passes because $K$ is typically very small.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window Maximum, Amortized Time Complexity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A beginner implements a flawless $O(N)$ Monotonic Deque, but when they submit their code, their output array size is $N$, but the judge expects an array of size $N - K + 1$. What critical "Startup Phase" logic did they forget in their `for` loop?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does a sliding window of size $K=3$ actually exist when you are looking at the very first element (index 0)?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        They forgot the `if (i >= k - 1)` boundary check! A sliding window of size $K$ does not physically exist until the iterator has read at least $K$ elements. If you blindly record `dq.front()` on every single iteration, you will record maximums for incomplete windows (e.g., a window of size 1, then size 2). You must wait until the window has fully formed before recording the answer.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                They forgot to resize the output array at the end of the function using `result.resize(N - K + 1)`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They forgot to add the condition `if (i >= k - 1)` before recording the answer. The window doesn't fully exist until the iterator reaches the $K$-th element.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They forgot to initialize the `for` loop at `i = k` instead of `i = 0`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They forgot to push `k` initial garbage values into the deque to pad the startup phase.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, Sliding Window Maximum, Output Boundaries, Startup Phase, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A candidate proposes solving the Sliding Window Maximum problem using a `std::multiset` instead of a Deque, arguing that the multiset will automatically sort the window and provide the maximum via `*s.rbegin()` in $O(N \log K)$ time. Beyond the mathematical slowdown, why is this architecturally a terrible idea for low-latency systems?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How does a Multiset (Red-Black Tree) allocate memory compared to a Deque/Vector?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::multiset` is a node-based Red-Black Tree. Every single insertion triggers a slow heap allocation for a new node, heavily fragmenting memory and completely destroying L1 CPU Cache Locality. A `std::deque` uses large contiguous blocks of memory, keeping the data packed tightly in the CPU cache and executing significantly faster on a hardware level. (Note: using `.erase(val)` on a multiset deletes ALL copies of the value, which is another algorithmic flaw requiring iterator deletion, but the cache locality issue is the primary systems killer).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Multiset will automatically delete duplicate values, artificially shrinking the window size.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Multiset is a node-based tree that requires separate heap allocations for every element, causing massive memory fragmentation and destroying L1 CPU Cache Locality.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::multiset` is mathematically unstable and may return the wrong maximum if the window contains negative numbers.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because multisets are strictly limited to $K \le 1024$ elements in the C++ standard library.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Deque, multiset, CPU Cache Locality, Memory Fragmentation, Systems Engineering, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
