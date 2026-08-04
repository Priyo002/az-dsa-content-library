<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Stack Mastery: Smallest Number

> *You are given a massive number represented as a string. Your task is to remove exactly `k` digits to form the smallest possible number. This is a classic Greedy FAANG question that seems impossible to optimize—until you realize it's secretly just another Monotonic Stack!*

---

## 1. The Core Intuition

**The Problem:** Given a string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer after removing exactly `k` digits.

**Example 1:**
Input: `num = "1432219"`, `k = 3`
Output: `"1219"` (We removed the 4, 3, and the first 2).

**Why does this work?**
In mathematics, the most significant digits (the ones on the far left) have the massive power to make a number huge. 
Given the choice to remove a `9` at the very end of a number or a `2` at the very beginning, you almost always want to make the beginning as small as possible.

**The Greedy Rule:** As we scan from left to right, if we encounter a new digit that is *smaller* than the previous digit, we should instantly destroy the previous digit!
Why? Because replacing a larger leading digit with a smaller one guarantees a smaller final number.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/fb7bbfa2-d9c6-4e9d-a36f-e4cfef6073a0.jpg" alt="Monotonic Stack Greedy Destruction" style="max-width: 100%; height: auto;" identifier="az-img-upload">

This "destroy the larger previous elements" logic is exactly the **Monotonic Stack**!

> 🚨 **The CP Trap: The `string::erase()` Illusion**
> A common beginner mistake is to find the digit to remove and call `num.erase(i, 1)`. **Never do this!**
> In C++, `std::string` uses contiguous memory. If you erase a character in the middle, the CPU must physically shift every single character to the right of it one space to the left to close the gap. This takes $O(N)$ time. If you do this $K$ times, your algorithm degrades to $O(N \times K)$ time, which will instantly trigger a Time Limit Exceeded (TLE) on massive strings!
> This is exactly why we use a Stack: appending and popping from the end of a string takes strictly $O(1)$ time, guaranteeing an $O(N)$ overall solution.

---

## 2. The Monotonic Stack Algorithm

We will maintain a stack (using a `std::string` for zero overhead) to build our final answer.

1. **Iterate Left-to-Right:** Look at each digit in the input string.
2. **The Purge:** While the stack is not empty, AND the current digit is strictly smaller than the top of the stack, AND we still have "removals" allowed (`k > 0`):
   - Pop the top of the stack! (We are throwing away a large significant digit).
   - Decrement `k`.
3. **Leading Zeros Check:** If the stack is empty, we must not push a `'0'`. Leading zeros are mathematically invalid (except for the number `"0"` itself).
4. **Push:** Push the current digit onto the stack.

### The Exhaustion Trap
What if the input is `"12345"` and `k = 3`?
The numbers are already in perfect increasing order! The `while` loop condition (`current < stack.top()`) will never trigger. At the end of the loop, `k` will still be `3`. 
**Solution:** If we finish the loop and `k > 0`, it means the stack is perfectly sorted from smallest to largest. We must simply chop off the largest numbers from the very end!

### The Code Implementation
```cpp
#include <iostream>
#include <string>
using namespace std;

string removeKdigits(string num, int k) {
    // We use a string as our Stack for O(1) character appending!
    string st = ""; 
    
    for (char c : num) {
        // 1. The Purge: Destroy larger previous digits
        while (!st.empty() && st.back() > c && k > 0) {
            st.pop_back();
            k--;
        }
        
        // 2. Prevent Leading Zeros
        if (!st.empty() || c != '0') {
            st.push_back(c);
        }
    }
    
    // 3. The Exhaustion Trap: What if we still need to remove digits?
    while (!st.empty() && k > 0) {
        st.pop_back();
        k--;
    }
    
    // 4. Edge Case: If we removed everything, return "0"
    return st.empty() ? "0" : st;
}
```

---

## 3. Complexity Analysis

- **Time Complexity:** $O(N)$
  Just like the Next Greater Element problem, every character is pushed onto the stack at most once, and popped at most once. The nested `while` loop does not cause $O(N^2)$ behavior.
- **Space Complexity:** $O(N)$
  In the worst-case scenario (e.g., `k = 0`), the stack will store the entire original string.

---

## 4. Elite CP Insights

> 💡 **Systems Insight: Pre-allocation**
> Notice how we used `string st = "";`. While this is clean, `std::string` allocates memory dynamically as it grows. In a competitive programming environment where `num.length()` might be $10^6$, you can aggressively speed up this code by adding `st.reserve(num.length());` at the very beginning. This reserves a contiguous block of RAM upfront, entirely preventing slow reallocation overhead during the `push_back` phase!

> 🚨 **The CP Trap: Removing vs Keeping**
> Be careful with how questions are phrased! Leetcode usually asks to *Remove $K$ Digits*. Codeforces sometimes asks to *Form the smallest number having exactly $K$ digits*. 
> If you are asked to keep exactly $K$ digits, the core logic is mathematically identical, but your target removal count simply becomes `removals = num.length() - K`. Always read the problem statement carefully to know if $K$ is what you are destroying, or what you are saving!



</READING_WIDGET>