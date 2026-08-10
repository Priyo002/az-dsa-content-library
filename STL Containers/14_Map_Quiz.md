<READING_WIDGET>
# Map Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In C++, what are the underlying data structures powering `std::map` and `std::unordered_map` respectively?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        One guarantees that keys are kept in sorted order, while the other scatters them randomly.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A `std::map` (Ordered Map) is powered by a balanced Binary Search Tree, keeping Keys strictly sorted. A `std::unordered_map` is powered by a Hash Table, offering extremely fast access but no order.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::map`: Hash Table | `std::unordered_map`: Doubly Linked List
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::map`: Balanced Binary Search Tree | `std::unordered_map`: Hash Table
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::map`: Max-Heap | `std::unordered_map`: Vector
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `std::map`: Array | `std::unordered_map`: Balanced Binary Search Tree
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Unordered Map, Data Structures, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Why is it generally recommended to avoid `std::unordered_map` on strict competitive programming platforms like Codeforces, despite its $O(1)$ average time complexity?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what powers the unordered map, and how malicious test designers might exploit it.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because `std::unordered_map` relies on a Hash Table, its worst-case time complexity degrades to $O(N)$. Platforms like Codeforces actively run "Anti-Hash" test cases specifically designed to force mass hash collisions, choking the table and causing a TLE.
        
        > 💡 **Elite CP Insight: The Anti-Hash Defense**
        > An elite competitive programmer doesn't always abandon the $O(1)$ unordered map for the slower $O(\log N)$ `std::map`. Instead, they neutralize the attack by writing a custom hash function (often utilizing `splitmix64` and a randomized time-based seed) to make collisions impossible to predict!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because allocating memory for the Hash Table takes $O(N \log N)$ time.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it is mathematically impossible to store strings inside an unordered map.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because malicious test cases are designed to force hash collisions, reducing its performance to a worst-case $O(N)$ and causing TLEs.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it takes $O(N)$ time to sort the unordered map internally before every insertion.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Hash Collisions, Codeforces, TLE, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When iterating through a map using a range-based for loop (e.g., `for (auto pair : myMap)`), how do you access the Key and the Value?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        A C++ Map stores its data as `std::pair` objects behind the scenes.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Map stores items as `std::pair`. The Key is accessed via `pair.first` and the Value is accessed via `pair.second`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `pair.key()` and `pair.value()`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `pair[0]` and `pair[1]`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `pair.first` and `pair.second`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `pair.index` and `pair.data`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Iterators, Pairs, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following C++ code snippet. The map is initially empty.**
```cpp
unordered_map<int, int> myMap;
if (myMap[100] == 5) {
    cout << "Found!";
}
cout << myMap.size();
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        This tests the "Accidental Insertion Trap". What does the `[]` operator do if the key doesn't exist?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If you check the value of a key using bracket notation (`myMap[100]`) and the key does not exist, C++ silently creates the key and initializes it to a default value of 0. Thus, the map will now contain `{100: 0}`, and `myMap.size()` will return `1`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `0`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `1`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `Found! 0`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `Segmentation Fault`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Insertion Trap, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In the classic "Two Sum" problem solved in $O(N)$ time using an `unordered_map`, what exactly is the map storing?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        What does the algorithm look up, and what does it need to return when it finds a match?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        In the $O(N)$ Two Sum algorithm, the map acts as memory. We store the `Number` we just saw as the Key, and its `Index` as the Value. This allows us to instantly check if the needed complement (a number) exists, and immediately retrieve its index to return the answer!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Key = Array Index | Value = Target Number
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Key = Target Number | Value = Complement Array
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Key = Array Number | Value = Array Index
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Key = Array Index | Value = Array Number
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Two Sum, Algorithmic Application, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When iterating through a map, you should write `for (const auto& pair : myMap)` instead of `for (auto pair : myMap)`. Why?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about what happens to memory when you don't use a reference (`&`).
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Writing `for (auto pair : myMap)` creates an expensive, deep copy of the `std::pair` on every single iteration. Using `const auto&` creates a read-only reference, which uses no extra memory and avoids the $O(K)$ overhead of copying strings or complex nested structures.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because omitting the `&` causes an infinite loop.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because using `&` avoids making expensive deep copies of the Key-Value pairs on every iteration.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because maps can only be iterated over backwards.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `auto` is not a valid C++ keyword.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Iterators, Const Reference, Memory, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **Consider the following C++ snippet:**
```cpp
map<int, string> myMap;
myMap[1] = "Apple";
myMap.insert({1, "Banana"});
cout << myMap[1];
```
**What will be printed to the standard output?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does `map::insert()` overwrite an existing value if the key is already present?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        `std::map::insert()` does NOT overwrite existing values! If the key already exists in the map, `.insert()` will silently ignore the operation. Only the `[]` operator or `insert_or_assign` will overwrite existing values. Therefore, the value remains "Apple".
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                `Apple`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `Banana`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Compilation Error
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                `AppleBanana`
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Insert Trap, Overwriting, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In low-latency engineering and competitive programming, what happens if you use the global algorithm `std::lower_bound(m.begin(), m.end(), key)` on a `std::map` instead of the member function `m.lower_bound(key)`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does `std::map` provide random-access iterators that allow the global algorithm to perform binary search in $O(\log N)$ time?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        If a developer uses the global algorithm `std::lower_bound` on a `std::map` instead of the member function, the compiler will allow it to compile, but the time complexity quietly degrades from $O(\log N)$ to $O(N)$! This happens because the global algorithm requires random-access iterators (like in vectors) to perform $O(\log N)$ jumps; without them, it falls back to a linear scan.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It throws a compilation error because global algorithms do not work on maps.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It works perfectly and runs in identical $O(\log N)$ time as the member function.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It successfully compiles but quietly degrades performance to $O(N)$, likely causing a TLE.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It causes a runtime Segmentation Fault.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Map, Lower Bound, Iterators, Time Complexity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
