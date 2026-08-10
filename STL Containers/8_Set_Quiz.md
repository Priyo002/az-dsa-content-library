<READING_WIDGET>
# Set Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, what are the underlying data structures powering `std::set` and `std::unordered_set` respectively?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        One must maintain strict sorting, while the other scatters elements purely based on math.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::set` (Ordered Set) is powered by a balanced Binary Search Tree (typically a Red-Black Tree) to keep elements strictly sorted. A `std::unordered_set` is powered by a Hash Table, which provides blazing fast random access but no ordering.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::set`: Hash Table | `std::unordered_set`: Doubly Linked List
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::set`: Balanced Binary Search Tree | `std::unordered_set`: Hash Table
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::set`: Max-Heap | `std::unordered_set`: Vector
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::set`: Array | `std::unordered_set`: Balanced Binary Search Tree
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Set, Unordered Set, Data Structures, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following C++ snippet:**
```cpp
set<int> mySet;
mySet.insert(10);
mySet.insert(20);
mySet.insert(10);
mySet.insert(10);
cout << mySet.size();
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Remember the fundamental mathematical definition of a "Set".
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Set only stores strictly unique elements. When you attempt to `.insert(10)` multiple times, the set silently ignores the duplicates. Therefore, the set will only contain `{10, 20}`, resulting in a size of 2.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `4`
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
                `2`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Compilation Error
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Set, Deduplication, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why might using `std::unordered_set` result in a Time Limit Exceeded (TLE) error in advanced competitive programming rounds, despite having an $O(1)$ average time complexity?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what powers the unordered set, and how a malicious test case might break it.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because `std::unordered_set` relies on a Hash Table, its worst-case time complexity degrades to $O(N)$. Many CP platforms deploy "Anti-Hash Tests" explicitly designed to force mass hash collisions, choking the Hash Table and causing a TLE. If you fear anti-hash tests, use `std::set` for a guaranteed $O(\log N)$ worst-case.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because sorting the unordered set internally takes $O(N \log N)$ time on every insertion
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because allocating memory for the Hash Table always takes $O(N)$ time
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because its worst-case time complexity is $O(N)$ due to hash collisions, which malicious test cases will exploit
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It never TLEs; an unordered set is mathematically guaranteed to always be $O(1)$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Unordered Set, Hash Collisions, TLE, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You need to find the first element in a `std::set<int> orderedSet` that is strictly greater than $X$. Which function should you use?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Review the definitions of the advanced ordered set operations. Which one means "strictly greater"?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `upper_bound(x)` returns an iterator to the first element that is strictly greater than ($> x$). In contrast, `lower_bound(x)` returns an iterator to the first element that is greater than or equal to ($\ge x$).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `orderedSet.find(x)`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `orderedSet.lower_bound(x)`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `orderedSet.upper_bound(x)`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `orderedSet.next(x)`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Set, Binary Search, Upper Bound, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **What happens if you use the global algorithm `std::lower_bound(mySet.begin(), mySet.end(), x)` on a `std::set` instead of the member function `mySet.lower_bound(x)`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does a set have random access iterators (like a vector) that allow the global algorithm to jump around in $O(1)$ time?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::set` does not have random access iterators. Because of this, the global `std::lower_bound` algorithm cannot perform rapid $O(1)$ jumps and will quietly degrade to a linear $O(N)$ scan, likely causing a TLE! You must always use the member function `mySet.lower_bound(x)` to guarantee $O(\log N)$ performance via the internal tree structure.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It will compile properly but quietly degrade to $O(N)$ Time Complexity and likely cause a TLE.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It works perfectly and runs in $O(\log N)$ time, exactly like the member function.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It throws a Compilation Error because `std::lower_bound` only works on arrays.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It causes a fatal Segmentation Fault.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Set, Lower Bound, Time Complexity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, if you need to find the $K$-th smallest element in a `std::set`, using `std::advance` takes $O(K)$ time. How do elite competitive programmers achieve this in $O(\log N)$ time instead?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        The standard Red-Black Tree in C++ does not store subtree sizes, making $O(\log N)$ random access impossible. What extension do CP veterans import to fix this?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because the standard `std::set` does not store subtree sizes in its nodes, finding the $K$-th element (Order Statistics) requires a linear traversal taking $O(K)$ time. Elite competitors bypass this limitation by importing the GCC Policy-Based Data Structure (PBDS) to create an "indexed set" (using `tree_order_statistics_node_update`), which natively supports finding the $K$-th element in strict $O(\log N)$ time.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                By using `std::unordered_set` instead, which supports $O(1)$ random access.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                By importing the GCC Policy-Based Data Structure (PBDS) to create an indexed set.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                By casting the `std::set` to a `std::vector` and using `v[K]`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                By using `std::lower_bound` combined with a custom comparator.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Set, PBDS, Indexed Set, Order Statistics, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
