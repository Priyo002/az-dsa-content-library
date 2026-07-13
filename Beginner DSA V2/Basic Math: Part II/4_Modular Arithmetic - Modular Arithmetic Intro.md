<VIDEO_WIDGET>

<VIDEO_ID>3504</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to Modular Arithmetic

In **Module 1 (Numbers, Divisibility, and Remainders)**, we introduced the modulo operator `%`. We used it primarily as a tool to find remainders or extract the last digit of a number.

However, in competitive programming, modulo is far more than just a remainder operator. It is the foundation of a massive branch of mathematics known as **Modular Arithmetic**. Let's formalize exactly what it is and why it behaves the way it does.

---

## 1. What is Modulo?

When dividing one integer by another, we typically get a quotient and a remainder. This concept is formalized with the notation $n \% m$, where $n$ is the dividend and $m$ is the divisor. The result represents the remainder when $n$ is divided by $m$.

$$\text{dividend} = \text{divisor} \times \text{quotient} + \text{remainder}$$

For mathematical precision, the modulo operation $n \% m$ can be formally defined as:

$$n \% m = n - \lfloor \frac{n}{m} \rfloor \times m$$

Here, $\lfloor x \rfloor$ represents the "floor" function (the largest integer that doesn't exceed $x$). This formula mathematically ensures that the result always falls within the strict range of $0$ to $m-1$ inclusive.

### Simple Division with Remainders

When you divide 7 by 3, you get a quotient of 2 and a remainder of 1:
$$7 = 3 \times 2 + 1$$

Thus, $7 \% 3 = 1$.

```cpp
int a = 7, m = 3;
int expr = a % m; // expr will be 1
```

### Division with Negative Numbers

$$-8 \% 7 = -1 \text{ (in C++)}$$
$$\text{Corrected: } -1 + 7 = 6$$

> 💡 **CP Must-Know (Negative Modulo Trap):** Consider dividing $-8$ by $7$. According to the mathematical floor formula above, $-8 / 7 = -1.14$, and the floor of $-1.14$ is $-2$. So the true remainder is $-8 - (-2 \times 7) = 6$. However, in C++, `-8 % 7` natively evaluates to `-1`! This is because C++ uses _truncation division_ (rounding towards zero) instead of true floor division. To fix this programmatically, you must adjust the C++ result by adding $m$ (which is $7$) to map it back into the positive range.

---

## 2. The "Need": Handling Large Numbers

If you've solved problems on LeetCode or Codeforces, you have likely seen this phrase: _"Return the answer modulo 10^9 + 7."_

When working with factorials, combinations, or binary exponentiation, numbers grow monstrously fast. There's an immense risk of exceeding the maximum value that can be stored in a 64-bit integer (a catastrophic error known as **integer overflow**).

By applying modulo arithmetic throughout your calculations, you mathematically guarantee that your intermediate numbers stay trapped within a small, perfectly manageable range ($0$ to $m-1$).

---

## 3. Properties of Modulo

Modulo possesses two extremely important mathematical properties that competitive programmers exploit heavily.

### Property 1: Cyclic Nature

The modulo operation is cyclic, meaning it creates an infinite repeating loop that wraps around the moment it reaches the modulus.

If we look at a sequence of numbers modulo $4$, the pattern is undeniable:

- $0 \% 4 = 0$
- $1 \% 4 = 1$
- $2 \% 4 = 2$
- $3 \% 4 = 3$
- $4 \% 4 = 0$ **(The cycle restarts!)**
- $5 \% 4 = 1$
- $6 \% 4 = 2$

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/4e879e58-2948-4c13-9a1a-c6311a8eb77f.png" alt="Modulo Cycle Viz" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Property 2: Congruence

In modular arithmetic, we often use a special mathematical symbol: $\equiv$. It is read as _"is congruent to"_.

Two numbers are considered congruent modulo $m$ if they leave the **exact same remainder** when divided by $m$. We denote this as:
$$a \equiv b \pmod m$$

For example:
$$17 \equiv 5 \pmod{12}$$
This statement is true because $17 \% 12 = 5$, and $5 \% 12 = 5$. Because their remainders match perfectly, they are congruent.

---

## 4. Clock Modulo Congruences

The easiest way to intuitively grasp congruences and cyclic nature is to look at a standard analog clock.

Imagine a clock face divided into twelve hours (1 to 12). If it is 12 o'clock and you move forward one hour, it becomes 1 o'clock. If you advance by multiple hours, the hands just wrap around the circle. The time is always trapped within the 12-hour constraint!

> 💡 **The Programmer's Clock:** While a real-world clock goes from $1$ to $12$, a programmer's clock is **0-indexed**. It operates strictly from $0$ to $m-1$ (e.g., $0$ to $11$). In the world of modulo, "12 o'clock" is mathematically identical to $0$ o'clock!

Clock modulo congruences assert that two integers are mathematically equivalent (congruent modulo 12) if they point to the exact same hour on the clock face.

### Example 1: Large Positive Integers

Let's evaluate $7$ and $19$. Although they are numerically different, they are congruent modulo 12:

- $7$ represents the 7th hour on the clock.
- $19$ wraps all the way around the clock (12 hours) and lands directly on the 7th hour again.

Therefore, $7 \equiv 19 \pmod{12}$.

### Example 2: Negative Integers

Even negative integers perfectly adhere to clock congruences. Consider $-4$ and $8$:

- $-4$ represents moving **backward** 4 hours from 12 o'clock, landing on the 8th hour.
- $8$ represents moving **forward** 8 hours from 12 o'clock, landing on the 8th hour.

Because they land on the exact same physical position on the clock face, we can confidently state:
$$-4 \equiv 8 \pmod{12}$$

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/995c5409-84a2-4aab-b69b-14be0eca1fcf.png" alt="Modulo Clock Viz" style="max-width: 100%; height: auto;" identifier="az-img-upload">

</READING_WIDGET>
