<READING_WIDGET>
# Stack Mastery Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In the classic "Valid Parentheses" problem, elite competitive programmers use a trick called "Pushing Expectations." Why do they explicitly push a closing bracket `)` onto the stack when they encounter an opening bracket `(` in the string?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does this make it easier to match brackets when you finally encounter a closing bracket in the string?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By pushing the *expected* closing bracket onto the stack immediately, it drastically simplifies the logic later on. When you finally encounter a closing bracket in the string, you don't need complex `if/else` rules to verify the type; you simply check: `if (st.top() == current_char)`. If it matches perfectly, you pop it!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because C++ stacks cannot accept opening brackets natively without triggering an escape-character warning.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It drastically simplifies the logic. When a closing bracket is found, you simply check if it perfectly matches the top of the stack without needing complex `if/else` matching rules.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It forces the stack to reverse the string, allowing you to iterate from right-to-left instead.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because pushing closing brackets consumes less memory in the CPU cache than opening brackets.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Valid Parentheses, CP Tricks, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A hacker on Codeforces feeds your "Valid Parentheses" algorithm a massive string of 10,000,001 unmatched brackets. Your code pushes 5 million brackets to the stack before finally returning `false`, causing a Time Limit Exceeded (TLE) error. What $O(1)$ math check can you add at the very beginning of the function to instantly reject this string and bypass millions of useless CPU cycles?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Is it mathematically possible to perfectly pair up 10,000,001 items?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `if (s.length() % 2 != 0) return false;`. It is mathematically impossible to perfectly pair up an odd number of brackets. By checking the string length modulo 2 at the very beginning, you can instantly reject massive invalid inputs in $O(1)$ time, completely bypassing the $O(N)$ stack allocation!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Checking if the string starts with a closing bracket.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Checking if the first and last characters are identical.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Checking if the string length is an odd number using `s.length() % 2 != 0`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Checking if the string contains alphanumeric characters.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Valid Parentheses, Early Exit, Optimization, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In the Next Greater Element problem (iterating right-to-left), the Monotonic Stack algorithm permanently pops and destroys any element smaller than the current number. Why is it mathematically safe to permanently throw away these smaller elements?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Imagine tall and short people in a line. Can someone on the far left see a short person hiding behind a tall person?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If an element is smaller than the current element, it is mathematically impossible for it to be the "Next Greater Element" for anything further to the left, because the current larger number completely blocks it! Therefore, those smaller numbers are useless and can be safely purged from the stack forever.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the problem statement explicitly forbids small numbers from appearing more than once.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because if an element is smaller than the current number, the current larger number will block it. It can never be the "Next Greater Element" for anything further to the left.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because popping smaller numbers allows the Stack to convert into a Queue.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is not actually safe; the algorithm uses a secondary backup array to recover them later.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Monotonic Stack, Next Greater Element, Logic, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A beginner looks at the Monotonic Stack implementation and sees a `while` loop nested inside a `for` loop. They immediately declare that the time complexity is $O(N^2)$. Why are they completely wrong?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Across the entire execution of the program, what is the absolute maximum number of times a single element can be pushed or popped?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Every single element is pushed onto the stack exactly once, and can be popped at most once. Because an element can never be popped twice, the nested `while` loop runs a combined total of at most $N$ times across the *entire program execution* (not per iteration!). Therefore, the amortized time complexity is strictly $O(N)$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the compiler unrolls the nested `while` loop into an $O(1)$ mathematical formula.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the array is pre-sorted in $O(N \log N)$ time, bypassing the loop.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because every element is pushed exactly once and popped at most once. The nested `while` loop runs at most $N$ times total across the entire execution, guaranteeing amortized $O(N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They are correct. The algorithm is $O(N^2)$ but competitive programming platforms have fast enough servers to ignore it.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Monotonic Stack, Amortized Time Complexity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In the "Smallest Number after removing K digits" problem, a junior developer successfully finds the optimal large digit to remove, and deletes it using `num.erase(i, 1)`. Why will this exact line of code instantly trigger a Time Limit Exceeded (TLE) error on a massive string?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        `std::string` uses contiguous memory (like an array). What happens physically to all the characters to the right when you delete a character in the middle?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because `std::string` uses contiguous memory, erasing a character in the middle forces the CPU to physically shift every single character to its right one space to the left to close the gap. This takes $O(N)$ time per deletion. If you do this $K$ times, your overall time degrades to an apocalyptic $O(N \times K)$! You must use a Stack (or `std::string` as a stack) because appending and popping from the *end* of a string guarantees $O(1)$ operations.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `num.erase` forces the string to re-encode into UTF-16, taking massive CPU cycles.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because erasing a character in the middle of a string forces the CPU to physically shift all subsequent characters left. This takes $O(N)$ time, degrading the entire algorithm to $O(N \times K)$.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `num.erase` returns a completely new copy of the string rather than modifying it in-place.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because deleting digits accidentally shortens the length of the `for` loop, causing an out-of-bounds segfault.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Greedy, Contiguous Memory, string erase, TLE, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In the "Smallest Number" problem, what edge-case occurs if the input string is `12345` and `K=2`? How does the Monotonic Stack handle the "Exhaustion Trap"?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If the numbers are already in perfect increasing order, will the `current < stack.top()` condition ever trigger to destroy a digit?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If the numbers are already perfectly sorted in ascending order, the Monotonic Stack's destruction condition (`current < stack.top()`) will never trigger! At the end of the main loop, no digits will have been removed, and `K` will still be `2`. To fix this Exhaustion Trap, you must run a final loop at the very end to explicitly pop `K` elements from the back of the stack (removing the largest numbers `5` and `4`).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The Stack throws a runtime error because it expects unsorted data.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the numbers are ascending, the condition never triggers, leaving `K > 0`. You must explicitly pop `K` elements from the back of the stack at the very end of the algorithm.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The algorithm naturally deletes the numbers `1` and `2` because they are the smallest.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The algorithm automatically switches to a decreasing stack logic and removes the digits from the front.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Greedy, Monotonic Stack, Exhaustion Trap, Edge Case, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In advanced Monotonic Stack problems (like calculating the Largest Rectangle in a Histogram or finding the "Daily Temperatures" waiting time), why is pushing the actual integer values onto the stack considered a fatal trap? What must elite competitive programmers store instead?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If you only store the value `75` on the stack, do you know exactly how many days ago you saw that `75`?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Elite competitive programmers strictly store the **array indices**, never the actual values! Without the indices, it is mathematically impossible to calculate the "width" of a rectangle or the "distance/time" between elements when elements are finally popped. You can always retrieve the value using `nums[index]`, but you can never retrieve an index from a raw value!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                They must store custom `structs` containing a boolean flag indicating if the element is active.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They strictly store the array indices. Without indices, it is impossible to calculate width or distance between elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They store memory pointers to the values to bypass array lookups.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They store the absolute difference between the current value and the global maximum.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, Monotonic Stack, Indices vs Values, Distance, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In a low-latency systems engineering environment, using `std::string` as a stack (via `push_back`) is extremely fast but introduces a dangerous penalty: contiguous memory reallocation lag spikes. If you know the maximum possible size of the string in advance (e.g., `num.length()`), what C++ function must you call to guarantee strict $O(1)$ performance without reallocation lag?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How do you tell the OS to allocate a massive block of memory upfront before the `for` loop even begins?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        You must call `st.reserve(num.length());` before starting the loop. Because `std::string` uses contiguous memory, appending elements forces it to periodically allocate larger memory blocks and copy all existing characters over (triggering a lag spike). By pre-allocating the maximum required memory upfront with `reserve()`, you entirely prevent reallocation overhead!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `st.resize(num.length());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `st.reserve(num.length());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `st.shrink_to_fit();`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `st.allocate_static(num.length());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Stack, string, reserve, Memory Reallocation, Systems Engineering, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
