<VIDEO_WIDGET>

<VIDEO_ID>3505</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Rules of Modulo

In the previous section, we established that modulo is a cyclic mathematical system. But how do we actually perform arithmetic inside this system?

To safely keep numbers small during intermediate steps, we use fundamental distributive rules. If we want to add, subtract, multiply, or exponentiate numbers, we can apply modulo _before_ and _after_ the operation without altering the final mathematical truth.

Let's dive into the core rules.

---

## 1. The Rules of Calculations

### Addition

The sum of two numbers modulo $m$ is exactly the same as the sum of their individual remainders modulo $m$.
$$(a + b) \pmod m = ((a \pmod m) + (b \pmod m)) \pmod m$$

In C++, this is implemented safely as:

```cpp
int mod_add(int a, int b, int m) {
    return (a % m + b % m) % m;
}
```

_Example:_ $5 + 7 \pmod{10}$ is calculated as `(5 % 10 + 7 % 10) % 10`, resulting in $12 \% 10 = 2$.

### Subtraction

The difference of two numbers modulo $m$ follows the same distributive property, but we must add $m$ before the final modulo to prevent negative results in C++.
$$(a - b) \pmod m = ((a \pmod m) - (b \pmod m) + m) \pmod m$$

In C++:

```cpp
int mod_sub(int a, int b, int m) {
    return (a % m - b % m + m) % m;
}
```

_Example:_ $8 - 3 \pmod 5$ yields $(8 \% 5 - 3 \% 5 + 5) \% 5$, resulting in $0$.

### Multiplication

The product of two numbers modulo $m$ is the product of their individual remainders. This is the crucial rule that prevents massive numbers like $100!$ from instantly overflowing your integer capacity.
$$(a \times b) \pmod m = ((a \pmod m) \times (b \pmod m)) \pmod m$$

In C++:

```cpp
int mod_mul(int a, int b, int m) {
    return (1LL * (a % m) * (b % m)) % m;
}
```

> 💡 **CP Must-Know (Multiplication Overflow):** Even if `a % m` and `b % m` fit safely in a 32-bit `int`, their product might not! For example, if $m = 10^9 + 7$, then `(a % m) * (b % m)` can peak at $10^{18}$. Notice how we cast to `1LL` (a 64-bit `long long`) before multiplying in the `mod_mul` function!

### Exponentiation

Exponentiation is just repeated multiplication. Therefore, the exponentiation of a number modulo $m$ is the same as the exponentiation of its residue modulo $m$.
$$a^b \pmod m = (a \pmod m)^b \pmod m$$

---

## 2. Integrating Modulo into Binary Exponentiation

In **Module 5 (Binary Exponentiation)**, we learned how to calculate $a^b$ in an incredibly fast $O(\log b)$ time. We also learned that even $2^{65}$ overflows a 64-bit integer, making raw binary exponentiation completely useless for large inputs.

Now that we know the **Rule of Multiplication** and **Rule of Exponentiation**, we can upgrade our Binary Exponentiation code into a competitive programming powerhouse that safely calculates $a^b \pmod m$!

```cpp
// Time Complexity: O(log b)
// Space Complexity: O(1)
long long powerModulo(long long a, long long b, long long m) {
    long long ans = 1;
    a = a % m; // Apply Exponentiation Rule: reduce base first

    while (b > 0) {
        if (b % 2 != 0) { // If b is odd
            ans = (ans * a) % m; // Apply Multiplication Rule
        }
        a = (a * a) % m; // Apply Multiplication Rule
        b = b / 2; // Halve the power
    }
    return ans;
}
```

---

## 3. Power of Modulo: Analytical Examples

Let's look at two analytical examples that prove how powerful these rules are when evaluated by hand.

### Example 1: Remainders when Adding and Multiplying

**Problem:** What are the remainders when $3333 + 4444$ and $3333 \times 4444$ are divided by 5?

**Solution:**
We know that:

- $3333 \equiv 3 \pmod 5$
- $4444 \equiv 4 \pmod 5$

For addition:
$3333 + 4444 \equiv 3 + 4 \equiv 7 \equiv 2 \pmod 5$.

For multiplication:
$3333 \times 4444 \equiv 3 \times 4 \equiv 12 \equiv 2 \pmod 5$.

### Example 2: Modular Replacement

**Problem:** What is the remainder when $2015^{2015}$ is divided by $2014$?

**Solution:**
$2015^{2015}$ is an unimaginably massive number ($2015 \times 2015 \times \dots \times 2015$). Calculating it directly is impossible.
However, because $2015 \equiv 1 \pmod{2014}$, we can use the Rule of Exponentiation to replace the base with its remainder!

$2015^{2015} \pmod{2014}$
$\equiv 1^{2015} \pmod{2014}$
$\equiv 1$

By mathematically replacing the base instantly, a seemingly impossible calculation becomes trivial.

---

## 4. Special Edge Cases

Always watch out for these traps when dealing with modulo in your code:

- **Negative Dividend:** When the dividend is negative (e.g., `-5 % 3`), C++ will return a negative remainder (`-2`). Always use the normalized modulo trick: `(a % m + m) % m`.
- **Zero Dividend:** If $a = 0$, then $0 \% m$ is strictly $0$. (Don't confuse this with $m \% 0$!).
- **Zero Divisor:** Division by zero ($n \% 0$) is mathematically undefined. Doing this in C++ will instantly trigger a fatal Runtime Error.

> 💡 **What about Division?**
> Notice that we covered Addition, Subtraction, Multiplication, and Exponentiation. Why isn't there a formula for $(a / b) \pmod m$?
> Because modular division behaves entirely differently! You cannot simply divide the remainders. To perform division under a modulo, you must use an advanced technique called the **Modular Multiplicative Inverse**, which we will uncover in the very next section!

</READING_WIDGET>
