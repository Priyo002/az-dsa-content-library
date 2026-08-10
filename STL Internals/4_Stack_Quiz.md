<READING_WIDGET>
# Stack Internals Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **According to the C++ Standard Template Library, how is a `std::stack` technically classified?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does a stack manage its own dynamic memory, nodes, and pointers from scratch?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::stack` is classified as a **Container Adaptor**. It does not possess its own memory management or pointer systems; it is simply a lightweight wrapper placed over an existing sequence container to restrict access to strict LIFO (Last-In, First-Out) operations.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Node-Based Container
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Dynamic Array
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Container Adaptor
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Policy-Based Data Structure
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Container Adaptor, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why will the C++ compiler throw an error if you attempt to print a `std::stack` using a standard `for(int x : st)` range-based loop?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        What functions must a container expose in order to support a range-based loop?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because a Stack is designed as a strict LIFO wrapper, it intentionally hides the `.begin()` and `.end()` iterators of its underlying container. Without exposed iterators, you cannot iterate through a stack! The only way to view the elements is to repeatedly read `.top()` and then `.pop()` them.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a stack is mathematically un-ordered.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because iterating through a stack causes memory corruption.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a stack intentionally hides its `.begin()` and `.end()` iterators to enforce strict LIFO rules.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because you must pass the stack by reference into the loop.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Iterators, Compilation Error, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If you declare `std::stack<int> st;`, what is the default underlying container doing the heavy lifting behind the scenes?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        It is a container that supports both front and back operations efficiently.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By default, the C++ STL builds a Stack on top of a `std::deque` (Double-Ended Queue).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::vector`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::deque`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::list`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::array`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Deque, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In low-latency systems programming, why is `std::deque` chosen as the default backing for a Stack instead of `std::vector`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what happens to a Vector when it completely runs out of capacity.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        When a `std::vector` runs out of capacity, it must allocate a massive new contiguous block and copy every single element over, causing an unpredictable $O(N)$ latency spike during a `push()`. Because a `std::deque` allocates memory in smaller chunks, it never copies old elements when expanding, guaranteeing strict $O(1)$ insertions without lag spikes.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Deque uses significantly less memory overall than a Vector.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Vector cannot execute `push_back()`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Deque provides better L1 CPU cache locality than a Vector.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Deque guarantees strict $O(1)$ insertions by avoiding the massive $O(N)$ reallocation penalty suffered by Vectors.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Time Complexity, Reallocation, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In Competitive Programming, a developer might manually override the default stack engine to use a `std::vector` for improved speed (since CP environments care less about random latency spikes and more about raw throughput). What is the correct syntax to do this?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You must pass the desired container as the second template argument.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because a Stack is just a template wrapper, you can completely swap out the underlying engine by passing the container type as the second argument: `std::stack<int, std::vector<int>>`. This provides better CPU cache locality than the chunked deque!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::stack<int> st = new std::vector<int>();`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::stack<int, std::vector<int>> st;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::vector<int> st = std::stack();`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::stack<int>::override(std::vector<int>);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Vector, Customization, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **From a C++ Systems Engineering perspective, why does `std::stack::pop()` return `void` instead of returning the popped element directly to you?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If `pop()` returned the element by value, it would have to invoke a Copy Constructor. What happens if the system is out of memory and that copy throws an error?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If `pop()` removed the element from the stack *and then* tried to return it by value, a failed copy constructor (e.g., due to low memory) would throw an exception. The element would already be deleted from the stack, but you would never receive it, resulting in permanent data loss! By separating this into `top()` (which reads safely via reference) and `pop()` (which returns `void`), C++ guarantees Strong Exception Safety.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                To enforce Strong Exception Safety and prevent permanent data loss if a copy constructor fails.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the C++ compiler cannot infer the return type of a template class dynamically.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because returning values from a container takes $O(N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the underlying `std::deque` also returns `void` when popped, and the stack simply forwards the result.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Stack, Exception Safety, pop, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
