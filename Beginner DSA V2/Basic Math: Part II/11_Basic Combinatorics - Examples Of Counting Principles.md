<VIDEO_WIDGET>

<VIDEO_ID>3509</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Examples of Counting Principles

In the previous module, we learned the Golden Rule of Counting: "AND" means multiply, "OR" means add. Let's see how these simple rules scale to solve complex, constraint-based combinatorial problems.

---

## 1. License Plates with Specific Constraints

**Problem:**
Determine the number of possible license plates that can be created under the following conditions:

- The plate starts with exactly **two distinct** English letters.
- Followed by exactly **three distinct** digits.
- The first digit **cannot** be 0.

**Solution:**
We must select Letters **AND** Digits to form the full plate. Therefore, we will use the Multiplication Principle.

_Step 1: Choosing the Letters_

- The first letter has **26** possible choices (A-Z).
- The second letter must be distinct from the first, leaving exactly **25** choices.
- Total combinations for letters: $26 \times 25 = 650$

_Step 2: Choosing the Digits_

- The first digit has **9** possible choices (1-9), because 0 is excluded.
- The second digit can be any digit _except_ the one just chosen. Since 0 is now allowed, we have $10 - 1 = \mathbf{9}$ choices.
- The third digit must be different from the first two, leaving $10 - 2 = \mathbf{8}$ choices.
- Total combinations for digits: $9 \times 9 \times 8 = 648$

_Step 3: Total License Plates_
Since we need letters **AND** digits, we multiply the two intermediate results:
$$650 \times 648 = \mathbf{421,200}$$

> 💡 **CP Insight:** When dealing with multiple constraint blocks (like letters then digits), solve each block completely independently first. Then, use the Multiplication Principle to join them together at the very end.

---

## 2. Palindromic Words

**Problem:**
Calculate the total number of possible 5-letter palindromes that can be formed using standard English letters. Then, extend this formula to an $N$-letter palindrome.

**Solution:**
A palindrome reads the exact same forward as it does backward (e.g., "abcba").

_For a 5-letter palindrome:_

- The 1st and 5th letters are identical.
- The 2nd and 4th letters are identical.
- The 3rd letter is entirely unique.

Because the back-half of the word is just a mirror of the front-half, we only actually get to "choose" the first half of the word! The rest of the letters are forced choices (meaning we only have 1 choice for them).

- Choices for 1st letter: **26**
- Choices for 2nd letter: **26**
- Choices for 3rd letter: **26**
- Choices for 4th letter: **1** (Must exactly match 2nd letter)
- Choices for 5th letter: **1** (Must exactly match 1st letter)

Total combinations:
$$26 \times 26 \times 26 \times 1 \times 1 = 26^3 = \mathbf{17,576}$$

_Extension to an $N$-letter palindrome:_
If you look closely, the number of "free choices" we get is exactly half the length of the string, rounded up.

- **If N is even:** The first $\frac{N}{2}$ letters uniquely determine the entire palindrome.
  Formula: $26^{\frac{N}{2}}$
- **If N is odd:** The first $\lfloor\frac{N}{2}\rfloor + 1$ letters determine the palindrome (including the unique middle character).
  Formula: $26^{\lfloor\frac{N}{2}\rfloor + 1}$

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/6eb59367-a050-47b7-ac6f-358a321cf0ea.png" alt="Palindrome Example" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **CP Trick (Unifying Even and Odd):**
> Instead of writing an `if/else` statement in your code for even and odd lengths, you can use a brilliant integer math trick. In C++ (where division automatically rounds down), the number of "free choices" is always exactly `(N + 1) / 2`.
>
> - If $N=5$: `(5 + 1) / 2` $\rightarrow$ `6 / 2` = **3 choices**.
> - If $N=6$: `(6 + 1) / 2` $\rightarrow$ `7 / 2` = **3 choices**.
>   The math unifies perfectly, meaning you can just calculate $26^{\frac{N + 1}{2}}$.

---

## 3. Numbers with Odd Digits & No Consecutive Repeats

**Problem:**
Find the number of 10-digit numbers that can be formed using only odd digits (`1, 3, 5, 7, 9`) such that absolutely no two consecutive digits are the same. Extend this to an $N$-digit number.

**Solution:**
We have a pool of **5** available odd digits.

_Step-by-Step Construction:_

- The 1st digit has no restrictions, so it has **5** possible choices.
- The 2nd digit can be any odd digit _except_ the one immediately preceding it. This leaves exactly **4** choices.
- The 3rd digit can be any odd digit _except_ the 2nd digit. This again leaves exactly **4** choices.
- Every subsequent digit will permanently have exactly **4** choices.

_Total for a 10-digit number:_
$$5 \times 4 \times 4 \times 4 \dots \text{(9 times)}$$
$$= \mathbf{5 \times 4^9}$$

_Extension to an $N$-digit number:_
The logic remains identical. The very first slot gets 5 choices, and the remaining $(N-1)$ slots get exactly 4 choices each.
Formula:
$$\mathbf{5 \times 4^{N-1}}$$

</READING_WIDGET>
