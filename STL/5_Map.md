<VIDEO_WIDGET>

<VIDEO_ID>3558</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# The Map Data Structure

> _Why limit yourself to indexing arrays with integers? The C++ STL Map allows you to create lightning-fast lookup tables using strings, pairs, or any data type as the key._

In the previous lessons, we learned how to store and sort raw numbers using Sets and Multisets. But what if you want to store a relationship between two pieces of data? Imagine you have a physical English dictionary. You open it to look up the word "Algorithm." The word itself is unique—there is only one entry for "Algorithm" in the book. However, the definition assigned to it might be identical to another word's definition.

In Computer Science, this concept of linking a unique **Key** to a specific **Value** is called a **Map** (also known as a Dictionary or an Associative Array).

---

## 1. Map vs Unordered Map

Just like Sets, C++ provides two entirely different engines for Maps. The distinction is exactly the same:

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/ec1e3d9e-a519-4d80-a690-c14aa2b725f6.jpg" alt="Map Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### `std::map` (Ordered Map)

- **The Engine:** Powered by a balanced Binary Search Tree.
- **The Guarantee:** The **Keys** are ALWAYS kept in strictly sorted (ascending) order.
- **The Cost:** Inserting, deleting, or looking up a Key takes **$O(\log N)$ Time**.

### `std::unordered_map` (Unordered Map)

- **The Engine:** Powered by a Hash Table.
- **The Guarantee:** The Keys are scattered randomly. There is absolutely no order.
- **The Cost:** Inserting, deleting, or looking up a Key takes blazing fast **$O(1)$ Average Time**.

> 💡 **CP Insight: The Default Choice (With a Catch!)**
> In most platforms like LeetCode, your default weapon of choice should be `std::unordered_map` for that sweet $O(1)$ lookup time. However, on competitive platforms like Codeforces, malicious test cases are explicitly designed to cause hash collisions and force your `unordered_map` into an $O(N)$ Time Limit Exceeded (TLE) trap! If you are on Codeforces, either use `std::map` ($O(\log N)$ is usually fast enough) or learn how to write a custom hash function!

---

## 2. Core Operations

A Map stores data in `std::pair` objects behind the scenes. The `.first` element is the Key, and the `.second` element is the Value.

1. **Insert / Update (`map[key] = value`):** Adds or overwrites a Key-Value pair in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
2. **Erase (`erase(key)`):** Removes the Key (and its associated Value) from the map in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
3. **Count (`count(key)`):** Returns `1` if the Key exists, and `0` if it does not in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
4. **Find (`find(key)`):** Returns an iterator to the Key-Value pair in **$O(\log N)$ time** ($O(1)$ average, $O(N)$ worst-case for unordered).
5. **Size (`size()`):** Returns the total number of Key-Value pairs in **$O(1)$ time** for both.

> 🚨 **The CP Trap: Accidental Insertion**
> In C++, if you simply check the value of a key using bracket notation (e.g., `if (myMap[100] == 5)`), and the key `100` didn't exist, **C++ will secretly create it and assign it a default value of 0!** This can bloat your map's size and slow down your program. Always use `.count()` to check existence before accessing!

### The Code (C++)

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    unordered_map<string, int> ages;

    // 1. Inserting Data
    ages["Alice"] = 25;
    ages["Bob"] = 30;
    ages["Charlie"] = 30; // Values can be duplicates!

    // 2. Updating Data
    ages["Alice"] = 26; // Overwrites 25 with 26

    // 3. Iterating through a Map
    // Notice we use 'const auto&' to avoid making expensive copies of the data!
    cout << "Map Contents:\n";
    for (const auto& pair : ages) {
        cout << pair.first << " is " << pair.second << " years old.\n";
    }

    // 4. Safely checking if a Key exists
    if (ages.count("David") == 0) {
        cout << "David is not in the map!\n";
    }

    return 0;
}
```

---

## 3. Solving "Two Sum"

Let's look at the absolute quintessential Map problem. This is arguably the most famous coding interview question of all time: **Two Sum**.

**The Problem:** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

**Example:**
Input: `nums = [2,7,11,15]`, `target = 9`
Output: `[0,1]` _(Because nums[0] + nums[1] == 9)_

### The Intuition

You could use two nested loops to check every possible pair, but that takes $O(N^2)$ time.

Let's use an `unordered_map` to do it in **$O(N)$ Time**!
As we iterate through the array, we look at the current number, let's say `2`. We know the target is `9`. This means we absolutely _need_ to find a `7`.
Instead of searching the rest of the array for a `7`, we just ask our Map: _"Hey, have we seen a 7 earlier?"_
If the Map says no, we store our current number `2` (and its index) in the Map for the future, and move on.

The Map serves as our lightning-fast memory of everything we've seen so far!

### The Code (C++)

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Map will store: { number -> index }
        unordered_map<int, int> memory;

        for (int i = 0; i < nums.size(); i++) {
            int currentNumber = nums[i];
            int neededNumber = target - currentNumber;

            // Did we see the needed number earlier?
            if (memory.count(neededNumber)) {
                // Yes! Return both indices
                return {memory[neededNumber], i};
            }

            // No. Store the current number and its index for the future
            memory[currentNumber] = i;
        }

        return {}; // Should never reach here if a solution is guaranteed
    }
};
```

---

## 5. Practice Problem: Two Sum (Easy)

**The Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
**The Direct Application:** The quintessential map problem! We can solve this in a single $O(N)$ pass. As we iterate through the array, we calculate the `needed_value = target - nums[i]`. We use an `unordered_map` to instantly check if we've seen that value before. If yes, we win! If not, we save the current number and its index in the map.

### The Code (C++)

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    // Map to store: <Number, Index>
    unordered_map<int, int> seen;

    for (int i = 0; i < nums.size(); i++) {
        int needed = target - nums[i];

        // 1. Check if the complement exists in O(1) time
        if (seen.count(needed)) {
            return {seen[needed], i};
        }

        // 2. Otherwise, save the current number and its index
        seen[nums[i]] = i;
    }

    return {};
}
```

---

> 🚀 **Next Up:** You've now mastered the standard C++ STL! But what if you need to find the K-th smallest element in a dynamic set in $O(\log N)$ time? Standard Sets and Maps can't do that. It's time to unlock the secret weapon of Competitive Programmers: the **Indexed Set (PBDS)**!

</READING_WIDGET>
