<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Stack Mastery: Valid Parentheses

> *The "Valid Parentheses" problem is arguably the most famous Stack question in all of computer science. It is asked in almost every FAANG entry-level interview because it perfectly tests a candidate's understanding of Last-In, First-Out (LIFO) logic. Let's master the intuition and discover a clever CP trick to write the cleanest possible code.*

---

## 1. The Core Intuition

**The Problem:** Given a string containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid.
A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Why a Stack?**
Think about reading a math formula from left to right: `{[()]}`. 
The *last* bracket you opened `(` is the *very first* bracket you are forced to close `)`. This perfectly matches the **Last-In, First-Out (LIFO)** architecture of a Stack!

---

## 2. The Standard Algorithm

The logic is remarkably simple:
1. Iterate through every character in the string.
2. **If it's an opening bracket:** Push it onto the stack. We are "waiting" for it to be closed.
3. **If it's a closing bracket:** 
   - Check if the stack is empty. If it is, there is no opening bracket to match it with (Invalid!).
   - Look at the top of the stack (`st.top()`). Does it perfectly match the current closing bracket? 
   - If yes, pop it off the stack (`st.pop()`). They have successfully annihilated each other.
   - If no, the order is wrong (Invalid!).
4. **The Final Check:** After reading the entire string, the stack must be completely empty. If there are brackets left over on the stack, it means they were never closed (Invalid!).

### The Standard Code
```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isValid(string s) {
    stack<char> st;

    for (char c : s) {
        // 1. Push opening brackets
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } 
        // 2. Process closing brackets
        else {
            // Unmatched closing bracket
            if (st.empty()) return false; 
            
            char top = st.top();
            // Check for perfect match
            if ((c == ')' && top == '(') || 
                (c == '}' && top == '{') || 
                (c == ']' && top == '[')) {
                st.pop();
            } else {
                return false; // Mismatched bracket type
            }
        }
    }
    
    // 3. Are there any unclosed brackets left?
    return st.empty();
}
```

---

## 3. The Elite CP Trick: Pushing Expectations

While the standard code works perfectly, the massive `if` statement checking for matches `(c == ')' && top == '(') || ...` is notoriously ugly and prone to typos during a high-pressure contest or whiteboard interview.

Elite competitive programmers use a brilliant structural trick: **Instead of pushing the opening bracket, push the EXPECTED closing bracket!**

If you see a `(`, you instantly push a `)` onto the stack. 
Now, when you eventually encounter a closing bracket in the string, you don't need complex `if` logic. You just check: *Is this character exactly equal to `st.top()`?* 

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/27e47d43-184c-4e56-8d88-ebae4762a6f5.jpg" alt="Pushing Expectations" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### The Refactored "Clean" Code
```cpp
bool isValidClean(string s) {
    // 💡 Instant speed optimization: An odd-length string is mathematically impossible to perfectly pair!
    if (s.length() % 2 != 0) return false;

    stack<char> st;

    for (char c : s) {
        // Push the EXPECTED matching bracket!
        if (c == '(') st.push(')');
        else if (c == '{') st.push('}');
        else if (c == '[') st.push(']');
        
        // It's a closing bracket! Just compare it directly to the top!
        else if (st.empty() || st.top() != c) {
            return false;
        } 
        // It matched! Pop the expectation.
        else {
            st.pop();
        }
    }
    
    return st.empty();
}
```

> 🚨 **The CP Trap: Short-Circuit SegFaults**
> Notice the exact order of this check: `st.empty() || st.top() != c`.
> In C++, the `||` (OR) operator uses **short-circuit evaluation**. If `st.empty()` is true, C++ instantly knows the whole condition is true and skips checking `st.top()`.
> If you reverse the order to `st.top() != c || st.empty()`, your code will crash with a Segmentation Fault the moment it encounters a string like `]`, because it tries to read the top of an empty stack!

> 💡 **Systems Insight: Zero-Overhead Stacks**
> `std::stack<char>` wraps a `std::deque`, which allocates memory in chunks. For absolute maximum speed and L1 cache locality, elite competitive programmers just use a `std::string` (or `std::vector<char>`) as their stack!
> You can simply use `str.push_back(c)`, read the top with `str.back()`, and pop with `str.pop_back()`. It acts exactly like a stack but runs significantly faster on massive inputs!

> 💡 **CP / Systems Insight: Early Exits**
> Notice the `if (s.length() % 2 != 0)` check at the very beginning of the clean code. 
> In competitive programming, you might be fed a string of 10 million characters. If the string is $10,000,001$ characters long, the standard algorithm will meticulously push 5 million brackets onto the stack and allocate megabytes of memory before finally returning `false` at the very end. The modulo check executes in $O(1)$ time, instantly rejecting invalid inputs and bypassing millions of useless CPU cycles!

---

## 4. Summary

- **Why a Stack?** Bracket matching is fundamentally a Last-In, First-Out (LIFO) problem.
- **The Expected Bracket Trick:** Push the closing bracket you *want* to see. It drastically simplifies the comparison logic and leads to ultra-clean code.
- **The Odd-Length Optimization:** Always check if the string length is odd for an instant $O(1)$ early exit to prevent Time Limit Exceeded (TLE) on massive bad inputs.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ (in the worst-case scenario where the string is entirely opening brackets: `((((((((`).

</READING_WIDGET>