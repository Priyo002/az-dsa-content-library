<VIDEO_WIDGET>

<VIDEO_ID>3589</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Stack Mastery: Next Greater Element

> _Finding the Next Greater Element (NGE) is a foundational pattern in competitive programming. If you try to solve it with nested loops, you will get an instant Time Limit Exceeded (TLE) on massive arrays. Let's master the "Monotonic Stack", a genius architecture that solves this in strict $O(N)$ time._

---

## 1. The Core Intuition

**The Problem:** Given an array of integers, for every element, find the first element to its right that is strictly greater than it. If no such element exists, output `-1`.

Example:
Input: `[2, 1, 5, 3]`
Output: `[5, 5, -1, -1]`

**The Naive Approach ($O(N^2)$):**
You could use two `for` loops. For every element, scan the rest of the array to its right until you find a larger number. This is incredibly slow and will fail large test cases.

**The Monotonic Stack Approach ($O(N)$):**
Imagine tall and short people standing in a line, looking to the right.
If a tall person is standing directly in front of a short person, the short person is completely hidden from anyone looking from the left! **If an element is smaller than the current element, it is completely useless to everyone on the left.**

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/b1c96c74-3329-4d21-81eb-f76db5fa09e0.jpg" alt="Monotonic Stack Line of Sight" style="max-width: 100%; height: auto;" identifier="az-img-upload">

This gives us our algorithm: We iterate from **Right to Left**, maintaining a stack of "useful" numbers.

---

## 2. The Algorithm (Right to Left)

When looking at the current number:

1. **Clear the Losers:** Look at the top of the stack. If the top of the stack is _smaller than or equal_ to our current number, it is useless! Pop it! Keep popping until you find a number strictly greater than the current number, or the stack becomes empty.
2. **Record the Answer:**
   - If the stack is empty, there is no greater element to the right (Record `-1`).
   - If the stack is not empty, the top of the stack is our Next Greater Element!
3. **Save Yourself:** Push the current number onto the stack, because it might be the Next Greater Element for someone further to the left.

Because the stack only ever holds numbers in strictly increasing order (from top to bottom), it is called a **Monotonic Stack**.

### The Code Implementation

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> nextGreaterElement(const vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1); // Default all answers to -1

    // We will use a vector as a stack for Zero-Overhead speed!
    vector<int> st;

    // Iterate from RIGHT to LEFT
    for (int i = n - 1; i >= 0; i--) {

        // 1. Clear the Losers (Pop all elements smaller than or equal to current)
        while (!st.empty() && st.back() <= nums[i]) {
            st.pop_back();
        }

        // 2. Record the Answer
        if (!st.empty()) {
            result[i] = st.back();
        }

        // 3. Save Yourself for the next iterations
        st.push_back(nums[i]);
    }

    return result;
}
```

> 🚨 **The CP Trap: Strict vs Non-Strict Monotonicity**
> Pay close attention to the `st.back() <= nums[i]` condition. Because of the `=`, this stack pops elements that are exactly identical to the current number, guaranteeing we only find a strictly greater element. If a problem asks for the "Next Greater or Equal Element", you must change this to `<` so duplicates survive on the stack! Messing up this single character is the #1 cause of Wrong Answer (WA) verdicts on Monotonic Stack problems.

---

## 3. Why is this $O(N)$ Time?

Beginners often look at the nested `while` loop inside the `for` loop and mistakenly assume the time complexity is $O(N^2)$. **This is a massive CP Trap!**

Look closely at the mechanics of the stack:

- Every single element is pushed onto the stack exactly **once**.
- Every single element can be popped from the stack at most **once**.

Because an element can never be popped twice, the `while` loop runs a total of at most $N$ times across the _entire execution_ of the program, not per iteration. Therefore, the amortized time complexity is strictly **$O(N)$**.

---

## 4. Elite CP Variations

The Monotonic Stack is a template that can be slightly tweaked to solve dozens of complex FAANG interview questions.

### Variation 1: Storing Indices (The "Distance" Problem)

What if the question asks: _"How many days do you have to wait until a warmer temperature?"_ (Next Greater Element Distance).
Instead of pushing the _values_ onto the stack, you push the **indices** of the values!

```cpp
// 1. Clear losers by comparing values via indices
while (!st.empty() && nums[st.back()] <= nums[i]) st.pop_back();

// 2. The answer is the distance between indices
if (!st.empty()) result[i] = st.back() - i;

// 3. Push the current index!
st.push_back(i);
```

### Variation 2: Circular Arrays

What if the array wraps around? (e.g., the element to the right of the last element is the first element).
Instead of doing complex modulo math with indices, simply run the `for` loop from `(2 * n) - 1` down to `0`. Use `nums[i % n]` to access the elements. This effectively simulates placing two copies of the array side-by-side!

### Variation 3: Next Smallest Element

To find the Next Smallest Element, simply change the `while` loop condition from `<= nums[i]` to `>= nums[i]`. Instead of popping the "losers" (small elements), you pop the "tall elements" because they are blocking the small elements behind them!

### Variation 4: Left-to-Right (Online Processing)

What if the numbers are streaming in live, and you can't start from the right? You can iterate **Left-to-Right**! Instead of pushing answers to the stack, you push _unresolved indices_. When a new large number arrives, it acts as the "answer" for all the smaller unresolved indices currently sitting on the stack. You pop them, record the current number as their answer, and then push the current index to wait for its own greater element!

---

## 5. Summary

- **The Monotonic Stack:** A stack that maintains strictly increasing or decreasing elements to find the Next Greater/Smaller elements in $O(N)$ time.
- **The Core Intuition:** Iterate backwards. Pop useless elements. Record the answer. Push yourself.
- **Indices over Values:** If a problem requires "distance" or "width" (like the Largest Rectangle in Histogram problem), store array indices in the stack, not the actual values!

</READING_WIDGET>
