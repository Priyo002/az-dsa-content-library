<READING_WIDGET>
# STL Algorithms Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When sorting complex objects like `structs` or `pairs`, what is the fundamental difference between `std::sort` and `std::stable_sort`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If you are sorting employees by salary, what happens to employees who have the exact same salary?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `std::sort` (using IntroSort) is an unstable sort, meaning identical elements might be swapped arbitrarily and lose their original order. `std::stable_sort` (using MergeSort) guarantees that identical elements will strictly retain their original relative order from before the sort started.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::sort` executes in $O(N \log N)$ time, while `std::stable_sort` executes in faster $O(N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::stable_sort` mathematically guarantees that identical elements will strictly retain their original relative order.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::stable_sort` prevents the compiler from throwing an exception if the array contains negative numbers.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::sort` uses a temporary auxiliary array in memory, while `std::stable_sort` operates strictly in-place.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Sorting, stable_sort, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If you call `std::sort` on a `vector<pair<int, int>>` without providing a custom comparator, how will C++ sort the data?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        How does the STL natively break ties when dealing with pairs?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By default, the STL automatically sorts pairs based on their `.first` element. If two pairs have the exact same first element, it automatically uses the `.second` element as the tiebreaker!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It will throw a Compilation Error, as pairs cannot be sorted natively without a custom comparator.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It sorts strictly by the `.first` element, ignoring the `.second` element completely even if there are ties.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It sorts by the `.first` element, and automatically uses the `.second` element as a tiebreaker for identical first elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It sorts by adding both values of the pair together and comparing the sums.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Sorting, Pairs, Tiebreaker, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If you want to sort a vector `v` in perfectly descending order, what is the cleanest and most idiomatic STL shortcut that avoids writing a custom comparator entirely?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Can you pass iterators that traverse the array backwards?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By using the reverse iterators `.rbegin()` and `.rend()`, the STL will scan and sort the array backwards, naturally resulting in a descending sort without needing `greater<int>()` or a custom function!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `sort(v.end(), v.begin());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `sort(v.rbegin(), v.rend());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `sort(v.begin(), v.end(), false);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `v.sort_descending();`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Sorting, Descending, Reverse Iterators, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **What is the single most critical mathematical prerequisite that must be satisfied before calling `std::lower_bound` or `std::upper_bound` on an array?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Because these algorithms use Binary Search under the hood, what shape must the array be in?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because both bound algorithms are highly optimized binary searches, the array **must be completely sorted first**. If you call them on an unsorted array, the binary search math will fail completely, silently returning garbage iterators without throwing any errors!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must be completely sorted first.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must contain absolutely no duplicate elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The target element must explicitly exist inside the array.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must contain an even number of elements to calculate the exact midpoint.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Binary Search, Prerequisites, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You successfully located an element using `auto it = std::lower_bound(v.begin(), v.end(), 30);`. However, `it` is a raw memory iterator. How do you mathematically convert this iterator into a standard, zero-based integer index?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If the iterator points to a memory address, how can you find its distance from the start of the array?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By subtracting the starting iterator (`v.begin()`) from your found iterator (`it`), C++ automatically calculates the exact mathematical distance between the two memory addresses, perfectly returning the standard zero-based integer index of your element!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `int index = *it;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `int index = &it;`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `int index = it - v.begin();`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `int index = static_cast<int>(it);`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Iterators, Pointer Arithmetic, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A beginner attempts to find an element inside a `std::set` using the algorithm `std::lower_bound(s.begin(), s.end(), val)`. Why does this instantly trigger a catastrophic Time Limit Exceeded (TLE) error on Codeforces?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does a set have random-access iterators that allow the global binary search algorithm to instantly jump to the middle element?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The global `std::lower_bound` algorithm strictly requires Random-Access iterators to jump instantly to the midpoint. Because a Set is a node-based Red-Black tree, it lacks these iterators. The STL is forced to painfully traverse the tree node-by-node, silently degrading the search from $O(\log N)$ to an apocalyptic $O(N)$! The correct solution is to use the Set's built-in member function: `s.lower_bound(val)`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Sets are inherently unsorted, so the binary search mathematics break down completely.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Sets use Hash Tables under the hood, and hash collisions trap the algorithm in an infinite loop.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Sets lack random-access iterators, forcing the global algorithm to traverse the tree node-by-node, degrading performance from $O(\log N)$ to $O(N)$.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because standard lower_bound only works on raw arrays, not STL containers.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, std::set, TLE, Member Functions vs Global Algorithms, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When generating all possible permutations of an array, why is it absolutely mandatory to use a `do-while` loop rather than a standard `while` loop?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about exactly when a standard `while` loop checks its condition. What happens to the very first arrangement?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A standard `while` loop checks its condition at the very beginning of the loop. This means it would immediately execute `next_permutation`, instantly mutating the array before the code inside the loop even runs! By doing this, you permanently skip testing the very first original arrangement. A `do-while` loop perfectly executes the code on the original array first, and then generates the next permutation at the bottom of the loop.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::next_permutation` is a macro that cannot compile inside a standard `while` statement.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because a standard `while` loop would execute the function before running the code block, permanently skipping the initial original arrangement.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `do-while` loops operate in $O(1)$ time, while standard `while` loops operate in $O(N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `next_permutation` requires the array to be reset to its initial state upon failure, which only `do-while` supports.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Permutations, next_permutation, Loops, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **To guarantee that a `do-while(next_permutation(...))` loop successfully generates *every single mathematically possible* arrangement without terminating early, what critical setup step must be done to the array before the loop starts?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        `next_permutation` only generates *larger* arrangements. If the array is already at its absolute maximum lexicographical state, what does the function return?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        You must `std::sort` the array in ascending order before starting the loop! Because `next_permutation` only generates lexicographically greater arrangements, starting with a partially shuffled array (like `3, 1, 2`) will skip all the smaller permutations (like `1, 2, 3`) and terminate early.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must be stripped of all duplicate elements.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must be reversed completely.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must be sorted perfectly in ascending order.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The array must be converted into a `std::set`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Permutations, Sorting Prerequisites, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If a FAANG interviewer bans the STL and asks you to verbally explain the algorithmic logic used by C++ to find the "Next Permutation" in $O(N)$ time, what is the core 3-step sequence?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You need to find a pivot to swap, and then reset everything to its lowest state.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The algorithm works in three strict $O(N)$ phases: (1) Traverse backwards to find the first Pivot that breaks ascending order (`a[i] < a[i+1]`). (2) Traverse backwards again to find the Successor (the smallest element greater than the Pivot) and swap them. (3) Reverse the remaining suffix chunk to reset it to its lowest possible lexicographical order.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Sort the array, find the median, and swap the median with the last element.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Find a pivot from the right, find a successor to swap it with, and reverse the remaining suffix.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Shift every element one position to the right in a circular array format.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Use recursion to swap the first element with every subsequent element until the end of the array is reached.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Permutations, Interview, Pivot Algorithm, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why did the C++ Standards Committee permanently delete `std::random_shuffle` from the language in C++17, forcing developers to use `std::shuffle` instead?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        What internal legacy C function did `random_shuffle` rely on, and why was it so terrible?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The old `random_shuffle` relied entirely on the legacy C `rand()` function. This function was notoriously terrible—it suffered from mathematically biased modulo mechanics, severe predictability, and a tiny maximum threshold (often capping at 32767). Modern `std::shuffle` requires you to pass a powerful, modern generator (like `mt19937`) to guarantee robust, cryptographically stronger randomness.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it relied on the legacy C `rand()` function, which suffered from modulo bias, predictability, and tiny limits.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it executed in $O(N^2)$ time instead of $O(N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it was unable to shuffle non-integer data types like strings or structs.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it caused memory leaks when used on dynamically allocated arrays.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Random, shuffle vs random_shuffle, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **On specific contest platforms (like Codeforces), relying on `std::random_device` to seed your generator is extremely dangerous because it is often implemented deterministically, allowing hackers to easily reverse-engineer your random numbers. What is the standard CP trick to guarantee a perfectly unhackable seed?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        What value on the computer changes every single nanosecond?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        To bypass broken random devices, Elite programmers seed their `mt19937` generator using the system's high-precision clock (`chrono::steady_clock::now().time_since_epoch().count()`). Because the exact nanosecond of execution will always be wildly different across runs, the resulting seed is mathematically impossible to predict or hack.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Seeding the generator using the size of the array.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Seeding the generator by summing all elements in the input.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Seeding the generator using the system's high-precision `chrono` clock nanoseconds.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Seeding the generator with a constant massive prime number.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Random, mt19937, Chrono Seed, Codeforces Hack, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When you execute `std::shuffle`, what legendary algorithm does C++ use under the hood to mathematically guarantee a perfectly uniform, unbiased random permutation of the array in exactly $O(N)$ time?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        It works by looping backwards from the end of the array and swapping the current element with a randomly chosen element before it.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        The STL utilizes the famous **Fisher-Yates (Knuth) Shuffle** algorithm. By looping backwards and continually swapping the current element with a completely random element from the un-shuffled portion of the array, it mathematically guarantees a perfectly uniform distribution with exactly $O(N)$ operations.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                The Monte Carlo Shuffle
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The Fisher-Yates (Knuth) Shuffle
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The Introspective Shuffle
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                The Quick-Scramble Algorithm
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, Random, std::shuffle, Fisher-Yates, Knuth, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A junior developer is trying to remove duplicate elements from a sorted `std::vector` by calling `std::unique(v.begin(), v.end());`. They are shocked to discover that the size of the vector did not change, and the end of the array is now filled with garbage values. What legendary C++ idiom must they use to actually delete the duplicates?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        `std::unique` does not physically delete memory; it only shifts the unique items to the front and returns an iterator to the new logical boundary.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because algorithms in the `<algorithm>` library only modify data and cannot reallocate a container's physical memory, `std::unique` physically cannot shrink a vector! It merely shifts the unique elements to the front, leaves the duplicates as garbage values at the end, and returns an iterator to the boundary between them. To actually reclaim the memory, you must execute the **Erase-Remove Idiom**: `v.erase(std::unique(v.begin(), v.end()), v.end());`. This uses the vector's own `erase` method to chop off the garbage suffix!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                They must call `v.shrink_to_fit();` immediately after calling `std::unique`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They must use the Erase-Remove Idiom: `v.erase(std::unique(v.begin(), v.end()), v.end());`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::unique` only works on `std::set`, not vectors.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                They must pass a custom `std::delete` flag as the third argument to `std::unique`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL Algorithms, std::unique, Erase-Remove Idiom, Memory Management, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
