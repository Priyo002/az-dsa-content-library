<READING_WIDGET>
# Indexed Set (PBDS) Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why do competitive programmers often use the GCC Policy-Based Data Structure (PBDS) / Indexed Set instead of the standard `std::set`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        What operation takes $O(N)$ time on a standard C++ set because it lacks random-access indexing?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A standard C++ `std::set` does not store subtree sizes, making it impossible to access elements by their index without doing an $O(N)$ linear traversal. The PBDS Indexed Set tracks subtree sizes, unlocking two $O(\log N)$ superpowers: `find_by_order(k)` (finding the K-th smallest element) and `order_of_key(x)` (counting how many elements are strictly smaller than X).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because PBDS supports $O(1)$ insertions via Hash Tables.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because PBDS provides $O(\log N)$ index-based access and order statistics, which a standard set lacks.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because standard sets cannot store custom objects.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because PBDS consumes significantly less memory than a standard set.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, Indexed Set, Order Statistics, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider a PBDS Indexed Set containing the elements `[10, 20, 30, 40, 50]`. What will the function `s.find_by_order(2)` return?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Is `find_by_order()` 0-indexed or 1-indexed?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `find_by_order(k)` uses 0-based indexing. Index 0 is `10`, Index 1 is `20`, and Index 2 is `30`. It returns an iterator pointing to `30`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                An iterator pointing to `10`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                An iterator pointing to `20`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                An iterator pointing to `30`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The integer `30`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, find_by_order, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider a PBDS Indexed Set containing the elements `[10, 20, 30, 40, 50]`. What will the function `s.order_of_key(35)` return?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Read the exact definition of `order_of_key(x)`. What does it count?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `order_of_key(x)` returns the exact integer count of elements in the set that are *strictly smaller* than `x`. In this set, only `10`, `20`, and `30` are strictly smaller than `35`. Therefore, it returns `3`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
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
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `4`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                An iterator pointing to `40`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, order_of_key, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why is it a terrible idea to simply change `less<int>` to `less_equal<int>` in the PBDS macro definition to create an Indexed Multiset?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what happens to the internal operations of a Binary Search Tree when the comparison operator allows identical values without unique identifiers.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Changing `less<int>` to `less_equal<int>` fundamentally breaks the internal `erase()` function in PBDS, leading to silent bugs and undefined behavior when trying to remove elements.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It causes a Compilation Error because `less_equal` is not a valid STL comparator.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It fundamentally breaks the internal `erase()` function, preventing safe deletion of elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It changes the time complexity of `find_by_order` from $O(\log N)$ to $O(N)$.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It reverses the sorting order from ascending to descending.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, Indexed Multiset, Erase Trap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **What is the universally accepted Competitive Programming trick to safely create an Indexed Multiset (allowing duplicates) using PBDS?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How can we trick the PBDS into thinking every inserted element is mathematically unique, even if their base values are identical?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        To safely allow duplicates, elite programmers use `pair<int, int>` as the data type. The first integer is the actual value, and the second integer is a unique ID (like a rising timer counter). This guarantees that every pair is mathematically unique, allowing identical values to coexist without breaking the internal BST logic.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Store the data inside an `std::unordered_map` and sync it with the PBDS.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Use `std::multiset` and cast it to a PBDS tree using a compiler flag.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Change the underlying tree structure from `rb_tree_tag` to `splay_tree_tag`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Use `std::pair<int, int>` where the second element is a unique rising ID (like a timer) to force uniqueness.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, Indexed Multiset, Pair Trick, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Which famous algorithmic problem can be elegantly solved in $O(N \log N)$ time by iterating backwards through an array and using `order_of_key(x)` to see how many smaller elements exist to the right?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        This problem asks you to find pairs of indices $(i, j)$ where $i < j$ but $nums[i] > nums[j]$.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The Count Inversions problem is the quintessential application of PBDS. By iterating backwards, everything currently inside the PBDS represents the numbers "to the right" of the current element. `order_of_key(nums[i])` instantly tells us exactly how many of them are strictly smaller!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Two Sum
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Count Inversions
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Sliding Window Maximum
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Longest Increasing Subsequence
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, Count Inversions, Algorithmic Application, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If you have created an Indexed Multiset using `pair<int, int>` and it currently contains `{10, 1}`, `{10, 2}`, and `{10, 3}`, how must you correctly erase a single instance of `10`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You cannot simply use `.erase({10, 0})` because that exact pair (with an ID of 0) does not exist in the set! How do you fetch the iterator for the first actual instance of 10?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because the multiset strictly stores unique pairs, passing `.erase({10, 0})` fails because `{10, 0}` is not in the set. You must use `.lower_bound({10, 0})` to fetch the iterator pointing to the very first instance of `10` (which would be `{10, 1}`), and then pass that iterator into the `.erase()` function to safely remove it.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase({10, 0});`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase(10);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase(ms.lower_bound({10, 0}));`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `ms.erase(ms.find({10, 0}));`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, PBDS, Indexed Multiset, Erase Iterator, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
