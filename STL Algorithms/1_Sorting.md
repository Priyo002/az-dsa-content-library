<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Sorting

> *Welcome to the STL Algorithms suite! The `std::sort` function is arguably the most heavily used feature in all of competitive programming. Let's master everything from basic sorting to completely overriding the rules of math with custom comparators.*

Before the STL, sorting an array required writing 20+ lines of QuickSort or MergeSort logic from scratch. Today, `std::sort` handles it instantly in exactly **$O(N \log N)$** time. Under the hood, C++ uses an algorithm called **IntroSort** (a highly optimized hybrid of QuickSort, HeapSort, and InsertionSort).

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/0a9716d3-8b43-49b9-b27c-2e506bdf3585.jpg" alt="std::sort IntroSort Algorithm Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. The Basics: Ascending, Descending, and Arrays

By default, `std::sort` sorts elements in ascending order (smallest to largest). You must provide it with two iterators: the start and the end.

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // Required for sort
using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 1, 5, 6};
    
    // 1. Sort Ascending
    sort(v.begin(), v.end());
    // Result: [1, 2, 5, 5, 6, 9]
    
    // 2. Sort Descending using greater<int>()
    sort(v.begin(), v.end(), greater<int>());
    // Result: [9, 6, 5, 5, 2, 1]
    
    // 3. Sort Descending using reverse iterators (Shortcut!)
    sort(v.rbegin(), v.rend());
    // Result: [9, 6, 5, 5, 2, 1]
    
    // 4. Sorting raw C-style arrays (using pointers instead of iterators)
    int arr[] = {4, 1, 3, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr + n); 
    // Result: [1, 2, 3, 4]
    
    return 0;
}
```

> 💡 **CP / Interview Insight: Stable Sorting**
> `std::sort` is an "unstable" sort. If you have two identical elements, their original relative order might get scrambled during the sorting process. If you are sorting complex objects (like employees by salary) and need identically salaried employees to stay in their original alphabetical order, you must use `std::stable_sort(v.begin(), v.end())` instead. It uses MergeSort under the hood and guarantees relative order is preserved!

---

## 2. Sorting in Chunks (Subarrays)

You don't always have to sort the *entire* container! `std::sort` allows you to sort a specific "chunk" of the array by simply shifting the iterators.

To sort only the elements from index `L` to index `R` (inclusive), you use:
`sort(v.begin() + L, v.begin() + R + 1);`

> 💡 **CP Insight:** Why the `+ 1`? Iterators in C++ are always **exclusive** at the end bound `[start, end)`. If you want to include index `R` in the sort, your end iterator must point to `R + 1`!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Indices:      0   1   2   3   4   5
    vector<int> v = {10, 50, 20, 40, 30, 60};
    
    // Sort only the chunk from index 1 to index 4 inclusive
    sort(v.begin() + 1, v.begin() + 4 + 1);
    
    // Result: [10, 20, 30, 40, 50, 60]
    // Notice that indices 0 and 5 were completely untouched!
    
    return 0;
}
```

---

## 3. Sorting Pairs (The Default Tiebreaker)

Before we sort them, let's briefly look at `std::pair`. A `pair` is a simple container defined in `<utility>` that binds two values together into a single unit. You can access the first value using `.first` and the second using `.second`.

In CP, you often store paired data, such as a student's ID and their test score: `vector<pair<int, int>>`.
How does C++ sort this? By default, `std::sort` sorts pairs based on the **first** element. If there is a tie, it automatically uses the **second** element as a tiebreaker!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int, int>> v = {
        {5, 100}, 
        {2, 50}, 
        {5, 10}
    };
    
    sort(v.begin(), v.end());
    
    // Result: [{2, 50}, {5, 10}, {5, 100}]
    // Notice how the tied 5s were sorted using their second values (10 < 100)!
    
    return 0;
}
```

---

## 5. Practice Problem: Sort the People (Easy)

**The Problem:** You are given an array of strings `names`, and an array `heights` that consists of distinct positive integers. Both arrays are of length `n`. For each index `i`, `names[i]` and `heights[i]` denote the name and height of the $i^{th}$ person. Return `names` sorted in **descending order** by the people's heights.
**The Direct Application:** This is a classic example of using `std::pair` and reverse iterators! We can combine the names and heights into a `vector<pair<int, string>>`, sort them descending using `rbegin()` and `rend()`, and then extract the sorted names.

### The Code (C++)

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
    int n = names.size();
    vector<pair<int, string>> people;
    
    // 1. Bind heights and names together
    // We put height FIRST because std::sort uses the first element!
    for (int i = 0; i < n; i++) {
        people.push_back({heights[i], names[i]});
    }
    
    // 2. Sort descending by height
    sort(people.rbegin(), people.rend());
    
    // 3. Extract the names in their new sorted order
    vector<string> sorted_names;
    for (int i = 0; i < n; i++) {
        sorted_names.push_back(people[i].second);
    }
    
    return sorted_names;
}

int main() {
    vector<string> names = {"Mary", "John", "Emma"};
    vector<int> heights = {180, 165, 170};
    
    vector<string> ans = sortPeople(names, heights);
    cout << "Sorted: ";
    for (string name : ans) cout << name << " "; // Output: Mary Emma John
    cout << "\n";
    
    return 0;
}
```

---

> 🚀 **Next Up:** Now that you've mastered `std::sort`, you are ready to tackle one of the most powerful paradigms in computer science. Let's move on to `std::lower_bound` and `std::upper_bound`!

</READING_WIDGET>
