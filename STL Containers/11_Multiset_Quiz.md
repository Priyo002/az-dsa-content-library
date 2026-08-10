<READING_WIDGET>
# Multiset Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **What is the primary difference between a `std::set` and a `std::multiset` in C++?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the core mathematical definition of a set, and how a multiset relaxes that rule.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::set` strictly rejects duplicates; inserting a number that already exists will be silently ignored. A `std::multiset` is physically identical (powered by a balanced Binary Search Tree), but allows multiple elements to have the exact same value.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                A multiset is powered by a Hash Table, while a set is powered by a Binary Search Tree.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A multiset allows duplicate values to coexist, while a set strictly rejects them.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A multiset does not sort its elements, while a set does.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A set has $O(1)$ insertions, while a multiset takes $O(\log N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Duplicates, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following C++ snippet:**
```cpp
multiset<int> ms;
ms.insert(10);
ms.insert(20);
ms.insert(10);
ms.insert(10);
ms.erase(10);
cout << ms.size();
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        This tests the "Dangerous `erase()` Trap" discussed in the module. Does passing a raw value to `erase()` delete one copy or all copies?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        When you pass a raw value directly to `erase()` (e.g., `ms.erase(10)`), the multiset deletes **ALL** copies of that value. Since all three `10`s are erased, only the `20` remains, leaving a size of 1.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `1`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `2`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `3`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `4`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Erase Trap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If a `std::multiset` contains multiple copies of the number `10`, what is the correct and safe way to delete exactly ONE instance of `10`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You need to point the `erase()` function to a specific element in memory, rather than giving it a raw value.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        To safely erase just a single copy, you must first locate its iterator using `.find()`, and then pass that exact iterator into the `.erase()` function: `ms.erase(ms.find(10));`. Passing the raw value (`ms.erase(10)`) would fatally delete all copies!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase(10);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.delete(10);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase_single(10);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase(ms.find(10));`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Safe Erase, Iterators, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why is it a dangerous CP Trap to use `ms.count(X) > 0` to check if an element $X$ exists inside a multiset?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about how the `.count()` function behaves when there are a massive number of duplicates.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        In a multiset, `.count(x)` takes $O(\log N + K)$ time, where $K$ is the number of duplicate copies of $X$. If a test case feeds you 100,000 copies of $X$, `.count()` will manually iterate through every single one, resulting in a fatal $O(N)$ Time Limit Exceeded (TLE). You should always use `ms.find(X) != ms.end()` which is strictly $O(\log N)$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it is a syntax error; `.count()` is only available for `std::set`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `.count(X)` returns a boolean, not an integer, so checking `> 0` fails compilation.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `.count(X)` takes $O(\log N + K)$ time. If there are many copies ($K$), it behaves like an $O(N)$ linear scan and causes a TLE.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `.count(X)` always takes $O(N \log N)$ time, regardless of duplicates.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Time Complexity, Count Trap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How do you fetch the absolute maximum element currently stored inside a `std::multiset` in $O(1)$ time?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        A multiset is automatically sorted in ascending order. Where does the largest element sit?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because a multiset keeps elements sorted in a Binary Search Tree, the smallest element is always at the front (`*ms.begin()`) and the largest element is always at the absolute back (`*ms.rbegin()`).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.max()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.top()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `*ms.end()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `*ms.rbegin()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Maximum, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In a Sliding Window problem, both a `std::deque` and a `std::multiset` can be used. Why would you explicitly choose to use a `std::multiset` over an $O(N)$ `std::deque`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        A deque is great for tracking the absolute maximum or minimum. What can't it track?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Deque works in $O(N)$ time but relies on a monotonic structure that *only* keeps track of the absolute maximum or minimum. If the problem requires you to query the **Median** or check the complete sorted order of the window at any moment, the Deque fails completely. A Multiset naturally keeps the entire window sorted at all times.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a multiset provides faster overall time complexity ($O(N)$ vs $O(N \log K)$).
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a multiset allows you to query the Median or exact sorted order of the window, which a Deque cannot do.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a multiset consumes significantly less memory than a Deque.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a Deque does not allow you to remove elements from the back of the window.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Multiset, Sliding Window, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
