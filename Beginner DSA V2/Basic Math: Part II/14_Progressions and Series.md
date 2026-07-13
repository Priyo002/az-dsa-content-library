<VIDEO_WIDGET>

<VIDEO_ID>3510</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Progressions and Series

Many algorithmic problems, especially those involving counting, dynamic programming, or optimization, can be boiled down to finding the sum of a specific mathematical sequence. Instead of running an $O(N)$ loop to sum the elements, you can use mathematical formulas to calculate the answer instantly in $O(1)$ time!

Let's explore the most common progressions and series you will encounter in competitive programming.

---

## 1. Arithmetic Progression (AP)

An **Arithmetic Progression** is a sequence of numbers where the difference between any two consecutive terms is constant. This constant is called the **common difference** ($d$).

**Example:** $3, 7, 11, 15, 19 \dots$ (Here, the starting term $a = 3$, and $d = 4$).

### Important Formulas

- **$N$-th Term ($T_n$):**
  $$T_n = a + (n - 1)d$$
- **Sum of First $N$ Terms ($S_n$):**
  $$S_n = \frac{n}{2} \left[ 2a + (n - 1)d \right]$$
  _(Alternatively, if you know the last term $l$: $S_n = \frac{n}{2}(a + l)$)_

> 💡 **CP Insight:** The sum of an AP is incredibly common when analyzing the time complexity of nested loops. For example, a loop running $N$ times, then $N-1$ times, down to $1$ time, is simply an AP sum yielding $O(N^2)$ time complexity!

---

## 2. Geometric Progression (GP)

A **Geometric Progression** is a sequence where the ratio of any two consecutive terms is constant. This constant is called the **common ratio** ($r$).

**Example:** $2, 6, 18, 54 \dots$ (Here, $a = 2$, and $r = 3$).

### Important Formulas

- **$N$-th Term ($T_n$):**
  $$T_n = a \times r^{n-1}$$
- **Sum of First $N$ Terms ($S_n$):**
  If $r \neq 1$:
  $$S_n = a \times \frac{r^n - 1}{r - 1}$$
  _(If $r = 1$, the sequence is just $a, a, a \dots$, so $S_n = n \times a$)_

### Infinite Geometric Progression

If the geometric progression goes on forever, can we find its sum? Yes, but **ONLY if the common ratio is strictly between -1 and 1** ($-1 < r < 1$). If $|r| \ge 1$, the sum mathematically explodes to infinity.

- **Sum to Infinity ($S_\infty$):**
  $$S_\infty = \frac{a}{1 - r}$$
  _(Validity: Strictly requires $-1 < r < 1$)_

---

## 3. Other Essential Series in CP

Problem setters love to disguise these three specific series in combinatorics and grid-based problems. Memorize them!

### Sum of the First $N$ Natural Numbers

$$1 + 2 + 3 + \dots + n = \frac{n(n + 1)}{2}$$

### Sum of the First $N$ Squares

$$1^2 + 2^2 + 3^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$$

### Sum of the First $N$ Cubes

$$1^3 + 2^3 + 3^3 + \dots + n^3 = \left[ \frac{n(n + 1)}{2} \right]^2$$

---

## 4. The Modulo Trap: Division in CP

In competitive programming, you are frequently asked to output your answer modulo $10^9 + 7$.

Look closely at the formulas for AP Sum ($\frac{n}{2}$), GP Sum ($\frac{r^n-1}{r-1}$), and Sum of Squares ($\frac{n(n+1)(2n+1)}{6}$). They all involve **division**.

A beginner will instinctively write `ans = (1LL * n * (n + 1) / 2) % MOD;`. This is extremely dangerous! If $N$ is massive, `n * (n+1)` will overflow 64-bit bounds before the division even happens.

To prevent overflow, they might try applying modulo _before_ dividing: `ans = ((1LL * n * (n + 1)) % MOD) / 2;`. **This completely breaks the math!** If the modulo operation results in an odd number (e.g., 27), dividing it by 2 in C++ truncates it to 13, irreversibly destroying the true mathematical remainder!

**The CP Fix:** You must apply the **Modular Multiplicative Inverse** we learned earlier!

To calculate $\frac{n(n+1)}{2} \pmod M$:

```cpp
long long n_mod = n % M;
long long n_plus_1_mod = (n + 1) % M;
long long numerator = (n_mod * n_plus_1_mod) % M;
long long inverse_of_2 = powerModulo(2, M - 2, M); // Fermat's Little Theorem
long long ans = (numerator * inverse_of_2) % M;
```

</READING_WIDGET>
