<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Counting Solutions for Linear Equations (Stars and Bars)

> *How many ways can you distribute $N$ identical items into $R$ distinct boxes? This is one of the most frequently asked combinatorics questions in competitive programming. The "Stars and Bars" technique is an incredibly elegant visual trick that converts algebra directly into basic combinations.*

---

## 1. The Challenge: Linear Equations

In combinatorics, you will frequently encounter problems asking for the number of integer solutions to an equation of the form:
$$ x_1 + x_2 + \dots + x_r = n $$

You are usually asked to solve this under two different constraints:
1. **Non-negative solutions:** $x_i \ge 0$ for all $i$. (Empty boxes are allowed).
2. **Strictly Positive solutions:** $x_i > 0$ for all $i$. (Every box must have at least 1 item).

Let's break down how the **Stars and Bars** method solves both of these instantly.

---

## 2. Case 1: Non-Negative Solutions ($x_i \ge 0$)

### 2.1 The Visual Idea Behind Stars and Bars
Imagine you have $n$ identical items, represented as glowing **Stars** ($\star$). 
You want to divide these stars among $r$ variables. To create $r$ separate groups, you need exactly $(r - 1)$ dividers, represented as vertical **Bars** ($|$).

If we arrange these $n$ stars and $(r - 1)$ bars in a straight sequence, the bars physically partition the stars into $r$ groups! The number of stars between the bars represents the integer value assigned to each $x_i$.

**Example:** Suppose we want to solve $x_1 + x_2 + x_3 = 4$.
- We have $n = 4$ stars ($\star \star \star \star$).
- We have $r = 3$ variables, so we need $r - 1 = 2$ bars ($|$ $|$).

A possible arrangement might be:
$$ \star \star \ |\  \star \ |\  \star $$

This physical layout instantly translates to a mathematical solution:
- $x_1 = 2$ (stars before the first bar)
- $x_2 = 1$ (stars between the bars)
- $x_3 = 1$ (stars after the second bar)

<img src="images/stars_and_bars_architecture.jpg" alt="Stars and Bars Combinatorics Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 2.2 The Combinatorial Formula
To find the total number of solutions, we just need to find the total number of valid string arrangements of stars and bars!

- Total objects to arrange: $n$ stars $+$ $(r - 1)$ bars $=$ **$n + r - 1$ total positions**.
- Out of these total positions, we just need to choose exactly $(r - 1)$ spots to place our bars. (The remaining spots will automatically be filled with stars).

This is a basic combinations calculation! The number of non-negative solutions is:
$$ \binom{n + r - 1}{r - 1} $$

**Solving our example ($n=4, r=3$):**
$$ \binom{4 + 3 - 1}{3 - 1} = \binom{6}{2} = 15 \text{ solutions.} $$

---

## 3. Case 2: Strictly Positive Solutions ($x_i > 0$)

What if the problem states that $x_i \ge 1$? (i.e., No variable is allowed to be $0$).

> 💡 **Elite CP Insight: The Substitution Method**
> The standard Stars and Bars formula $\binom{n+r-1}{r-1}$ assumes variables can be $0$. If variables must be at least $1$, elite programmers don't memorize a new complex formula. They simply use **Substitution** to shift the problem back to zero!

### 3.1 Shifting to Zero
Since every variable must be at least $1$, let's literally pre-allocate $1$ to every variable!
Let:
$$ x_i = y_i + 1 \quad (\text{where } y_i \ge 0) $$

Substitute this back into the original equation:
$$ (y_1 + 1) + (y_2 + 1) + \dots + (y_r + 1) = n $$

Group all the $1$s together (there are exactly $r$ of them, one for each variable):
$$ (y_1 + y_2 + \dots + y_r) + r = n $$
$$ y_1 + y_2 + \dots + y_r = n - r $$

### 3.2 Applying Stars and Bars
We have successfully shifted the equation! The variables $y_i$ are now allowed to be $0$ (non-negative). We can apply our standard Stars and Bars formula to the new sum $(n - r)$.

Using the formula $\binom{\text{Sum} + r - 1}{r - 1}$:
$$ \binom{(n - r) + r - 1}{r - 1} $$
Which beautifully simplifies to:
$$ \binom{n - 1}{r - 1} $$

**Example:** Solve $x_1 + x_2 + x_3 = 6$, where $x_i > 0$.
- $n = 6, r = 3$.
- Using our simplified formula:
$$ \binom{6 - 1}{3 - 1} = \binom{5}{2} = 10 \text{ solutions.} $$

---

## 4. Module Summary

The **Stars and Bars** technique transforms abstract algebra into physical string arrangements, allowing us to solve distribution problems using basic $nCr$ combinations.

| Constraint | Target Equation | Combinatorial Formula |
| :--- | :--- | :--- |
| **Non-negative** ($x_i \ge 0$) | $x_1 + x_2 + \dots + x_r = n$ | $\binom{n + r - 1}{r - 1}$ |
| **Strictly Positive** ($x_i > 0$) | $x_1 + x_2 + \dots + x_r = n$ | $\binom{n - 1}{r - 1}$ |

> 🚨 **The CP Trap: Modulo Inverse**
> In competitive programming, $n$ and $r$ can be as large as $10^5$. You cannot compute $\binom{N}{K}$ using Pascal's Triangle or basic factorials because the numbers will massively overflow! You must precompute factorials and use **Fermat's Little Theorem** to calculate the Modular Multiplicative Inverse when computing $\frac{N!}{K!(N-K)!} \pmod{10^9+7}$.

</READING_WIDGET>
