<READING_WIDGET>
# Custom Comparator Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When writing a custom comparator, why is it considered a fatal error in Competitive Programming to pass arguments by value (e.g., `bool compare(string a, string b)`) instead of by constant reference (`const string& a`)?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How many times does `std::sort` execute its comparator on an array of $10^5$ elements?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Sorting algorithms execute their comparator $O(N \log N)$ times. If you pass large objects (like strings or vectors) by value, the compiler is forced to execute a deep copy of the entire object for every single comparison! This massive memory and CPU overhead instantly causes a Time Limit Exceeded (TLE) error. You must use `const T&` to strictly pass a read-only memory reference.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because passing by value allows `std::sort` to accidentally mutate and corrupt the original array elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it triggers a deep memory copy of the object for every single comparison, transforming a fast $O(N \log N)$ algorithm into a massive TLE lag spike.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because C++ strictly prohibits passing non-primitive types (like structs or strings) by value into any `<algorithm>` function.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because passing by value forces the compiler to switch the internal engine from QuickSort to the slower MergeSort.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Pass by Reference, TLE, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **The C++ STL mandates a mathematical property called Strict Weak Ordering. What catastrophic event occurs if your comparator returns `true` when evaluating two mathematically identical elements (e.g., using `return a >= b;`)?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How do the internal QuickSort pointers know when to stop scanning?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        QuickSort relies on identical elements returning `false` to act as a mathematical boundary, forcing its internal scanning pointers to stop. If you return `true` for identical elements, the pointers will blow right past the array boundaries and read forbidden memory, triggering an instant, unrecoverable Segmentation Fault!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The compiler detects the violation and immediately throws a `std::logic_error` exception.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The sorting algorithm silently degrades into an infinite loop, resulting in a Time Limit Exceeded (TLE) error.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The internal QuickSort boundary checks fail, causing the pointers to scan out-of-bounds memory and triggering a Segmentation Fault.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The algorithm automatically deletes one of the duplicates to resolve the conflict.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Strict Weak Ordering, Segmentation Fault, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Since C++11, what is the modern, highly preferred method for writing a custom comparator for `std::sort` without polluting the global namespace with loose functions?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Can you define the comparison logic directly inside the third argument of `std::sort`?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Modern C++ utilizes inline **Lambda Expressions**. By defining the anonymous function directly inside the `std::sort` call (`sort(v.begin(), v.end(), [](const int& a, const int& b) { ... })`), you keep the logic perfectly encapsulated where it is actually used, dramatically improving code readability.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Writing a generic Template Class.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Using an inline Lambda Expression directly inside the `std::sort` call.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Overloading the standard `<` operator globally inside the `<algorithm>` library header.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Using a Preprocessor Macro `#define`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Lambda Expressions, std::sort, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When creating a Functor to flip a `std::priority_queue` into a Min-Heap, the internal operator must return `a > b`. Why does checking for "greater than" result in the *smallest* numbers floating to the top?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Priority queues evaluate "priority," not strictly "greater than or less than."
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Priority Queue uses the comparator to ask: *"Should element `a` have LOWER priority than element `b`?"* By returning `true` when `a > b`, you are telling the heap that larger numbers have worse priority! Therefore, the larger numbers sink to the bottom, allowing the smallest numbers to naturally float up to the `.top()`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Priority Queues natively reverse all comparators to maintain stability.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because returning `true` tells the queue that `a` has LOWER priority than `b`. If `a > b` is true, the larger numbers sink, leaving the smallest numbers at the top.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Min-Heap operates on absolute values, ignoring the standard mathematical operator logic.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because C++ Priority Queues are actually implemented as Stacks (LIFO), which naturally inverts the ordering.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Functor, Priority Queue, Min-Heap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why is it completely impossible to pass a standard Custom Comparator Functor (which evaluates if `A` should come before `B`) into an `std::unordered_set`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How does a Hash Table organize its elements compared to a Red-Black Tree?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        An `unordered_set` is built using a Hash Table, not a branching Tree! It has absolutely no concept of elements being "greater than" or "less than" each other. It only cares about assigning an element to a mathematical bucket (Hash Function) and checking if two elements are exactly identical (Equality Operator `==`). Greater-than/Less-than comparators are mathematically useless here!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because unordered containers strictly use Hash Tables. They only care about Hash Functions and absolute equality (`==`), completely ignoring greater-than/less-than logic.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because unordered containers require Lambdas instead of Functor Structs.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Custom Comparators force the unordered set to execute in $O(\log N)$ time, breaking its $O(1)$ guarantee.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::unordered_set` only accepts custom rules written in Assembly language.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, unordered_set, Hash Table vs Tree, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A beginner writes a custom struct and overloads `bool operator<(const MyStruct& other)` directly inside the struct. When they try to call `std::sort`, the compiler throws a massive, unreadable template error. What single keyword did they forget at the very end of the method signature?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        The STL algorithms mathematically require absolute proof that your comparator will never mutate (change) the object it is evaluating.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        They forgot the trailing `const`! The signature must be `bool operator<(const MyStruct& other) const`. The trailing `const` is a mathematical promise to the C++ compiler that this method will never mutate the parent object's member variables. Because algorithms like `std::sort` require read-only safety while executing thousands of comparisons, failing to provide this promise results in a hard compilation failure.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `inline`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `const`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `static`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `override`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Operator Overloading, trailing const, Compilation Error, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You successfully used an inline Lambda expression to sort a vector using `std::sort`. However, when you try to pass that exact same Lambda into a `std::priority_queue`, the compiler throws an error. Why does it fail, and how must you declare the Priority Queue to fix it?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        `std::sort` is a Function Template (which accepts instance arguments). `std::priority_queue` is a Class Template (which strictly requires Data Types).
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `std::sort` is just a function, so it can accept the Lambda directly as an argument. However, `std::priority_queue` is a C++ Class Template. The angle brackets `<...>` strictly require C++ Types, not instances of variables! To pass a lambda to a priority queue, you must mathematically extract its Type using `decltype(cmp)` and then pass the lambda instance into the queue's constructor: `priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Lambdas cannot handle the `<` or `>` operators required by heaps.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::priority_queue` is a Class Template that requires a Type, not an instance. You must use `decltype(cmp)` as the template argument and pass the lambda into the constructor.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Priority Queues only accept Functor Structs that inherit from `std::unary_function`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It doesn't fail; Lambdas can be dropped directly into the priority queue template brackets just like `std::sort`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Custom Comparator, Priority Queue, Lambdas, decltype, Class Template, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
