<READING_WIDGET>
# Vector Internals Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, what happens to existing pointers and references to a `std::vector`'s elements if a `push_back()` operation triggers a capacity Reallocation?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about how a vector physically achieves its "growth" by moving to a brand new memory block. What happens to the old memory block?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        When a vector hits its capacity and needs to grow, it allocates a new, larger contiguous block of memory, copies the elements over, and completely deletes the old block. Therefore, all existing pointers, references, and iterators pointing to the old memory block are instantly invalidated and will cause memory corruption if accessed!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                They are automatically updated by the compiler to point to the new memory block.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They are instantly invalidated because the old memory block is deleted.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They temporarily point to null until the reallocation finishes.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Nothing; vectors do not delete their old memory blocks, they just append to them.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Vector, Iterator Invalidation, Reallocation, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If you know in advance that your program will push exactly $1,000,000$ elements into an empty `std::vector`, what is the most efficient way to completely prevent the vector from wasting time on internal reallocations?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You want to tell the vector to allocate a massive chunk of capacity up front, without actually changing its current "Size".
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Calling `v.reserve(1000000)` immediately allocates memory for 1 million elements without changing the vector's actual `size`. This guarantees that your next 1 million `push_back()` calls will execute in strict $O(1)$ time with absolutely zero reallocations triggered.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Call `v.resize(1000000);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Call `v.capacity(1000000);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Call `v.reserve(1000000);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Reallocations cannot be prevented; they are hardcoded into the C++ compiler.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Vector, Reserve, Optimization, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You have a massive `std::vector` taking up 2GB of RAM. You call `v.clear()` because you no longer need the data. Does this action free the 2GB of RAM back to the operating system?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does clearing a vector reduce its internal `Capacity`, or just its `Size`?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Calling `v.clear()` only sets the internal `Size` tracker to 0, destroying the elements but keeping the 2GB `Capacity` fully allocated! To actually free the physical RAM back to the operating system, you must call `v.shrink_to_fit()`, which forces the vector's capacity to shrink down to match its current size.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Yes, `v.clear()` instantly deletes the internal array and frees all memory.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                No, it only sets the size to 0. You must call `v.shrink_to_fit()` to actually free the allocated capacity.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                No, it only sets the size to 0. You must call `v.free()` to release the memory.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Yes, but the memory is only freed when the program entirely terminates.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Vector, Memory Management, clear, shrink_to_fit, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A FAANG interviewer asks you: "If a `std::vector` undergoes $O(N)$ reallocations when it runs out of capacity, why do we mathematically classify `push_back()` as having an $O(1)$ Time Complexity?"**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the concept of Amortized Time and the vector's exponential Growth Factor (e.g., doubling in size).
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because the vector multiplies its capacity by a Growth Factor (usually $2\times$) instead of just adding 1 slot, reallocations happen exponentially less often. The massive cost of the $O(N)$ copies is averaged out ("amortized") over a huge number of fast $O(1)$ insertions. Mathematically, inserting $N$ elements takes roughly $2N$ operations, yielding an average cost of strict **$O(1)$ Amortized Time** per insertion.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the C++ compiler executes the $O(N)$ reallocation asynchronously on a separate CPU thread, taking $0$ time on the main thread.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the $O(N)$ cost only happens once at startup and is never triggered again.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the vector uses an exponential growth factor (like $2\times$), the $O(N)$ reallocation penalty happens so rarely that the average mathematical cost per insertion averages out to $O(1)$ Amortized Time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `push_back()` is actually $O(N)$; developers just call it $O(1)$ for simplicity.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Vector, Amortized Time Complexity, Reallocation, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In quantitative and high-frequency C++ engineering, what is the critical performance difference between calling `v.push_back(Object(a, b))` versus `v.emplace_back(a, b)`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        One creates a temporary object and moves/copies it into the vector. The other constructs the object directly in place.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `push_back` expects a fully formed object, meaning `push_back(Object(a, b))` first constructs a temporary object in memory, and then invokes a copy or move constructor to place it into the vector's raw array. `emplace_back` forwards the raw arguments `(a, b)` and constructs the object directly inside the vector's pre-allocated RAM, entirely bypassing the expensive temporary copy/move operations!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                There is no difference; `emplace_back` is simply a modern syntax alias for `push_back`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `push_back` constructs a temporary object and copies/moves it into the vector, whereas `emplace_back` constructs the object perfectly in place, bypassing unnecessary copies.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `emplace_back` prevents the vector from triggering reallocations, making it strictly $O(1)$.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `push_back` can take multiple arguments, whereas `emplace_back` only takes one.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Internals, Vector, emplace_back, push_back, Memory Optimization, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
