<VIDEO_WIDGET>

<VIDEO_ID>3568</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Next Permutations

> _Welcome to the world of permutations! In Competitive Programming, you will frequently encounter problems that ask you to "try all possible arrangements" of a string or array. Instead of writing complex recursive backtracking functions from scratch, the C++ STL provides a magical function that handles everything for you in $O(N)$ time per step._

---

## 1. What is a Permutation?

A **permutation** is simply a mathematical rearrangement of elements. For example, if you have the numbers `{1, 2, 3}`, they can be arranged in exactly $3! = 6$ different ways.

These permutations have a natural **lexicographical (dictionary) order**:

1. `1 2 3` _(The smallest possible permutation)_
2. `1 3 2`
3. `2 1 3`
4. `2 3 1`
5. `3 1 2`
6. `3 2 1` _(The largest possible permutation)_

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/75a66558-7dfe-4e12-bfc1-a3e71dd77a69.jpg" alt="Lexicographical Permutations Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **CP Insight: Unique Permutations Only!**
> One of the greatest superpowers of `std::next_permutation` is that it naturally handles duplicates. If you run it on the array `{1, 1, 2}`, it will only generate the 3 mathematically unique arrangements (`1 1 2`, `1 2 1`, `2 1 1`). It completely skips redundant swaps!

---

## 2. `std::next_permutation`

The `std::next_permutation` function mathematically rearranges the array into the _next_ lexicographically greater permutation. It modifies the array in-place and returns `true` if it successfully found a larger permutation.
If the array is already at its absolute maximum (e.g., `3 2 1`), the function returns `false` and resets the array back to its absolute minimum state (`1 2 3`).

### The `do-while` Paradigm

Because `next_permutation` modifies the array _and_ returns a boolean, we can use it directly inside a loop! However, we must use a **`do-while`** loop. If we used a standard `while` loop, we would accidentally skip checking the very first arrangement!

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3};

    // The legendary CP permutation template
    do {
        // Print the current permutation
        for (int x : v) cout << x << " ";
        cout << "\n";
    } while (next_permutation(v.begin(), v.end()));

    return 0;
}
```

> 🚨 **The CP Trap: The N <= 11 Rule**
> Because there are $N!$ total permutations, generating all of them takes $O(N \times N!)$ time. In competitive programming, you can typically perform around $10^8$ operations per second. This means brute-forcing all permutations is only safe if $N \le 11$. If $N \ge 12$, using a `do-while` permutation loop will guarantee a Time Limit Exceeded (TLE)!

> 🚨 **The CP Trap: The Pre-Sorting Rule**
> If you want to generate _every single permutation_, you **MUST `std::sort` the array first**!
> If you start with `v = {3, 1, 2}`, the `do-while` loop will only generate `{3, 1, 2}` and `{3, 2, 1}` before terminating. It will miss the first four permutations! Always call `sort(v.begin(), v.end())` before starting your `do-while` loop.

---

## 3. `std::prev_permutation`

As you might expect, `std::prev_permutation` is the exact opposite. It rearranges the array into the _previous_ lexicographically smaller permutation. If the array is already at its absolute minimum (`1 2 3`), it returns `false` and resets it to the maximum (`3 2 1`).

If you wanted to print all permutations in reverse (largest to smallest), you would sort the array in _descending_ order first, and then use a `do-while` loop with `prev_permutation`.

---

## 4. Working with Strings

These permutation algorithms do not just work on arrays and vectors; they work flawlessly on `std::string` as well! The characters are permuted alphabetically.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s = "abc";

    do {
        cout << s << "\n";
    } while (next_permutation(s.begin(), s.end()));

    // Output:
    // abc
    // acb
    // bac
    // bca
    // cab
    // cba

    return 0;
}
```

---

## 5. Practice Problem: Next Permutation (Medium)

**The Problem:** A permutation of an array of integers is an arrangement of its members into a sequence or linear order. Given an array of integers `nums`, find the next lexicographically greater permutation of its sequence. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order). The replacement must be in place and use only constant extra memory.

**The Direct Application:** This is an incredibly famous interview problem (LeetCode 31). Interviewers usually want you to write the complex mathematical suffix-swapping logic from scratch. But in a Competitive Programming contest, you don't have time for that. You literally just call the STL function!

**How does it actually work? (For Interviews):**
If an interviewer bans the STL, here is the $O(N)$ algorithm C++ uses under the hood:

1. **Find the Pivot:** Traverse from right to left to find the first element that is smaller than the element directly to its right (`nums[i] < nums[i+1]`).
2. **Find the Successor:** Traverse from right to left again to find the smallest element that is strictly greater than the Pivot. Swap them.
3. **Reverse the Suffix:** Reverse all the elements to the right of the original Pivot index to reset that chunk to its lowest lexicographical order.

### The Code (C++)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void nextPermutation(vector<int>& nums) {
    // The STL function handles the exact requirements of the problem!
    // It rearranges in-place, and if it reaches the max permutation,
    // it automatically loops back to the ascending order minimum!
    next_permutation(nums.begin(), nums.end());
}

int main() {
    vector<int> nums = {1, 2, 3};
    nextPermutation(nums);

    cout << "Next: ";
    for (int x : nums) cout << x << " "; // Output: 1 3 2
    cout << "\n";

    return 0;
}
```

---

> 🚀 **Next Up:** Now that you've mastered permutations, let's explore randomness and probability. We will learn how to properly shuffle elements and generate random numbers using the modern `<random>` library!

</READING_WIDGET>
